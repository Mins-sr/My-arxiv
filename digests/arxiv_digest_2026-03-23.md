# arXiv Daily Digest - 2026-03-23

Total papers: 350

---

## cs.AI

**50 papers**

### 1. From Masks to Pixels and Meaning: A New Taxonomy, Benchmark, and Metrics for VLM Image Tampering

**Authors:** Xinyi Shang, Yi Tang, Jiacheng Cui, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20193v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20193v1)

**Summary:** Existing tampering detection benchmarks largely rely on object masks, which severely misalign with the true edit signal: many pixels inside a mask are untouched or only trivially modified, while subtle yet consequential edits outside the mask are treated as natural. We reformulate VLM image tampering from coarse region labels to a pixel-grounded, meaning and language-aware task. First, we introduce a taxonomy spanning edit primitives (replace/remove/splice/inpaint/attribute/colorization, etc.) a...

---

### 2. LumosX: Relate Any Identities with Their Attributes for Personalized Video Generation

**Authors:** Jiazheng Xing, Fei Du, Hangjie Yuan, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20192v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20192v1)

**Summary:** Recent advances in diffusion models have significantly improved text-to-video generation, enabling personalized content creation with fine-grained control over both foreground and background elements. However, precise face-attribute alignment across subjects remains challenging, as existing methods lack explicit mechanisms to ensure intra-group consistency. Addressing this gap requires both explicit modeling strategies and face-attribute-aware data resources. We therefore propose LumosX, a frame...

---

### 3. VideoSeek: Long-Horizon Video Agent with Tool-Guided Seeking

**Authors:** Jingyang Lin, Jialian Wu, Jiang Liu, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20185v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20185v1)

**Summary:** Video agentic models have advanced challenging video-language tasks. However, most agentic approaches still heavily rely on greedy parsing over densely sampled video frames, resulting in high computational cost. We present VideoSeek, a long-horizon video agent that leverages video logic flow to actively seek answer-critical evidence instead of exhaustively parsing the full video. This insight allows the model to use far fewer frames while maintaining, or even improving, its video understanding c...

---

### 4. Improving Generalization on Cybersecurity Tasks with Multi-Modal Contrastive Learning

**Authors:** Jianan Huang, Rodolfo V. Valentim, Luca Vassio, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20181v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20181v1)

**Summary:** The use of ML in cybersecurity has long been impaired by generalization issues: Models that work well in controlled scenarios fail to maintain performance in production. The root cause often lies in ML algorithms learning superficial patterns (shortcuts) rather than underlying cybersecurity concepts. We investigate contrastive multi-modal learning as a first step towards improving ML performance in cybersecurity tasks. We aim at transferring knowledge from data-rich modalities, such as text, to ...

---

### 5. Adaptive Greedy Frame Selection for Long Video Understanding

**Authors:** Yuning Huang, Fengqing Zhu

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20180v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20180v1)

**Summary:** Large vision--language models (VLMs) are increasingly applied to long-video question answering, yet inference is often bottlenecked by the number of input frames and resulting visual tokens. Naive sparse sampling can miss decisive moments, while purely relevance-driven selection frequently collapses onto near-duplicate frames and sacrifices coverage of temporally distant evidence. We propose a question-adaptive greedy frame selection method that jointly optimizes query relevance and semantic rep...

---

### 6. AI Agents Can Already Autonomously Perform Experimental High Energy Physics

**Authors:** Eric A. Moreno, Samuel Bright-Thonney, Andrzej Novak, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20179v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20179v1)

**Summary:** Large language model-based AI agents are now able to autonomously execute substantial portions of a high energy physics (HEP) analysis pipeline with minimal expert-curated input. Given access to a HEP dataset, an execution framework, and a corpus of prior experimental literature, we find that Claude Code succeeds in automating all stages of a typical analysis: event selection, background estimation, uncertainty quantification, statistical inference, and paper drafting. We argue that the experime...

---

### 7. Measuring Faithfulness Depends on How You Measure: Classifier Sensitivity in LLM Chain-of-Thought Evaluation

**Authors:** Richard J. Young

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20172v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20172v1)

**Summary:** Recent work on chain-of-thought (CoT) faithfulness reports single aggregate numbers (e.g., DeepSeek-R1 acknowledges hints 39% of the time), implying that faithfulness is an objective, measurable property of a model. This paper demonstrates that it is not. Three classifiers (a regex-only detector, a two-stage regex-plus-LLM pipeline, and an independent Claude Sonnet 4 judge) are applied to 10,276 influenced reasoning traces from 12 open-weight models spanning 9 families and 7B to 1T parameters. O...

---

### 8. Learning Dynamic Belief Graphs for Theory-of-mind Reasoning

**Authors:** Ruxiao Chen, Xilei Zhao, Thomas J. Cova, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20170v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20170v1)

**Summary:** Theory of Mind (ToM) reasoning with Large Language Models (LLMs) requires inferring how people's implicit, evolving beliefs shape what they seek and how they act under uncertainty -- especially in high-stakes settings such as disaster response, emergency medicine, and human-in-the-loop autonomy. Prior approaches either prompt LLMs directly or use latent-state models that treat beliefs as static and independent, often producing incoherent mental models over time and weak reasoning in dynamic cont...

---

### 9. The Robot's Inner Critic: Self-Refinement of Social Behaviors through VLM-based Replanning

**Authors:** Jiyu Lim, Youngwoo Yoon, Kwanghyun Park

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20164v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20164v1)

**Summary:** Conventional robot social behavior generation has been limited in flexibility and autonomy, relying on predefined motions or human feedback. This study proposes CRISP (Critique-and-Replan for Interactive Social Presence), an autonomous framework where a robot critiques and replans its own actions by leveraging a Vision-Language Model (VLM) as a `human-like social critic.' CRISP integrates (1) extraction of movable joints and constraints by analyzing the robot's description file (e.g., MJCF), (2)...

---

### 10. Semantic Token Clustering for Efficient Uncertainty Quantification in Large Language Models

**Authors:** Qi Cao, Andrew Gambardella, Takeshi Kojima, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20161v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20161v1)

**Summary:** Large language models (LLMs) have demonstrated remarkable capabilities across diverse tasks. However, the truthfulness of their outputs is not guaranteed, and their tendency toward overconfidence further limits reliability. Uncertainty quantification offers a promising way to identify potentially unreliable outputs, but most existing methods rely on repeated sampling or auxiliary models, introducing substantial computational overhead. To address these limitations, we propose Semantic Token Clust...

---

### 11. Design-OS: A Specification-Driven Framework for Engineering System Design with a Control-Systems Design Case

**Authors:** H. Sinan Bank, Daniel R. Herber, Thomas H. Bradley

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20151v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20151v1)

**Summary:** Engineering system design -- whether mechatronic, control, or embedded -- often proceeds in an ad hoc manner, with requirements left implicit and traceability from intent to parameters largely absent. Existing specification-driven and systematic design methods mostly target software, and AI-assisted tools tend to enter the workflow at solution generation rather than at problem framing. Human--AI collaboration in the design of physical systems remains underexplored. This paper presents Design-OS,...

---

### 12. Enhancing Hyperspace Analogue to Language (HAL) Representations via Attention-Based Pooling for Text Classification

**Authors:** Ali Sakour, Zoalfekar Sakour

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20149v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20149v1)

**Summary:** The Hyperspace Analogue to Language (HAL) model relies on global word co-occurrence matrices to construct distributional semantic representations. While these representations capture lexical relationships effectively, aggregating them into sentence-level embeddings via standard mean pooling often results in information loss. Mean pooling assigns equal weight to all tokens, thereby diluting the impact of contextually salient words with uninformative structural tokens. In this paper, we address th...

---

### 13. An Agentic Multi-Agent Architecture for Cybersecurity Risk Management

**Authors:** Ravish Gupta, Saket Kumar, Shreeya Sharma, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20131v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20131v1)

**Summary:** Getting a real cybersecurity risk assessment for a small organization is expensive -- a NIST CSF-aligned engagement runs $15,000 on the low end, takes weeks, and depends on practitioners who are genuinely scarce. Most small companies skip it entirely. We built a six-agent AI system where each agent handles one analytical stage: profiling the organization, mapping assets, analyzing threats, evaluating controls, scoring risks, and generating recommendations. Agents share a persistent context that ...

---

### 14. Evolving Jailbreaks: Automated Multi-Objective Long-Tail Attacks on Large Language Models

**Authors:** Wenjing Hong, Zhonghua Rong, Li Wang, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20122v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20122v1)

**Summary:** Large Language Models (LLMs) have been widely deployed, especially through free Web-based applications that expose them to diverse user-generated inputs, including those from long-tail distributions such as low-resource languages and encrypted private data. This open-ended exposure increases the risk of jailbreak attacks that undermine model safety alignment. While recent studies have shown that leveraging long-tail distributions can facilitate such jailbreaks, existing approaches largely rely o...

---

### 15. Chain-of-Adaptation: Surgical Vision-Language Adaptation with Reinforcement Learning

**Authors:** Jiajie Li, Chenhui Xu, Meihuan Liu, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20116v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20116v1)

**Summary:** Conventional fine-tuning on domain-specific datasets can inadvertently alter a model's pretrained multimodal priors, leading to reduced generalization. To address this, we propose Chain-of-Adaptation (CoA), an adaptation framework designed to integrate domain knowledge while maintaining the model's inherent reasoning and perceptual capabilities. CoA introduces a structured reasoning format that enhances domain alignment without sacrificing general multimodal competence by reinforcement learning....

---

### 16. Demonstration of Adapt4Me: An Uncertainty-Aware Authoring Environment for Personalizing Automatic Speech Recognition to Non-normative Speech

**Authors:** Niclas Pokel, Yiming Zhao, Pehuén Moure, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20112v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20112v1)

**Summary:** Personalizing Automatic Speech Recognition (ASR) for non-normative speech remains challenging because data collection is labor-intensive and model training is technically complex. To address these limitations, we propose Adapt4Me, a web-based decentralized environment that operationalizes Bayesian active learning to enable end-to-end personalization without expert supervision. The app exposes data selection, adaptation, and validation to lay users through a three-stage human-in-the-loop workflow...

---

### 17. Var-JEPA: A Variational Formulation of the Joint-Embedding Predictive Architecture -- Bridging Predictive and Generative Self-Supervised Learning

**Authors:** Moritz Gögl, Christopher Yau

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20111v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20111v1)

**Summary:** The Joint-Embedding Predictive Architecture (JEPA) is often seen as a non-generative alternative to likelihood-based self-supervised learning, emphasizing prediction in representation space rather than reconstruction in observation space. We argue that the resulting separation from probabilistic generative modeling is largely rhetorical rather than structural: the canonical JEPA design, coupled encoders with a context-to-target predictor, mirrors the variational posteriors and learned conditiona...

---

### 18. The $\mathbf{Y}$-Combinator for LLMs: Solving Long-Context Rot with $λ$-Calculus

**Authors:** Amartya Roy, Rasul Tutunov, Xiaotong Ji, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20105v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20105v1)

**Summary:** LLMs are increasingly used as general-purpose reasoners, but long inputs remain bottlenecked by a fixed context window. Recursive Language Models (RLMs) address this by externalising the prompt and recursively solving subproblems. Yet existing RLMs depend on an open-ended read-eval-print loop (REPL) in which the model generates arbitrary control code, making execution difficult to verify, predict, and analyse.   We introduce $λ$-RLM, a framework for long-context reasoning that replaces free-form...

---

### 19. Spectral Alignment in Forward-Backward Representations via Temporal Abstraction

**Authors:** Seyed Mahdi B. Azad, Jasper Hoffmann, Iman Nematollahi, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20103v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20103v1)

**Summary:** Forward-backward (FB) representations provide a powerful framework for learning the successor representation (SR) in continuous spaces by enforcing a low-rank factorization. However, a fundamental spectral mismatch often exists between the high-rank transition dynamics of continuous environments and the low-rank bottleneck of the FB architecture, making accurate low-rank representation learning difficult. In this work, we analyze temporal abstraction as a mechanism to mitigate this mismatch. By ...

---

### 20. Pitfalls in Evaluating Interpretability Agents

**Authors:** Tal Haklay, Nikhil Prakash, Sana Pandey, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20101v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20101v1)

**Summary:** Automated interpretability systems aim to reduce the need for human labor and scale analysis to increasingly large models and diverse tasks. Recent efforts toward this goal leverage large language models (LLMs) at increasing levels of autonomy, ranging from fixed one-shot workflows to fully autonomous interpretability agents. This shift creates a corresponding need to scale evaluation approaches to keep pace with both the volume and complexity of generated explanations. We investigate this chall...

---

### 21. An Empirical Study of SFT-DPO Interaction and Parameterization in Small Language Models

**Authors:** Yuming Feng, Christy Yang

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20100v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20100v1)

**Summary:** Direct Preference Optimization (DPO) is widely used after supervised fine-tuning (SFT) to align language models, yet empirical behavior under small backbones and modest data is under-specified. We systematically compare SFT-only, DPO-only, and staged SFT-to-DPO training alongside full fine-tuning (FFT) versus LoRA on a GPT-2-scale decoder, evaluating paraphrase detection and Shakespearean sonnet continuation. DPO yields small, task-dependent gains over strong SFT and can match competitive SFT ac...

---

### 22. LLM-Enhanced Semantic Data Integration of Electronic Component Qualifications in the Aerospace Domain

**Authors:** Antonio De Santis, Marco Balduini, Matteo Belcao, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20094v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20094v1)

**Summary:** Large manufacturing companies face challenges in information retrieval due to data silos maintained by different departments, leading to inconsistencies and misalignment across databases. This paper presents an experience in integrating and retrieving qualification data for electronic components used in satellite board design. Due to data silos, designers cannot immediately determine the qualification status of individual components. However, this process is critical during the planning phase, w...

---

### 23. Agentic Harness for Real-World Compilers

**Authors:** Yingwei Zheng, Cong Li, Shaohua Li, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20075v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20075v1)

**Summary:** Compilers are critical to modern computing, yet fixing compiler bugs is difficult. While recent large language model (LLM) advancements enable automated bug repair, compiler bugs pose unique challenges due to their complexity, deep cross-domain expertise requirements, and sparse, non-descriptive bug reports, necessitating compiler-specific tools. To bridge the gap, we introduce llvm-autofix, the first agentic harness designed to assist LLM agents in understanding and fixing compiler bugs. Our fo...

---

### 24. Fine-tuning Timeseries Predictors Using Reinforcement Learning

**Authors:** Hugo Cazaux, Ralph Rudd, Hlynur Stefánsson, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20063v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20063v1)

**Summary:** This chapter presents three major reinforcement learning algorithms used for fine-tuning financial forecasters. We propose a clear implementation plan for backpropagating the loss of a reinforcement learning task to a model trained using supervised learning, and compare the performance before and after the fine-tuning. We find an increase in performance after fine-tuning, and transfer learning properties to the models, indicating the benefits of fine-tuning. We also highlight the tuning process ...

---

### 25. The End of Rented Discovery: How AI Search Redistributes Power Between Hotels and Intermediaries

**Authors:** Peiying Zhu, Sidi Chang

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20062v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20062v1)

**Summary:** When a traveler asks an AI search engine to recommend a hotel, which sources get cited -- and does query framing matter? We audit 1,357 grounding citations from Google Gemini across 156 hotel queries in Tokyo and document a systematic pattern we call the Intent-Source Divide. Experiential queries draw 55.9\% of their citations from non-OTA sources, compared to 30.8\% for transactional queries -- a 25.1 percentage-point gap ($p < 5 \times 10^{-20}$). The effect is amplified in Japanese, where exp...

---

### 26. DIAL-KG: Schema-Free Incremental Knowledge Graph Construction via Dynamic Schema Induction and Evolution-Intent Assessment

**Authors:** Weidong Bao, Yilin Wang, Ruyu Gao, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20059v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20059v1)

**Summary:** Knowledge Graphs (KGs) are foundational to applications such as search, question answering, and recommendation. Conventional knowledge graph construction methods are predominantly static, rely ing on a single-step construction from a fixed corpus with a prede f ined schema. However, such methods are suboptimal for real-world sce narios where data arrives dynamically, as incorporating new informa tion requires complete and computationally expensive graph reconstruc tions. Furthermore, predefined ...

---

### 27. Experience is the Best Teacher: Motivating Effective Exploration in Reinforcement Learning for LLMs

**Authors:** Wenjian Zhang, Kongcheng Zhang, Jiaxin Qi, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20046v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20046v1)

**Summary:** Reinforcement Learning (RL) with rubric-based rewards has recently shown remarkable progress in enhancing general reasoning capabilities of Large Language Models (LLMs), yet still suffers from ineffective exploration confined to curent policy distribution. In fact, RL optimization can be viewed as steering the policy toward an ideal distribution that maximizes the rewards, while effective exploration should align efforts with desired target. Leveraging this insight, we propose HeRL, a Hindsight ...

---

### 28. LoASR-Bench: Evaluating Large Speech Language Models on Low-Resource Automatic Speech Recognition Across Language Families

**Authors:** Jianan Chen, Xiaoxue Gao, Tatsuya Kawahara, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20042v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20042v1)

**Summary:** Large language models (LLMs) have driven substantial advances in speech language models (SpeechLMs), yielding strong performance in automatic speech recognition (ASR) under high-resource conditions. However, existing benchmarks predominantly focus on high-resource languages, leaving the ASR behavior of SpeechLMs in low-resource languages insufficiently understood. This gap is critical, as practical ASR systems must reliably support low-resource languages and generalize across diverse language fa...

---

### 29. CoverageBench: Evaluating Information Coverage across Tasks and Domains

**Authors:** Saron Samuel, Andrew Yates, Dawn Lawrie, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20034v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20034v1)

**Summary:** We wish to measure the information coverage of an ad hoc retrieval algorithm, that is, how much of the range of available relevant information is covered by the search results. Information coverage is a central aspect for retrieval, especially when the retrieval system is integrated with generative models in a retrieval-augmented generation (RAG) system. The classic metrics for ad hoc retrieval, precision and recall, reward a system as more and more relevant documents are retrieved. However, sin...

---

### 30. Orchestrating Human-AI Software Delivery: A Retrospective Longitudinal Field Study of Three Software Modernization Programs

**Authors:** Maximiliano Armesto, Christophe Kolb

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20028v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20028v1)

**Summary:** Evidence on AI in software engineering still leans heavily toward individual task completion, while evidence on team-level delivery remains scarce. We report a retrospective longitudinal field study of Chiron, an industrial platform that coordinates humans and AI agents across four delivery stages: analysis, planning, implementation, and validation. The study covers three real software modernization programs -- a COBOL banking migration (~30k LOC), a large accounting modernization (~400k LOC), a...

---

### 31. Detached Skip-Links and $R$-Probe: Decoupling Feature Aggregation from Gradient Propagation for MLLM OCR

**Authors:** Ziye Yuan, Ruchang Yao, Chengxin Zheng, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20020v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20020v1)

**Summary:** Multimodal large language models (MLLMs) excel at high-level reasoning yet fail on OCR tasks where fine-grained visual details are compromised or misaligned. We identify an overlooked optimization issue in multi-layer feature fusion. Skip pathways introduce direct back-propagation paths from high-level semantic objectives to early visual layers. This mechanism overwrites low-level signals and destabilizes training. To mitigate this gradient interference, we propose Detached Skip-Links, a minimal...

---

### 32. Physics-Informed Long-Range Coulomb Correction for Machine-learning Hamiltonians

**Authors:** Yang Zhong, Xiwen Li, Xingao Gong, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20007v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20007v1)

**Summary:** Machine-learning electronic Hamiltonians achieve orders-of-magnitude speedups over density-functional theory, yet current models omit long-range Coulomb interactions that govern physics in polar crystals and heterostructures. We derive closed-form long-range Hamiltonian matrix elements in a nonorthogonal atomic-orbital basis through variational decomposition of the electrostatic energy, deriving a variationally consistent mapping from the electron density matrix to effective atomic charges. We i...

---

### 33. Breaking the Capability Ceiling of LLM Post-Training by Reintroducing Markov States

**Authors:** Yurun Yuan, Tengyang Xie

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19987v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19987v1)

**Summary:** Reinforcement learning (RL) has become a standard paradigm for post-training and aligning Large Language Models (LLMs), yet recent evidence suggests it faces a persistent "capability ceiling": unlike classical RL systems that discover novel strategies, RL for LLMs often acts as a mere refiner of patterns already latent in pre-trained weights. In this work, we identify a fundamental structural bottleneck: while classical RL relies on compact, informative Markov states, current LLM post-training f...

---

### 34. X-World: Controllable Ego-Centric Multi-Camera World Models for Scalable End-to-End Driving

**Authors:** Chaoda Zheng, Sean Li, Jinhao Deng, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19979v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19979v1)

**Summary:** Scalable and reliable evaluation is increasingly critical in the end-to-end era of autonomous driving, where vision--language--action (VLA) policies directly map raw sensor streams to driving actions. Yet, current evaluation pipelines still rely heavily on real-world road testing, which is costly, biased toward limited scenario coverage, and difficult to reproduce. These challenges motivate a real-world simulator that can generate realistic future observations under proposed actions, while remai...

---

### 35. Promoting Critical Thinking With Domain-Specific Generative AI Provocations

**Authors:** Thomas Şerban von Davier, Hao-Ping Lee, Jodi Forlizzi, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19975v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19975v1)

**Summary:** The evidence on the effects of generative AI (GenAI) on critical thinking is mixed, with studies suggesting both potential harms and benefits depending on its implementation. Some argue that AI-driven provocations, such as questions asking for human clarification and justification, are beneficial for eliciting critical thinking. Drawing on our experience designing and evaluating two GenAI-powered tools for knowledge work, ArtBot in the domain of fine art interpretation and Privy in the domain of...

---

### 36. Trojan's Whisper: Stealthy Manipulation of OpenClaw through Injected Bootstrapped Guidance

**Authors:** Fazhong Liu, Zhuoyan Chen, Tu Lan, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19974v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19974v1)

**Summary:** Autonomous coding agents are increasingly integrated into software development workflows, offering capabilities that extend beyond code suggestion to active system interaction and environment management. OpenClaw, a representative platform in this emerging paradigm, introduces an extensible skill ecosystem that allows third-party developers to inject behavioral guidance through lifecycle hooks during agent initialization. While this design enhances automation and customization, it also opens a n...

---

### 37. Graph2TS: Structure-Controlled Time Series Generation via Quantile-Graph VAEs

**Authors:** Shaoshuai Du, Joze M. Rozanec, Andy Pimentel, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19970v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19970v1)

**Summary:** Although recent generative models can produce time series with close marginal distributions, they often face a fundamental tension between preserving global temporal structure and modeling stochastic local variations, particularly for highly volatile signals with weak or irregular periodicity. Direct distribution matching in such settings can amplify noise or suppress meaningful temporal patterns. In this work, we propose a structure-residual perspective on time-series generation, viewing tempor...

---

### 38. HiPath: Hierarchical Vision-Language Alignment for Structured Pathology Report Prediction

**Authors:** Ruicheng Yuan, Zhenxuan Zhang, Anbang Wang, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19957v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19957v1)

**Summary:** Pathology reports are structured, multi-granular documents encoding diagnostic conclusions, histological grades, and ancillary test results across one or more anatomical sites; yet existing pathology vision-language models (VLMs) reduce this output to a flat label or free-form text. We present HiPath, a lightweight VLM framework built on frozen UNI2 and Qwen3 backbones that treats structured report prediction as its primary training objective. Three trainable modules totalling 15M parameters add...

---

### 39. On the Ability of Transformers to Verify Plans

**Authors:** Yash Sarrof, Yupei Du, Katharina Stein, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19954v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19954v1)

**Summary:** Transformers have shown inconsistent success in AI planning tasks, and theoretical understanding of when generalization should be expected has been limited. We take important steps towards addressing this gap by analyzing the ability of decoder-only models to verify whether a given plan correctly solves a given planning instance. To analyse the general setting where the number of objects -- and thus the effective input alphabet -- grows at test time, we introduce C*-RASP, an extension of C-RASP ...

---

### 40. RAM: Recover Any 3D Human Motion in-the-Wild

**Authors:** Sen Jia, Ning Zhu, Jinqin Zhong, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19929v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19929v1)

**Summary:** RAM incorporates a motion-aware semantic tracker with adaptive Kalman filtering to achieve robust identity association under severe occlusions and dynamic interactions. A memory-augmented Temporal HMR module further enhances human motion reconstruction by injecting spatio-temporal priors for consistent and smooth motion estimation. Moreover, a lightweight Predictor module forecasts future poses to maintain reconstruction continuity, while a gated combiner adaptively fuses reconstructed and predi...

---

### 41. Span-Level Machine Translation Meta-Evaluation

**Authors:** Stefano Perrella, Eric Morales Agostinho, Hugo Zaragoza

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19921v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19921v1)

**Summary:** Machine Translation (MT) and automatic MT evaluation have improved dramatically in recent years, enabling numerous novel applications. Automatic evaluation techniques have evolved from producing scalar quality scores to precisely locating translation errors and assigning them error categories and severity levels. However, it remains unclear how to reliably measure the evaluation capabilities of auto-evaluators that do error detection, as no established technique exists in the literature. This wo...

---

### 42. Learning Like Humans: Analogical Concept Learning for Generalized Category Discovery

**Authors:** Jizhou Han, Chenhao Ding, Yuhang He, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19918v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19918v1)

**Summary:** Generalized Category Discovery (GCD) seeks to uncover novel categories in unlabeled data while preserving recognition of known categories, yet prevailing visual-only pipelines and the loose coupling between supervised learning and discovery often yield brittle boundaries on fine-grained, look-alike categories. We introduce the Analogical Textual Concept Generator (ATCG), a plug-and-play module that analogizes from labeled knowledge to new observations, forming textual concepts for unlabeled samp...

---

### 43. Revealing Domain-Spatiality Patterns for Configuration Tuning: Domain Knowledge Meets Fitness Landscapes

**Authors:** Yulong Ye, Hongyuan Liang, Chao Jiang, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19897v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19897v1)

**Summary:** Configuration tuning for better performance is crucial in quality assurance. Yet, there has long been a mystery on tuners' effectiveness, due to the black-box nature of configurable systems. Prior efforts predominantly adopt static domain analysis (e.g., static taint analysis), which often lacks generalizability, or dynamic data analysis (e.g., benchmarking performance analysis), limiting explainability. In this work, we embrace Fitness Landscape Analysis (FLA) as a bridge between domain knowled...

---

### 44. Utility-Guided Agent Orchestration for Efficient LLM Tool Use

**Authors:** Boyan Liu, Gongming Zhao, Hongli Xu

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19896v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19896v1)

**Summary:** Tool-using large language model (LLM) agents often face a fundamental tension between answer quality and execution cost. Fixed workflows are stable but inflexible, while free-form multi-step reasoning methods such as ReAct may improve task performance at the expense of excessive tool calls, longer trajectories, higher token consumption, and increased latency. In this paper, we study agent orchestration as an explicit decision problem rather than leaving it entirely to prompt-level behavior. We p...

---

### 45. Integrating Meta-Features with Knowledge Graph Embeddings for Meta-Learning

**Authors:** Antonis Klironomos, Ioannis Dasoulas, Francesco Periti, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19888v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19888v1)

**Summary:** The vast collection of machine learning records available on the web presents a significant opportunity for meta-learning, where past experiments are leveraged to improve performance. Two crucial meta-learning tasks are pipeline performance estimation (PPE), which predicts pipeline performance on target datasets, and dataset performance-based similarity estimation (DPSE), which identifies datasets with similar performance patterns. Existing approaches primarily rely on dataset meta-features (e.g...

---

### 46. What If Consensus Lies? Selective-Complementary Reinforcement Learning at Test Time

**Authors:** Dong Yan, Jian Liang, Yanbo Wang, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19880v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19880v1)

**Summary:** Test-Time Reinforcement Learning (TTRL) enables Large Language Models (LLMs) to enhance reasoning capabilities on unlabeled test streams by deriving pseudo-rewards from majority voting consensus. However, existing TTRL methods rely exclusively on positive pseudo-labeling strategies. Such reliance becomes vulnerable under challenging scenarios where answer distributions are highly dispersed, resulting in weak consensus that inadvertently reinforces incorrect trajectories as supervision signals. I...

---

### 47. Failure Modes for Deep Learning-Based Online Mapping: How to Measure and Address Them

**Authors:** Michael Hubbertz, Qi Han, Tobias Meisen

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19852v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19852v1)

**Summary:** Deep learning-based online mapping has emerged as a cornerstone of autonomous driving, yet these models frequently fail to generalize beyond familiar environments. We propose a framework to identify and measure the underlying failure modes by disentangling two effects: Memorization of input features and overfitting to known map geometries. We propose measures based on evaluation subsets that control for geographical proximity and geometric similarity between training and validation scenes. We in...

---

### 48. Semantic Delta: An Interpretable Signal Differentiating Human and LLMs Dialogue

**Authors:** Riccardo Scantamburlo, Mauro Mezzanzana, Giacomo Buonanno, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19849v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19849v1)

**Summary:** Do LLMs talk like us? This question intrigues a multitude of scholar and it is relevant in many fields, from education to academia. This work presents an interpretable statistical feature for distinguishing human written and LLMs generated dialogue. We introduce a lightweight metric derived from semantic categories distribution. Using the Empath lexical analysis framework, each text is mapped to a set of thematic intensity scores. We define semantic delta as the difference between the two most d...

---

### 49. Gesture2Speech: How Far Can Hand Movements Shape Expressive Speech?

**Authors:** Lokesh Kumar, Nirmesh Shah, Ashishkumar P. Gudmalwar, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19831v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19831v1)

**Summary:** Human communication seamlessly integrates speech and bodily motion, where hand gestures naturally complement vocal prosody to express intent, emotion, and emphasis. While recent text-to-speech (TTS) systems have begun incorporating multimodal cues such as facial expressions or lip movements, the role of hand gestures in shaping prosody remains largely underexplored. We propose a novel multimodal TTS framework, Gesture2Speech, that leverages visual gesture cues to modulate prosody in synthesized ...

---

### 50. FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization

**Authors:** Haijian Lu, Wei Wang, Jing Liu

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19828v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19828v1)

**Summary:** Autoformalization aims to translate natural-language mathematics into compilable, machine-checkable statements. However, semantic consistency does not imply prover effectiveness: even semantically consistent formalizations can differ substantially in proof-search cost and success rate. In this work, we formulate autoformalization as a budgeted, test-time search for semantically consistent repertoires, and propose FormalEvolve, a compilation-gated neuro-symbolic evolutionary framework. FormalEvol...

---

## cs.CL

**50 papers**

### 1. VideoSeek: Long-Horizon Video Agent with Tool-Guided Seeking

**Authors:** Jingyang Lin, Jialian Wu, Jiang Liu, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20185v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20185v1)

**Summary:** Video agentic models have advanced challenging video-language tasks. However, most agentic approaches still heavily rely on greedy parsing over densely sampled video frames, resulting in high computational cost. We present VideoSeek, a long-horizon video agent that leverages video logic flow to actively seek answer-critical evidence instead of exhaustively parsing the full video. This insight allows the model to use far fewer frames while maintaining, or even improving, its video understanding c...

---

### 2. Adaptive Greedy Frame Selection for Long Video Understanding

**Authors:** Yuning Huang, Fengqing Zhu

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20180v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20180v1)

**Summary:** Large vision--language models (VLMs) are increasingly applied to long-video question answering, yet inference is often bottlenecked by the number of input frames and resulting visual tokens. Naive sparse sampling can miss decisive moments, while purely relevance-driven selection frequently collapses onto near-duplicate frames and sacrifices coverage of temporally distant evidence. We propose a question-adaptive greedy frame selection method that jointly optimizes query relevance and semantic rep...

---

### 3. Measuring Faithfulness Depends on How You Measure: Classifier Sensitivity in LLM Chain-of-Thought Evaluation

**Authors:** Richard J. Young

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20172v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20172v1)

**Summary:** Recent work on chain-of-thought (CoT) faithfulness reports single aggregate numbers (e.g., DeepSeek-R1 acknowledges hints 39% of the time), implying that faithfulness is an objective, measurable property of a model. This paper demonstrates that it is not. Three classifiers (a regex-only detector, a two-stage regex-plus-LLM pipeline, and an independent Claude Sonnet 4 judge) are applied to 10,276 influenced reasoning traces from 12 open-weight models spanning 9 families and 7B to 1T parameters. O...

---

### 4. Evaluating Evidence Grounding Under User Pressure in Instruction-Tuned Language Models

**Authors:** Sai Koneru, Elphin Joe, Christine Kirchhoff, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20162v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20162v1)

**Summary:** In contested domains, instruction-tuned language models must balance user-alignment pressures against faithfulness to the in-context evidence. To evaluate this tension, we introduce a controlled epistemic-conflict framework grounded in the U.S. National Climate Assessment. We conduct fine-grained ablations over evidence composition and uncertainty cues across 19 instruction-tuned models spanning 0.27B to 32B parameters. Across neutral prompts, richer evidence generally improves evidence-consiste...

---

### 5. Semantic Token Clustering for Efficient Uncertainty Quantification in Large Language Models

**Authors:** Qi Cao, Andrew Gambardella, Takeshi Kojima, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20161v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20161v1)

**Summary:** Large language models (LLMs) have demonstrated remarkable capabilities across diverse tasks. However, the truthfulness of their outputs is not guaranteed, and their tendency toward overconfidence further limits reliability. Uncertainty quantification offers a promising way to identify potentially unreliable outputs, but most existing methods rely on repeated sampling or auxiliary models, introducing substantial computational overhead. To address these limitations, we propose Semantic Token Clust...

---

### 6. Enhancing Hyperspace Analogue to Language (HAL) Representations via Attention-Based Pooling for Text Classification

**Authors:** Ali Sakour, Zoalfekar Sakour

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20149v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20149v1)

**Summary:** The Hyperspace Analogue to Language (HAL) model relies on global word co-occurrence matrices to construct distributional semantic representations. While these representations capture lexical relationships effectively, aggregating them into sentence-level embeddings via standard mean pooling often results in information loss. Mean pooling assigns equal weight to all tokens, thereby diluting the impact of contextually salient words with uninformative structural tokens. In this paper, we address th...

---

### 7. Reasoning Gets Harder for LLMs Inside A Dialogue

**Authors:** Ivan Kartáč, Mateusz Lango, Ondřej Dušek

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20133v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20133v1)

**Summary:** Large Language Models (LLMs) achieve strong performance on many reasoning benchmarks, yet these evaluations typically focus on isolated tasks that differ from real-world usage in task-oriented dialogue (TOD). In this setting, LLMs must perform reasoning inherently while generating text and adhering to instructions on role, format, and style. This mismatch raises concerns about whether benchmark performance accurately reflects models' reasoning robustness in TOD setting. We investigate how framin...

---

### 8. Current LLMs still cannot 'talk much' about grammar modules: Evidence from syntax

**Authors:** Mohammed Q. Shormani

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20114v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20114v1)

**Summary:** We aim to examine the extent to which Large Language Models (LLMs) can 'talk much' about grammar modules, providing evidence from syntax core properties translated by ChatGPT into Arabic. We collected 44 terms from generative syntax previous works, including books and journal articles, as well as from our experience in the field. These terms were translated by humans, and then by ChatGPT-5. We then analyzed and compared both translations. We used an analytical and comparative approach in our ana...

---

### 9. An Empirical Study of SFT-DPO Interaction and Parameterization in Small Language Models

**Authors:** Yuming Feng, Christy Yang

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20100v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20100v1)

**Summary:** Direct Preference Optimization (DPO) is widely used after supervised fine-tuning (SFT) to align language models, yet empirical behavior under small backbones and modest data is under-specified. We systematically compare SFT-only, DPO-only, and staged SFT-to-DPO training alongside full fine-tuning (FFT) versus LoRA on a GPT-2-scale decoder, evaluating paraphrase detection and Shakespearean sonnet continuation. DPO yields small, task-dependent gains over strong SFT and can match competitive SFT ac...

---

### 10. Predicting States of Understanding in Explanatory Interactions Using Cognitive Load-Related Linguistic Cues

**Authors:** Yu Wang, Olcay Türk, Angela Grimminger, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20079v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20079v1)

**Summary:** We investigate how verbal and nonverbal linguistic features, exhibited by speakers and listeners in dialogue, can contribute to predicting the listener's state of understanding in explanatory interactions on a moment-by-moment basis. Specifically, we examine three linguistic cues related to cognitive load and hypothesised to correlate with listener understanding: the information value (operationalised with surprisal) and syntactic complexity of the speaker's utterances, and the variation in the ...

---

### 11. LoASR-Bench: Evaluating Large Speech Language Models on Low-Resource Automatic Speech Recognition Across Language Families

**Authors:** Jianan Chen, Xiaoxue Gao, Tatsuya Kawahara, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20042v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20042v1)

**Summary:** Large language models (LLMs) have driven substantial advances in speech language models (SpeechLMs), yielding strong performance in automatic speech recognition (ASR) under high-resource conditions. However, existing benchmarks predominantly focus on high-resource languages, leaving the ASR behavior of SpeechLMs in low-resource languages insufficiently understood. This gap is critical, as practical ASR systems must reliably support low-resource languages and generalize across diverse language fa...

---

### 12. RouterKGQA: Specialized--General Model Routing for Constraint-Aware Knowledge Graph Question Answering

**Authors:** Bo Yuan, Hexuan Deng, Xuebo Liu, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20017v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20017v1)

**Summary:** Knowledge graph question answering (KGQA) is a promising approach for mitigating LLM hallucination by grounding reasoning in structured and verifiable knowledge graphs. Existing approaches fall into two paradigms: retrieval-based methods utilize small specialized models, which are efficient but often produce unreachable paths and miss implicit constraints, while agent-based methods utilize large general models, which achieve stronger structural grounding at substantially higher cost. We propose ...

---

### 13. ReViSQL: Achieving Human-Level Text-to-SQL

**Authors:** Yuxuan Zhu, Tengjun Jin, Yoojin Choi, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20004v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20004v1)

**Summary:** Translating natural language to SQL (Text-to-SQL) is a critical challenge in both database research and data analytics applications. Recent efforts have focused on enhancing SQL reasoning by developing large language models and AI agents that decompose Text-to-SQL tasks into manually designed, step-by-step pipelines. However, despite these extensive architectural engineering efforts, a significant gap remains: even state-of-the-art (SOTA) AI agents have not yet achieved the human-level accuracy ...

---

### 14. An Agentic Approach to Generating XAI-Narratives

**Authors:** Yifan He, David Martens

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20003v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20003v1)

**Summary:** Explainable AI (XAI) research has experienced substantial growth in recent years. Existing XAI methods, however, have been criticized for being technical and expert-oriented, motivating the development of more interpretable and accessible explanations. In response, large language model (LLM)-generated XAI narratives have been proposed as a promising approach for translating post-hoc explanations into more accessible, natural-language explanations. In this work, we propose a multi-agent framework...

---

### 15. When Contextual Inference Fails: Cancelability in Interactive Instruction Following

**Authors:** Natalia Bila, Kata Naszádi, Alexandra Mayn, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19997v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19997v1)

**Summary:** We investigate the separation of literal interpretation from contextual inference in a collaborative block-building task where a builder must resolve underspecified instructions using contextual inferences. Building on an existing two-speaker psycholinguistic paradigm -- which contrasts a pragmatically cooperative speaker with one who is only literally reliable -- we introduce Build What I Mean (BWIM), an interactive benchmark for contextual meaning construction. In BWIM, models must resolve amb...

---

### 16. Breaking the Capability Ceiling of LLM Post-Training by Reintroducing Markov States

**Authors:** Yurun Yuan, Tengyang Xie

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19987v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19987v1)

**Summary:** Reinforcement learning (RL) has become a standard paradigm for post-training and aligning Large Language Models (LLMs), yet recent evidence suggests it faces a persistent "capability ceiling": unlike classical RL systems that discover novel strategies, RL for LLMs often acts as a mere refiner of patterns already latent in pre-trained weights. In this work, we identify a fundamental structural bottleneck: while classical RL relies on compact, informative Markov states, current LLM post-training f...

---

### 17. On the Ability of Transformers to Verify Plans

**Authors:** Yash Sarrof, Yupei Du, Katharina Stein, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19954v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19954v1)

**Summary:** Transformers have shown inconsistent success in AI planning tasks, and theoretical understanding of when generalization should be expected has been limited. We take important steps towards addressing this gap by analyzing the ability of decoder-only models to verify whether a given plan correctly solves a given planning instance. To analyse the general setting where the number of objects -- and thus the effective input alphabet -- grows at test time, we introduce C*-RASP, an extension of C-RASP ...

---

### 18. Hybrid topic modelling for computational close reading: Mapping narrative themes in Pushkin's Evgenij Onegin

**Authors:** Angelo Maria Sabatini

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19940v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19940v1)

**Summary:** This study presents a hybrid topic modelling framework for computational literary analysis that integrates Latent Dirichlet Allocation (LDA) with sparse Partial Least Squares Discriminant Analysis (sPLS-DA) to model thematic structure and longitudinal dynamics in narrative poetry. As a case study, we analyse Evgenij Onegin-Aleksandr S. Pushkin's novel in verse-using an Italian translation, testing whether unsupervised and supervised lexical structures converge in a small-corpus setting. The poet...

---

### 19. SAGE: Sustainable Agent-Guided Expert-tuning for Culturally Attuned Translation in Low-Resource Southeast Asia

**Authors:** Zhixiang Lu, Chong Zhang, Yulong Li, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19931v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19931v1)

**Summary:** The vision of an inclusive World Wide Web is impeded by a severe linguistic divide, particularly for communities in low-resource regions of Southeast Asia. While large language models (LLMs) offer a potential solution for translation, their deployment in data-poor contexts faces a dual challenge: the scarcity of high-quality, culturally relevant data and the prohibitive energy costs of training on massive, noisy web corpora. To resolve the tension between digital inclusion and environmental sust...

---

### 20. Translation from the Information Bottleneck Perspective: an Efficiency Analysis of Spatial Prepositions in Bitexts

**Authors:** Antoine Taroni, Ludovic Moncla, Frederique Laforest

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19924v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19924v1)

**Summary:** Efficient communication requires balancing informativity and simplicity when encoding meanings. The Information Bottleneck (IB) framework captures this trade-off formally, predicting that natural language systems cluster near an optimal accuracy-complexity frontier. While supported in visual domains such as colour and motion, linguistic stimuli such as words in sentential context remain unexplored. We address this gap by framing translation as an IB optimisation problem, treating source sentence...

---

### 21. Span-Level Machine Translation Meta-Evaluation

**Authors:** Stefano Perrella, Eric Morales Agostinho, Hugo Zaragoza

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19921v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19921v1)

**Summary:** Machine Translation (MT) and automatic MT evaluation have improved dramatically in recent years, enabling numerous novel applications. Automatic evaluation techniques have evolved from producing scalar quality scores to precisely locating translation errors and assigning them error categories and severity levels. However, it remains unclear how to reliably measure the evaluation capabilities of auto-evaluators that do error detection, as no established technique exists in the literature. This wo...

---

### 22. Semantic Delta: An Interpretable Signal Differentiating Human and LLMs Dialogue

**Authors:** Riccardo Scantamburlo, Mauro Mezzanzana, Giacomo Buonanno, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19849v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19849v1)

**Summary:** Do LLMs talk like us? This question intrigues a multitude of scholar and it is relevant in many fields, from education to academia. This work presents an interpretable statistical feature for distinguishing human written and LLMs generated dialogue. We introduce a lightweight metric derived from semantic categories distribution. Using the Empath lexical analysis framework, each text is mapped to a set of thematic intensity scores. We define semantic delta as the difference between the two most d...

---

### 23. Overreliance on AI in Information-seeking from Video Content

**Authors:** Anders Giovanni Møller, Elisa Bassignana, Francesco Pierri, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19843v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19843v1)

**Summary:** The ubiquity of multimedia content is reshaping online information spaces, particularly in social media environments. At the same time, search is being rapidly transformed by generative AI, with large language models (LLMs) routinely deployed as intermediaries between users and multimedia content to retrieve and summarize information. Despite their growing influence, the impact of LLM inaccuracies and potential vulnerabilities on multimedia information-seeking tasks remains largely unexplored. W...

---

### 24. FrameNet Semantic Role Classification by Analogy

**Authors:** Van-Duy Ngo, Stergos Afantenos, Emiliano Lorini, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19825v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19825v1)

**Summary:** In this paper, we adopt a relational view of analogies applied to Semantic Role Classification in FrameNet. We define analogies as formal relations over the Cartesian product of frame evoking lexical units (LUs) and frame element (FEs) pairs, which we use to construct a new dataset. Each element of this binary relation is labelled as a valid analogical instance if the frame elements share the same semantic role, or as invalid otherwise. This formulation allows us to transform Semantic Role Class...

---

### 25. Borderless Long Speech Synthesis

**Authors:** Xingchen Song, Di Wu, Dinghao Zhou, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19798v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19798v1)

**Summary:** Most existing text-to-speech (TTS) systems either synthesize speech sentence by sentence and stitch the results together, or drive synthesis from plain-text dialogues alone. Both approaches leave models with little understanding of global context or paralinguistic cues, making it hard to capture real-world phenomena such as multi-speaker interactions (interruptions, overlapping speech), evolving emotional arcs, and varied acoustic environments. We introduce the Borderless Long Speech Synthesis f...

---

### 26. Neither Here Nor There: Cross-Lingual Representation Dynamics of Code-Mixed Text in Multilingual Encoders

**Authors:** Debajyoti Mazumder, Divyansh Pathak, Prashant Kodali, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19771v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19771v1)

**Summary:** Multilingual encoder-based language models are widely adopted for code-mixed analysis tasks, yet we know surprisingly little about how they represent code-mixed inputs internally - or whether those representations meaningfully connect to the constituent languages being mixed. Using Hindi-English as a case study, we construct a unified trilingual corpus of parallel English, Hindi (Devanagari), and Romanized code-mixed sentences, and probe cross-lingual representation alignment across standard mul...

---

### 27. Rethinking Ground Truth: A Case Study on Human Label Variation in MLLM Benchmarking

**Authors:** Tomas Ruiz, Tanalp Agustoslu, Carsten Schwemmer

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19744v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19744v1)

**Summary:** Human Label Variation (HLV), i.e. systematic differences among annotators' judgments, remains underexplored in benchmarks despite rapid progress in large language model (LLM) development. We address this gap by introducing an evaluation protocol for multimodal large language model (MLLM) benchmarking that explicitly accounts for two conditions: (1) human label agreement and (2) disagreement. We apply this protocol to two state-of-the-art MLLM families (Gemma 3, Qwen 2.5 VL) using non-aggregated ...

---

### 28. Dual Path Attribution: Efficient Attribution for SwiGLU-Transformers through Layer-Wise Target Propagation

**Authors:** Lasse Marten Jantsch, Dong-Jae Koh, Seonghyeon Lee, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19742v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19742v1)

**Summary:** Understanding the internal mechanisms of transformer-based large language models (LLMs) is crucial for their reliable deployment and effective operation. While recent efforts have yielded a plethora of attribution methods attempting to balance faithfulness and computational efficiency, dense component attribution remains prohibitively expensive. In this work, we introduce Dual Path Attribution (DPA), a novel framework that faithfully traces information flow on the frozen transformer in one forwa...

---

### 29. FedPDPO: Federated Personalized Direct Preference Optimization for Large Language Model Alignment

**Authors:** Kewen Zhu, Liping Yi, Zhiming Zhao, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19741v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19741v1)

**Summary:** Aligning large language models (LLMs) with human preferences in federated learning (FL) is challenging due to decentralized, privacy-sensitive, and highly non-IID preference data. Direct Preference Optimization (DPO) offers an efficient alternative to reinforcement learning with human feedback (RLHF), but its direct application in FL suffers from severe performance degradation under non-IID data and limited generalization of implicit rewards. To bridge this gap, we propose FedPDPO (Federated Per...

---

### 30. MOSS-TTSD: Text to Spoken Dialogue Generation

**Authors:** Yuqian Zhang, Donghua Yu, Zhengyuan Lin, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19739v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19739v1)

**Summary:** Spoken dialogue generation is crucial for applications like podcasts, dynamic commentary, and entertainment content, but poses significant challenges compared to single-utterance text-to-speech (TTS). Key requirements include accurate turn-taking, cross-turn acoustic consistency, and long-form stability, which current models often fail to address due to a lack of dialogue context modeling. To bridge this gap, we present MOSS-TTSD, a spoken dialogue synthesis model designed for expressive, multi-...

---

### 31. PoC: Performance-oriented Context Compression for Large Language Models via Performance Prediction

**Authors:** Runsong Zhao, Shilei Liu, Jiwei Tang, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19733v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19733v1)

**Summary:** While context compression can mitigate the growing inference costs of Large Language Models (LLMs) by shortening contexts, existing methods that specify a target compression ratio or length suffer from unpredictable performance degradation, hindering their reliable deployment. We introduce a paradigm shift to Performance-oriented Context Compression (PoC), where developers specify an acceptable performance floor instead of a compression ratio. PoC employs a lightweight performance predictor to a...

---

### 32. LoopRPT: Reinforcement Pre-Training for Looped Language Models

**Authors:** Guo Tang, Shixin Jiang, Heng Chang, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19714v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19714v1)

**Summary:** Looped language models (LoopLMs) perform iterative latent computation to refine internal representations, offering a promising alternative to explicit chain-of-thought (CoT) reasoning. However, existing reinforcement learning (RL) paradigms primarily target output tokens, creating a structural mismatch with looped architectures whose reasoning unfolds implicitly. In this work, we propose LoopRPT, a reinforcement pre-training framework tailored for LoopLMs. By reframing next-token prediction as a...

---

### 33. TAB-AUDIT: Detecting AI-Fabricated Scientific Tables via Multi-View Likelihood Mismatch

**Authors:** Shuo Huang, Yan Pen, Lizhen Qu

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19712v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19712v1)

**Summary:** AI-generated fabricated scientific manuscripts raise growing concerns with large-scale breaches of academic integrity. In this work, we present the first systematic study on detecting AI-generated fabricated scientific tables in empirical NLP papers, as information in tables serve as critical evidence for claims. We construct FabTab, the first benchmark dataset of fabricated manuscripts with tables, comprising 1,173 AI-generated papers and 1,215 human-authored ones in empirical NLP. Through a co...

---

### 34. EvoTaxo: Building and Evolving Taxonomy from Social Media Streams

**Authors:** Yiyang Li, Tianyi Ma, Yanfang Ye

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19711v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19711v1)

**Summary:** Constructing taxonomies from social media corpora is challenging because posts are short, noisy, semantically entangled, and temporally dynamic. Existing taxonomy induction methods are largely designed for static corpora and often struggle to balance robustness, scalability, and sensitivity to evolving discourse. We propose EvoTaxo, a LLM-based framework for building and evolving taxonomies from temporally ordered social media streams. Rather than clustering raw posts directly, EvoTaxo converts ...

---

### 35. DataProphet: Demystifying Supervision Data Generalization in Multimodal LLMs

**Authors:** Xuan Qi, Luxi He, Dan Roth, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19688v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19688v1)

**Summary:** Conventional wisdom for selecting supervision data for multimodal large language models (MLLMs) is to prioritize datasets that appear similar to the target benchmark, such as text-intensive or vision-centric tasks. However, it remains unclear whether such intuitive similarity reliably predicts downstream performance gains. In this work, we take a first step toward answering a practical question: can we estimate the influence of a training dataset on a target benchmark before any training is perf...

---

### 36. Structured Prompting for Arabic Essay Proficiency: A Trait-Centric Evaluation Approach

**Authors:** Salim Al Mandhari, Hieu Pham Dinh, Mo El-Haj, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19668v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19668v1)

**Summary:** This paper presents a novel prompt engineering framework for trait specific Automatic Essay Scoring (AES) in Arabic, leveraging large language models (LLMs) under zero-shot and few-shot configurations. Addressing the scarcity of scalable, linguistically informed AES tools for Arabic, we introduce a three-tier prompting strategy (standard, hybrid, and rubric-guided) that guides LLMs in evaluating distinct language proficiency traits such as organization, vocabulary, development, and style. The hy...

---

### 37. BEAVER: A Training-Free Hierarchical Prompt Compression Method via Structure-Aware Page Selection

**Authors:** Zhengpei Hu, Kai Li, Dapeng Fu, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19635v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19635v1)

**Summary:** The exponential expansion of context windows in LLMs has unlocked capabilities for long-document understanding but introduced severe bottlenecks in inference latency and information utilization. Existing compression methods often suffer from high training costs or semantic fragmentation due to aggressive token pruning. In this paper, we propose BEAVER, a novel training-free framework that shifts compression from linear token removal to structure-aware hierarchical selection. BEAVER maximizes har...

---

### 38. CAF-Score: Calibrating CLAP with LALMs for Reference-free Audio Captioning Evaluation

**Authors:** Insung Lee, Taeyoung Jeong, Haejun Yoo, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19615v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19615v1)

**Summary:** While Large Audio-Language Models (LALMs) have advanced audio captioning, robust evaluation remains difficult. Reference-based metrics are expensive and often fail to assess acoustic fidelity, while Contrastive Language-Audio Pretraining (CLAP)-based approaches frequently overlook syntactic errors and fine-grained details. We propose CAF-Score, a reference-free metric that calibrates CLAP's coarse-grained semantic alignment with the fine-grained comprehension and syntactic awareness of LALMs. By...

---

### 39. All-Mem: Agentic Lifelong Memory via Dynamic Topology Evolution

**Authors:** Can Lv, Heng Chang, Yuchen Guo, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19595v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19595v1)

**Summary:** Lifelong interactive agents are expected to assist users over months or years, which requires continually writing long term memories while retrieving the right evidence for each new query under fixed context and latency budgets. Existing memory systems often degrade as histories grow, yielding redundant, outdated, or noisy retrieved contexts. We present All-Mem, an online/offline lifelong memory framework that maintains a topology structured memory bank via explicit, non destructive consolidatio...

---

### 40. AI Psychosis: Does Conversational AI Amplify Delusion-Related Language?

**Authors:** Soorya Ram Shimgekar, Vipin Gunda, Jiwon Kim, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19574v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19574v1)

**Summary:** Conversational AI systems are increasingly used for personal reflection and emotional disclosure, raising concerns about their effects on vulnerable users. Recent anecdotal reports suggest that prolonged interactions with AI may reinforce delusional thinking -- a phenomenon sometimes described as AI Psychosis. However, empirical evidence on this phenomenon remains limited. In this work, we examine how delusion-related language evolves during multi-turn interactions with conversational AI. We con...

---

### 41. TextReasoningBench: Does Reasoning Really Improve Text Classification in Large Language Models?

**Authors:** Xinyu Guo, Yazhou Zhang, Jing Qin

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19558v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19558v1)

**Summary:** Eliciting explicit, step-by-step reasoning traces from large language models (LLMs) has emerged as a dominant paradigm for enhancing model capabilities. Although such reasoning strategies were originally designed for problems requiring explicit multi-step reasoning, they have increasingly been applied to a broad range of NLP tasks. This expansion implicitly assumes that deliberative reasoning uniformly benefits heterogeneous tasks. However, whether such reasoning mechanisms truly benefit classif...

---

### 42. FDARxBench: Benchmarking Regulatory and Clinical Reasoning on FDA Generic Drug Assessment

**Authors:** Betty Xiong, Jillian Fisher, Benjamin Newman, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19539v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19539v1)

**Summary:** We introduce an expert curated, real-world benchmark for evaluating document-grounded question-answering (QA) motivated by generic drug assessment, using the U.S. Food and Drug Administration (FDA) drug label documents. Drug labels contain rich but heterogeneous clinical and regulatory information, making accurate question answering difficult for current language models. In collaboration with FDA regulatory assessors, we introduce FDARxBench, and construct a multi-stage pipeline for generating h...

---

### 43. EvidenceRL: Reinforcing Evidence Consistency for Trustworthy Language Models

**Authors:** J. Ben Tamo, Yuxing Lu, Benoit L. Marteau, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19532v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19532v1)

**Summary:** Large Language Models (LLMs) are fluent but prone to hallucinations, producing answers that appear plausible yet are unsupported by available evidence. This failure is especially problematic in high-stakes domains where decisions must be justified by verifiable information. We introduce \textbf{EvidenceRL}, a reinforcement learning framework that enforces evidence adherence during training. EvidenceRL scores candidate responses for grounding (entailment with retrieved evidence and context) and c...

---

### 44. Inducing Sustained Creativity and Diversity in Large Language Models

**Authors:** Queenie Luo, Gary King, Michael Puett, et al.

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.19519v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19519v1)

**Summary:** We address a not-widely-recognized subset of exploratory search, where a user sets out on a typically long "search quest" for the perfect wedding dress, overlooked research topic, killer company idea, etc. The first few outputs of current large language models (LLMs) may be helpful but only as a start, since the quest requires learning the search space and evaluating many diverse and creative alternatives along the way. Although LLMs encode an impressive fraction of the world's knowledge, common...

---

### 45. Cooperation and Exploitation in LLM Policy Synthesis for Sequential Social Dilemmas

**Authors:** Víctor Gallego

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.19453v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19453v1)

**Summary:** We study LLM policy synthesis: using a large language model to iteratively generate programmatic agent policies for multi-agent environments. Rather than training neural policies via reinforcement learning, our framework prompts an LLM to produce Python policy functions, evaluates them in self-play, and refines them using performance feedback across iterations. We investigate feedback engineering (the design of what evaluation information is shown to the LLM during refinement) comparing sparse f...

---

### 46. Vocabulary shapes cross-lingual variation of word-order learnability in language models

**Authors:** Jonas Mayer Martins, Jaap Jumelet, Viola Priesemann, et al.

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.19427v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19427v1)

**Summary:** Why do some languages like Czech permit free word order, while others like English do not? We address this question by pretraining transformer language models on a spectrum of synthetic word-order variants of natural languages. We observe that greater word-order irregularity consistently raises model surprisal, indicating reduced learnability. Sentence reversal, however, affects learnability only weakly. A coarse distinction of free- (e.g., Czech and Finnish) and fixed-word-order languages (e.g....

---

### 47. Is Evaluation Awareness Just Format Sensitivity? Limitations of Probe-Based Evidence under Controlled Prompt Structure

**Authors:** Viliana Devbunova

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.19426v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19426v1)

**Summary:** Prior work uses linear probes on benchmark prompts as evidence of evaluation awareness in large language models. Because evaluation context is typically entangled with benchmark format and genre, it is unclear whether probe-based signals reflect context or surface structure. We test whether these signals persist under partial control of prompt format using a controlled 2x2 dataset and diagnostic rewrites. We find that probes primarily track benchmark-canonical structure and fail to generalize to...

---

### 48. Scalable Prompt Routing via Fine-Grained Latent Task Discovery

**Authors:** Yunyi Zhang, Soji Adeshina, Patrick Guan, et al.

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.19415v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19415v1)

**Summary:** Prompt routing dynamically selects the most appropriate large language model from a pool of candidates for each query, optimizing performance while managing costs. As model pools scale to include dozens of frontier models with narrow performance gaps, existing approaches face significant challenges: manually defined task taxonomies cannot capture fine-grained capability distinctions, while monolithic routers struggle to differentiate subtle differences across diverse tasks. We propose a two-stag...

---

### 49. FinTradeBench: A Financial Reasoning Benchmark for LLMs

**Authors:** Yogesh Agrawal, Aniruddha Dutta, Md Mahadi Hasan, et al.

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.19225v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19225v1)

**Summary:** Real-world financial decision-making is a challenging problem that requires reasoning over heterogeneous signals, including company fundamentals derived from regulatory filings and trading signals computed from price dynamics. Recently, with the advancement of Large Language Models (LLMs), financial analysts have begun to use them for financial decision-making tasks. However, existing financial question answering benchmarks for testing these models primarily focus on company balance sheet data a...

---

### 50. F2LLM-v2: Inclusive, Performant, and Efficient Embeddings for a Multilingual World

**Authors:** Ziyin Zhang, Zihan Liao, Hang Yu, et al.

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.19223v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19223v1)

**Summary:** We present F2LLM-v2, a new family of general-purpose, multilingual embedding models in 8 distinct sizes ranging from 80M to 14B. Trained on a newly curated composite of 60 million publicly available high-quality data samples, F2LLM-v2 supports more than 200 languages, with a particular emphasis on previously underserved mid- and low-resource languages. By integrating a two-stage LLM-based embedding training pipeline with matryoshka learning, model pruning, and knowledge distillation techniques, ...

---

## cs.CV

**50 papers**

### 1. MME-CoF-Pro: Evaluating Reasoning Coherence in Video Generative Models with Text and Visual Hints

**Authors:** Yu Qi, Xinyi Xu, Ziyu Guo, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20194v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20194v1)

**Summary:** Video generative models show emerging reasoning behaviors. It is essential to ensure that generated events remain causally consistent across frames for reliable deployment, a property we define as reasoning coherence. To bridge the gap in literature for missing reasoning coherence evaluation, we propose MME-CoF-Pro, a comprehensive video reasoning benchmark to assess reasoning coherence in video models. Specifically, MME-CoF-Pro contains 303 samples across 16 categories, ranging from visual logi...

---

### 2. From Masks to Pixels and Meaning: A New Taxonomy, Benchmark, and Metrics for VLM Image Tampering

**Authors:** Xinyi Shang, Yi Tang, Jiacheng Cui, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20193v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20193v1)

**Summary:** Existing tampering detection benchmarks largely rely on object masks, which severely misalign with the true edit signal: many pixels inside a mask are untouched or only trivially modified, while subtle yet consequential edits outside the mask are treated as natural. We reformulate VLM image tampering from coarse region labels to a pixel-grounded, meaning and language-aware task. First, we introduce a taxonomy spanning edit primitives (replace/remove/splice/inpaint/attribute/colorization, etc.) a...

---

### 3. LumosX: Relate Any Identities with Their Attributes for Personalized Video Generation

**Authors:** Jiazheng Xing, Fei Du, Hangjie Yuan, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20192v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20192v1)

**Summary:** Recent advances in diffusion models have significantly improved text-to-video generation, enabling personalized content creation with fine-grained control over both foreground and background elements. However, precise face-attribute alignment across subjects remains challenging, as existing methods lack explicit mechanisms to ensure intra-group consistency. Addressing this gap requires both explicit modeling strategies and face-attribute-aware data resources. We therefore propose LumosX, a frame...

---

### 4. Deterministic Mode Proposals: An Efficient Alternative to Generative Sampling for Ambiguous Segmentation

**Authors:** Sebastian Gerard, Josephine Sullivan

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20191v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20191v1)

**Summary:** Many segmentation tasks, such as medical image segmentation or future state prediction, are inherently ambiguous, meaning that multiple predictions are equally correct. Current methods typically rely on generative models to capture this uncertainty. However, identifying the underlying modes of the distribution with these methods is computationally expensive, requiring large numbers of samples and post-hoc clustering. In this paper, we shift the focus from stochastic sampling to the direct genera...

---

### 5. CoVR-R:Reason-Aware Composed Video Retrieval

**Authors:** Omkar Thawakar, Dmitry Demidov, Vaishnav Potlapalli, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20190v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20190v1)

**Summary:** Composed Video Retrieval (CoVR) aims to find a target video given a reference video and a textual modification. Prior work assumes the modification text fully specifies the visual changes, overlooking after-effects and implicit consequences (e.g., motion, state transitions, viewpoint or duration cues) that emerge from the edit. We argue that successful CoVR requires reasoning about these after-effects. We introduce a reasoning-first, zero-shot approach that leverages large multimodal models to (...

---

### 6. Wildfire Spread Scenarios: Increasing Sample Diversity of Segmentation Diffusion Models with Training-Free Methods

**Authors:** Sebastian Gerard, Josephine Sullivan

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20188v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20188v1)

**Summary:** Predicting future states in uncertain environments, such as wildfire spread, medical diagnosis, or autonomous driving, requires models that can consider multiple plausible outcomes. While diffusion models can effectively learn such multi-modal distributions, naively sampling from these models is computationally inefficient, potentially requiring hundreds of samples to find low-probability modes that may still be operationally relevant. In this work, we address the challenge of sample-efficient a...

---

### 7. MuSteerNet: Human Reaction Generation from Videos via Observation-Reaction Mutual Steering

**Authors:** Yuan Zhou, Yongzhi Li, Yanqi Dai, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20187v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20187v1)

**Summary:** Video-driven human reaction generation aims to synthesize 3D human motions that directly react to observed video sequences, which is crucial for building human-like interactive AI systems. However, existing methods often fail to effectively leverage video inputs to steer human reaction synthesis, resulting in reaction motions that are mismatched with the content of video sequences. We reveal that this limitation arises from a severe relational distortion between visual observations and reaction ...

---

### 8. Improving Image-to-Image Translation via a Rectified Flow Reformulation

**Authors:** Satoshi Iizuka, Shun Okamoto, Kazuhiro Fukui

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20186v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20186v1)

**Summary:** In this work, we propose Image-to-Image Rectified Flow Reformulation (I2I-RFR), a practical plug-in reformulation that recasts standard I2I regression networks as continuous-time transport models. While pixel-wise I2I regression is simple, stable, and easy to adapt across tasks, it often over-smooths ill-posed and multimodal targets, whereas generative alternatives often require additional components, task-specific tuning, and more complex training and inference pipelines. Our method augments th...

---

### 9. VideoSeek: Long-Horizon Video Agent with Tool-Guided Seeking

**Authors:** Jingyang Lin, Jialian Wu, Jiang Liu, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20185v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20185v1)

**Summary:** Video agentic models have advanced challenging video-language tasks. However, most agentic approaches still heavily rely on greedy parsing over densely sampled video frames, resulting in high computational cost. We present VideoSeek, a long-horizon video agent that leverages video logic flow to actively seek answer-critical evidence instead of exhaustively parsing the full video. This insight allows the model to use far fewer frames while maintaining, or even improving, its video understanding c...

---

### 10. Adaptive Greedy Frame Selection for Long Video Understanding

**Authors:** Yuning Huang, Fengqing Zhu

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20180v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20180v1)

**Summary:** Large vision--language models (VLMs) are increasingly applied to long-video question answering, yet inference is often bottlenecked by the number of input frames and resulting visual tokens. Naive sparse sampling can miss decisive moments, while purely relevance-driven selection frequently collapses onto near-duplicate frames and sacrifices coverage of temporally distant evidence. We propose a question-adaptive greedy frame selection method that jointly optimizes query relevance and semantic rep...

---

### 11. LagerNVS: Latent Geometry for Fully Neural Real-time Novel View Synthesis

**Authors:** Stanislaw Szymanowicz, Minghao Chen, Jianyuan Wang, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20176v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20176v1)

**Summary:** Recent work has shown that neural networks can perform 3D tasks such as Novel View Synthesis (NVS) without explicit 3D reconstruction. Even so, we argue that strong 3D inductive biases are still helpful in the design of such networks. We show this point by introducing LagerNVS, an encoder-decoder neural network for NVS that builds on `3D-aware' latent features. The encoder is initialized from a 3D reconstruction network pre-trained using explicit 3D supervision. This is paired with a lightweight...

---

### 12. TinyML Enhances CubeSat Mission Capabilities

**Authors:** Luigi Capogrosso, Michele Magno

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20174v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20174v1)

**Summary:** Earth observation (EO) missions traditionally rely on transmitting raw or minimally processed imagery from satellites to ground stations for computationally intensive analysis. This paradigm is infeasible for CubeSat systems due to stringent constraints on the onboard embedded processors, energy availability, and communication bandwidth. To overcome these limitations, the paper presents a TinyML-based Convolutional Neural Networks (ConvNets) model optimization and deployment pipeline for onboard...

---

### 13. EgoForge: Goal-Directed Egocentric World Simulator

**Authors:** Yifan Shen, Jiateng Liu, Xinzhuo Li, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20169v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20169v1)

**Summary:** Generative world models have shown promise for simulating dynamic environments, yet egocentric video remains challenging due to rapid viewpoint changes, frequent hand-object interactions, and goal-directed procedures whose evolution depends on latent human intent. Existing approaches either focus on hand-centric instructional synthesis with limited scene evolution, perform static view translation without modeling action dynamics, or rely on dense supervision, such as camera trajectories, long vi...

---

### 14. Beyond Single Tokens: Distilling Discrete Diffusion Models via Discrete MMD

**Authors:** Emiel Hoogeboom, David Ruhe, Jonathan Heek, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20155v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20155v1)

**Summary:** It is currently difficult to distill discrete diffusion models. In contrast, continuous diffusion literature has many distillation approaches methods that can reduce sampling steps to a handful.   Our method, Discrete Moment Matching Distillation (D-MMD), leverages ideas that have been highly successful in the continuous domain. Whereas previous discrete distillation methods collapse, D-MMD maintains high quality and diversity (given sufficient sampling steps). This is demonstrated on both text ...

---

### 15. Can Large Multimodal Models Inspect Buildings? A Hierarchical Benchmark for Structural Pathology Reasoning

**Authors:** Hui Zhong, Yichun Gao, Luyan Liu, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20148v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20148v1)

**Summary:** Automated building facade inspection is a critical component of urban resilience and smart city maintenance. Traditionally, this field has relied on specialized discriminative models (e.g., YOLO, Mask R-CNN) that excel at pixel-level localization but are constrained to passive perception and worse generization without the visual understandng to interpret structural topology. Large Multimodal Models (LMMs) promise a paradigm shift toward active reasoning, yet their application in such high-stakes...

---

### 16. Synergistic Perception and Generative Recomposition: A Multi-Agent Orchestration for Expert-Level Building Inspection

**Authors:** Hui Zhong, Yichun Gao, Luyan Liu, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20143v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20143v1)

**Summary:** Building facade defect inspection is fundamental to structural health monitoring and sustainable urban maintenance, yet it remains a formidable challenge due to extreme geometric variability, low contrast against complex backgrounds, and the inherent complexity of composite defects (e.g., cracks co-occurring with spalling). Such characteristics lead to severe pixel imbalance and feature ambiguity, which, coupled with the critical scarcity of high-quality pixel-level annotations, hinder the gener...

---

### 17. Generalizable NGP-SR: Generalizable Neural Radiance Fields Super-Resolution via Neural Graph Primitives

**Authors:** Wanqi Yuan, Omkar Sharad Mayekar, Connor Pennington, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20128v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20128v1)

**Summary:** Neural Radiance Fields (NeRF) achieve photorealistic novel view synthesis but become costly when high-resolution (HR) rendering is required, as HR outputs demand dense sampling and higher-capacity models. Moreover, naively super-resolving per-view renderings in 2D often breaks multi-view consistency. We propose Generalizable NGP-SR, a 3D-aware super-resolution framework that reconstructs an HR radiance field directly from low-resolution (LR) posed images. Built on Neural Graphics Primitives (NGP...

---

### 18. Chain-of-Adaptation: Surgical Vision-Language Adaptation with Reinforcement Learning

**Authors:** Jiajie Li, Chenhui Xu, Meihuan Liu, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20116v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20116v1)

**Summary:** Conventional fine-tuning on domain-specific datasets can inadvertently alter a model's pretrained multimodal priors, leading to reduced generalization. To address this, we propose Chain-of-Adaptation (CoA), an adaptation framework designed to integrate domain knowledge while maintaining the model's inherent reasoning and perceptual capabilities. CoA introduces a structured reasoning format that enhances domain alignment without sacrificing general multimodal competence by reinforcement learning....

---

### 19. Preference-Guided Debiasing for No-Reference Enhancement Image Quality Assessment

**Authors:** Shiqi Gao, Kang Fu, Zitong Xu, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20086v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20086v1)

**Summary:** Current no-reference image quality assessment (NR-IQA) models for enhanced images often struggle to generalize, as they tend to overfit to the distinct patterns of specific enhancement algorithms rather than evaluating genuine perceptual quality. To address this issue, we propose a preference-guided debiasing framework for no-reference enhancement image quality assessment (EIQA). Specifically, we first learn a continuous enhancement-preference embedding space using supervised contrastive learnin...

---

### 20. A Unified Platform and Quality Assurance Framework for 3D Ultrasound Reconstruction with Robotic, Optical, and Electromagnetic Tracking

**Authors:** Lewis Howell, Manisha Waterston, Tze Min Wah, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20077v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20077v1)

**Summary:** Three-dimensional (3D) Ultrasound (US) can facilitate diagnosis, treatment planning, and image-guided therapy. However, current studies rarely provide a comprehensive evaluation of volumetric accuracy and reproducibility, highlighting the need for robust Quality Assurance (QA) frameworks, particularly for tracked 3D US reconstruction using freehand or robotic acquisition. This study presents a QA framework for 3D US reconstruction and a flexible open source platform for tracked US research. A cu...

---

### 21. MFil-Mamba: Multi-Filter Scanning for Spatial Redundancy-Aware Visual State Space Models

**Authors:** Puskal Khadka, KC Santosh

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20074v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20074v1)

**Summary:** State Space Models (SSMs), especially recent Mamba architecture, have achieved remarkable success in sequence modeling tasks. However, extending SSMs to computer vision remains challenging due to the non-sequential structure of visual data and its complex 2D spatial dependencies. Although several early studies have explored adapting selective SSMs for vision applications, most approaches primarily depend on employing various traversal strategies over the same input. This introduces redundancy an...

---

### 22. Investigating a Policy-Based Formulation for Endoscopic Camera Pose Recovery

**Authors:** Jan Emily Mangulabnan, Akshat Chauhan, Laura Fleig, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20045v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20045v1)

**Summary:** In endoscopic surgery, surgeons continuously locate the endoscopic view relative to the anatomy by interpreting the evolving visual appearance of the intraoperative scene in the context of their prior knowledge. Vision-based navigation systems seek to replicate this capability by recovering camera pose directly from endoscopic video, but most approaches do not embody the same principles of reasoning about new frames that makes surgeons successful. Instead, they remain grounded in feature matchin...

---

### 23. Layered Quantum Architecture Search for 3D Point Cloud Classification

**Authors:** Natacha Kuete Meli, Jovita Lukasik, Vladislav Golyanik, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20024v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20024v1)

**Summary:** We introduce layered Quantum Architecture Search (layered-QAS), a strategy inspired by classical network morphism that designs Parametrised Quantum Circuit (PQC) architectures by progressively growing and adapting them. PQCs offer strong expressiveness with relatively few parameters, yet they lack standard architectural layers (e.g., convolution, attention) that encode inductive biases for a given learning task. To assess the effectiveness of our method, we focus on 3D point cloud classification...

---

### 24. Detached Skip-Links and $R$-Probe: Decoupling Feature Aggregation from Gradient Propagation for MLLM OCR

**Authors:** Ziye Yuan, Ruchang Yao, Chengxin Zheng, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20020v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20020v1)

**Summary:** Multimodal large language models (MLLMs) excel at high-level reasoning yet fail on OCR tasks where fine-grained visual details are compromised or misaligned. We identify an overlooked optimization issue in multi-layer feature fusion. Skip pathways introduce direct back-propagation paths from high-level semantic objectives to early visual layers. This mechanism overwrites low-level signals and destabilizes training. To mitigate this gradient interference, we propose Detached Skip-Links, a minimal...

---

### 25. CFCML: A Coarse-to-Fine Crossmodal Learning Framework For Disease Diagnosis Using Multimodal Images and Tabular Data

**Authors:** Tianling Liu, Hongying Liu, Fanhua Shang, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20016v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20016v1)

**Summary:** In clinical practice, crossmodal information including medical images and tabular data is essential for disease diagnosis. There exists a significant modality gap between these data types, which obstructs advancements in crossmodal diagnostic accuracy. Most existing crossmodal learning (CML) methods primarily focus on exploring relationships among high-level encoder outputs, leading to the neglect of local information in images. Additionally, these methods often overlook the extraction of task-r...

---

### 26. Diffusion-Based Makeup Transfer with Facial Region-Aware Makeup Features

**Authors:** Zheng Gao, Debin Meng, Yunqi Miao, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20012v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20012v1)

**Summary:** Current diffusion-based makeup transfer methods commonly use the makeup information encoded by off-the-shelf foundation models (e.g., CLIP) as condition to preserve the makeup style of reference image in the generation. Although effective, these works mainly have two limitations: (1) foundation models pre-trained for generic tasks struggle to capture makeup styles; (2) the makeup features of reference image are injected to the diffusion denoising model as a whole for global makeup transfer, over...

---

### 27. NEC-Diff: Noise-Robust Event-RAW Complementary Diffusion for Seeing Motion in Extreme Darkness

**Authors:** Haoyue Liu, Jinghan Xu, Luxin Feng, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20005v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20005v1)

**Summary:** High-quality imaging of dynamic scenes in extremely low-light conditions is highly challenging. Photon scarcity induces severe noise and texture loss, causing significant image degradation. Event cameras, featuring a high dynamic range (120 dB) and high sensitivity to motion, serve as powerful complements to conventional cameras by offering crucial cues for preserving subtle textures. However, most existing approaches emphasize texture recovery from events, while paying little attention to image...

---

### 28. Evaluating Test-Time Adaptation For Facial Expression Recognition Under Natural Cross-Dataset Distribution Shifts

**Authors:** John Turnbull, Shivam Grover, Amin Jalali, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19994v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19994v1)

**Summary:** Deep learning models often struggle under natural distribution shifts, a common challenge in real-world deployments. Test-Time Adaptation (TTA) addresses this by adapting models during inference without labeled source data. We present the first evaluation of TTA methods for FER under natural domain shifts, performing cross-dataset experiments with widely used FER datasets. This moves beyond synthetic corruptions to examine real-world shifts caused by differing collection protocols, annotation st...

---

### 29. MedSPOT: A Workflow-Aware Sequential Grounding Benchmark for Clinical GUI

**Authors:** Rozain Shakeel, Abdul Rahman Mohammad Ali, Muneeb Mushtaq, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19993v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19993v1)

**Summary:** Despite the rapid progress of Multimodal Large Language Models (MLLMs), their ability to perform reliable visual grounding in high-stakes clinical software environments remains underexplored. Existing GUI benchmarks largely focus on isolated, single-step grounding queries, overlooking the sequential, workflow-driven reasoning required in real-world medical interfaces, where tasks evolve across independent steps and dynamic interface states. We introduce MedSPOT, a workflow-aware sequential groun...

---

### 30. X-World: Controllable Ego-Centric Multi-Camera World Models for Scalable End-to-End Driving

**Authors:** Chaoda Zheng, Sean Li, Jinhao Deng, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19979v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19979v1)

**Summary:** Scalable and reliable evaluation is increasingly critical in the end-to-end era of autonomous driving, where vision--language--action (VLA) policies directly map raw sensor streams to driving actions. Yet, current evaluation pipelines still rely heavily on real-world road testing, which is costly, biased toward limited scenario coverage, and difficult to reproduce. These challenges motivate a real-world simulator that can generate realistic future observations under proposed actions, while remai...

---

### 31. 2K Retrofit: Entropy-Guided Efficient Sparse Refinement for High-Resolution 3D Geometry Prediction

**Authors:** Tianbao Zhang, Zhenyu Liang, Zhenbo Song, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19964v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19964v1)

**Summary:** High-resolution geometric prediction is essential for robust perception in autonomous driving, robotics, and AR/MR, but current foundation models are fundamentally limited by their scalability to real-world, high-resolution scenarios. Direct inference on 2K images with these models incurs prohibitive computational and memory demands, making practical deployment challenging. To tackle the issue, we present 2K Retrofit, a novel framework that enables efficient 2K-resolution inference for any geome...

---

### 32. Cov2Pose: Leveraging Spatial Covariance for Direct Manifold-aware 6-DoF Object Pose Estimation

**Authors:** Nassim Ali Ousalah, Peyman Rostami, Vincent Gaudillière, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19961v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19961v1)

**Summary:** In this paper, we address the problem of 6-DoF object pose estimation from a single RGB image. Indirect methods that typically predict intermediate 2D keypoints, followed by a Perspective-n-Point solver, have shown great performance. Direct approaches, which regress the pose in an end-to-end manner, are usually computationally more efficient but less accurate. However, direct heads rely on globally pooled features, ignoring spatial second-order statistics despite their informativeness in pose pr...

---

### 33. HiPath: Hierarchical Vision-Language Alignment for Structured Pathology Report Prediction

**Authors:** Ruicheng Yuan, Zhenxuan Zhang, Anbang Wang, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19957v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19957v1)

**Summary:** Pathology reports are structured, multi-granular documents encoding diagnostic conclusions, histological grades, and ancillary test results across one or more anatomical sites; yet existing pathology vision-language models (VLMs) reduce this output to a flat label or free-form text. We present HiPath, a lightweight VLM framework built on frozen UNI2 and Qwen3 backbones that treats structured report prediction as its primary training objective. Three trainable modules totalling 15M parameters add...

---

### 34. Timestep-Aware Block Masking for Efficient Diffusion Model Inference

**Authors:** Haodong He, Yuan Gao, Weizhong Zhang, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19939v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19939v1)

**Summary:** Diffusion Probabilistic Models (DPMs) have achieved great success in image generation but suffer from high inference latency due to their iterative denoising nature. Motivated by the evolving feature dynamics across the denoising trajectory, we propose a novel framework to optimize the computational graph of pre-trained DPMs on a per-timestep basis. By learning timestep-specific masks, our method dynamically determines which blocks to execute or bypass through feature reuse at each inference sta...

---

### 35. LIORNet: Self-Supervised LiDAR Snow Removal Framework for Autonomous Driving under Adverse Weather Conditions

**Authors:** Ji-il Park, Inwook Shim

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19936v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19936v1)

**Summary:** LiDAR sensors provide high-resolution 3D perception and long-range detection, making them indispensable for autonomous driving and robotics. However, their performance significantly degrades under adverse weather conditions such as snow, rain, and fog, where spurious noise points dominate the point cloud and lead to false perception. To address this problem, various approaches have been proposed: distance-based filters exploiting spatial sparsity, intensity-based filters leveraging reflectance d...

---

### 36. RAM: Recover Any 3D Human Motion in-the-Wild

**Authors:** Sen Jia, Ning Zhu, Jinqin Zhong, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19929v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19929v1)

**Summary:** RAM incorporates a motion-aware semantic tracker with adaptive Kalman filtering to achieve robust identity association under severe occlusions and dynamic interactions. A memory-augmented Temporal HMR module further enhances human motion reconstruction by injecting spatio-temporal priors for consistent and smooth motion estimation. Moreover, a lightweight Predictor module forecasts future poses to maintain reconstruction continuity, while a gated combiner adaptively fuses reconstructed and predi...

---

### 37. SegVGGT: Joint 3D Reconstruction and Instance Segmentation from Multi-View Images

**Authors:** Jinyuan Qu, Hongyang Li, Lei Zhang

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19926v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19926v1)

**Summary:** 3D instance segmentation methods typically rely on high-quality point clouds or posed RGB-D scans, requiring complex multi-stage processing pipelines, and are highly sensitive to reconstruction noise. While recent feed-forward transformers have revolutionized multi-view 3D reconstruction, they remain decoupled from high-level semantic understanding. In this work, we present SegVGGT, a unified end-to-end framework that simultaneously performs feed-forward 3D reconstruction and instance segmentati...

---

### 38. ReconMIL: Synergizing Latent Space Reconstruction with Bi-Stream Mamba for Whole Slide Image Analysis

**Authors:** Lubin Gan, Jing Zhang, Heng Zhang, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19925v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19925v1)

**Summary:** Whole slide image (WSI) analysis heavily relies on multiple instance learning (MIL). While recent methods benefit from large-scale foundation models and advanced sequence modeling to capture long-range dependencies, they still struggle with two critical issues. First, directly applying frozen, task-agnostic features often leads to suboptimal separability due to the domain gap with specific histological tasks. Second, relying solely on global aggregators can cause over-smoothing, where sparse but...

---

### 39. PanORama: Multiview Consistent Panoptic Segmentation in Operating Rooms

**Authors:** Tuna Gürbüz, Ege Özsoy, Tony Danjun Wang, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19920v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19920v1)

**Summary:** Operating rooms (ORs) are cluttered, dynamic, highly occluded environments, where reliable spatial understanding is essential for situational awareness during complex surgical workflows. Achieving spatial understanding for panoptic segmentation from sparse multiview images poses a fundamental challenge, as limited visibility in a subset of views often leads to mispredictions across cameras. To this end, we introduce PanORama, the first panoptic segmentation for the operating room that is multivi...

---

### 40. Learning Like Humans: Analogical Concept Learning for Generalized Category Discovery

**Authors:** Jizhou Han, Chenhao Ding, Yuhang He, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19918v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19918v1)

**Summary:** Generalized Category Discovery (GCD) seeks to uncover novel categories in unlabeled data while preserving recognition of known categories, yet prevailing visual-only pipelines and the loose coupling between supervised learning and discovery often yield brittle boundaries on fine-grained, look-alike categories. We introduce the Analogical Textual Concept Generator (ATCG), a plug-and-play module that analogizes from labeled knowledge to new observations, forming textual concepts for unlabeled samp...

---

### 41. SIMPLER: Efficient Foundation Model Adaptation via Similarity-Guided Layer Pruning for Earth Observation

**Authors:** Víctor Barreiro, Johannes Jakubik, Francisco Argüello, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19873v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19873v1)

**Summary:** Fine-tuning foundation models for Earth Observation is computationally expensive, with high training time and memory demands for both training and deployment. Parameter-efficient methods reduce training cost but retain full inference complexity, while post-hoc compression optimizes inference only after costly full fine-tuning. We introduce SIMPLER, a pre-fine-tuning architecture selection method that reduces inference and deployment costs by identifying an effective model depth before adaptation...

---

### 42. MedQ-Engine: A Closed-Loop Data Engine for Evolving MLLMs in Medical Image Quality Assessment

**Authors:** Jiyao Liu, Junzhi Ning, Wanying Qu, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19863v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19863v1)

**Summary:** Medical image quality assessment (Med-IQA) is a prerequisite for clinical AI deployment, yet multimodal large language models (MLLMs) still fall substantially short of human experts, particularly when required to provide descriptive assessments with clinical reasoning beyond simple quality scores. However, improving them is hindered by the high cost of acquiring descriptive annotations and by the inability of one-time data collection to adapt to the model's evolving weaknesses. To address these ...

---

### 43. IsoCLIP: Decomposing CLIP Projectors for Efficient Intra-modal Alignment

**Authors:** Simone Magistri, Dipam Goswami, Marco Mistretta, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19862v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19862v1)

**Summary:** Vision-Language Models like CLIP are extensively used for inter-modal tasks which involve both visual and text modalities. However, when the individual modality encoders are applied to inherently intra-modal tasks like image-to-image retrieval, their performance suffers from the intra-modal misalignment. In this paper we study intra-modal misalignment in CLIP with a focus on the role of the projectors that map pre-projection image and text embeddings into the shared embedding space. By analyzing...

---

### 44. FoleyDirector: Fine-Grained Temporal Steering for Video-to-Audio Generation via Structured Scripts

**Authors:** You Li, Dewei Zhou, Fan Ma, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19857v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19857v1)

**Summary:** Recent Video-to-Audio (V2A) methods have achieved remarkable progress, enabling the synthesis of realistic, high-quality audio. However, they struggle with fine-grained temporal control in multi-event scenarios or when visual cues are insufficient, such as small regions, off-screen sounds, or occluded or partially visible objects. In this paper, we propose FoleyDirector, a framework that, for the first time, enables precise temporal guidance in DiT-based V2A generation while preserving the base ...

---

### 45. Failure Modes for Deep Learning-Based Online Mapping: How to Measure and Address Them

**Authors:** Michael Hubbertz, Qi Han, Tobias Meisen

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19852v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19852v1)

**Summary:** Deep learning-based online mapping has emerged as a cornerstone of autonomous driving, yet these models frequently fail to generalize beyond familiar environments. We propose a framework to identify and measure the underlying failure modes by disentangling two effects: Memorization of input features and overfitting to known map geometries. We propose measures based on evaluation subsets that control for geographical proximity and geometric similarity between training and validation scenes. We in...

---

### 46. Hyper-Connections for Adaptive Multi-Modal MRI Brain Tumor Segmentation

**Authors:** Lokendra Kumar, Shubham Aggarwal

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19844v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19844v1)

**Summary:** We present the first study of Hyper-Connections (HC) for volumetric multi-modal brain tumor segmentation, integrating them as a drop-in replacement for fixed residual connections across five architectures: nnU-Net, SwinUNETR, VT-UNet, U-Net, and U-Netpp. Dynamic HC consistently improves all 3D models on the BraTS 2021 dataset, yielding up to +1.03 percent mean Dice gain with negligible parameter overhead. Gains are most pronounced in the Enhancing Tumor sub-region, reflecting improved fine-grain...

---

### 47. Fourier Splatting: Generalized Fourier encoded primitives for scalable radiance fields

**Authors:** Mihnea-Bogdan Jurca, Bert Van hauwermeiren, Adrian Munteanu

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19834v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19834v1)

**Summary:** Novel view synthesis has recently been revolutionized by 3D Gaussian Splatting (3DGS), which enables real-time rendering through explicit primitive rasterization. However, existing methods tie visual fidelity strictly to the number of primitives: quality downscaling is achieved only through pruning primitives. We propose the first inherently scalable primitive for radiance field rendering. Fourier Splatting employs scalable primitives with arbitrary closed shapes obtained by parameterizing plana...

---

### 48. HUGE-Bench: A Benchmark for High-Level UAV Vision-Language-Action Tasks

**Authors:** Jingyu Guo, Ziye Chen, Ziwen Li, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19822v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19822v1)

**Summary:** Existing UAV vision-language navigation (VLN) benchmarks have enabled language-guided flight, but they largely focus on long, step-wise route descriptions with goal-centric evaluation, making them less diagnostic for real operations where brief, high-level commands must be grounded into safe multi-stage behaviors. We present HUGE-Bench, a benchmark for High-Level UAV Vision-Language-Action (HL-VLA) tasks that tests whether an agent can interpret concise language and execute complex, process-orie...

---

### 49. Enhancing Alignment for Unified Multimodal Models via Semantically-Grounded Supervision

**Authors:** Jiyeong Kim, Yerim So, Hyesong Choi, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19807v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19807v1)

**Summary:** Unified Multimodal Models (UMMs) have emerged as a promising paradigm that integrates multimodal understanding and generation within a unified modeling framework. However, current generative training paradigms suffer from inherent limitations. We present Semantically-Grounded Supervision (SeGroS), a fine-tuning framework designed to resolve the granularity mismatch and supervisory redundancy in UMMs. At its core, we propose a novel visual grounding map to construct two complementary supervision ...

---

### 50. Evaluating Vision Foundation Models for Pixel and Object Classification in Microscopy

**Authors:** Carolin Teuber, Anwai Archit, Tobias Boothe, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19802v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19802v1)

**Summary:** Deep learning underlies most modern approaches and tools in computer vision, including biomedical imaging. However, for interactive semantic segmentation (often called pixel classification in this context) and interactive object-level classification (object classification), feature-based shallow learning remains widely used. This is due to the diversity of data in this domain, the lack of large pretraining datasets, and the need for computational and label efficiency. In contrast, state-of-the-a...

---

## cs.LG

**50 papers**

### 1. From Masks to Pixels and Meaning: A New Taxonomy, Benchmark, and Metrics for VLM Image Tampering

**Authors:** Xinyi Shang, Yi Tang, Jiacheng Cui, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20193v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20193v1)

**Summary:** Existing tampering detection benchmarks largely rely on object masks, which severely misalign with the true edit signal: many pixels inside a mask are untouched or only trivially modified, while subtle yet consequential edits outside the mask are treated as natural. We reformulate VLM image tampering from coarse region labels to a pixel-grounded, meaning and language-aware task. First, we introduce a taxonomy spanning edit primitives (replace/remove/splice/inpaint/attribute/colorization, etc.) a...

---

### 2. MeanFlow Meets Control: Scaling Sampled-Data Control for Swarms

**Authors:** Anqi Dong, Yongxin Chen, Karl H. Johansson, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20189v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20189v1)

**Summary:** Steering large-scale swarms in only a few control updates is challenging because real systems operate in sampled-data form: control inputs are updated intermittently and applied over finite intervals. In this regime, the natural object is not an instantaneous velocity field, but a finite-window control quantity that captures the system response over each sampling interval. Inspired by MeanFlow, we introduce a control-space learning framework for swarm steering under linear time-invariant dynamic...

---

### 3. Kolmogorov-Arnold causal generative models

**Authors:** Alejandro Almodóvar, Mar Elizo, Patricia A. Apellániz, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20184v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20184v1)

**Summary:** Causal generative models provide a principled framework for answering observational, interventional, and counterfactual queries from observational data. However, many deep causal models rely on highly expressive architectures with opaque mechanisms, limiting auditability in high-stakes domains. We propose KaCGM, a causal generative model for mixed-type tabular data where each structural equation is parameterized by a Kolmogorov--Arnold Network (KAN). This decomposition enables direct inspection ...

---

### 4. AI Agents Can Already Autonomously Perform Experimental High Energy Physics

**Authors:** Eric A. Moreno, Samuel Bright-Thonney, Andrzej Novak, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20179v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20179v1)

**Summary:** Large language model-based AI agents are now able to autonomously execute substantial portions of a high energy physics (HEP) analysis pipeline with minimal expert-curated input. Given access to a HEP dataset, an execution framework, and a corpus of prior experimental literature, we find that Claude Code succeeds in automating all stages of a typical analysis: event selection, background estimation, uncertainty quantification, statistical inference, and paper drafting. We argue that the experime...

---

### 5. Measuring Faithfulness Depends on How You Measure: Classifier Sensitivity in LLM Chain-of-Thought Evaluation

**Authors:** Richard J. Young

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20172v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20172v1)

**Summary:** Recent work on chain-of-thought (CoT) faithfulness reports single aggregate numbers (e.g., DeepSeek-R1 acknowledges hints 39% of the time), implying that faithfulness is an objective, measurable property of a model. This paper demonstrates that it is not. Three classifiers (a regex-only detector, a two-stage regex-plus-LLM pipeline, and an independent Claude Sonnet 4 judge) are applied to 10,276 influenced reasoning traces from 12 open-weight models spanning 9 families and 7B to 1T parameters. O...

---

### 6. Semantic Token Clustering for Efficient Uncertainty Quantification in Large Language Models

**Authors:** Qi Cao, Andrew Gambardella, Takeshi Kojima, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20161v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20161v1)

**Summary:** Large language models (LLMs) have demonstrated remarkable capabilities across diverse tasks. However, the truthfulness of their outputs is not guaranteed, and their tendency toward overconfidence further limits reliability. Uncertainty quantification offers a promising way to identify potentially unreliable outputs, but most existing methods rely on repeated sampling or auxiliary models, introducing substantial computational overhead. To address these limitations, we propose Semantic Token Clust...

---

### 7. Beyond Single Tokens: Distilling Discrete Diffusion Models via Discrete MMD

**Authors:** Emiel Hoogeboom, David Ruhe, Jonathan Heek, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20155v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20155v1)

**Summary:** It is currently difficult to distill discrete diffusion models. In contrast, continuous diffusion literature has many distillation approaches methods that can reduce sampling steps to a handful.   Our method, Discrete Moment Matching Distillation (D-MMD), leverages ideas that have been highly successful in the continuous domain. Whereas previous discrete distillation methods collapse, D-MMD maintains high quality and diversity (given sufficient sampling steps). This is demonstrated on both text ...

---

### 8. Enhancing Hyperspace Analogue to Language (HAL) Representations via Attention-Based Pooling for Text Classification

**Authors:** Ali Sakour, Zoalfekar Sakour

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20149v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20149v1)

**Summary:** The Hyperspace Analogue to Language (HAL) model relies on global word co-occurrence matrices to construct distributional semantic representations. While these representations capture lexical relationships effectively, aggregating them into sentence-level embeddings via standard mean pooling often results in information loss. Mean pooling assigns equal weight to all tokens, thereby diluting the impact of contextually salient words with uninformative structural tokens. In this paper, we address th...

---

### 9. Revisiting Gene Ontology Knowledge Discovery with Hierarchical Feature Selection and Virtual Study Group of AI Agents

**Authors:** Cen Wan, Alex A. Freitas

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20132v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20132v1)

**Summary:** Large language models have achieved great success in multiple challenging tasks, and their capacity can be further boosted by the emerging agentic AI techniques. This new computing paradigm has already started revolutionising the traditional scientific discovery pipelines. In this work, we propose a novel agentic AI-based knowledge discovery-oriented virtual study group that aims to extract meaningful ageing-related biological knowledge considering highly ageing-related Gene Ontology terms that ...

---

### 10. Conditioning Protein Generation via Hopfield Pattern Multiplicity

**Authors:** Jeffrey D. Varner

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20115v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20115v1)

**Summary:** Protein sequence generation via stochastic attention produces plausible family members from small alignments without training, but treats all stored sequences equally and cannot direct generation toward a functional subset of interest. We show that a single scalar parameter, added as a bias to the sampler's attention logits, continuously shifts generation from the full family toward a user-specified subset, with no retraining and no change to the model architecture. A practitioner supplies a sma...

---

### 11. Var-JEPA: A Variational Formulation of the Joint-Embedding Predictive Architecture -- Bridging Predictive and Generative Self-Supervised Learning

**Authors:** Moritz Gögl, Christopher Yau

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20111v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20111v1)

**Summary:** The Joint-Embedding Predictive Architecture (JEPA) is often seen as a non-generative alternative to likelihood-based self-supervised learning, emphasizing prediction in representation space rather than reconstruction in observation space. We argue that the resulting separation from probabilistic generative modeling is largely rhetorical rather than structural: the canonical JEPA design, coupled encoders with a context-to-target predictor, mirrors the variational posteriors and learned conditiona...

---

### 12. GO-GenZip: Goal-Oriented Generative Sampling and Hybrid Compression

**Authors:** Pietro Talli, Qi Liao, Alessandro Lieto, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20109v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20109v1)

**Summary:** Current network data telemetry pipelines consist of massive streams of fine-grained Key Performance Indicators (KPIs) from multiple distributed sources towards central aggregators, making data storage, transmission, and real-time analysis increasingly unsustainable. This work presents a generative AI (GenAI)-driven sampling and hybrid compression framework that redesigns network telemetry from a goal-oriented perspective. Unlike conventional approaches that passively compress fully observed data...

---

### 13. Trojan horse hunt in deep forecasting models: Insights from the European Space Agency competition

**Authors:** Krzysztof Kotowski, Ramez Shendy, Jakub Nalepa, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20108v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20108v1)

**Summary:** Forecasting plays a crucial role in modern safety-critical applications, such as space operations. However, the increasing use of deep forecasting models introduces a new security risk of trojan horse attacks, carried out by hiding a backdoor in the training data or directly in the model weights. Once implanted, the backdoor is activated by a specific trigger pattern at test time, causing the model to produce manipulated predictions. We focus on this issue in our \textit{Trojan Horse Hunt} data ...

---

### 14. The $\mathbf{Y}$-Combinator for LLMs: Solving Long-Context Rot with $λ$-Calculus

**Authors:** Amartya Roy, Rasul Tutunov, Xiaotong Ji, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20105v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20105v1)

**Summary:** LLMs are increasingly used as general-purpose reasoners, but long inputs remain bottlenecked by a fixed context window. Recursive Language Models (RLMs) address this by externalising the prompt and recursively solving subproblems. Yet existing RLMs depend on an open-ended read-eval-print loop (REPL) in which the model generates arbitrary control code, making execution difficult to verify, predict, and analyse.   We introduce $λ$-RLM, a framework for long-context reasoning that replaces free-form...

---

### 15. Spectral Alignment in Forward-Backward Representations via Temporal Abstraction

**Authors:** Seyed Mahdi B. Azad, Jasper Hoffmann, Iman Nematollahi, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20103v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20103v1)

**Summary:** Forward-backward (FB) representations provide a powerful framework for learning the successor representation (SR) in continuous spaces by enforcing a low-rank factorization. However, a fundamental spectral mismatch often exists between the high-rank transition dynamics of continuous environments and the low-rank bottleneck of the FB architecture, making accurate low-rank representation learning difficult. In this work, we analyze temporal abstraction as a mechanism to mitigate this mismatch. By ...

---

### 16. How Out-of-Equilibrium Phase Transitions can Seed Pattern Formation in Trained Diffusion Models

**Authors:** Luca Ambrogioni

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20092v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20092v1)

**Summary:** In this work, we propose a theoretical framework that interprets the generation process in trained diffusion models as an instance of out-of-equilibrium phase transitions. We argue that, rather than evolving smoothly from noise to data, reverse diffusion passes through a critical regime in which small spatial fluctuations are amplified and seed the emergence of large-scale structure. Our central insight is that architectural constraints, such as locality, sparsity, and translation equivariance, ...

---

### 17. Antenna Array Beamforming Based on a Hybrid Quantum Optimization Framework

**Authors:** Shuai Zeng

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20072v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20072v1)

**Summary:** This paper proposes a hybrid quantum optimization framework for large-scale antenna-array beamforming with jointly optimized discrete phases and continuous amplitudes. The method combines quantum-inspired search with classical gradient refinement to handle mixed discrete-continuous variables efficiently. For phase optimization, a Gray-code and odd-combination encoding scheme is introduced to improve robustness and avoid the complexity explosion of higher-order Ising models. For amplitude optimiz...

---

### 18. Fine-tuning Timeseries Predictors Using Reinforcement Learning

**Authors:** Hugo Cazaux, Ralph Rudd, Hlynur Stefánsson, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20063v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20063v1)

**Summary:** This chapter presents three major reinforcement learning algorithms used for fine-tuning financial forecasters. We propose a clear implementation plan for backpropagating the loss of a reinforcement learning task to a model trained using supervised learning, and compare the performance before and after the fine-tuning. We find an increase in performance after fine-tuning, and transfer learning properties to the models, indicating the benefits of fine-tuning. We also highlight the tuning process ...

---

### 19. Structured Latent Dynamics in Wireless CSI via Homomorphic World Models

**Authors:** Salmane Naoumi, Mehdi Bennis, Marwa Chafii

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20048v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20048v1)

**Summary:** We introduce a self-supervised framework for learning predictive and structured representations of wireless channels by modeling the temporal evolution of channel state information (CSI) in a compact latent space. Our method casts the problem as a world modeling task and leverages the Joint Embedding Predictive Architecture (JEPA) to learn action-conditioned latent dynamics from CSI trajectories. To promote geometric consistency and compositionality, we parameterize transitions using homomorphic...

---

### 20. Federated Hyperdimensional Computing for Resource-Constrained Industrial IoT

**Authors:** Nikita Zeulin, Olga Galinina, Nageen Himayat, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20037v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20037v1)

**Summary:** In the Industrial Internet of Things (IIoT) systems, edge devices often operate under strict constraints in memory, compute capability, and wireless bandwidth. These limitations challenge the deployment of advanced data analytics tasks, such as predictive and prescriptive maintenance. In this work, we explore hyperdimensional computing (HDC) as a lightweight learning paradigm for resource-constrained IIoT. Conventional centralized HDC leverages the properties of high-dimensional vector spaces to...

---

### 21. Continual Learning as Shared-Manifold Continuation Under Compatible Shift

**Authors:** Henry J. Kobs

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20036v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20036v1)

**Summary:** Continual learning methods usually preserve old behavior by regularizing parameters, matching old outputs, or replaying previous examples. These strategies can reduce forgetting, but they do not directly specify how the latent representation should evolve. We study a narrower geometric alternative for the regime where old and new data should remain on the same latent support: continual learning as continuation of a shared manifold. We instantiate this view within Support-Preserving Manifold Assi...

---

### 22. Graph-Informed Adversarial Modeling: Infimal Subadditivity of Interpolative Divergences

**Authors:** Panagiota Birmpa, Eric Joseph Hall

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20025v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20025v1)

**Summary:** We study adversarial learning when the target distribution factorizes according to a known Bayesian network. For interpolative divergences, including $(f,Γ)$-divergences, we prove a new infimal subadditivity principle showing that, under suitable conditions, a global variational discrepancy is controlled by an average of family-level discrepancies aligned with the graph. In an additive regime, this surrogate is exact. This provides a variational justification for replacing a graph-agnostic GAN w...

---

### 23. Layered Quantum Architecture Search for 3D Point Cloud Classification

**Authors:** Natacha Kuete Meli, Jovita Lukasik, Vladislav Golyanik, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20024v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20024v1)

**Summary:** We introduce layered Quantum Architecture Search (layered-QAS), a strategy inspired by classical network morphism that designs Parametrised Quantum Circuit (PQC) architectures by progressively growing and adapting them. PQCs offer strong expressiveness with relatively few parameters, yet they lack standard architectural layers (e.g., convolution, attention) that encode inductive biases for a given learning task. To assess the effectiveness of our method, we focus on 3D point cloud classification...

---

### 24. ODySSeI: An Open-Source End-to-End Framework for Automated Detection, Segmentation, and Severity Estimation of Lesions in Invasive Coronary Angiography Images

**Authors:** Anand Choudhary, Xiaowu Sun, Thabo Mahendiran, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20021v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20021v1)

**Summary:** Invasive Coronary Angiography (ICA) is the clinical gold standard for the assessment of coronary artery disease. However, its interpretation remains subjective and prone to intra- and inter-operator variability. In this work, we introduce ODySSeI: an Open-source end-to-end framework for automated Detection, Segmentation, and Severity estimation of lesions in ICA images. ODySSeI integrates deep learning-based lesion detection and lesion segmentation models trained using a novel Pyramidal Augmenta...

---

### 25. AgenticRS-EnsNAS: Ensemble-Decoupled Self-Evolving Architecture Search

**Authors:** Yun Chen, Moyu Zhang, Jinxin Hu, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20014v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20014v1)

**Summary:** Neural Architecture Search (NAS) deployment in industrial production systems faces a fundamental validation bottleneck: verifying a single candidate architecture pi requires evaluating the deployed ensemble of M models, incurring prohibitive O(M) computational cost per candidate. This cost barrier severely limits architecture iteration frequency in real-world applications where ensembles (M=50-200) are standard for robustness. This work introduces Ensemble-Decoupled Architecture Search, a framew...

---

### 26. A Super Fast K-means for Indexing Vector Embeddings

**Authors:** Leonardo Kuffo, Sven Hepkema, Peter Boncz

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20009v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20009v1)

**Summary:** We present SuperKMeans: a k-means variant designed for clustering collections of high-dimensional vector embeddings. SuperKMeans' clustering is up to 7x faster than FAISS and Scikit-Learn on modern CPUs and up to 4x faster than cuVS on GPUs (Figure 1), while maintaining the quality of the resulting centroids for vector similarity search tasks. SuperKMeans acceleration comes from reducing data-access and compute overhead by reliably and efficiently pruning dimensions that are not needed to assign...

---

### 27. Evaluating Test-Time Adaptation For Facial Expression Recognition Under Natural Cross-Dataset Distribution Shifts

**Authors:** John Turnbull, Shivam Grover, Amin Jalali, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19994v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19994v1)

**Summary:** Deep learning models often struggle under natural distribution shifts, a common challenge in real-world deployments. Test-Time Adaptation (TTA) addresses this by adapting models during inference without labeled source data. We present the first evaluation of TTA methods for FER under natural domain shifts, performing cross-dataset experiments with widely used FER datasets. This moves beyond synthetic corruptions to examine real-world shifts caused by differing collection protocols, annotation st...

---

### 28. Breaking the Capability Ceiling of LLM Post-Training by Reintroducing Markov States

**Authors:** Yurun Yuan, Tengyang Xie

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19987v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19987v1)

**Summary:** Reinforcement learning (RL) has become a standard paradigm for post-training and aligning Large Language Models (LLMs), yet recent evidence suggests it faces a persistent "capability ceiling": unlike classical RL systems that discover novel strategies, RL for LLMs often acts as a mere refiner of patterns already latent in pre-trained weights. In this work, we identify a fundamental structural bottleneck: while classical RL relies on compact, informative Markov states, current LLM post-training f...

---

### 29. Model-Driven Learning-Based Physical Layer Authentication for Mobile Wi-Fi Devices

**Authors:** Yijia Guo, Junqing Zhang, Yao-Win Peter Hong, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19972v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19972v1)

**Summary:** The rise of wireless technologies has made the Internet of Things (IoT) ubiquitous, but the broadcast nature of wireless communications exposes IoT to authentication risks. Physical layer authentication (PLA) offers a promising solution by leveraging unique characteristics of wireless channels. As a common approach in PLA, hypothesis testing yields a theoretically optimal Neyman-Pearson (NP) detector, but its reliance on channel statistics limits its practicality in real-world scenarios. In cont...

---

### 30. Graph2TS: Structure-Controlled Time Series Generation via Quantile-Graph VAEs

**Authors:** Shaoshuai Du, Joze M. Rozanec, Andy Pimentel, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19970v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19970v1)

**Summary:** Although recent generative models can produce time series with close marginal distributions, they often face a fundamental tension between preserving global temporal structure and modeling stochastic local variations, particularly for highly volatile signals with weak or irregular periodicity. Direct distribution matching in such settings can amplify noise or suppress meaningful temporal patterns. In this work, we propose a structure-residual perspective on time-series generation, viewing tempor...

---

### 31. Channel Prediction-Based Physical Layer Authentication under Consecutive Spoofing Attacks

**Authors:** Yijia Guo, Junqing Zhang, Yao-Win Peter Hong

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19962v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19962v1)

**Summary:** Wireless networks are highly vulnerable to spoofing attacks, especially when attackers transmit consecutive spoofing packets. Conventional physical layer authentication (PLA) methods have mostly focused on single-packet spoofing attack. However, under consecutive spoofing attacks, they become ineffective due to channel evolution caused by device mobility and channel fading. To address this challenge, we propose a channel prediction-based PLA framework. Specifically, a Transformer-based channel p...

---

### 32. HiPath: Hierarchical Vision-Language Alignment for Structured Pathology Report Prediction

**Authors:** Ruicheng Yuan, Zhenxuan Zhang, Anbang Wang, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19957v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19957v1)

**Summary:** Pathology reports are structured, multi-granular documents encoding diagnostic conclusions, histological grades, and ancillary test results across one or more anatomical sites; yet existing pathology vision-language models (VLMs) reduce this output to a flat label or free-form text. We present HiPath, a lightweight VLM framework built on frozen UNI2 and Qwen3 backbones that treats structured report prediction as its primary training objective. Three trainable modules totalling 15M parameters add...

---

### 33. Structural Controllability of Large-Scale Hypergraphs

**Authors:** Joshua Pickard, Xin Mao, Can Chen

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19955v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19955v1)

**Summary:** Controlling real-world networked systems, including ecological, biomedical, and engineered networks that exhibit higher-order interactions, remains challenging due to inherent nonlinearities and large system scales. Despite extensive studies on graph controllability, the controllability properties of hypergraphs remain largely underdeveloped. Existing results focus primarily on exact controllability, which is often impractical for large-scale hypergraphs. In this article, we develop a structural...

---

### 34. On the Ability of Transformers to Verify Plans

**Authors:** Yash Sarrof, Yupei Du, Katharina Stein, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19954v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19954v1)

**Summary:** Transformers have shown inconsistent success in AI planning tasks, and theoretical understanding of when generalization should be expected has been limited. We take important steps towards addressing this gap by analyzing the ability of decoder-only models to verify whether a given plan correctly solves a given planning instance. To analyse the general setting where the number of objects -- and thus the effective input alphabet -- grows at test time, we introduce C*-RASP, an extension of C-RASP ...

---

### 35. TAPAS: Efficient Two-Server Asymmetric Private Aggregation Beyond Prio(+)

**Authors:** Harish Karthikeyan, Antigoni Polychroniadou

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19949v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19949v1)

**Summary:** Privacy-preserving aggregation is a cornerstone for AI systems that learn from distributed data without exposing individual records, especially in federated learning and telemetry. Existing two-server protocols (e.g., Prio and successors) set a practical baseline by validating inputs while preventing any single party from learning users' values, but they impose symmetric costs on both servers and communication that scales with the per-client input dimension $L$. Modern learning tasks routinely i...

---

### 36. Memori: A Persistent Memory Layer for Efficient, Context-Aware LLM Agents

**Authors:** Luiz C. Borro, Luiz A. B. Macarini, Gordon Tindall, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19935v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19935v1)

**Summary:** As large language models (LLMs) evolve into autonomous agents, persistent memory at the API layer is essential for enabling context-aware behavior across LLMs and multi-session interactions. Existing approaches force vendor lock-in and rely on injecting large volumes of raw conversation into prompts, leading to high token costs and degraded performance.   We introduce Memori, an LLM-agnostic persistent memory layer that treats memory as a data structuring problem. Its Advanced Augmentation pipel...

---

### 37. Infinite-dimensional spherical-radial decomposition for probabilistic functions, with application to constrained optimal control and Gaussian process regression

**Authors:** Kewei Wang, Georg Stadler

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19907v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19907v1)

**Summary:** The spherical-radial decomposition (SRD) is an efficient method for estimating probabilistic functions and their gradients defined over finite-dimensional elliptical distributions. In this work, we generalize the SRD to infinite stochastic dimensions by combining subspace SRD with standard Monte Carlo methods. The resulting method, which we call hybrid infinite-dimensional SRD (hiSRD) provides an unbiased, low-variance estimator for convex sets arising, for instance, in chance-constrained optimi...

---

### 38. Deep Autocorrelation Modeling for Time-Series Forecasting: Progress and Prospects

**Authors:** Hao Wang, Licheng Pan, Qingsong Wen, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19899v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19899v1)

**Summary:** Autocorrelation is a defining characteristic of time-series data, where each observation is statistically dependent on its predecessors. In the context of deep time-series forecasting, autocorrelation arises in both the input history and the label sequences, presenting two central research challenges: (1) designing neural architectures that model autocorrelation in history sequences, and (2) devising learning objectives that model autocorrelation in label sequences. Recent studies have made stri...

---

### 39. Integrating Meta-Features with Knowledge Graph Embeddings for Meta-Learning

**Authors:** Antonis Klironomos, Ioannis Dasoulas, Francesco Periti, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19888v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19888v1)

**Summary:** The vast collection of machine learning records available on the web presents a significant opportunity for meta-learning, where past experiments are leveraged to improve performance. Two crucial meta-learning tasks are pipeline performance estimation (PPE), which predicts pipeline performance on target datasets, and dataset performance-based similarity estimation (DPSE), which identifies datasets with similar performance patterns. Existing approaches primarily rely on dataset meta-features (e.g...

---

### 40. What If Consensus Lies? Selective-Complementary Reinforcement Learning at Test Time

**Authors:** Dong Yan, Jian Liang, Yanbo Wang, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19880v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19880v1)

**Summary:** Test-Time Reinforcement Learning (TTRL) enables Large Language Models (LLMs) to enhance reasoning capabilities on unlabeled test streams by deriving pseudo-rewards from majority voting consensus. However, existing TTRL methods rely exclusively on positive pseudo-labeling strategies. Such reliance becomes vulnerable under challenging scenarios where answer distributions are highly dispersed, resulting in weak consensus that inadvertently reinforces incorrect trajectories as supervision signals. I...

---

### 41. Discovery of Decision Synchronization Patterns from Event Logs

**Authors:** Tijmen Kuijpers, Karolin Winter, Remco Dijkman

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19879v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19879v1)

**Summary:** Synchronizing decisions between running cases in business processes facilitates fair and efficient use of resources, helps prioritize the most valuable cases, and prevents unnecessary waiting. Consequently, decision synchronization patterns are regularly built into processes, in the form of mechanisms that temporarily delay one case to favor another. These decision mechanisms therefore consider properties of multiple cases at once, rather than just the properties of a single case; an aspect that...

---

### 42. Minimax Generalized Cross-Entropy

**Authors:** Kartheek Bondugula, Santiago Mazuelas, Aritz Pérez, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19874v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19874v1)

**Summary:** Loss functions play a central role in supervised classification. Cross-entropy (CE) is widely used, whereas the mean absolute error (MAE) loss can offer robustness but is difficult to optimize. Interpolating between the CE and MAE losses, generalized cross-entropy (GCE) has recently been introduced to provide a trade-off between optimization difficulty and robustness. Existing formulations of GCE result in a non-convex optimization over classification margins that is prone to underfitting, leadi...

---

### 43. On the Dynamics & Transferability of Latent Generalization during Memorization

**Authors:** Simran Ketha, Venkatakrishnan Ramaswamy

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19865v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19865v1)

**Summary:** Deep networks have been known to have extraordinary generalization abilities, via mechanisms that aren't yet well understood. It is also known that upon shuffling labels in the training data to varying degrees, deep networks, trained with standard methods, can still achieve perfect or high accuracy on this corrupted training data. This phenomenon is called memorization, and typically comes at the cost of poorer generalization to true labels. Our recent work has demonstrated, that the internal re...

---

### 44. NASimJax: GPU-Accelerated Policy Learning Framework for Penetration Testing

**Authors:** Raphael Simon, José Carrasquel, Wim Mees, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19864v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19864v1)

**Summary:** Penetration testing, the practice of simulating cyberattacks to identify vulnerabilities, is a complex sequential decision-making task that is inherently partially observable and features large action spaces. Training reinforcement learning (RL) policies for this domain faces a fundamental bottleneck: existing simulators are too slow to train on realistic network scenarios at scale, resulting in policies that fail to generalize. We present NASimJax, a complete JAX-based reimplementation of the N...

---

### 45. IsoCLIP: Decomposing CLIP Projectors for Efficient Intra-modal Alignment

**Authors:** Simone Magistri, Dipam Goswami, Marco Mistretta, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19862v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19862v1)

**Summary:** Vision-Language Models like CLIP are extensively used for inter-modal tasks which involve both visual and text modalities. However, when the individual modality encoders are applied to inherently intra-modal tasks like image-to-image retrieval, their performance suffers from the intra-modal misalignment. In this paper we study intra-modal misalignment in CLIP with a focus on the role of the projectors that map pre-projection image and text embeddings into the shared embedding space. By analyzing...

---

### 46. Failure Modes for Deep Learning-Based Online Mapping: How to Measure and Address Them

**Authors:** Michael Hubbertz, Qi Han, Tobias Meisen

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19852v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19852v1)

**Summary:** Deep learning-based online mapping has emerged as a cornerstone of autonomous driving, yet these models frequently fail to generalize beyond familiar environments. We propose a framework to identify and measure the underlying failure modes by disentangling two effects: Memorization of input features and overfitting to known map geometries. We propose measures based on evaluation subsets that control for geographical proximity and geometric similarity between training and validation scenes. We in...

---

### 47. Modeling subgrid scale production rates on complex meshes using graph neural networks

**Authors:** Priyabrat Dash, Mathis Bode, Konduri Aditya

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19841v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19841v1)

**Summary:** Large-eddy simulations (LES) require closures for filtered production rates because the resolved fields do not contain all correlations that govern chemical source terms. We develop a graph neural network (GNN) that predicts filtered species production rates on non-uniform meshes from inputs of filtered mass fractions and temperature. Direct numerical simulations of turbulent premixed hydrogen-methane jet flames with hydrogen fractions of 10%, 50%, and 80% provide the dataset. All fields are Fav...

---

### 48. Explainable cluster analysis: a bagging approach

**Authors:** Federico Maria Quetti, Elena Ballante, Silvia Figini, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19840v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19840v1)

**Summary:** A major limitation of clustering approaches is their lack of explainability: methods rarely provide insight into which features drive the grouping of similar observations. To address this limitation, we propose an ensemble-based clustering framework that integrates bagging and feature dropout to generate feature importance scores, in analogy with feature importance mechanisms in supervised random forests. By leveraging multiple bootstrap resampling schemes and aggregating the resulting partition...

---

### 49. FIPO: Eliciting Deep Reasoning with Future-KL Influenced Policy Optimization

**Authors:** Chiyu Ma, Shuo Yang, Kexin Huang, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19835v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19835v1)

**Summary:** We present Future-KL Influenced Policy Optimization (FIPO), a reinforcement learning algorithm designed to overcome reasoning bottlenecks in large language models. While GRPO style training scales effectively, it typically relies on outcome-based rewards (ORM) that distribute a global advantage uniformly across every token in a trajectory. We argue that this coarse-grained credit assignment imposes a performance ceiling by failing to distinguish critical logical pivots from trivial tokens. FIPO ...

---

### 50. GDEGAN: Gaussian Dynamic Equivariant Graph Attention Network for Ligand Binding Site Prediction

**Authors:**  Animesh, Plaban Kumar Bhowmick, Pralay Mitra

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19817v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19817v1)

**Summary:** Accurate prediction of binding sites of a given protein, to which ligands can bind, is a critical step in structure-based computational drug discovery. Recently, Equivariant Graph Neural Networks (GNNs) have emerged as a powerful paradigm for binding site identification methods due to the large-scale availability of 3D structures of proteins via protein databases and AlphaFold predictions. The state-of-the-art equivariant GNN methods implement dot product attention, disregarding the variation in...

---

## cs.NE

**50 papers**

### 1. A Unified Phase-native Computational Principle Governs Hippocampal Spike Timing and Neural Coding

**Authors:** Reza Ahmadvand, Sara Safura Sharif, Yaser Mike Banad

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19690v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19690v1)

**Summary:** Hippocampal neurons exhibit precise phase locking to network oscillations, but the computational principle governing this temporal precision is still unclear. Neural information is conveyed jointly by firing rates and spike timing, but existing models treat these dimensions separately, limiting mechanistic interpretation of spike-field coupling and its reported association with spectral features such as the aperiodic slope. Here we show that hippocampal phase locking emerges from a fundamental d...

---

### 2. Recovering Sparse Neural Connectivity from Partial Measurements: A Covariance-Based Approach with Granger-Causality Refinement

**Authors:** Quilee Simeon

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.18497v1) | 📄 [PDF](https://arxiv.org/pdf/2603.18497v1)

**Summary:** Inferring the connectivity of neural circuits from incomplete observations is a fundamental challenge in neuroscience. We present a covariance-based method for estimating the weight matrix of a recurrent neural network from sparse, partial measurements across multiple recording sessions. By accumulating pairwise covariance estimates across sessions where different subsets of neurons are observed, we reconstruct the full connectivity matrix without requiring simultaneous recording of all neurons....

---

### 3. ALIGN: Adversarial Learning for Generalizable Speech Neuroprosthesis

**Authors:** Zhanqi Zhang, Shun Li, Bernardo L. Sabatini, et al.

**Published:** 2026-03-18

🔗 [Paper](http://arxiv.org/abs/2603.18299v1) | 📄 [PDF](https://arxiv.org/pdf/2603.18299v1)

**Summary:** Intracortical brain-computer interfaces (BCIs) can decode speech from neural activity with high accuracy when trained on data pooled across recording sessions. In realistic deployment, however, models must generalize to new sessions without labeled data, and performance often degrades due to cross-session nonstationarities (e.g., electrode shifts, neural turnover, and changes in user strategy). In this paper, we propose ALIGN, a session-invariant learning framework based on multi-domain adversar...

---

### 4. Constrained Hybrid Metaheuristic: A Universal Framework for Continuous Optimisation

**Authors:** Piotr A. Kowalski, Szymon Kucharczyk, Jacek Mańdziuk

**Published:** 2026-03-18

🔗 [Paper](http://arxiv.org/abs/2603.18295v1) | 📄 [PDF](https://arxiv.org/pdf/2603.18295v1)

**Summary:** This paper presents the constrained Hybrid Metaheuristic (cHM) algorithm as a general framework for continuous optimisation. Unlike many existing metaheuristics that are tailored to specific function classes or problem domains, cHM is designed to operate across a broad spectrum of objective functions, including those with unknown, heterogeneous, or complex properties such as non-convexity, non-separability, and varying smoothness. We provide a formal description of the algorithm, highlighting it...

---

### 5. Adaptive Domain Models: Bayesian Evolution, Warm Rotation, and Principled Training for Geometric and Neuromorphic AI

**Authors:** Houston Haynes

**Published:** 2026-03-18

🔗 [Paper](http://arxiv.org/abs/2603.18104v1) | 📄 [PDF](https://arxiv.org/pdf/2603.18104v1)

**Summary:** Prevailing AI training infrastructure assumes reverse-mode automatic differentiation over IEEE-754 arithmetic. The memory overhead of training relative to inference, optimizer complexity, and structural degradation of geometric properties through training are consequences of this arithmetic substrate. This paper develops an alternative training architecture grounded in three prior results: the Dimensional Type System and Deterministic Memory Management framework [6], which establishes stack-elig...

---

### 6. Large Language Models as a Semantic Interface and Ethical Mediator in Neuro-Digital Ecosystems: Conceptual Foundations and a Regulatory Imperative

**Authors:** Alexander V. Shenderuk-Zhidkov, Alexander E. Hramov

**Published:** 2026-03-18

🔗 [Paper](http://arxiv.org/abs/2603.17444v1) | 📄 [PDF](https://arxiv.org/pdf/2603.17444v1)

**Summary:** This article introduces and substantiates the concept of Neuro-Linguistic Integration (NLI), a novel paradigm for human-technology interaction where Large Language Models (LLMs) act as a key semantic interface between raw neural data and their social application. We analyse the dual nature of LLMs in this role: as tools that augment human capabilities in communication, medicine, and education, and as sources of unprecedented ethical risks to mental autonomy and neurorights. By synthesizing insig...

---

### 7. A Synthesizable RTL Implementation of Predictive Coding Networks

**Authors:** Timothy Oh

**Published:** 2026-03-18

🔗 [Paper](http://arxiv.org/abs/2603.18066v1) | 📄 [PDF](https://arxiv.org/pdf/2603.18066v1)

**Summary:** Backpropagation has enabled modern deep learning but is difficult to realize as an online, fully distributed hardware learning system due to global error propagation, phase separation, and heavy reliance on centralized memory. Predictive coding offers an alternative in which inference and learning arise from local prediction-error dynamics between adjacent layers. This paper presents a digital architecture that implements a discrete-time predictive coding update directly in hardware. Each neural...

---

### 8. Quadratic Surrogate Attractor for Particle Swarm Optimization

**Authors:** Maurizio Clemente, Marcello Canova

**Published:** 2026-03-17

🔗 [Paper](http://arxiv.org/abs/2603.17163v1) | 📄 [PDF](https://arxiv.org/pdf/2603.17163v1)

**Summary:** This paper presents a particle swarm optimization algorithm that leverages surrogate modeling to replace the conventional global best solution with the minimum of an n-dimensional quadratic form, providing a better-conditioned dynamic attractor for the swarm. This refined convergence target, informed by the local landscape, enhances global convergence behavior and increases robustness against premature convergence and noise, while incurring only minimal computational overhead. The surrogate-augm...

---

### 9. Optimization-Embedded Active Multi-Fidelity Surrogate Learning for Multi-Condition Airfoil Shape Optimization

**Authors:** Isaac Robledo, Alberto Vilariño, Arnau Miró, et al.

**Published:** 2026-03-17

🔗 [Paper](http://arxiv.org/abs/2603.17057v1) | 📄 [PDF](https://arxiv.org/pdf/2603.17057v1)

**Summary:** Active multi-fidelity surrogate modeling is developed for multi-condition airfoil shape optimization to reduce high-fidelity CFD cost while retaining RANS-level accuracy. The framework couples a low-fidelity-informed Gaussian process regression transfer model with uncertainty-triggered sampling and a synchronized elitism rule embedded in a hybrid genetic algorithm. Low-fidelity XFOIL evaluations provide inexpensive features, while sparse RANS simulations are adaptively allocated when predictive ...

---

### 10. Attractor-Keyed Memory

**Authors:** Natalia G. Berloff

**Published:** 2026-03-17

🔗 [Paper](http://arxiv.org/abs/2603.17049v1) | 📄 [PDF](https://arxiv.org/pdf/2603.17049v1)

**Summary:** Physical selectors (lasers choosing a mode, Ising machines settling on a ground state, condensates occupying a spin state) produce high-dimensional signatures at the moment of decision: full field amplitudes, multimode interference patterns, or scattering responses. These signatures are richer than the winner's index, yet they are routinely discarded. We show that when the signatures are repeatable across trials (stereotyped) and linearly independent across routes, a single linear decoder compil...

---

### 11. Linearized Bregman Iterations for Sparse Spiking Neural Networks

**Authors:** Daniel Windhager, Bernhard A. Moser, Michael Lunglmayr

**Published:** 2026-03-17

🔗 [Paper](http://arxiv.org/abs/2603.16462v1) | 📄 [PDF](https://arxiv.org/pdf/2603.16462v1)

**Summary:** Spiking Neural Networks (SNNs) offer an energy efficient alternative to conventional Artificial Neural Networks (ANNs) but typically still require a large number of parameters. This work introduces Linearized Bregman Iterations (LBI) as an optimizer for training SNNs, enforcing sparsity through iterative minimization of the Bregman distance and proximal soft thresholding updates. To improve convergence and generalization, we employ the AdaBreg optimizer, a momentum and bias corrected Bregman var...

---

### 12. Deep Reinforcement Learning-Assisted Automated Operator Portfolio for Constrained Multi-objective Optimization

**Authors:** Shuai Shao, Ye Tian, Shangshang Yang, et al.

**Published:** 2026-03-17

🔗 [Paper](http://arxiv.org/abs/2603.16401v1) | 📄 [PDF](https://arxiv.org/pdf/2603.16401v1)

**Summary:** Constrained multi-objective optimization problems (CMOPs) are of great significance in the context of practical applications, ranging from scientific to engineering domains. Most existing constrained multi-objective evolutionary algorithms (CMOEAs) usually employ fixed operators all the time, which exhibit poor versatility in handling various CMOPs. Therefore, some recent studies have focused on adaptively selecting the best operators for the current population states during the search process. ...

---

### 13. Surrogate-Assisted Genetic Programming with Rank-Based Phenotypic Characterisation for Dynamic Multi-Mode Project Scheduling

**Authors:** Yuan Tian, Yi Mei, Mengjie Zhang

**Published:** 2026-03-17

🔗 [Paper](http://arxiv.org/abs/2603.16286v1) | 📄 [PDF](https://arxiv.org/pdf/2603.16286v1)

**Summary:** The dynamic multi-mode resource-constrained project scheduling problem (DMRCPSP) is of practical importance, as it requires making real-time decisions under changing project states and resource availability. Genetic Programming (GP) has been shown to effectively evolve heuristic rules for such decision-making tasks; however, the evolutionary process typically relies on a large number of simulation-based fitness evaluations, resulting in high computational cost. Surrogate models offer a promising...

---

### 14. Analytically tractable model of synaptic crowding explains emergent small-world structure and network dynamics

**Authors:** Makoto Fukushima

**Published:** 2026-03-16

🔗 [Paper](http://arxiv.org/abs/2603.19320v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19320v1)

**Summary:** Neural circuits must balance local connectivity constraints against the need for global integration. Here we introduce a minimal wiring rule motivated by synaptic crowding: as a neuron accumulates incoming connections, each additional synapse becomes progressively harder to form. This single-parameter model admits an exact finite-size solution for the induced in-degree distribution and yields simple scaling laws: mean connectivity grows only logarithmically with network size while variance remai...

---

### 15. EvoIQA - Explaining Image Distortions with Evolved White-Box Logic

**Authors:** Ruchika Gupta, Illya Bakurov, Nathan Haut, et al.

**Published:** 2026-03-16

🔗 [Paper](http://arxiv.org/abs/2603.15887v1) | 📄 [PDF](https://arxiv.org/pdf/2603.15887v1)

**Summary:** Traditional Image Quality Assessment (IQA) metrics typically fall into one of two extremes: rigid, hand-crafted mathematical models or "black-box" deep learning architectures that completely lack interpretability. To bridge this gap, we propose EvoIQA, a fully explainable symbolic regression framework based on Genetic Programming that Evolves explicit, human-readable mathematical formulas for image quality assessment (IQA). Utilizing a rich terminal set from the VSI, VIF, FSIM, and HaarPSI metri...

---

### 16. Towards Foundation Models for Consensus Rank Aggregation

**Authors:** Yijun Jin, Simon Klüttermann, Chiara Balestra, et al.

**Published:** 2026-03-16

🔗 [Paper](http://arxiv.org/abs/2603.15218v1) | 📄 [PDF](https://arxiv.org/pdf/2603.15218v1)

**Summary:** Aggregating a consensus ranking from multiple input rankings is a fundamental problem with applications in recommendation systems, search engines, job recruitment, and elections. Despite decades of research in consensus ranking aggregation, minimizing the Kemeny distance remains computationally intractable. Specifically, determining an optimal aggregation of rankings with respect to the Kemeny distance is an NP-hard problem, limiting its practical application to relatively small-scale instances....

---

### 17. CATFormer: When Continual Learning Meets Spiking Transformers With Dynamic Thresholds

**Authors:** Vaishnavi Nagabhushana, Kartikay Agrawal, Ayon Borthakur

**Published:** 2026-03-16

🔗 [Paper](http://arxiv.org/abs/2603.15184v1) | 📄 [PDF](https://arxiv.org/pdf/2603.15184v1)

**Summary:** Although deep neural networks perform extremely well in controlled environments, they fail in real-world scenarios where data isn't available all at once, and the model must adapt to a new data distribution that may or may not follow the initial distribution. Previously acquired knowledge is lost during subsequent updates based on new data. a phenomenon commonly known as catastrophic forgetting. In contrast, the brain can learn without such catastrophic forgetting, irrespective of the number of ...

---

### 18. Towards Solving Polynomial-Objective Integer Programming with Hypergraph Neural Networks

**Authors:** Minshuo Li, Yaoxin Wu, Pavel Troubil, et al.

**Published:** 2026-03-16

🔗 [Paper](http://arxiv.org/abs/2603.19318v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19318v1)

**Summary:** Complex real-world optimization problems often involve both discrete decisions and nonlinear relationships between variables. Many such problems can be modeled as polynomial-objective integer programs, encompassing cases with quadratic and higher-degree variable interactions. Nonlinearity makes them more challenging than their linear counterparts. In this paper, we propose a hypergraph neural network (HNN) based method to solve polynomial-objective integer programming (POIP). Besides presenting ...

---

### 19. MorphSNN: Adaptive Graph Diffusion and Structural Plasticity for Spiking Neural Networks

**Authors:** Yongsheng Huang, Peibo Duan, Yujie Wu, et al.

**Published:** 2026-03-15

🔗 [Paper](http://arxiv.org/abs/2603.14285v1) | 📄 [PDF](https://arxiv.org/pdf/2603.14285v1)

**Summary:** Spiking Neural Networks (SNNs) currently face a critical bottleneck: while individual neurons exhibit dynamic biological properties, their macro-scopic architectures remain confined within conventional connectivity patterns that are static and hierarchical. This discrepancy between neuron-level dynamics and network-level fixed connectivity eliminates critical brain-like lateral interactions, limiting adaptability in changing environments. To address this, we propose MorphSNN, a backbone framewor...

---

### 20. ST-ResGAT: Explainable Spatio-Temporal Graph Neural Network for Road Condition Prediction and Priority-Driven Maintenance

**Authors:** Mohsin Mahmud Topu, Azmine Toushik Wasi, Mahfuz Ahmed Anik, et al.

**Published:** 2026-03-14

🔗 [Paper](http://arxiv.org/abs/2603.14107v1) | 📄 [PDF](https://arxiv.org/pdf/2603.14107v1)

**Summary:** Climate-vulnerable road networks require a paradigm shift from reactive, fix-on-failure repairs to predictive, decision-ready maintenance. This paper introduces ST-ResGAT, a novel Spatio-Temporal Residual Graph Attention Network that fuses residual graph-attention encoding with GRU temporal aggregation to forecast pavement deterioration. Engineered for resource-constrained deployment, the framework translates continuous Pavement Condition Index (PCI) forecasts directly into the American Society ...

---

### 21. A Theory of Appropriateness That Accounts for Norms of Rationality

**Authors:** Joel Z. Leibo, Alexander Sasha Vezhnevets, Manfred Diaz, et al.

**Published:** 2026-03-14

🔗 [Paper](http://arxiv.org/abs/2603.14050v1) | 📄 [PDF](https://arxiv.org/pdf/2603.14050v1)

**Summary:** We propose a society-first theory of normative appropriateness where individuals, modeled as pre-trained actors with cognitive architectures analogous to Large Language Models (LLMs), generate behavior via predictive pattern completion. Our theory posits that individuals act by completing distributed symbolic patterns based on context, answering questions such as "What does a person such as I do in a situation such as this?". This sense-making mechanism provides a parsimonious account of the key...

---

### 22. MO-SAE:Multi-Objective Stacked Autoencoders Optimization for Edge Anomaly Detection

**Authors:** Lizhao Zhang, Shengsong Kong, Tao Guo, et al.

**Published:** 2026-03-14

🔗 [Paper](http://arxiv.org/abs/2603.13895v1) | 📄 [PDF](https://arxiv.org/pdf/2603.13895v1)

**Summary:** Stacked AutoEncoders (SAE) have been widely adopted in edge anomaly detection scenarios. However, the resource-intensive nature of SAE can pose significant challenges for edge devices, which are typically resource-constrained and must adapt rapidly to dynamic and changing conditions. Optimizing SAE to meet the heterogeneous demands of real-world deployment scenarios, including high performance under constrained storage, low power consumption, fast inference, and efficient model updates, remains ...

---

### 23. Benchmarking the Energy Cost of Assurance in Neuromorphic Edge Robotics

**Authors:** Sylvester Kaczmarek

**Published:** 2026-03-14

🔗 [Paper](http://arxiv.org/abs/2603.13880v1) | 📄 [PDF](https://arxiv.org/pdf/2603.13880v1)

**Summary:** Deploying trustworthy artificial intelligence on edge robotics imposes a difficult trade-off between high-assurance robustness and energy sustainability. Traditional defense mechanisms against adversarial attacks typically incur significant computational overhead, threatening the viability of power-constrained platforms in environments such as cislunar space. This paper quantifies the energy cost of assurance in event-driven neuromorphic systems. We benchmark the Hierarchical Temporal Defense (H...

---

### 24. Collapse or Preserve: Data-Dependent Temporal Aggregation for Spiking Neural Network Acceleration

**Authors:** Jiahao Qin

**Published:** 2026-03-14

🔗 [Paper](http://arxiv.org/abs/2603.13810v1) | 📄 [PDF](https://arxiv.org/pdf/2603.13810v1)

**Summary:** Spike sparsity is widely believed to enable efficient spiking neural network (SNN) inference on GPU hardware. We demonstrate this is an illusion: five distinct sparse computation strategies on Apple M3 Max all fail to outperform dense convolution, because SIMD architectures cannot exploit the fine-grained, unstructured sparsity of i.i.d. binary spikes. Instead, we propose Temporal Aggregated Convolution (TAC), which exploits convolution linearity to pre-aggregate $K$ spike frames before a single...

---

### 25. Projection-Free Evolution Strategies for Continuous Prompt Search

**Authors:** Yu Cai, Canxi Huang, Xiaoyu He

**Published:** 2026-03-14

🔗 [Paper](http://arxiv.org/abs/2603.13786v1) | 📄 [PDF](https://arxiv.org/pdf/2603.13786v1)

**Summary:** Continuous prompt search offers a computationally efficient alternative to conventional parameter tuning in natural language processing tasks. Nevertheless, its practical effectiveness can be significantly hindered by the black-box nature and the inherent high-dimensionality of the objective landscapes. Existing methods typically mitigate these challenges by restricting the search to a randomly projected low-dimensional subspace. However, the effectiveness and underlying motivation of the projec...

---

### 26. Sharpness Aware Surrogate Training for Spiking Neural Networks

**Authors:** Maximilian Nicholson

**Published:** 2026-03-14

🔗 [Paper](http://arxiv.org/abs/2603.18039v1) | 📄 [PDF](https://arxiv.org/pdf/2603.18039v1)

**Summary:** Surrogate gradients are a standard tool for training spiking neural networks (SNNs), but conventional hard forward or surrogate backward training couples a nonsmooth forward model with a biased gradient estimator. We study sharpness aware Surrogate Training (SAST), which applies sharpness aware Minimization (SAM) to a surrogate forward SNN trained by backpropagation. In this formulation, the optimization target is an ordinary smooth empirical risk, so the training gradient is exact for the auxil...

---

### 27. Equivalence of approximation by networks of single- and multi-spike neurons

**Authors:** Dominik Dold, Philipp Christian Petersen

**Published:** 2026-03-13

🔗 [Paper](http://arxiv.org/abs/2603.13478v1) | 📄 [PDF](https://arxiv.org/pdf/2603.13478v1)

**Summary:** In a spiking neural network, is it enough for each neuron to spike at most once? In recent work, approximation bounds for spiking neural networks have been derived, quantifying how well they can fit target functions. However, these results are only valid for neurons that spike at most once, which is commonly thought to be a strong limitation. Here, we show that the opposite is true for a large class of spiking neuron models, including the commonly used leaky integrate-and-fire model with subtrac...

---

### 28. MXNorm: Reusing MXFP block scales for efficient tensor normalisation

**Authors:** Callum McLean, Luke Y. Prince, Alexandre Payot, et al.

**Published:** 2026-03-13

🔗 [Paper](http://arxiv.org/abs/2603.13180v1) | 📄 [PDF](https://arxiv.org/pdf/2603.13180v1)

**Summary:** Matrix multiplication performance has long been the major bottleneck to scaling deep learning workloads, which has stimulated the design of new accelerators that use increasingly low-precision number formats. However, improvements in matrix multiplication performance have far outstripped improvements in performance on reductions and elementwise computations, which are still being performed in higher precision. In this work, we propose MXNorm, a drop-in replacement for RMSNorm that estimates the ...

---

### 29. Federated Few-Shot Learning on Neuromorphic Hardware: An Empirical Study Across Physical Edge Nodes

**Authors:** Steven Motta, Gioele Nanni

**Published:** 2026-03-13

🔗 [Paper](http://arxiv.org/abs/2603.13037v1) | 📄 [PDF](https://arxiv.org/pdf/2603.13037v1)

**Summary:** Federated learning on neuromorphic hardware remains unexplored because on-chip spike-timing-dependent plasticity (STDP) produces binary weight updates rather than the floating-point gradients assumed by standard algorithms. We build a two-node federated system with BrainChip Akida AKD1000 processors and run approximately 1,580 experimental trials across seven analysis phases. Of four weight-exchange strategies tested, neuron-level concatenation (FedUnion) consistently preserves accuracy while el...

---

### 30. Finite Difference Flow Optimization for RL Post-Training of Text-to-Image Models

**Authors:** David McAllister, Miika Aittala, Tero Karras, et al.

**Published:** 2026-03-13

🔗 [Paper](http://arxiv.org/abs/2603.12893v1) | 📄 [PDF](https://arxiv.org/pdf/2603.12893v1)

**Summary:** Reinforcement learning (RL) has become a standard technique for post-training diffusion-based image synthesis models, as it enables learning from reward signals to explicitly improve desirable aspects such as image quality and prompt alignment. In this paper, we propose an online RL variant that reduces the variance in the model updates by sampling paired trajectories and pulling the flow velocity in the direction of the more favorable image. Unlike existing methods that treat each sampling step...

---

### 31. SRAM-Based Compute-in-Memory Accelerator for Linear-decay Spiking Neural Networks

**Authors:** Hongyang Shang, Shuai Dong, Yahan Yang, et al.

**Published:** 2026-03-13

🔗 [Paper](http://arxiv.org/abs/2603.12739v1) | 📄 [PDF](https://arxiv.org/pdf/2603.12739v1)

**Summary:** Spiking Neural Networks (SNNs) have emerged as a biologically inspired alternative to conventional deep networks, offering event-driven and energy-efficient computation. However, their throughput remains constrained by the serial update of neuron membrane states. While many hardware accelerators and Compute-in-Memory (CIM) architectures efficiently parallelize the synaptic operation (W x I) achieving O(1) complexity for matrix-vector multiplication, the subsequent state update step still require...

---

### 32. Alternating Gradient Flow Utility: A Unified Metric for Structural Pruning and Dynamic Routing in Deep Networks

**Authors:** Tianhao Qian, Zhuoxuan Li, Jinde Cao, et al.

**Published:** 2026-03-12

🔗 [Paper](http://arxiv.org/abs/2603.12354v2) | 📄 [PDF](https://arxiv.org/pdf/2603.12354v2)

**Summary:** Efficient deep learning traditionally relies on static heuristics like weight magnitude or activation awareness (e.g., Wanda, RIA). While successful in unstructured settings, we observe a critical limitation when applying these metrics to the structural pruning of deep vision networks. These contemporary metrics suffer from a magnitude bias, failing to preserve critical functional pathways. To overcome this, we propose a decoupled kinetic paradigm inspired by Alternating Gradient Flow (AGF), uti...

---

### 33. Pruning-induced phases in fully-connected neural networks: the eumentia, the dementia, and the amentia

**Authors:** Haining Pan, Nakul Aggarwal, J. H. Pixley

**Published:** 2026-03-12

🔗 [Paper](http://arxiv.org/abs/2603.12316v1) | 📄 [PDF](https://arxiv.org/pdf/2603.12316v1)

**Summary:** Modern neural networks are heavily overparameterized, and pruning, which removes redundant neurons or connections, has emerged as a key approach to compressing them without sacrificing performance. However, while practical pruning methods are well developed, whether pruning induces sharp phase transitions in the neural networks and, if so, to what universality class they belong, remain open questions. To address this, we study fully-connected neural networks trained on MNIST, independently varyi...

---

### 34. Topological DeepONets and a generalization of the Chen-Chen operator approximation theorem

**Authors:** Vugar Ismailov

**Published:** 2026-03-12

🔗 [Paper](http://arxiv.org/abs/2603.11972v1) | 📄 [PDF](https://arxiv.org/pdf/2603.11972v1)

**Summary:** Deep Operator Networks (DeepONets) provide a branch-trunk neural architecture for approximating nonlinear operators acting between function spaces. In the classical operator approximation framework, the input is a function $u\in C(K_1)$ defined on a compact set $K_1$ (typically a compact subset of a Banach space), and the operator maps $u$ to an output function $G(u)\in C(K_2)$ defined on a compact Euclidean domain $K_2\subset\mathbb{R}^d$. In this paper, we develop a topological extension in wh...

---

### 35. SNAP-V: A RISC-V SoC with Configurable Neuromorphic Acceleration for Small-Scale Spiking Neural Networks

**Authors:** Kanishka Gunawardana, Sanka Peeris, Kavishka Rambukwella, et al.

**Published:** 2026-03-12

🔗 [Paper](http://arxiv.org/abs/2603.11939v1) | 📄 [PDF](https://arxiv.org/pdf/2603.11939v1)

**Summary:** Spiking Neural Networks (SNNs) have gained significant attention in edge computing due to their low power consumption and computational efficiency. However, existing implementations either use conventional System on Chip (SoC) architectures that suffer from memory-processor bottlenecks, or large-scale neuromorphic hardware that is inefficient and wasteful for small-scale SNN applications. This work presents SNAP-V, a RISC-V-based neuromorphic SoC with two accelerator variants: Cerebra-S (bus-bas...

---

### 36. An Evolutionary Algorithm with Probabilistic Annealing for Large-scale Sparse Multi-objective Optimization

**Authors:** Shuai Shao, Yuhao Sun, Xing Chen, et al.

**Published:** 2026-03-12

🔗 [Paper](http://arxiv.org/abs/2603.11874v1) | 📄 [PDF](https://arxiv.org/pdf/2603.11874v1)

**Summary:** Large-scale sparse multi-objective optimization problems (LSMOPs) are prevalent in real-world applications, where optimal solutions typically contain only a few nonzero variables, such as in adversarial attacks, critical node detection, and sparse signal reconstruction. Since the function evaluation of LSMOPs often relies on large-scale datasets involving a large number of decision variables, the search space becomes extremely high-dimensional. The coexistence of sparsity and high dimensionality...

---

### 37. Stable Spike: Dual Consistency Optimization via Bitwise AND Operations for Spiking Neural Networks

**Authors:** Yongqi Ding, Kunshan Yang, Linze Li, et al.

**Published:** 2026-03-12

🔗 [Paper](http://arxiv.org/abs/2603.11676v1) | 📄 [PDF](https://arxiv.org/pdf/2603.11676v1)

**Summary:** Although the temporal spike dynamics of spiking neural networks (SNNs) enable low-power temporal pattern capture capabilities, they also incur inherent inconsistencies that severely compromise representation. In this paper, we perform dual consistency optimization via Stable Spike to mitigate this problem, thereby improving the recognition performance of SNNs. With the hardware-friendly ``AND" bit operation, we efficiently decouple the stable spike skeleton from the multi-timestep spike maps, th...

---

### 38. Quantum mechanical framework for quantization-based optimization: from Gradient flow to Schroedinger equation

**Authors:** Jinwuk Seok, Changsik Cho

**Published:** 2026-03-12

🔗 [Paper](http://arxiv.org/abs/2603.11536v1) | 📄 [PDF](https://arxiv.org/pdf/2603.11536v1)

**Summary:** This work presents a quantum mechanical framework for analyzing quantization-based optimization algorithms. The sampling process of the quantization-based search is modeled as a gradient-flow dissipative system, leading to a Hamilton-Jacobi-Bellman (HJB) representation. Through a suitable transformation of the objective function, this formulation yields the Schroedinger equation, which reveals that quantum tunneling enables escape from local minima and guarantees access to the global optimum. By...

---

### 39. COMIC: Agentic Sketch Comedy Generation

**Authors:** Susung Hong, Brian Curless, Ira Kemelmacher-Shlizerman, et al.

**Published:** 2026-03-11

🔗 [Paper](http://arxiv.org/abs/2603.11048v1) | 📄 [PDF](https://arxiv.org/pdf/2603.11048v1)

**Summary:** We propose a fully automated AI system that produces short comedic videos similar to sketch shows such as Saturday Night Live. Starting with character references, the system employs a population of agents loosely based on real production studio roles, structured to optimize the quality and diversity of ideas and outputs through iterative competition, evaluation, and improvement. A key contribution is the introduction of LLM critics aligned with real viewer preferences through the analysis of a c...

---

### 40. ForwardFlow: Simulation only statistical inference using deep learning

**Authors:** Stefan Böhringer

**Published:** 2026-03-11

🔗 [Paper](http://arxiv.org/abs/2603.10991v1) | 📄 [PDF](https://arxiv.org/pdf/2603.10991v1)

**Summary:** Deep learning models are being used for the analysis of parametric statistical models based on simulation-only frameworks. Bayesian models using normalizing flows simulate data from a prior distribution and are composed of two deep neural networks: a summary network that learns a sufficient statistic for the parameter and a normalizing flow that conditional on the summary network can approximate the posterior distribution. Here, we explore frequentist models that are based on a single summary ne...

---

### 41. Efficient Approximation to Analytic and $L^p$ functions by Height-Augmented ReLU Networks

**Authors:** ZeYu Li, FengLei Fan, TieYong Zeng

**Published:** 2026-03-11

🔗 [Paper](http://arxiv.org/abs/2603.11128v1) | 📄 [PDF](https://arxiv.org/pdf/2603.11128v1)

**Summary:** This work addresses two fundamental limitations in neural network approximation theory. We demonstrate that a three-dimensional network architecture enables a significantly more efficient representation of sawtooth functions, which serves as the cornerstone in the approximation of analytic and $L^p$ functions. First, we establish substantially improved exponential approximation rates for several important classes of analytic functions and offer a parameter-efficient network design. Second, for t...

---

### 42. Multi-objective Genetic Programming with Multi-view Multi-level Feature for Enhanced Protein Secondary Structure Prediction

**Authors:** Yining Qian, Lijie Su, Meiling Xu, et al.

**Published:** 2026-03-11

🔗 [Paper](http://arxiv.org/abs/2603.12293v1) | 📄 [PDF](https://arxiv.org/pdf/2603.12293v1)

**Summary:** Predicting protein secondary structure is essential for understanding protein function and advancing drug discovery. However, the intricate sequence-structure relationship poses significant challenges for accurate modeling. To address these, we propose MOGP-MMF, a multi-objective genetic programming framework that reformulates PSSP as an automated optimization task focused on feature selection and fusion. Specifically, MOGP-MMF introduces a multi-view multi-level representation strategy that int...

---

### 43. An Event-Driven E-Skin System with Dynamic Binary Scanning and real time SNN Classification

**Authors:** Gaishan Li, Zhengnan Fu, Anubhab Tripathi, et al.

**Published:** 2026-03-11

🔗 [Paper](http://arxiv.org/abs/2603.10537v1) | 📄 [PDF](https://arxiv.org/pdf/2603.10537v1)

**Summary:** This paper presents a novel hardware system for high-speed, event-sparse sampling-based electronic skin (e-skin)that integrates sensing and neuromorphic computing. The system is built around a 16x16 piezoresistive tactile array with front end and introduces a event-based binary scan search strategy to classify the digits. This event-driven strategy achieves a 12.8x reduction in scan counts, a 38.2x data compression rate and a 28.4x equivalent dynamic range, a 99% data sparsity, drastically reduc...

---

### 44. Resource-constrained Amazons chess decision framework integrating large language models and graph attention

**Authors:** Tianhao Qian, Zhuoxuan Li, Jinde Cao, et al.

**Published:** 2026-03-11

🔗 [Paper](http://arxiv.org/abs/2603.10512v1) | 📄 [PDF](https://arxiv.org/pdf/2603.10512v1)

**Summary:** Artificial intelligence has advanced significantly through the development of intelligent game-playing systems, providing rigorous testbeds for decision-making, strategic planning, and adaptive learning. However, resource-constrained environments pose critical challenges, as conventional deep learning methods heavily rely on extensive datasets and computational resources. In this paper, we propose a lightweight hybrid framework for the Game of the Amazons, which explores the paradigm of weak-to-...

---

### 45. Muscle Synergy Priors Enhance Biomechanical Fidelity in Predictive Musculoskeletal Locomotion Simulation

**Authors:** Ilseung Park, Eunsik Choi, Jangwhan Ahn, et al.

**Published:** 2026-03-11

🔗 [Paper](http://arxiv.org/abs/2603.10474v1) | 📄 [PDF](https://arxiv.org/pdf/2603.10474v1)

**Summary:** Human locomotion emerges from high-dimensional neuromuscular control, making predictive musculoskeletal simulation challenging. We present a physiology-informed reinforcement-learning framework that constrains control using muscle synergies. We extracted a low-dimensional synergy basis from inverse musculoskeletal analyses of a small set of overground walking trials and used it as the action space for a muscle-driven three-dimensional model trained across variable speeds, slopes and uneven terra...

---

### 46. Intrinsic Numerical Robustness and Fault Tolerance in a Neuromorphic Algorithm for Scientific Computing

**Authors:** Bradley H. Theilman, James B. Aimone

**Published:** 2026-03-10

🔗 [Paper](http://arxiv.org/abs/2603.10246v1) | 📄 [PDF](https://arxiv.org/pdf/2603.10246v1)

**Summary:** The potential for neuromorphic computing to provide intrinsic fault tolerance has long been speculated, but the brain's robustness in neuromorphic applications has yet to be demonstrated. Here, we show that a previously described, natively spiking neuromorphic algorithm for solving partial differential equations is intrinsically tolerant to structural perturbations in the form of ablated neurons and dropped spikes. The tolerance band for these perturbations is large: we find that as many as 32 p...

---

### 47. GPU-Accelerated Genetic Programming for Symbolic Regression with Beagle Framework

**Authors:** Nathan Haut, Ilya Basin, Marzieh Kianinejad, et al.

**Published:** 2026-03-10

🔗 [Paper](http://arxiv.org/abs/2603.12292v1) | 📄 [PDF](https://arxiv.org/pdf/2603.12292v1)

**Summary:** Beagle is a new software framework that enables execution of Genetic Programming tasks on the GPU. Currently available for symbolic regression, it processes individuals of the population and fitness cases for training in a way that maximizes throughput on extant GPU platforms. In this contribution, we report on the benchmarking of Beagle on the Feynman Symbolic Regression dataset and compare its performance with a fast CPU system called StackGP and the widely available PySR system under the same...

---

### 48. A Variational Latent Equilibrium for Learning in Neuronal Circuits

**Authors:** Simon Brandt, Paul Haider, Walter Senn, et al.

**Published:** 2026-03-10

🔗 [Paper](http://arxiv.org/abs/2603.09600v2) | 📄 [PDF](https://arxiv.org/pdf/2603.09600v2)

**Summary:** Brains remain unrivaled in their ability to recognize and generate complex spatiotemporal patterns. While AI is able to reproduce some of these capabilities, deep learning algorithms remain largely at odds with our current understanding of brain circuitry and dynamics. This is prominently the case for backpropagation through time (BPTT), the go-to algorithm for learning complex temporal dependencies. In this work we propose a general formalism to approximate BPTT in a controlled, biologically pl...

---

### 49. Symbolic Discovery of Stochastic Differential Equations with Genetic Programming

**Authors:** Sigur de Vries, Sander W. Keemink, Marcel A. J. van Gerven

**Published:** 2026-03-10

🔗 [Paper](http://arxiv.org/abs/2603.09597v1) | 📄 [PDF](https://arxiv.org/pdf/2603.09597v1)

**Summary:** Automated scientific discovery aims to improve scientific understanding through machine learning. A central approach in this field is symbolic regression, which uses genetic programming or sparse regression to learn interpretable mathematical expressions to explain observed data. Conventionally, the focus of symbolic regression is on identifying ordinary differential equations. The general view is that noise only complicates the recovery of deterministic dynamics. However, explicitly learning a ...

---

### 50. DendroNN: Dendrocentric Neural Networks for Energy-Efficient Classification of Event-Based Data

**Authors:** Jann Krausse, Zhe Su, Kyrus Mama, et al.

**Published:** 2026-03-10

🔗 [Paper](http://arxiv.org/abs/2603.09274v1) | 📄 [PDF](https://arxiv.org/pdf/2603.09274v1)

**Summary:** Spatiotemporal information is at the core of diverse sensory processing and computational tasks. Feed-forward spiking neural networks can be used to solve these tasks while offering potential benefits in terms of energy efficiency by computing event-based. However, they have trouble decoding temporal information with high accuracy. Thus, they commonly resort to recurrence or delays to enhance their temporal computing ability which, however, bring downsides in terms of hardware-efficiency. In the...

---

## q-bio.NC

**50 papers**

### 1. Problem difficulty and waiting time shape the level of detail and temporal organization of visual strategies in human planning

**Authors:** Mattia Eluchans, Giovanni Pezzulo

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19881v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19881v1)

**Summary:** Planning entails identifying sequences of actions to reach a goal, yet we still have incomplete knowledge of how problem constraints, such as difficulty and available time, influence the visual strategies supporting plan construction, both in terms of coverage of the to-be-executed plans and its temporal organization. To fill this gap, we recorded participants' cursor and eye movements in a multi-target problem solving task on a grid. We manipulated two orthogonal dimensions: problem difficulty,...

---

### 2. Multimodal branched transport infers anatomically aligned brain reaction maps

**Authors:** Cristian Mendico

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19761v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19761v1)

**Summary:** How external stimulation is transformed into distributed reaction patterns remains unresolved at the level of propagation architecture. Existing large-scale control models quantify transition costs on prescribed networks but do not infer the routing map itself from source and target activity. Here we combine task-related blood-oxygen-level-dependent responses, source-reconstructed electrophysiology and tractography-derived anisotropy to estimate stimulation and reaction measures, define an anato...

---

### 3. Branched Optimal Transport for Stimulus to Reaction Brain Mapping

**Authors:** Cristian Mendico

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19751v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19751v1)

**Summary:** A central problem in systems neuroscience is to determine how an external stimulation is propagated through the brain so as to produce a reaction. Current deterministic and stochastic control models quantify transition costs between brain states on a prescribed network, but do not treat the transport network itself as an unknown. Here we propose a variational framework in which the inferred object is a graph/current connecting a stimulation source measure to a reaction target measure. The model ...

---

### 4. A Unified Phase-native Computational Principle Governs Hippocampal Spike Timing and Neural Coding

**Authors:** Reza Ahmadvand, Sara Safura Sharif, Yaser Mike Banad

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19690v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19690v1)

**Summary:** Hippocampal neurons exhibit precise phase locking to network oscillations, but the computational principle governing this temporal precision is still unclear. Neural information is conveyed jointly by firing rates and spike timing, but existing models treat these dimensions separately, limiting mechanistic interpretation of spike-field coupling and its reported association with spectral features such as the aperiodic slope. Here we show that hippocampal phase locking emerges from a fundamental d...

---

### 5. Curvature Sensitive Cells in the Modular Structures of The Visual Cortex

**Authors:** Giovanna Citti, Vasiliki Liontou

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.19425v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19425v1)

**Summary:** We propose a model of the functional architecture of curvature-sensitive cells in the primary visual cortex. The model accounts for the modular and hierarchical organization of the cortex, the horizontal connectivity, and the shape of receptive profiles of these cells as Gabor-type filters. We construct a canonical affine subbundle of the cotangent bundle of the manifold of oriented contact elements of the retina as a geometric model for these cells, and show that this subbundle carries an Engel...

---

### 6. Hierarchical Latent Structure Learning through Online Inference

**Authors:** Ines Aitsahalia, Kiyohito Iigaya

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.19139v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19139v1)

**Summary:** Learning systems must balance generalization across experiences with discrimination of task-relevant details. Effective learning therefore requires representations that support both. Online latent-cause models support incremental inference but assume flat partitions, whereas hierarchical Bayesian models capture multilevel structure but typically require offline inference. We introduce the Hierarchical Online Learning of Multiscale Experience Structure (HOLMES) model, a computational framework fo...

---

### 7. Resolving the Blow-Up: A Time-Dilated Numerical Framework for Multiple Firing Events in Mean-Field Neuronal Networks

**Authors:** Xu'an Dou, Louis Tao, Zhe Xue, et al.

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.18475v1) | 📄 [PDF](https://arxiv.org/pdf/2603.18475v1)

**Summary:** In large-scale excitatory neuronal networks, rapid synchronization manifests as {multiple firing events (MFEs)}, mathematically characterized by a finite-time blow-up of the neuronal firing rate in the mean-field Fokker-Planck equation. Standard numerical methods struggle to resolve this singularity due to the divergent boundary flux and the instantaneous nature of the population voltage reset. In this work, we propose a robust {multiscale numerical framework based on time dilation}. By transfor...

---

### 8. Unified Policy Value Decomposition for Rapid Adaptation

**Authors:** Cristiano Capone, Luca Falorsi, Andrea Ciardiello, et al.

**Published:** 2026-03-18

🔗 [Paper](http://arxiv.org/abs/2603.17947v1) | 📄 [PDF](https://arxiv.org/pdf/2603.17947v1)

**Summary:** Rapid adaptation in complex control systems remains a central challenge in reinforcement learning. We introduce a framework in which policy and value functions share a low-dimensional coefficient vector - a goal embedding - that captures task identity and enables immediate adaptation to novel tasks without retraining representations. During pretraining, we jointly learn structured value bases and compatible policy bases through a bilinear actor-critic decomposition. The critic factorizes as Q = ...

---

### 9. Inhibitory normalization of error signals improves learning in neural circuits

**Authors:** Roy Henha Eyono, Daniel Levenstein, Arna Ghosh, et al.

**Published:** 2026-03-18

🔗 [Paper](http://arxiv.org/abs/2603.17676v1) | 📄 [PDF](https://arxiv.org/pdf/2603.17676v1)

**Summary:** Normalization is a critical operation in neural circuits. In the brain, there is evidence that normalization is implemented via inhibitory interneurons and allows neural populations to adjust to changes in the distribution of their inputs. In artificial neural networks (ANNs), normalization is used to improve learning in tasks that involve complex input distributions. However, it is unclear whether inhibition-mediated normalization in biological neural circuits also improves learning. Here, we e...

---

### 10. Agentic Cognitive Profiling: Realigning Automated Alzheimer's Disease Detection with Clinical Construct Validity

**Authors:** Jiawen Kang, Kun Li, Dongrui Han, et al.

**Published:** 2026-03-18

🔗 [Paper](http://arxiv.org/abs/2603.17392v1) | 📄 [PDF](https://arxiv.org/pdf/2603.17392v1)

**Summary:** Automated Alzheimer's Disease (AD) screening has predominantly followed the inductive paradigm of pattern recognition, which directly maps the input signal to the outcome label. This paradigm sacrifices construct validity of clinical protocol for statistical shortcuts. This paper proposes Agentic Cognitive Profiling (ACP), an agentic framework that realigns automated screening with clinical protocol logic across multiple cognitive domains. Rather than learning opaque mappings from transcripts to...

---

### 11. Beyond bouba/kiki: Multidimensional semantic signals are deeply woven into the fabric of natural language

**Authors:** Gexin Zhao

**Published:** 2026-03-18

🔗 [Paper](http://arxiv.org/abs/2603.17306v2) | 📄 [PDF](https://arxiv.org/pdf/2603.17306v2)

**Summary:** A foundational assumption in linguistics holds that the relationship between a word's sound and its meaning is arbitrary. Accumulating evidence from sound symbolism challenges this view, yet no study has systematically mapped the multidimensional semantic profile of every phonological unit within a language. Here we show that individual letter-phonemes in English carry structured, multidimensional semantic signals. Using a minimal-pair paradigm spanning all 220 pairwise letter contrasts, three l...

---

### 12. Bayesian Inference of Psychometric Variables From Brain and Behavior in Implicit Association Tests

**Authors:** Christian A. Kothe, Sean Mullen, Michael V. Bronstein, et al.

**Published:** 2026-03-17

🔗 [Paper](http://arxiv.org/abs/2603.16741v1) | 📄 [PDF](https://arxiv.org/pdf/2603.16741v1)

**Summary:** Objective. We establish a principled method for inferring mental health related psychometric variables from neural and behavioral data using the Implicit Association Test (IAT) as the data generation engine, aiming to overcome the limited predictive performance (typically under 0.7 AUC) of the gold-standard D-score method, which relies solely on reaction times.   Approach. We propose a sparse hierarchical Bayesian model that leverages multi-modal data to predict experiences related to mental ill...

---

### 13. The immediate effect of kangaroo mother care on Mother-infant inter-brain synchrony and infant brain function

**Authors:** Yu Liu, Jiayang Xu, Tianzi Wang, et al.

**Published:** 2026-03-17

🔗 [Paper](http://arxiv.org/abs/2603.16501v1) | 📄 [PDF](https://arxiv.org/pdf/2603.16501v1)

**Summary:** Kangaroo mother care (KMC) is an intervention involving skin-to-skin contact that promotes physiological stability and supports long-term neurodevelopment in preterm infants. However, the underlying neurophysiological mechanisms remain unclear. We aimed to investigate the immediate effects of the first KMC on infants' brain function, mother-infant inter-brain synchrony, as well as their associations. Fifty-eight preterm infants (gestational age < 32 weeks or birth weight < 1500 g) and their moth...

---

### 14. Hippocampus mediates conceptual generalization of pain modulation

**Authors:** Dylan Sutterlin Guindon, Tor D Wager, Leonie Koban

**Published:** 2026-03-17

🔗 [Paper](http://arxiv.org/abs/2603.16288v1) | 📄 [PDF](https://arxiv.org/pdf/2603.16288v1)

**Summary:** Pain is strongly influenced by expectations and learning from previous experience, such as in classical conditioning. Conditioned responses and expectations can generalize to perceptually and conceptually related cues, but how generalization influences pain experience and the neurobiological processing of pain remains unclear. We used fMRI and multilevel mediation analyses to address this question. Thirty-six human participants first learned to associate two visual cues from distinct conceptual ...

---

### 15. Laya: A LeJEPA Approach to EEG via Latent Prediction over Reconstruction

**Authors:** Saarang Panchavati, Uddhav Panchavati, Corey Arnold, et al.

**Published:** 2026-03-17

🔗 [Paper](http://arxiv.org/abs/2603.16281v1) | 📄 [PDF](https://arxiv.org/pdf/2603.16281v1)

**Summary:** Electroencephalography (EEG) is a widely used tool for studying brain function, with applications in clinical neuroscience, diagnosis, and brain-computer interfaces (BCIs). Recent EEG foundation models trained on large unlabeled corpora aim to learn transferable representations, but their effectiveness remains unclear; reported improvements over smaller task-specific models are often modest, sensitive to downstream adaptation and fine-tuning strategies, and limited under linear probing. We hypot...

---

### 16. Early Pre-Stroke Detection via Wearable IMU-Based Gait Variability and Postural Drift Analysis

**Authors:** Chanakan Chaipan, Aueaphum Aueawatthanaphisut

**Published:** 2026-03-17

🔗 [Paper](http://arxiv.org/abs/2603.16178v1) | 📄 [PDF](https://arxiv.org/pdf/2603.16178v1)

**Summary:** Early identification of individuals at risk of stroke remains a major clinical challenge, as prodromal motor im- pairments are often subtle and transient. In this pilot study, a wearable sensor-based framework is proposed for early pre- stroke risk screening using a single inertial measurement unit mounted on the sacral region to capture pelvic motion during gait and standing tasks. The pelvis is treated as a biomechanical proxy for global motor control, enabling the quantification of gait varia...

---

### 17. Analytically tractable model of synaptic crowding explains emergent small-world structure and network dynamics

**Authors:** Makoto Fukushima

**Published:** 2026-03-16

🔗 [Paper](http://arxiv.org/abs/2603.19320v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19320v1)

**Summary:** Neural circuits must balance local connectivity constraints against the need for global integration. Here we introduce a minimal wiring rule motivated by synaptic crowding: as a neuron accumulates incoming connections, each additional synapse becomes progressively harder to form. This single-parameter model admits an exact finite-size solution for the induced in-degree distribution and yields simple scaling laws: mean connectivity grows only logarithmically with network size while variance remai...

---

### 18. The Neuroscience of Transformers

**Authors:** Peter Koenig, Mario Negrello

**Published:** 2026-03-16

🔗 [Paper](http://arxiv.org/abs/2603.15339v1) | 📄 [PDF](https://arxiv.org/pdf/2603.15339v1)

**Summary:** Neuroscience has long informed the development of artificial neural networks, but the success of modern architectures invites, in turn, the converse: can modern networks teach us lessons about brain function? Here, we examine the structure of the cortical column and propose that the transformer provides a natural computational analogy for multiple elements of cortical microcircuit organization. Rather than claiming a literal implementation of transformer equations in cortex, we develop a hypothe...

---

### 19. BCMI-Driven Motion Control Detection: EEG-Based Machine Learning and Interaction Entropy for High-Order Brain Networks

**Authors:** Jiajia Li, Fan Li, Jian Song

**Published:** 2026-03-16

🔗 [Paper](http://arxiv.org/abs/2603.15208v1) | 📄 [PDF](https://arxiv.org/pdf/2603.15208v1)

**Summary:** This study investigates the cognitive motor control detection and the underlying neuroregulatory mechanisms during music-assisted simulated driving. Using a dynamic higher-order network model constructed with EEG-based cross-information entropy, we quantify the dynamic coordination within brain networks activated during both music listening and driving. This approach, which contrasts with previous static network analyses, provides novel insights into how musical stimuli modulate the complex inte...

---

### 20. D-MEM: Dopamine-Gated Agentic Memory via Reward Prediction Error Routing

**Authors:** Yuru Song, Qi Xin

**Published:** 2026-03-15

🔗 [Paper](http://arxiv.org/abs/2603.14597v1) | 📄 [PDF](https://arxiv.org/pdf/2603.14597v1)

**Summary:** Autonomous LLM agents require structured long-term memory, yet current "append-and-evolve" systems like A-MEM face O(N^2) write-latency and excessive token costs. We introduce D-MEM (Dopamine-Gated Agentic Memory), a biologically inspired architecture that decouples short-term interaction from cognitive restructuring via a Fast/Slow routing system based on Reward Prediction Error (RPE). A lightweight Critic Router evaluates stimuli for Surprise and Utility. Routine, low-RPE inputs are bypassed o...

---

### 21. Deep probabilistic model synthesis enables unified modeling of whole-brain neural activity across individual subjects

**Authors:** William E. Bishop, Luuk W. Hesselink, Bernhard Englitz, et al.

**Published:** 2026-03-15

🔗 [Paper](http://arxiv.org/abs/2603.14161v1) | 📄 [PDF](https://arxiv.org/pdf/2603.14161v1)

**Summary:** Many disciplines need quantitative models that synthesize experimental data across multiple instances of the same general system. For example, neuroscientists must combine data from the brains of many individual animals to understand the species' brain in general. However, typical machine learning models treat one system instance at a time. Here we introduce a machine learning framework, deep probabilistic model synthesis (DPMS), that leverages system properties auxiliary to the model to combine...

---

### 22. Human-like Object Grouping in Self-supervised Vision Transformers

**Authors:** Hossein Adeli, Seoyoung Ahn, Andrew Luo, et al.

**Published:** 2026-03-14

🔗 [Paper](http://arxiv.org/abs/2603.13994v1) | 📄 [PDF](https://arxiv.org/pdf/2603.13994v1)

**Summary:** Vision foundation models trained with self-supervised objectives achieve strong performance across diverse tasks and exhibit emergent object segmentation properties. However, their alignment with human object perception remains poorly understood. Here, we introduce a behavioral benchmark in which participants make same/different object judgments for dot pairs on naturalistic scenes, scaling up a classical psychophysics paradigm to over 1000 trials. We test a diverse set of vision models using a ...

---

### 23. Equivalence of approximation by networks of single- and multi-spike neurons

**Authors:** Dominik Dold, Philipp Christian Petersen

**Published:** 2026-03-13

🔗 [Paper](http://arxiv.org/abs/2603.13478v1) | 📄 [PDF](https://arxiv.org/pdf/2603.13478v1)

**Summary:** In a spiking neural network, is it enough for each neuron to spike at most once? In recent work, approximation bounds for spiking neural networks have been derived, quantifying how well they can fit target functions. However, these results are only valid for neurons that spike at most once, which is commonly thought to be a strong limitation. Here, we show that the opposite is true for a large class of spiking neuron models, including the commonly used leaky integrate-and-fire model with subtrac...

---

### 24. Developing the PsyCogMetrics AI Lab to Evaluate Large Language Models and Advance Cognitive Science -- A Three-Cycle Action Design Science Study

**Authors:** Zhiye Jin, Yibai Li, K. D. Joshi, et al.

**Published:** 2026-03-13

🔗 [Paper](http://arxiv.org/abs/2603.13126v1) | 📄 [PDF](https://arxiv.org/pdf/2603.13126v1)

**Summary:** This study presents the development of the PsyCogMetrics AI Lab (psycogmetrics.ai), an integrated, cloud-based platform that operationalizes psychometric and cognitive-science methodologies for Large Language Model (LLM) evaluation. Framed as a three-cycle Action Design Science study, the Relevance Cycle identifies key limitations in current evaluation methods and unfulfilled stakeholder needs. The Rigor Cycle draws on kernel theories such as Popperian falsifiability, Classical Test Theory, and ...

---

### 25. Pulse desynchronization of neural populations by targeting the centroid of the limit cycle in phase space

**Authors:** Ramón Guevara, Marco Zenari, Giorgio Nicoletti, et al.

**Published:** 2026-03-13

🔗 [Paper](http://arxiv.org/abs/2603.12878v1) | 📄 [PDF](https://arxiv.org/pdf/2603.12878v1)

**Summary:** The synchronized activity of neuronal populations can lead to pathological over-synchronization in conditions such as epilepsy and Parkinson disease. Such states can be desynchronized by brief electrical pulses. But when the underlying oscillating system is not known, as in most practical applications, to determine the specific times and intensities of pulses used for desynchronizaton is a difficult inverse problem. Here we propose a desynchronization scheme for neuronal models of bi-variate neu...

---

### 26. Dual-Laws Model for a theory of artificial consciousness

**Authors:** Yoshiyuki Ohmura, Yasuo Kuniyoshi

**Published:** 2026-03-13

🔗 [Paper](http://arxiv.org/abs/2603.12662v3) | 📄 [PDF](https://arxiv.org/pdf/2603.12662v3)

**Summary:** Objectively verifying the generative mechanism of consciousness is extremely difficult because of its subjective nature. As long as theories of consciousness focus solely on its generative mechanism, developing a theory remains challenging. We believe that broadening the theoretical scope and enhancing theoretical unification are necessary to establish a theory of consciousness. This study proposes seven questions that theories of consciousness should address: phenomena, self, causation, state, ...

---

### 27. Towards unified brain-to-text decoding across speech production and perception

**Authors:** Zhizhang Yuan, Yang Yang, Gaorui Zhang, et al.

**Published:** 2026-03-13

🔗 [Paper](http://arxiv.org/abs/2603.12628v1) | 📄 [PDF](https://arxiv.org/pdf/2603.12628v1)

**Summary:** Speech production and perception are the main ways humans communicate daily. Prior brain-to-text decoding studies have largely focused on a single modality and alphabetic languages. Here, we present a unified brain-to-sentence decoding framework for both speech production and perception in Mandarin Chinese. The framework exhibits strong generalization ability, enabling sentence-level decoding when trained only on single-character data and supporting characters and syllables unseen during trainin...

---

### 28. Formation of Artificial Neural Assemblies by Biologically Plausible Inhibition Mechanisms

**Authors:** Lucas Hoff, Gustavo Soroka, Matheus Guimarães, et al.

**Published:** 2026-03-12

🔗 [Paper](http://arxiv.org/abs/2603.12416v1) | 📄 [PDF](https://arxiv.org/pdf/2603.12416v1)

**Summary:** As proposed by Hebb's theory, neural assemblies are groups of excitatory neurons that fire synchronously and exhibit high synaptic density, representing external stimuli and supporting cognitive functions such as language and decision-making. Recently, a model called Assembly Calculus (AC) was proposed, enabling the formation of artificial neural assemblies through the $k$-winners-take-all selection process and Hebbian learning. Although the model is capable of forming assemblies according to He...

---

### 29. Neural network-based encoding in free-viewing fMRI with gaze-aware models

**Authors:** Dora Gozukara, Nasir Ahmad, Katja Seeliger, et al.

**Published:** 2026-03-12

🔗 [Paper](http://arxiv.org/abs/2603.11663v1) | 📄 [PDF](https://arxiv.org/pdf/2603.11663v1)

**Summary:** Representations learned by convolutional neural networks (CNNs) exhibit a remarkable resemblance to information processing patterns observed in the primate visual system on large neuroimaging datasets collected under diverse, naturalistic visual stimulation, but with instruction for participants to maintain central fixation. This viewing condition, however, diverges significantly from ecologically valid visual behaviour, suppresses activity in visually active regions, and imposes substantial cog...

---

### 30. Miniaturized microscopes to study neural dynamics in freely-behaving animals

**Authors:** Weijian Zong, Weijian Yang

**Published:** 2026-03-12

🔗 [Paper](http://arxiv.org/abs/2603.11435v1) | 📄 [PDF](https://arxiv.org/pdf/2603.11435v1)

**Summary:** Head-mounted miniaturized microscopes, commonly known as miniscopes, have undergone rapid development and seen widespread adoption over the past two decades, enabling the imaging of neural activity in freely-behaving animals such as rodents, songbirds, and non-human primates. These miniscopes facilitate numerous studies that are not feasible with head-fixed preparations. Recent advancements have enhanced their capabilities, allowing for faster imaging, larger fields of view, and deeper brain pen...

---

### 31. Human Navigation Behaviour and Brain Dynamics in Real-world Contexts

**Authors:** Pablo Fernandez Velasco, Antoine Coutrot, Hugo J. Spiers

**Published:** 2026-03-11

🔗 [Paper](http://arxiv.org/abs/2603.11347v1) | 📄 [PDF](https://arxiv.org/pdf/2603.11347v1)

**Summary:** The study of navigation behaviour and the associated brain dynamics have been a focus increasing research over the last decades. Coinciding with this has been an increased focus on a more ecological understanding of cognition. Here we review recent research seeking to provide a more naturalistic, ecological understanding of human navigation behaviour and brain dynamics. Research in this area falls into four categories: testing navigation in real-world environments, analysis of data collected fro...

---

### 32. The macaque IT cortex but not current artificial vision networks encode object position in perceptually aligned coordinates

**Authors:** Elizaveta Yakubovskaya, Hamidreza Ramezanpour, Matteo Dunnhofer, et al.

**Published:** 2026-03-11

🔗 [Paper](http://arxiv.org/abs/2603.11248v1) | 📄 [PDF](https://arxiv.org/pdf/2603.11248v1)

**Summary:** Efficient interaction with the visual world requires not only accurate object identification but also precise localization of objects in space. While spatial ("where") processing has traditionally been attributed to dorsal stream pathways, recent work has shown that object position can also be decoded from responses in ventral stream areas such as the inferior temporal (IT) cortex. However, because object position in these paradigms is tightly coupled to pixel-based location, it remains unclear ...

---

### 33. Uncovering statistical structure in large-scale neural activity with Restricted Boltzmann Machines

**Authors:** Nicolas Béreux, Giovanni Catania, Aurélien Decelle, et al.

**Published:** 2026-03-11

🔗 [Paper](http://arxiv.org/abs/2603.11032v1) | 📄 [PDF](https://arxiv.org/pdf/2603.11032v1)

**Summary:** Large-scale electrophysiological recordings now allow simultaneous monitoring of thousands of neurons across multiple brain regions, revealing structured variability in neural population activity. Understanding how these collective patterns emerge from microscopic neural interactions requires models that are scalable, predictive, and interpretable. Statistical physics provides principled frameworks to address this complexity, including maximum-entropy models that offer transparent descriptions o...

---

### 34. Cross-Species Transfer Learning for Electrophysiology-to-Transcriptomics Mapping in Cortical GABAergic Interneurons

**Authors:** Theo Schwider, Ramin Ramezani

**Published:** 2026-03-11

🔗 [Paper](http://arxiv.org/abs/2603.11000v1) | 📄 [PDF](https://arxiv.org/pdf/2603.11000v1)

**Summary:** Single-cell electrophysiological recordings provide a powerful window into neuronal functional diversity and offer an interpretable route for linking intrinsic physiology to transcriptomic identity. Here, we replicate and extend the electrophysiology-to-transcriptomics framework introduced by Gouwens et al. (2020) using publicly available Allen Institute Patch-seq datasets from both mouse and human cortex. We focus on GABAergic inhibitory interneurons to target a subclass structure (Lamp5, Pvalb...

---

### 35. Linear Readout of Neural Manifolds with Continuous Variables

**Authors:** Will Slatton, Chi-Ning Chou, SueYeon Chung

**Published:** 2026-03-11

🔗 [Paper](http://arxiv.org/abs/2603.10956v1) | 📄 [PDF](https://arxiv.org/pdf/2603.10956v1)

**Summary:** Brains and artificial neural networks compute with continuous variables such as object position or stimulus orientation. However, the complex variability in neural responses makes it difficult to link internal representational structure to task performance. We develop a statistical-mechanical theory of regression capacity that relates linear decoding efficiency of continuous variables to geometric properties of neural manifolds. Our theory handles complex neural variability and applies to real d...

---

### 36. JEDI: Jointly Embedded Inference of Neural Dynamics

**Authors:** Anirudh Jamkhandi, Ali Korojy, Olivier Codol, et al.

**Published:** 2026-03-11

🔗 [Paper](http://arxiv.org/abs/2603.10489v1) | 📄 [PDF](https://arxiv.org/pdf/2603.10489v1)

**Summary:** Animal brains flexibly and efficiently achieve many behavioral tasks with a single neural network. A core goal in modern neuroscience is to map the mechanisms of the brain's flexibility onto the dynamics underlying neural populations. However, identifying task-specific dynamical rules from limited, noisy, and high-dimensional experimental neural recordings remains a major challenge, as experimental data often provide only partial access to brain states and dynamical mechanisms. While recurrent n...

---

### 37. Curvature Blindness from Polarity Breaks and Orientation Channel Fragmentation in V1

**Authors:** Michael Menke

**Published:** 2026-03-10

🔗 [Paper](http://arxiv.org/abs/2603.09765v1) | 📄 [PDF](https://arxiv.org/pdf/2603.09765v1)

**Summary:** We present a mathematical model of the curvature blindness illusion in which sinusoids appear as angular zigzags when drawn with alternating contrast polarity against a gray background. The model identifies two complementary mechanisms, both operating in V1. First, polarity channel separation: simple cells are selective for contrast polarity, and lateral connections link only same polarity neurons; where the line switches from darker than background to lighter than background at each peak and tr...

---

### 38. Efficient and robust control with spikes that constrain free energy

**Authors:** André Urbano, Pablo Lanillos, Sander Keemink

**Published:** 2026-03-10

🔗 [Paper](http://arxiv.org/abs/2603.09729v1) | 📄 [PDF](https://arxiv.org/pdf/2603.09729v1)

**Summary:** Animal brains exhibit remarkable efficiency in perception and action, while being robust to both external and internal perturbations. The means by which brains accomplish this remains, for now, poorly understood, hindering our understanding of animal and human cognition, as well as our own implementation of efficient algorithms for control of dynamical systems.A potential candidate for a robust mechanism of state estimation and action computation is the free energy principle, but existing implem...

---

### 39. A Variational Latent Equilibrium for Learning in Neuronal Circuits

**Authors:** Simon Brandt, Paul Haider, Walter Senn, et al.

**Published:** 2026-03-10

🔗 [Paper](http://arxiv.org/abs/2603.09600v2) | 📄 [PDF](https://arxiv.org/pdf/2603.09600v2)

**Summary:** Brains remain unrivaled in their ability to recognize and generate complex spatiotemporal patterns. While AI is able to reproduce some of these capabilities, deep learning algorithms remain largely at odds with our current understanding of brain circuitry and dynamics. This is prominently the case for backpropagation through time (BPTT), the go-to algorithm for learning complex temporal dependencies. In this work we propose a general formalism to approximate BPTT in a controlled, biologically pl...

---

### 40. Compact Dynamical Mean-Field Theory of Oscillator Networks

**Authors:** Kanishka Reddy

**Published:** 2026-03-10

🔗 [Paper](http://arxiv.org/abs/2603.09402v1) | 📄 [PDF](https://arxiv.org/pdf/2603.09402v1)

**Summary:** We present a compact dynamical mean-field theory (DMFT) for large networks of coupled phase oscillators whose phases live on the circle $S^1$ and interact with both coherent mean-field coupling and quenched randomness. Starting from wrapped Langevin dynamics, we build a path-integral representation that keeps the $2π$-periodicity of the phases explicit. After averaging over the disorder in the thermodynamic limit, this construction reduces to a single-oscillator stochastic equation driven by a d...

---

### 41. Dreaming improves memorization in a Hopfield model with bounded synaptic strength

**Authors:** Enzo Marinari, Saverio Rossi, Francesco Zamponi

**Published:** 2026-03-10

🔗 [Paper](http://arxiv.org/abs/2603.09384v1) | 📄 [PDF](https://arxiv.org/pdf/2603.09384v1)

**Summary:** The Hopfield model provides a paradigmatic framework for associative memory. Its classical implementation, based on the Hebbian learning rule, suffers from catastrophic forgetting: when one attempts storing too many patterns, the network fails to retrieve any of them. Yet, the Hebbian rule does not take into account that synaptic strength is bounded. Introducing this biologically plausible modification, known as "clipping", eliminates catastrophic forgetting; the model is now able to retrieve th...

---

### 42. Sampling on Discrete Spaces with Temporal Point Processes

**Authors:** Cameron A. Stewart, Maneesh Sahani

**Published:** 2026-03-10

🔗 [Paper](http://arxiv.org/abs/2603.09089v1) | 📄 [PDF](https://arxiv.org/pdf/2603.09089v1)

**Summary:** Temporal point processes offer a powerful framework for sampling from discrete distributions, yet they remain underutilized in existing literature. We show how to construct, for any target multivariate count distribution with downward-closed support, a multivariate temporal point process whose event-count vector in a fixed-length sliding window converges in distribution to the target as time tends to infinity. Structured as a system of potentially coupled infinite-server queues with deterministi...

---

### 43. Diffusion of Neuromodulators for Temporal Credit Assignment

**Authors:** João Barretto-Bittar, Anna Levina, Emmanouil Giannakakis, et al.

**Published:** 2026-03-09

🔗 [Paper](http://arxiv.org/abs/2603.08949v1) | 📄 [PDF](https://arxiv.org/pdf/2603.08949v1)

**Summary:** Biological learning achieves temporal credit assignment despite sparse and imprecise feedback, often relying on neuromodulatory signals acting over space and time. Here, we introduce a learning mechanism in which error information diffuses locally through the network, similar to volume transmission of neuromodulators. This distributed modulation allows neurons to learn even in the absence of direct feedback, using the local concentration of the diffusing credit signal. Applied to recurrent spiki...

---

### 44. A Dynamical Systems and System Identification Framework for Phase Amplitude Coupling Analysis

**Authors:** Rajintha Gunawardena, Fei He

**Published:** 2026-03-09

🔗 [Paper](http://arxiv.org/abs/2603.08866v1) | 📄 [PDF](https://arxiv.org/pdf/2603.08866v1)

**Summary:** Phase-amplitude coupling (PAC), a form of cross-frequency interaction, has been implicated in various cognitive functions and, by extension, in neural communication and information integration. Accurately detecting and characterising PAC is essential for understanding its role in processes such as memory and attention. However, this remains a significant challenge. Most existing methods rely on variations in the temporal profile to detect PAC, but they often suffer from key limitations, most not...

---

### 45. Embodied intelligence solves the centipede's dilemma

**Authors:** Adam Dionne, Fabio Giardina, L. Mahadevan

**Published:** 2026-03-09

🔗 [Paper](http://arxiv.org/abs/2603.08409v2) | 📄 [PDF](https://arxiv.org/pdf/2603.08409v2)

**Summary:** Although commonly associated with limbless animals like snakes and fish, multi-legged organisms like centipedes also utilize undulatory locomotion. Whether these undulations are actively reinforced or resisted by the axial musculature remains an open question. We present a dynamical model of centipede locomotion that integrates leg-ground interactions, passive body mechanics, and active lateral musculature. By varying stepping rate, actuation, and body stiffness, we examine how locomotor strateg...

---

### 46. Task learning increases information redundancy of neural responses in macaque visual cortex

**Authors:** Shizhao Liu, Anton Pletenev, Ralf M. Haefner, et al.

**Published:** 2026-03-07

🔗 [Paper](http://arxiv.org/abs/2603.07369v1) | 📄 [PDF](https://arxiv.org/pdf/2603.07369v1)

**Summary:** How does the brain optimize sensory information for decision-making in new tasks? One hypothesis suggests learning reduces redundancy in neural representations to improve efficiency, while another, based on Bayesian inference, predicts learning increases redundancy by distributing information across neurons. We tested these hypotheses by tracking population responses in macaque cortical area V4 as monkeys learned visual discrimination tasks. We found strong support for the Bayesian predictions: ...

---

### 47. Neural Control and Learning of Simulated Hand Movements With an EMG-Based Closed-Loop Interface

**Authors:** Balint K. Hodossy, Dario Farina

**Published:** 2026-03-07

🔗 [Paper](http://arxiv.org/abs/2603.07364v1) | 📄 [PDF](https://arxiv.org/pdf/2603.07364v1)

**Summary:** The standard engineering approach when facing uncertainty is modelling. Mixing data from a well-calibrated model with real recordings has led to breakthroughs in many applications of AI, from computer vision to autonomous driving. This type of model-based data augmentation is now beginning to show promising results in biosignal processing as well. However, while these simulated data are necessary, they are not sufficient for virtual neurophysiological experiments. Simply generating neural signal...

---

### 48. Polarization-wave propagation as a biophysical mechanism of visual cognition

**Authors:** Hyun Myung Jang, Youngwoo Jang, Hyeon Han

**Published:** 2026-03-07

🔗 [Paper](http://arxiv.org/abs/2603.07275v1) | 📄 [PDF](https://arxiv.org/pdf/2603.07275v1)

**Summary:** Recent experimental studies indicate that visual cognition is accompanied by slowly propagating biophysical travelling waves in cortical tissue. Here we propose polarization waves as a coherent physical framework for visual cognition. We first compute the propagation of scalar potential fields generated by impressed ionic currents in the primary visual cortex using a telegraph-type model and extract the velocity of the moving potential ridge. By exploiting the linear convolution structure, we th...

---

### 49. A Miniature Brain Transformer: Thalamic Gating, Hippocampal Lateralization, Amygdaloid Salience, and Prefrontal Working Memory in Attention-Coupled Latent Memory

**Authors:** Hong Jeong

**Published:** 2026-03-07

🔗 [Paper](http://arxiv.org/abs/2603.07217v1) | 📄 [PDF](https://arxiv.org/pdf/2603.07217v1)

**Summary:** We present a miniature brain transformer architecture that extends the attention-coupled latent memory framework with four additional brain-region analogues: a thalamic relay, an amygdaloid salience module, a prefrontal working-memory (PFC) buffer, and a cerebellar fast-path, all coupled by inhibitory callosal cross-talk between lateralized hippocampal banks. We evaluate on a two-domain benchmark -- MQAR (Multi-Query Associative Recall; episodic domain) and modular arithmetic (+1 mod 10; rule-ba...

---

### 50. The DIME Architecture: A Unified Operational Algorithm for Neural Representation, Dynamics, Control and Integration

**Authors:** Ionel Cristian Vladu, Nicu Bizdoaca, Ionica Pirici, et al.

**Published:** 2026-03-07

🔗 [Paper](http://arxiv.org/abs/2603.12286v2) | 📄 [PDF](https://arxiv.org/pdf/2603.12286v2)

**Summary:** Modern neuroscience has accumulated extensive evidence on perception, memory, prediction, valuation, and consciousness, yet still lacks an explicit operational architecture capable of integrating these phenomena within a unified computational framework. Existing theories address specific aspects of neural function: predictive coding and active inference emphasize hierarchical inference and prediction error minimization; engram theories explain memory through distributed cell assemblies; neuromod...

---

## stat.ML

**50 papers**

### 1. Kolmogorov-Arnold causal generative models

**Authors:** Alejandro Almodóvar, Mar Elizo, Patricia A. Apellániz, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20184v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20184v1)

**Summary:** Causal generative models provide a principled framework for answering observational, interventional, and counterfactual queries from observational data. However, many deep causal models rely on highly expressive architectures with opaque mechanisms, limiting auditability in high-stakes domains. We propose KaCGM, a causal generative model for mixed-type tabular data where each structural equation is parameterized by a Kolmogorov--Arnold Network (KAN). This decomposition enables direct inspection ...

---

### 2. Beyond Single Tokens: Distilling Discrete Diffusion Models via Discrete MMD

**Authors:** Emiel Hoogeboom, David Ruhe, Jonathan Heek, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20155v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20155v1)

**Summary:** It is currently difficult to distill discrete diffusion models. In contrast, continuous diffusion literature has many distillation approaches methods that can reduce sampling steps to a handful.   Our method, Discrete Moment Matching Distillation (D-MMD), leverages ideas that have been highly successful in the continuous domain. Whereas previous discrete distillation methods collapse, D-MMD maintains high quality and diversity (given sufficient sampling steps). This is demonstrated on both text ...

---

### 3. The monotonicity of the Franz-Parisi potential is equivalent with Low-degree MMSE lower bounds

**Authors:** Konstantinos Tsirkas, Leda Wang, Ilias Zadik

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20070v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20070v1)

**Summary:** Over the last decades, two distinct approaches have been instrumental to our understanding of the computational complexity of statistical estimation. The statistical physics literature predicts algorithmic hardness through local stability and monotonicity properties of the Franz--Parisi (FP) potential \cite{franz1995recipes,franz1997phase}, while the mathematically rigorous literature characterizes hardness via the limitations of restricted algorithmic classes, most notably low-degree polynomial...

---

### 4. Graph-Informed Adversarial Modeling: Infimal Subadditivity of Interpolative Divergences

**Authors:** Panagiota Birmpa, Eric Joseph Hall

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.20025v1) | 📄 [PDF](https://arxiv.org/pdf/2603.20025v1)

**Summary:** We study adversarial learning when the target distribution factorizes according to a known Bayesian network. For interpolative divergences, including $(f,Γ)$-divergences, we prove a new infimal subadditivity principle showing that, under suitable conditions, a global variational discrepancy is controlled by an average of family-level discrepancies aligned with the graph. In an additive regime, this surrogate is exact. This provides a variational justification for replacing a graph-agnostic GAN w...

---

### 5. A Federated Many-to-One Hopfield model for associative Neural Networks

**Authors:** Andrea Alessandrelli, Fabrizio Durante, Andrea Ladiana, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19902v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19902v1)

**Summary:** Federated learning enables collaborative training without sharing raw data, but struggles under client heterogeneity and streaming distribution shifts, where drift and novel data can impair convergence and cause forgetting. We propose a federated associative-memory framework that learns shared archetypes in heterogeneous, continual settings, where client data are independent but not necessarily balanced. Each client encodes its experience as a low-rank Hebbian operator, sent to a central server ...

---

### 6. Deep Autocorrelation Modeling for Time-Series Forecasting: Progress and Prospects

**Authors:** Hao Wang, Licheng Pan, Qingsong Wen, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19899v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19899v1)

**Summary:** Autocorrelation is a defining characteristic of time-series data, where each observation is statistically dependent on its predecessors. In the context of deep time-series forecasting, autocorrelation arises in both the input history and the label sequences, presenting two central research challenges: (1) designing neural architectures that model autocorrelation in history sequences, and (2) devising learning objectives that model autocorrelation in label sequences. Recent studies have made stri...

---

### 7. Minimax Generalized Cross-Entropy

**Authors:** Kartheek Bondugula, Santiago Mazuelas, Aritz Pérez, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19874v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19874v1)

**Summary:** Loss functions play a central role in supervised classification. Cross-entropy (CE) is widely used, whereas the mean absolute error (MAE) loss can offer robustness but is difficult to optimize. Interpolating between the CE and MAE losses, generalized cross-entropy (GCE) has recently been introduced to provide a trade-off between optimization difficulty and robustness. Existing formulations of GCE result in a non-convex optimization over classification margins that is prone to underfitting, leadi...

---

### 8. Explainable cluster analysis: a bagging approach

**Authors:** Federico Maria Quetti, Elena Ballante, Silvia Figini, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19840v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19840v1)

**Summary:** A major limitation of clustering approaches is their lack of explainability: methods rarely provide insight into which features drive the grouping of similar observations. To address this limitation, we propose an ensemble-based clustering framework that integrates bagging and feature dropout to generate feature importance scores, in analogy with feature importance mechanisms in supervised random forests. By leveraging multiple bootstrap resampling schemes and aggregating the resulting partition...

---

### 9. Two-Time-Scale Learning Dynamics: A Population View of Neural Network Training

**Authors:** Giacomo Borghi, Hyesung Im, Lorenzo Pareschi

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19808v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19808v1)

**Summary:** Population-based learning paradigms, including evolutionary strategies, Population-Based Training (PBT), and recent model-merging methods, combine fast within-model optimisation with slower population-level adaptation. Despite their empirical success, a general mathematical description of the resulting collective training dynamics remains incomplete. We introduce a theoretical framework for neural network training based on two-time-scale population dynamics. We model a population of neural netwo...

---

### 10. Uncertainty Quantification Via the Posterior Predictive Variance

**Authors:** Sanjay Chaudhuri, Dean Dustin, Bertrand Clarke

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19804v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19804v1)

**Summary:** We use the law of total variance to generate multiple expansions for the posterior predictive variance. These expansions are sums of terms involving conditional expectations and conditional variances and provide a quantification of the sources of predictive uncertainty. Since the posterior predictive variance is fixed given the model, it represents a constant quantity that is conserved over these expansions. The terms in the expansions can be assessed in absolute or relative sense to understand ...

---

### 11. Scalable Learning of Multivariate Distributions via Coresets

**Authors:** Zeyu Ding, Katja Ickstadt, Nadja Klein, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19792v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19792v1)

**Summary:** Efficient and scalable non-parametric or semi-parametric regression analysis and density estimation are of crucial importance to the fields of statistics and machine learning. However, available methods are limited in their ability to handle large-scale data. We address this issue by developing a novel coreset construction for multivariate conditional transformation models (MCTMs) to enhance their scalability and training efficiency. To the best of our knowledge, these are the first coresets for...

---

### 12. Regularity of Solutions to Beckmann's Parametric Optimal Transport

**Authors:** Hanno Gottschalk, Tobias J. Riedlinger

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19755v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19755v1)

**Summary:** Beckmann's problem in optimal transport minimizes the total squared flux in a continuous transport problem from a source to a target distribution. In this article, the regularity theory for solutions to Beckmann's problem in optimal transport is developed utilizing an unconstrained Lagrangian formulation and solving the variational first order optimality conditions. It turns out that the Lagrangian multiplier that enforces Beckmann's divergence constraint fulfills a Poisson equation and the flux...

---

### 13. A two-step sequential approach for hyperparameter selection in finite context models

**Authors:** José Contente, Ana Martins, Armando J. Pinho, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19736v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19736v1)

**Summary:** Finite-context models (FCMs) are widely used for compressing symbolic sequences such as DNA, where predictive performance depends critically on the context length k and smoothing parameter α. In practice, these hyperparameters are typically selected through exhaustive search, which is computationally expensive and scales poorly with model complexity. This paper proposes a statistically grounded two-step sequential approach for efficient hyperparameter selection in FCMs. The key idea is to decomp...

---

### 14. Model Selection and Parameter Estimation of Multi-dimensional Gaussian Mixture Model

**Authors:** Xinyu Liu, Hai Zhang

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19657v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19657v1)

**Summary:** In this paper, we study the problem of learning multi-dimensional Gaussian Mixture Models (GMMs), with a specific focus on model order selection and efficient mixing distribution estimation. We first establish an information-theoretic lower bound on the critical sample complexity required for reliable model selection. More specifically, we show that distinguishing a $k$-component mixture from a simpler model necessitates a sample size scaling of $Ω(Δ^{-(4k-4)})$. We then propose a thresholding-b...

---

### 15. Heavy-Tailed and Long-Range Dependent Noise in Stochastic Approximation: A Finite-Time Analysis

**Authors:** Siddharth Chandak, Anuj Yadav, Ayfer Ozgur, et al.

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19648v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19648v1)

**Summary:** Stochastic approximation (SA) is a fundamental iterative framework with broad applications in reinforcement learning and optimization. Classical analyses typically rely on martingale difference or Markov noise with bounded second moments, but many practical settings, including finance and communications, frequently encounter heavy-tailed and long-range dependent (LRD) noise. In this work, we study SA for finding the root of a strongly monotone operator under these non-classical noise models. We ...

---

### 16. Alternating Diffusion for Proximal Sampling with Zeroth Order Queries

**Authors:** Hirohane Takagi, Atsushi Nitanda

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19633v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19633v1)

**Summary:** This work introduces a new approximate proximal sampler that operates solely with zeroth-order information of the potential function. Prior theoretical analyses have revealed that proximal sampling corresponds to alternating forward and backward iterations of the heat flow. The backward step was originally implemented by rejection sampling, whereas we directly simulate the dynamics. Unlike diffusion-based sampling methods that estimate scores via learned models or by invoking auxiliary samplers,...

---

### 17. On the role of memorization in learned priors for geophysical inverse problems

**Authors:** Ali Siahkoohi, Davide Sabeddu

**Published:** 2026-03-20

🔗 [Paper](http://arxiv.org/abs/2603.19629v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19629v1)

**Summary:** Learned priors based on deep generative models offer data-driven regularization for seismic inversion, but training them requires a dataset of representative subsurface models -- a resource that is inherently scarce in geoscience applications. Since the training objective of most generative models can be cast as maximum likelihood on a finite dataset, any such model risks converging to the empirical distribution -- effectively memorizing the training examples rather than learning the underlying ...

---

### 18. Near-Equivalent Q-learning Policies for Dynamic Treatment Regimes

**Authors:** Sophia Yazzourh, Erica E. M. Moodie

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.19440v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19440v1)

**Summary:** Precision medicine aims to tailor therapeutic decisions to individual patient characteristics. This objective is commonly formalized through dynamic treatment regimes, which use statistical and machine learning methods to derive sequential decision rules adapted to evolving clinical information. In most existing formulations, these approaches produce a single optimal treatment at each stage, leading to a unique decision sequence. However, in many clinical settings, several treatment options may ...

---

### 19. Subspace Projection Methods for Fast Spectral Embeddings of Evolving Graphs

**Authors:** Mohammad Eini, Abdullah Karaaslanli, Vassilis Kalantzis, et al.

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.19439v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19439v1)

**Summary:** Several graph data mining, signal processing, and machine learning downstream tasks rely on information related to the eigenvectors of the associated adjacency or Laplacian matrix. Classical eigendecomposition methods are powerful when the matrix remains static but cannot be applied to problems where the matrix entries are updated or the number of rows and columns increases frequently. Such scenarios occur routinely in graph analytics when the graph is changing dynamically and either edges and/o...

---

### 20. Pseudo-Labeling for Unsupervised Domain Adaptation with Kernel GLMs

**Authors:** Nathan Weill, Kaizheng Wang

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.19422v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19422v1)

**Summary:** We propose a principled framework for unsupervised domain adaptation under covariate shift in kernel Generalized Linear Models (GLMs), encompassing kernelized linear, logistic, and Poisson regression with ridge regularization. Our goal is to minimize prediction error in the target domain by leveraging labeled source data and unlabeled target data, despite differences in covariate distributions. We partition the labeled source data into two batches: one for training a family of candidate models, ...

---

### 21. The Exponentially Weighted Signature

**Authors:** Alexandre Bloch, Samuel N. Cohen, Terry Lyons, et al.

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.19198v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19198v1)

**Summary:** The signature is a canonical representation of a multidimensional path over an interval. However, it treats all historical information uniformly, offering no intrinsic mechanism for contextualising the relevance of the past. To address this, we introduce the Exponentially Weighted Signature (EWS), generalising the Exponentially Fading Memory (EFM) signature from diagonal to general bounded linear operators. These operators enable cross-channel coupling at the level of temporal weighting together...

---

### 22. PPI is the Difference Estimator: Recognizing the Survey Sampling Roots of Prediction-Powered Inference

**Authors:** Reagan Mozer

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.19160v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19160v1)

**Summary:** Prediction-powered inference (PPI) is a rapidly growing framework for combining machine learning predictions with a small set of gold-standard labels to conduct valid statistical inference. In this article, I argue that the core estimators underlying PPI are equivalent to well-established estimators from the survey sampling literature dating back to the 1970s. Specifically, the PPI estimator for a population mean is algebraically equivalent to the difference estimator of Cassel et al. (1976), an...

---

### 23. Numerical Considerations for the Construction of Karhunen-Loève Expansions

**Authors:** Cosmin Safta, Habib N. Najm

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.19108v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19108v1)

**Summary:** This report examines numerical aspects of constructing Karhunen-Loève expansions (KLEs) for second-order stochastic processes. The KLE relies on the spectral decomposition of the covariance operator via the Fredholm integral equation of the second kind, which is then discretized on a computational grid, leading to an eigendecomposition task. We derive the algebraic equivalence between this Fredholm-based eigensolution and the singular value decomposition of the weight-scaled sample matrix, yield...

---

### 24. Hardness of High-Dimensional Linear Classification

**Authors:** Alexander Munteanu, Simon Omlor, Jeff M. Phillips

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.19061v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19061v1)

**Summary:** We establish new exponential in dimension lower bounds for the Maximum Halfspace Discrepancy problem, which models linear classification. Both are fundamental problems in computational geometry and machine learning in their exact and approximate forms. However, only $O(n^d)$ and respectively $\tilde O(1/\varepsilon^d)$ upper bounds are known and complemented by polynomial lower bounds that do not support the exponential in dimension dependence. We close this gap up to polylogarithmic terms by re...

---

### 25. Adaptive Nonlinear Data Assimilation through P-Spline Triangular Measure Transport

**Authors:** Berent Å. S. Lunde, Maximilian Ramgraber

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.19058v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19058v1)

**Summary:** Non-Gaussian statistics are a challenge for data assimilation. Linear methods oversimplify the problem, yet fully nonlinear methods are often too expensive to use in practice. The best solution usually lies between these extremes. Triangular measure transport offers a flexible framework for nonlinear data assimilation. Its success, however, depends on how the map is parametrized. Too much flexibility leads to overfitting; too little misses important structure. To address this balance, we develop...

---

### 26. Fast and Interpretable Autoregressive Estimation with Neural Network Backpropagation

**Authors:** Anaísa Lucena, Ana Martins, Armando J. Pinho, et al.

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.19041v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19041v1)

**Summary:** Autoregressive (AR) models remain widely used in time series analysis due to their interpretability, but convencional parameter estimation methods can be computationally expensive and prone to convergence issues. This paper proposes a Neural Network (NN) formulation of AR estimation by embedding the autoregressive structure directly into a feedforward NN, enabling coefficient estimation through backpropagation while preserving interpretability. Simulation experiments on 125,000 synthetic AR(p) t...

---

### 27. Revisiting OmniAnomaly for Anomaly Detection: performance metrics and comparison with PCA-based models

**Authors:** Bruna Alves, Ana Martins, Armando J. Pinho, et al.

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.18985v1) | 📄 [PDF](https://arxiv.org/pdf/2603.18985v1)

**Summary:** Deep learning models have become the dominant approach for multivariate time series anomaly detection (MTSAD), often reporting substantial performance improvements over classical statistical methods. However, these gains are frequently evaluated under heterogeneous thresholding strategies and evaluation protocols, making fair comparisons difficult. This work revisits OmniAnomaly, a widely used stochastic recurrent model for MTSAD, and systematically compares it with a simple linear baseline base...

---

### 28. Maximum-Entropy Exploration with Future State-Action Visitation Measures

**Authors:** Adrien Bolland, Gaspard Lambrechts, Damien Ernst

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.18965v1) | 📄 [PDF](https://arxiv.org/pdf/2603.18965v1)

**Summary:** Maximum entropy reinforcement learning motivates agents to explore states and actions to maximize the entropy of some distribution, typically by providing additional intrinsic rewards proportional to that entropy function. In this paper, we study intrinsic rewards proportional to the entropy of the discounted distribution of state-action features visited during future time steps. This approach is motivated by two results. First, we show that the expected sum of these intrinsic rewards is a lower...

---

### 29. Unified Taxonomy for Multivariate Time Series Anomaly Detection using Deep Learning

**Authors:** Bruna Alves, Armando J. Pinho, Sónia Gouveia

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.18941v1) | 📄 [PDF](https://arxiv.org/pdf/2603.18941v1)

**Summary:** The topic of Multivariate Time Series Anomaly Detection (MTSAD) has grown rapidly over the past years, with a steady rise in publications and Deep Learning (DL) models becoming the dominant paradigm. To address the lack of systematization in the field, this study introduces a novel and unified taxonomy with eleven dimensions over three parts (Input, Output and Model) for the categorization of DL-based MTSAD methods. The dimensions were established in a two-fold approach. First, they derived from...

---

### 30. Kernel Single-Index Bandits: Estimation, Inference, and Learning

**Authors:** Sakshi Arya, Satarupa Bhattacharjee, Bharath K. Sriperumbudur

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.18938v1) | 📄 [PDF](https://arxiv.org/pdf/2603.18938v1)

**Summary:** We study contextual bandits with finitely many actions in which the reward of each arm follows a single-index model with an arm-specific index parameter and an unknown nonparametric link function. We consider a regime in which arms correspond to stable decision options and covariates evolve adaptively under the bandit policy. This setting creates significant statistical challenges: the sampling distribution depends on the allocation rule, observations are dependent over time, and inverse-propens...

---

### 31. A Model Ensemble-Based Post-Processing Framework for Fairness-Aware Prediction

**Authors:** Zhouting Zhao, Tin Lok James Ng

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.18838v1) | 📄 [PDF](https://arxiv.org/pdf/2603.18838v1)

**Summary:** Striking an optimal balance between predictive performance and fairness continues to be a fundamental challenge in machine learning. In this work, we propose a post-processing framework that facilitates fairness-aware prediction by leveraging model ensembling. Designed to operate independently of any specific model internals, our approach is widely applicable across various learning tasks, model architectures, and fairness definitions. Through extensive experiments spanning classification, regre...

---

### 32. SRRM: Improving Recursive Transport Surrogates in the Small-Discrepancy Regime

**Authors:** Yufei Zhang, Tao Wang, Jingyi Zhang

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.18781v1) | 📄 [PDF](https://arxiv.org/pdf/2603.18781v1)

**Summary:** Recursive partitioning methods provide computationally efficient surrogates for the Wasserstein distance, yet their statistical behavior and their resolution in the small-discrepancy regime remain insufficiently understood. We study Recursive Rank Matching (RRM) as a representative instance of this class under a population-anchored reference. In this setting, we establish consistency and an explicit convergence rate for the anchored empirical RRM under the quadratic cost. We then identify a domi...

---

### 33. CausalRM: Causal-Theoretic Reward Modeling for RLHF from Observational User Feedbacks

**Authors:** Hao Wang, Licheng Pan, Zhichao Chen, et al.

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.18736v1) | 📄 [PDF](https://arxiv.org/pdf/2603.18736v1)

**Summary:** Despite the success of reinforcement learning from human feedback (RLHF) in aligning language models, current reward modeling heavily relies on experimental feedback data collected from human annotators under controlled and costly conditions. In this work, we introduce observational reward modeling -- learning reward models with observational user feedback (e.g., clicks, copies, and upvotes) -- as a scalable and cost-effective alternative. We identify two fundamental challenges in this setting: ...

---

### 34. A mathematical framework for time-delay reservoir computing analysis

**Authors:** Anh-Tuan Clabaut, Jean Auriol, Islam Boussaada, et al.

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.18706v1) | 📄 [PDF](https://arxiv.org/pdf/2603.18706v1)

**Summary:** Reservoir computing is a well-established approach for processing data with a much lower complexity compared to traditional neural networks. Despite two decades of experimental progress, the core properties of reservoir computing (namely separation, robustness, and fading memory) still lack rigorous mathematical foundations. This paper addresses this gap by providing a control-theoretic framework for the analysis of time-delay-based reservoir computers. We introduce formal definitions of the sep...

---

### 35. A Theoretical Comparison of No-U-Turn Sampler Variants: Necessary and Su?cient Convergence Conditions and Mixing Time Analysis under Gaussian Targets

**Authors:** Samuel Gruffaz, Kyurae Kim, Fares Guehtar, et al.

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.18640v1) | 📄 [PDF](https://arxiv.org/pdf/2603.18640v1)

**Summary:** The No-U-Turn Sampler (NUTS) is the computational workhorse of modern Bayesian software libraries, yet its qualitative and quantitative convergence guarantees were established only recently. A significant gap remains in the theoretical comparison of its two main variants: NUTS-mul and NUTS-BPS, which use multinomial sampling and biased progressive sampling, respectively, for index selection. In this paper, we address this gap in three contributions. First, we derive the first necessary condition...

---

### 36. On the Peril of (Even a Little) Nonstationarity in Satisficing Regret Minimization

**Authors:** Yixuan Zhang, Ruihao Zhu, Qiaomin Xie

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.18514v1) | 📄 [PDF](https://arxiv.org/pdf/2603.18514v1)

**Summary:** Motivated by the principle of satisficing in decision-making, we study satisficing regret guarantees for nonstationary $K$-armed bandits. We show that in the general realizable, piecewise-stationary setting with $L$ stationary segments, the optimal regret is $Θ(L\log T)$ as long as $L\geq 2$. This stands in sharp contrast to the case of $L=1$ (i.e., the stationary setting), where a $T$-independent $Θ(1)$ satisficing regret is achievable under realizability. In other words, the optimal regret has...

---

### 37. Precise Performance of Linear Denoisers in the Proportional Regime

**Authors:** Reza Ghane, Danil Akhtiamov, Babak Hassibi

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.18483v1) | 📄 [PDF](https://arxiv.org/pdf/2603.18483v1)

**Summary:** In the present paper we study the performance of linear denoisers for noisy data of the form $\mathbf{x} + \mathbf{z}$, where $\mathbf{x} \in \mathbb{R}^d$ is the desired data with zero mean and unknown covariance $\mathbfΣ$, and $\mathbf{z} \sim \mathcal{N}(0, \mathbfΣ_{\mathbf{z}})$ is additive noise. Since the covariance $\mathbfΣ$ is not known, the standard Wiener filter cannot be employed for denoising. Instead we assume we are given samples $\mathbf{x}_1,\dots,\mathbf{x}_n \in \mathbb{R}^d...

---

### 38. The Truncation Blind Spot: How Decoding Strategies Systematically Exclude Human-Like Token Choices

**Authors:** Esteban Garces Arias, Nurzhan Sapargali, Christian Heumann, et al.

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.18482v1) | 📄 [PDF](https://arxiv.org/pdf/2603.18482v1)

**Summary:** Standard decoding strategies for text generation, including top-k, nucleus sampling, and contrastive search, select tokens based on likelihood, restricting selection to high-probability regions. Human language production operates differently: tokens are chosen for communicative appropriateness rather than statistical frequency. This mismatch creates a truncation blind spot: contextually appropriate but statistically rare tokens remain accessible to humans yet unreachable by likelihood-based deco...

---

### 39. Statistical Testing Framework for Clustering Pipelines by Selective Inference

**Authors:** Yugo Miyata, Tomohiro Shiraishi, Shunichi Nishino, et al.

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.18413v1) | 📄 [PDF](https://arxiv.org/pdf/2603.18413v1)

**Summary:** A data analysis pipeline is a structured sequence of steps that transforms raw data into meaningful insights by integrating multiple analysis algorithms.In many practical applications, analytical findings are obtained only after data pass through several data-dependent procedures within such pipelines.In this study, we address the problem of quantifying the statistical reliability of results produced by data analysis pipelines.As a proof of concept, we focus on clustering pipelines that identify...

---

### 40. Multi-Domain Causal Empirical Bayes Under Linear Mixing

**Authors:** Bohan Wu, Julius von Kügelgen, David M. Blei

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.18404v1) | 📄 [PDF](https://arxiv.org/pdf/2603.18404v1)

**Summary:** Causal representation learning (CRL) aims to learn low-dimensional causal latent variables from high-dimensional observations. While identifiability has been extensively studied for CRL, estimation has been less explored. In this paper, we explore the use of empirical Bayes (EB) to estimate causal representations. In particular, we consider the problem of learning from data from multiple domains, where differences between domains are modeled by interventions in a shared underlying causal model. ...

---

### 41. Computational and Statistical Hardness of Calibration Distance

**Authors:** Mingda Qiao

**Published:** 2026-03-19

🔗 [Paper](http://arxiv.org/abs/2603.18391v1) | 📄 [PDF](https://arxiv.org/pdf/2603.18391v1)

**Summary:** The distance from calibration, introduced by Błasiok, Gopalan, Hu, and Nakkiran (STOC 2023), has recently emerged as a central measure of miscalibration for probabilistic predictors. We study the fundamental problems of computing and estimating this quantity, given either an exact description of the data distribution or only sample access to it.   We give an efficient algorithm that exactly computes the calibration distance when the distribution has a uniform marginal and noiseless labels, which...

---

### 42. Learning to Reason with Curriculum I: Provable Benefits of Autocurriculum

**Authors:** Nived Rajaraman, Audrey Huang, Miro Dudik, et al.

**Published:** 2026-03-18

🔗 [Paper](http://arxiv.org/abs/2603.18325v1) | 📄 [PDF](https://arxiv.org/pdf/2603.18325v1)

**Summary:** Chain-of-thought reasoning, where language models expend additional computation by producing thinking tokens prior to final responses, has driven significant advances in model capabilities. However, training these reasoning models is extremely costly in terms of both data and compute, as it involves collecting long traces of reasoning behavior from humans or synthetic generators and further post-training the model via reinforcement learning. Are these costs fundamental, or can they be reduced th...

---

### 43. Computation-Utility-Privacy Tradeoffs in Bayesian Estimation

**Authors:** Sitan Chen, Jingqiu Ding, Mahbod Majid, et al.

**Published:** 2026-03-18

🔗 [Paper](http://arxiv.org/abs/2603.18254v1) | 📄 [PDF](https://arxiv.org/pdf/2603.18254v1)

**Summary:** Bayesian methods lie at the heart of modern data science and provide a powerful scaffolding for estimation in data-constrained settings and principled quantification and propagation of uncertainty. Yet in many real-world use cases where these methods are deployed, there is a natural need to preserve the privacy of the individuals whose data is being scrutinized. While a number of works have attempted to approach the problem of differentially private Bayesian estimation through either reasoning a...

---

### 44. FalconBC: Flow matching for Amortized inference of Latent-CONditioned physiologic Boundary Conditions

**Authors:** Chloe H. Choi, Alison L. Marsden, Daniele E. Schiavazzi

**Published:** 2026-03-18

🔗 [Paper](http://arxiv.org/abs/2603.19331v1) | 📄 [PDF](https://arxiv.org/pdf/2603.19331v1)

**Summary:** Boundary condition tuning is a fundamental step in patient-specific cardiovascular modeling. Despite an increase in offline training cost, recent methods in data-driven variational inference can efficiently estimate the joint posterior distribution of boundary conditions, with amortization of training efforts over clinical targets. However, even the most modern approaches fall short in two important scenarios: open-loop models with known mean flow and assumed waveform shapes, and anatomies affec...

---

### 45. A Hybrid Conditional Diffusion-DeepONet Framework for High-Fidelity Stress Prediction in Hyperelastic Materials

**Authors:** Purna Vindhya Kota, Meer Mehran Rashid, Somdatta Goswami, et al.

**Published:** 2026-03-18

🔗 [Paper](http://arxiv.org/abs/2603.18225v1) | 📄 [PDF](https://arxiv.org/pdf/2603.18225v1)

**Summary:** Predicting stress fields in hyperelastic materials with complex microstructures remains challenging for traditional deep learning surrogates, which struggle to capture both sharp stress concentrations and the wide dynamic range of stress magnitudes. Convolutional architectures such as UNet tend to oversmooth high-frequency gradients, while neural operators like DeepONet exhibit spectral bias and underpredict localized extremes. Diffusion models can recover fine-scale structure but often introduc...

---

### 46. Starting Off on the Wrong Foot: Pitfalls in Data Preparation

**Authors:** Jiayi Guo, Panyi Dong, Zhiyu Quan

**Published:** 2026-03-18

🔗 [Paper](http://arxiv.org/abs/2603.18190v1) | 📄 [PDF](https://arxiv.org/pdf/2603.18190v1)

**Summary:** When working with real-world insurance data, practitioners often encounter challenges during the data preparation stage that can undermine the statistical validity and reliability of downstream modeling. This study illustrates that conventional data preparation procedures such as random train-test partitioning, often yield unreliable and unstable results when confronted with highly imbalanced insurance loss data. To mitigate these limitations, we propose a novel data preparation framework levera...

---

### 47. ResNets of All Shapes and Sizes: Convergence of Training Dynamics in the Large-scale Limit

**Authors:** Louis-Pierre Chaintron, Lénaïc Chizat, Javier Maass

**Published:** 2026-03-18

🔗 [Paper](http://arxiv.org/abs/2603.18168v1) | 📄 [PDF](https://arxiv.org/pdf/2603.18168v1)

**Summary:** We establish convergence of the training dynamics of residual neural networks (ResNets) to their joint infinite depth L, hidden width M, and embedding dimension D limit. Specifically, we consider ResNets with two-layer perceptron blocks in the maximal local feature update (MLU) regime and prove that, after a bounded number of training steps, the error between the ResNet and its large-scale limit is O(1/L + sqrt(D/(L M)) + 1/sqrt(D)). This error rate is empirically tight when measured in embeddin...

---

### 48. Pretrained Multilingual Transformers Reveal Quantitative Distance Between Human Languages

**Authors:** Yue Zhao, Jiatao Gu, Paloma Jeretič, et al.

**Published:** 2026-03-18

🔗 [Paper](http://arxiv.org/abs/2603.17912v1) | 📄 [PDF](https://arxiv.org/pdf/2603.17912v1)

**Summary:** Understanding the distance between human languages is central to linguistics, anthropology, and tracing human evolutionary history. Yet, while linguistics has long provided rich qualitative accounts of cross-linguistic variation, a unified and scalable quantitative approach to measuring language distance remains lacking. In this paper, we introduce a method that leverages pretrained multilingual language models as systematic instruments for linguistic measurement. Specifically, we show that the ...

---

### 49. A Noise Sensitivity Exponent Controls Large Statistical-to-Computational Gaps in Single- and Multi-Index Models

**Authors:** Leonardo Defilippis, Florent Krzakala, Bruno Loureiro, et al.

**Published:** 2026-03-18

🔗 [Paper](http://arxiv.org/abs/2603.17896v1) | 📄 [PDF](https://arxiv.org/pdf/2603.17896v1)

**Summary:** Understanding when learning is statistically possible yet computationally hard is a central challenge in high-dimensional statistics. In this work, we investigate this question in the context of single- and multi-index models, classes of functions widely studied as benchmarks to probe the ability of machine learning methods to discover features in high-dimensional data. Our main contribution is to show that a Noise Sensitivity Exponent (NSE) - a simple quantity determined by the activation funct...

---

### 50. BoundAD: Boundary-Aware Negative Generation for Time Series Anomaly Detection

**Authors:** Xiancheng Wang, Lin Wang, Zhibo Zhang, et al.

**Published:** 2026-03-18

🔗 [Paper](http://arxiv.org/abs/2603.18111v1) | 📄 [PDF](https://arxiv.org/pdf/2603.18111v1)

**Summary:** Contrastive learning methods for time series anomaly detection (TSAD) heavily depend on the quality of negative sample construction. However, existing strategies based on random perturbations or pseudo-anomaly injection often struggle to simultaneously preserve temporal semantic consistency and provide effective decision-boundary supervision. Most existing methods rely on prior anomaly injection, while overlooking the potential of generating hard negatives near the data manifold boundary directl...

---

