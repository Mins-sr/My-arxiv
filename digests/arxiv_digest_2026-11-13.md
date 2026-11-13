# arXiv Daily Digest - 2026-11-13

Total papers: 350

---

## cs.AI

**50 papers**

### 1. AgentSSL: Can MLE Agents Leverage Unlabeled Data?

**Authors:** Ethan Lin, Akanksha Sarkar, Ziang Liu, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17323v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17323v1)

**Summary:** Applying machine learning systems to new domains introduces bottlenecks in both labeled data acquisition and manual pipeline engineering. While recent MLE agents show promise in automating pipeline design, they have been studied almost exclusively in fully supervised settings, leaving them untested in realistic regimes where labeled data is scarce but unlabeled data is abundant. In this work, we introduce Agentic Semi-Supervised Learning (AgentSSL), framing SSL as a program search problem and st...

---

### 2. CoReMem: Cost-Internalizing Memory for Successive Coding Tasks with Prospective Valuation

**Authors:** Peiwen Li, Harshit Verma, Sophia Zhou, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17316v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17316v1)

**Summary:** Coding agents tackle successive tasks on an evolving repository, carrying forward edits and writing memory before the next task is known. Selecting memory for unknown next tasks requires balancing future usefulness against the costs of writing and reading it. The actor must also decide when acting on available memory saves effort as the task unfolds. We introduce Coding-Repository Memory (CoReMem), a cost-internalizing framework that guides memory design and actor adaptation through measured mem...

---

### 3. Sketching Language Models for Context Attribution

**Authors:** Christopher Liaw, Aranyak Mehta, Grigoris Velegkas, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17313v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17313v1)

**Summary:** Context attribution asks how removing parts of a prompt changes a language model's output. We study leave-one-out (LOO) attribution for a prompt of $n$ tokens and a fixed measurement function. Computing all LOO values directly requires $n$ model evaluations. Under a stability assumption, our algorithm estimates all LOO values to error proportional to $\varepsilon$ with constant probability using $O(\sqrt{\log(1/\varepsilon)}/\varepsilon)$ evaluation calls. To complement our upper bound, we prove...

---

### 4. Classical Energies Learn to Reason 1,000x Faster than Looped Models

**Authors:** Benjamin Hoover, Hugh Blayney, James C. R. Whittington

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17309v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17309v1)

**Summary:** Looped models have emerged as a prominent paradigm for reasoning, with successes on simple reasoning puzzles such as Sudoku-Extreme and Maze-Unique. However, these models can be unstable, slow to train, and use many parameters and FLOPs to solve simple puzzles. Descent on an energy not only mitigates these issues but also offers advantages: built-in early stopping, compute that adapts to problem difficulty, fast training without differentiating through a solver, and interpretable weights that le...

---

### 5. Consistent Video-to-Video Translation via Explicit Correspondences

**Authors:** Gaurav Parmar, Zhengqi Li, Richard Zhang, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17298v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17298v1)

**Summary:** Interactive video-to-video applications require real-time generation while maintaining long-range temporal consistency. However, recent methods achieve speed by restricting attention to a fixed-length causal window. This limits long-range consistency whenever relevant history falls outside the context window. To address this limitation, we introduce vid2vid-long, a correspondence-based approach grounded in a simple observation. Video-to-video translation provides an explicit cross-frame referenc...

---

### 6. Goal Encoding in LLMs

**Authors:** Arnab Sen Sharma, Eric Todd, Sheridan Feucht, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17297v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17297v1)

**Summary:** We investigate whether and how LLMs encode goals: internal neural representations that precede and guide action, and that are flexible enough to be realized through many different execution paths. We construct a coding setting with multiple sub-tasks that allows us to evaluate goal-seeking behavior and the selection of sub-goals. In this setting, we localize an encoding of the next sub-goal in the outputs of a sparse set of attention heads. The same heads can be used to decode the LM's future ac...

---

### 7. Metal Sandbox: Isolated Execution and Command Scheduling for GPU Coding Agents on Apple Silicon

**Authors:** Haozhe Wang, Lina Chen, Fanqi Wan, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17294v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17294v1)

**Summary:** On-device inference requires kernels that make effective use of local accelerators. Efficient training and evaluation of models that generate Apple Metal kernels benefit from native macOS tools and concurrent agent sessions. These sessions alternate between model requests, development commands, and GPU execution, leaving GPU capacity idle for much of a rollout. We present Metal Sandbox, infrastructure that combines restricted per-instance file access, native command execution, and command-level ...

---

### 8. Synthesis Smuggling: Maliciously Hiding Inferred Personal Attributes in LLM Outputs

**Authors:** Gautam Galada, Supreeth Shastri, Sagnik Ray Choudhury

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17280v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17280v1)

**Summary:** We propose Synthesis Smuggling, a novel threat model in which an adversarial LLM infers sensitive information about a user from routine assistance-seeking interactions and steganographically encodes that into innocuous-looking model-generated content. The user may then unknowingly transmit that information by sharing the generated artifact, say as an email, social-media post, or message, through ordinary communication channels. An adversary monitoring these channels can discover this information...

---

### 9. LiveGeo: Benchmarking Geographic Agents in Continuously Evolving Worlds

**Authors:** Pengcheng Zhou, Xuanyu Liu, Yanchen Yin, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17267v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17267v1)

**Summary:** We introduce GeoWorld, a controllable and continuously evolving geographic environment platform for LLM agents, and LiveGeo, a benchmark for evaluating reliable decision-making in real-world geographic environments using GeoWorld. Unlike existing evaluations that largely reason and plan over fixed geographic states, GeoWorld is grounded in real-world geographic structure and allows external world states to evolve along their own temporal processes while preserving verifiable state histories. Liv...

---

### 10. Ballad: Bandit-Based LLM Routing for Automated Heuristic Discovery

**Authors:** Samidha Verma, Ankit Anand, Sayan Ranu

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17241v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17241v1)

**Summary:** Modern automated heuristic discovery (AHD) systems increasingly rival hand-crafted heuristics by leveraging Large Language Models (LLMs) to iteratively mutate and refine solutions. A natural assumption is that more powerful and more expensive models consistently yield better heuristics. We challenge this empirically: across multiple NP-hard combinatorial optimization problems, we find no consistent advantage for larger, costlier models. This raises a deeper question: given a pool of LLMs spannin...

---

### 11. When Both Sides Adapt: The Challenges of Evaluating Interactive LLM Systems

**Authors:** Hannah Li

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17239v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17239v1)

**Summary:** In interactive systems where users engage with LLMs, users are adaptive and, after observing LLM responses, can change their prompting strategy, as well as the type and difficulty of subsequent tasks. Thus model responses can influence the set of prompts on which the model is subsequently evaluated. We study the implications of this user adaptivity and prompt endogeneity for the evaluation of LLMs. We define two classes of estimands for comparing models: the common-distribution effect, which com...

---

### 12. Al-Ghasali: A Computational Framework for Simulating Islamic Jurisprudential Rulings via Finite State Automata and Large Language Models

**Authors:** Elnaserledinellah Mahmoud Abdelwahab

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17235v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17235v1)

**Summary:** This paper presents Al Ghasali, a computational framework designed to formalize and simulate Islamic jurisprudential (Fiqh) rulings. Building upon recent set theoretic formalizations of al sabr wa al Taqsim that extract minimal operational rules as simple Horn clause logical programs, this work proves that the semantics of closed Fiqh chapters collapse completely to deterministic Finite State Automata (FSA). We establish a formal computational hierarchy, demonstrating that restricting formalizat...

---

### 13. Scalable Conversational Assessment: Chat-Based Exams with a Two-Agent LLM Pipeline

**Authors:** Geoffrey Challen, Craig Zilles

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17220v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17220v1)

**Summary:** Oral exams are compelling because (1) students can be asked to provide their reasoning for an answer and (2) their interactive nature permits follow-up questions to resolve ambiguous answers. But oral exams scale poorly. In this paper, we present scalable conversational assessment, an LLM-based system that conducts interactive text-based conversations with students to assess their ability to make and support an argument. We use a two-agent architecture to separate concerns and reduce the likelih...

---

### 14. Introducing Feedback Delays to Non-Delayed Adversarial MDPs: Optimal $\sqrt S$ and $\sqrt K$ Dependencies in Tabular and Linear AMDPs

**Authors:** Aarush Kulkarni, Khang Nguyen, William Chang, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17214v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17214v1)

**Summary:** We study regret minimization in episodic Adversarial Markov Decision Processes (AMDPs) with unknown transitions and bandit feedback. In tabular AMDPs with $S$ states, $A$ actions, and horizon $H$, the best known $K$-episode regret is $\tilde O(HS\sqrt{AK})$, whose $\sqrt S$ gap to the $Ω(H\sqrt{SAK})$ lower bound has long remained open. In linear AMDPs with $d$-dimensional features, after a five-year line of improvements starting from $K^{14/15}$, computationally efficient algorithms without a s...

---

### 15. MALNISI-Infused Graph Construction and Weighted Contrastive Loss based GAT for Unsupervised Representation Learning in HSI

**Authors:** Soumi Sarkar, Subhadip Boral, Sarbani Palit, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17199v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17199v1)

**Summary:** Hyperspectral images (HSI) possess discriminating spectral characteristics with respect to land utilization due to high-dimensional information. Recently, unsupervised representation learning using graph neural networks has unveiled these utilization-specific complex spectral relations. This article has three main contributions. First, it proposes an index, the Mean Absolute Local Neighborhood Inverse Spectral Index (MALNISI), which measures the similarity between two pixels based on their neigh...

---

### 16. Cortex-FL: Agent-Mediated Collaboration for Federated Learning

**Authors:** Rui Sun, Jinfeng Peng, Zehua Cheng, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17186v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17186v1)

**Summary:** Federated learning (FL) enables independent data owners to train models collaboratively without centralizing raw data. However, identifying collaborators, preparing training tasks, and coordinating execution and incentives hinder its practical adoption by organizations without specialized expertise. We present Cortex-FL, an agent-native FL system that enables users to express learning objectives in natural language and delegate the collaboration required to train a model. Agents translate these ...

---

### 17. Actor, Judge, or Teacher? Understanding Decision Models in Long-Horizon Agents

**Authors:** Haochen Liu, Qianhao Zhu, Zixuan Wang, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17167v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17167v1)

**Summary:** Decision models answer a question with a typed output, such as a choice among options with a probability for each, so one model can choose an agent's actions, evaluate actions already taken, or score every action to teach a policy with reinforcement learning. Prior work has studied them mainly as actors, judging their usefulness by how well they act. We ask whether a decision model that acts poorly can still teach well. We compare three decision models and three general LLMs as actors and judges...

---

### 18. Cited but Unused: Parametric Provenance in Retrieval-Augmented Generation

**Authors:** Tanzeel Abbas, Tehseen Zia, David Windridge

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17161v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17161v1)

**Summary:** Retrieval-augmented generation systems attach citations to attribute claims to their sources. These citations frequently misstate provenance, and standard verification cannot detect this. We measure provenance by counterfactual value substitution: a fact in the retrieved passages is replaced with a false variant and the model re-queried. We find that across five sizes of one model family and a second comparator family, 1.2% to 15.7% of citable claims derive from parametric memory rather than the...

---

### 19. Parameter-Efficient Conciseness Adaptation: Differentiable Length Control for Concise Clinical Reasoning in Smaller Language Models

**Authors:** Tanzeel Abbas, Ahmad Kamran Malik, Nafees Qamar, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17128v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17128v1)

**Summary:** Smaller language models (SLMs) make it feasible to deploy clinical natural language processing where large proprietary models are too costly, and parameter-efficient fine-tuning allows them to be specialised on commodity hardware. One obstacle persists after training: on medical tasks these models answer at far greater length than the clinical question requires. In clinical decision support and point-of-care use, where time is short, such verbosity is hard to act on even when the underlying reas...

---

### 20. CapLite: Prompt-Injection Defense for Small Language Model Agents without Model-Written Security Artifacts

**Authors:** Zimo Xu, Wenzhuo Liu, Hideki Nakayama

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17115v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17115v1)

**Summary:** Enforcement defenses against prompt injection, such as CaMeL, Progent, IPIGuard and DRIFT, ask the agent's own model to write a security artifact (a program, a privilege policy, a dependency graph or a constraint list) that code then enforces. We ask whether small language model (SLM) agents can be trusted to write these artifacts. Across 15 open-weight models, 13 of them between 1.7B and 12B parameters, they cannot: the policies, graphs and constraints that the agent's model writes admit attack...

---

### 21. Designing Institutions for Autonomous AI

**Authors:** Petter Törnberg

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17114v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17114v1)

**Summary:** As autonomous AI agents increasingly interact in persistent populations, their collective capabilities and alignment depend not only on individual models, but also on the institutions governing their interactions. Yet AI research has largely focused on individual agents. In this Perspective, we argue that institutional design must become a distinct focus of AI research. Drawing on institutional political economy, social epistemology and organizational theory, we develop seven principles for desi...

---

### 22. SALA: Semantically Aligned Latent Actions Enable Dual-Axis Scaling of Embodied Foundation Models

**Authors:** Jiachun Jin, Zetong Zhou, Haonan Wang, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17110v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17110v1)

**Summary:** Embodied foundation models hinge on diverse robot interaction data, which are costly to collect. Egocentric human videos offer a complementary source of experience, and latent action models (LAMs) provide a popular means of leveraging these videos for policy supervision. Compared with world-action models (WAMs), LAMs can offer greater training efficiency and potentially lower inference costs by avoiding explicit pixel prediction during policy learning and execution. However, most existing LAMs l...

---

### 23. Predicting Ethanol Drinking Status from Nonhuman Primate Liver Histology: A Proof of Concept for Parameter-efficient Fine-tuning in Few-Shot Vision-Language Modeling

**Authors:** Amirmohammad Mohammadi, Rupak Khadka, Kathleen A. Grant, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17105v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17105v1)

**Summary:** Combining vision-language models (VLMs) with parameter-efficient fine-tuning (PEFT) offers a promising approach to few-shot whole-slide image (WSI) classification in computational pathology. This study evaluates this approach for predicting ethanol drinking status from nonhuman primate liver histology. Adapters are evaluated against non-PEFT configurations on a subset of the Monkey Alcohol Tissue Research Resource (MATRR). All evaluated PEFT configurations achieve higher mean balanced accuracy t...

---

### 24. A Compact xDAWN-Guided Spatio-Temporal Network with Filter-Bank Convolution for P300 Detection

**Authors:** Mohammad Mahdi Habibi Bina, Mohammad Reza Daliri

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17101v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17101v1)

**Summary:** P300-based brain-computer interfaces (BCIs) enable communication by decoding stimulus-evoked EEG responses into character selections without requiring voluntary motor output. Reliable P300 detection remains difficult because of low response amplitude and signal-to-noise ratio, while practical spellers require accurate character selection with few stimulus repetitions and low computational cost. We propose a compact deep learning architecture that combines xDAWN spatial filtering for event-relate...

---

### 25. Speed-to-Power Dominates Energy Costs for AI Data Centers: Technoeconomic Analysis of Powering AI in the Continental United States

**Authors:** Alex C. Newkirk, Daniel L. Gerber, Erica R. H. Fuchs, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17098v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17098v1)

**Summary:** The rapid growth of artificial intelligence is driving demand for new data centers at large scale and on short deployment timelines. To power them, firms connect to the commercial grid or contract generation directly, but interconnection and gas-turbine delays now incentivize on-site generation. We compare grid-connected and off-grid data center energy infrastructure (AC- and DC-coupled solar-plus-storage, islanded natural gas, and grid interconnection) across the continental U.S. Using an open-...

---

### 26. Reasoning Supervision and Capability Retention in LoRA Domain Adaptation

**Authors:** Saleh Ashkboos, Dhruv Desai, Lavinia Ghita

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17072v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17072v1)

**Summary:** Fine-tuning foundation models on financial data has a wide range of applications, including identifying event types from news, monitoring risk and compliance language, and answering questions over filings and earnings calls. In this setting, the main challenge is to improve task performance without degrading the generalization capabilities of the model. In this paper, we present an extensive set of ablations for fine-tuning Qwen3-8B with low-rank adaptation (LoRA). We compare three training regi...

---

### 27. Discovering Effective Agent Memory Designs through Program Evolution

**Authors:** Xinheng Ding, Seyyed Saeid Cheshmi, Ziyang Zhang, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17068v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17068v1)

**Summary:** Program evolution provides a promising approach to discover agent memory designs and study the choices underlying their effectiveness. We introduce MAPE, a framework that evolves whole memory programs from minimal seeds through a standardized lifecycle interface and an iterative diagnosis-proposal loop. Experiments on LoCoMo and LongMemEval yield an absolute accuracy gain of up to 12% over manually designed baselines at 35% of the serving cost, with further evaluations supporting transfer across...

---

### 28. Auditing AI peer reviewers: a benchmark on real scientific papers

**Authors:** Íñigo Zubeldia, Boris Bolliet, Francisco Villaescusa-Navarro, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17052v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17052v1)

**Summary:** LLM-based peer review is now used at production scale, but its evaluation remains limited. We introduce a benchmark that injects objective, localisable errors of four types (general issues, mathematics, numerics, citations) at three severity levels into real papers and measures each reviewer's detection rate by error type and severity, together with its false-positive rate on clean copies. We also present Skepthical, a multi-agent reviewer that verifies citation-backed claims by retrieving the c...

---

### 29. AURA 2.0: From User-Driven Responses to Model-Initiated Conversations in Streaming Video

**Authors:** Shuhan Li, Huankang Guan, Xintong Guo, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17048v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17048v1)

**Summary:** Most AI assistants respond only when prompted, remaining silent even when events in the video stream offer meaningful opportunities for conversation. To move beyond purely user-driven interaction, we present AURA 2.0, a streaming video large language model that introduces three core upgrades to AURA. The key advance is Model-Initiated Conversation (MIC), which enables the model to identify topics worth discussing in the evolving visual stream and initiate conversations at appropriate moments wit...

---

### 30. From Delegation to Coordination: Learning Efficient Multi-Agent Deep Research

**Authors:** Yuyang Wu, Yang Liu, Zequn Xie, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17041v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17041v1)

**Summary:** Multi-agent deep-research systems use delegation to parallelize search and keep long tool traces out of the main agent's context. Yet delegation helps only when task allocation and subtask execution are coordinated: the main agent must issue useful subtasks, while subagents must return reliable evidence. Existing training either optimizes only the main agent or broadcasts the same team advantage to all agents, which can reward misleading subagent reports and penalize useful ones. We introduce LE...

---

### 31. Your Vision Foundation Model Is Secretly an EEG Foundation Model

**Authors:** Guoan Wang, Feng Liu

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17031v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17031v1)

**Summary:** Electroencephalography (EEG) foundation models are pretrained on thousands of hours of recordings, yet their frozen features transfer poorly to downstream tasks, and this transfer does not consistently improve with larger models or more pretraining data. We show that a vision foundation model that has never seen EEG is a stronger frozen EEG encoder than these specialized models, once the signals are rendered as images that a vision transformer can read. Our method, SeeEEG, keeps the vision backb...

---

### 32. AI for Biologists: The Knowledge Boundaries of Foundation Models in the Age of Agentic Systems

**Authors:** Tian Cai, Andrew Kleist, Jaimin Patel, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17015v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17015v1)

**Summary:** Artificial intelligence (AI) is changing how biological research is done. Biological foundation models trained on millions of nucleotides, protein, and single-cell measurements predict protein structures, mutation effects, and cellular responses to genetic perturbations. Agentic systems, AI assistants built on large language models, can run multistep analyses from plain-language requests and increasingly call foundation models as tools. Yet it is often unclear when these models' outputs can be t...

---

### 33. Skill Adapter: Personalized Modification and Online Routing of General-Purpose Skills

**Authors:** Qijia Zhuang, Yanyi Gou, Wenbin Ma, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17007v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17007v1)

**Summary:** Large language model (LLM) agents use external skills to reuse task procedures and experience with tools. General-purpose skills describe shared execution procedures, while specific tool choices, operating practices, and output requirements vary across users. In long-horizon tasks, subgoals, available inputs, and environmental states change as execution progresses. Agents must select currently applicable skills from an expanding skill pool and prepare candidates for subsequent steps.   We propos...

---

### 34. AnalogLayoutWorld: An Open Benchmark for Agentic Analog Layout Design

**Authors:**  NovaSilicon Team

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16991v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16991v1)

**Summary:** Coding agents have demonstrated strong capabilities in software development, yet their ability to tackle long-horizon engineering tasks governed by physical constraints remains less understood. We study this question through analog circuit layout, which demands domain knowledge, geometric reasoning, and iterative interaction with design and verification tools. We introduce \textbf{AnalogLayoutWorld}, an open-source agent benchmark with 40 expert-reviewed tasks for end-to-end layout generation fr...

---

### 35. Primer: An AI Framework for Instructor-Centered Educational Simulation Creation

**Authors:** Ethan Mollick, Lilach Mollick, Ben Przystanski, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16986v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16986v1)

**Summary:** Educational simulations are a well-established pedagogical technique that gives learners opportunities to apply knowledge, respond to challenges, and reflect on their performance. High-quality simulations, however, are difficult to build, requiring instructor input, scenario design, character development, scaffolding, technical implementation, and repeated revision. This paper presents Primer, an open-source, LLM-agnostic AI-supported system that helps educators create adaptive educational simul...

---

### 36. ElasticDino: Dense Semantic Features Using Elastic Deformations

**Authors:** Ulysse Mizrahi, Sean Zaretzky, Dov Danon, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16984v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16984v1)

**Summary:** Vision transformers (ViTs) serve as the backbone for countless vision tasks, including dense prediction tasks, such as segmentation and depth estimation, even though the quadratic complexity of self-attention severely limits feature resolution and induces spatial artifacts. In this work, we introduce ElasticDino, a lightweight adapter which produces high-resolution feature maps, adhering to the fine details of the input image. As a key insight, we observe the consistency of artifacts across chan...

---

### 37. Compiling Known Rules into Compact Neural Agents: Weight-Space Programming on Unseen Games

**Authors:** Jens Lehmann

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16981v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16981v1)

**Summary:** Weight-space programming (WSP) uses language models to construct neural network weights without training. We test whether known game mechanics can be compiled into compact agents that generalise to held-out levels, renderings and start states within a game family. Writers receive simulator source with held-out level data removed for 20 privately authored, unpublished ARC-AGI-3-style game families. With a fixed 57k-parameter recurrent architecture, the strongest writer reaches 56% held-out-level ...

---

### 38. The Value of Thinking: Learning When to Reason in Hybrid Decision Models

**Authors:** Zhengxu Yu, Ke Xu, Meng Fang, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16961v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16961v1)

**Summary:** Existing adaptive-reasoning methods shorten the explicit reasoning a model writes, or skip it by switching modes; either way the answer is still written out token by token. \emph{Rather than deciding how much to think}, we explore a different paradigm, \emph{zero-or-$T$ thinking}: a single model either answers from the implicit thinking inside one forward pass, generating no token, or performs full autoregressive reasoning at a cost of $T$ tokens when that is worth paying. We realise it in a \em...

---

### 39. Lara Mini Base: Language Diversity as a Resource, Not a Trade-off

**Authors:**  Translated, Maria Pia Adinolfi, Isabelle Andrieu, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16956v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16956v1)

**Summary:** General-purpose language models are trained mostly on English: over open models we review, at most, non-English pretraining data makes up only a 12% share. Models built for European languages give them far more, but score well below general-purpose models of the same size. A common concern is that, in small models, languages compete for capacity. We present Lara Mini base, a model trained from scratch on 6T tokens in English and 44 other languages, which together cover all 24 official languages ...

---

### 40. S1-Evo: Experience-Guided Evidence Competition Attacks on Typed System-1 Decision Models

**Authors:** Kaixiang Wang, Junjie Li, Zhaojiacheng Zhou, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16937v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16937v1)

**Summary:** Typed System-1 (S1) decision models are increasingly deployed in LLM agents for routing, moderation, and authorization to cut inference cost, yet untrusted context can still manipulate typed outputs and alter execution branches. Unlike autoregressive System-2 (S2) models, S1 interfaces score dynamic rules and options without token-by-token decoding, mismatching attacks targeting text continuation or explicit override commands. We propose S1-Evo, a self-evolving framework tailored to S1's contrac...

---

### 41. Universal Infectious Disease Forecasting with Mantis 2

**Authors:** Carson Dudley, Reiden Magdaleno, Yutong Bi, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16935v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16935v1)

**Summary:** Public health agencies need to anticipate how outbreaks will unfold, when they will peak, and how long demand on health services will remain elevated. We previously developed a foundation model, Mantis, which was trained entirely on simulated outbreaks---enabling us to generate the diversity and scale of training data needed to support forecasting across diseases. However, our previous work left unresolved when simulation improves predictions and how it should complement observational data.   He...

---

### 42. Kezek: Splitting Mono Two-Person Conversations into Per-Speaker Tracks for Full-Duplex Dialogue Data

**Authors:** Bagzhan Karl, Alizhan Karl

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16933v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16933v1)

**Summary:** Full-duplex spoken dialogue models learn turn-taking, overlaps and backchannels from conversations recorded with one channel per speaker, but most available conversational audio is a single mono mix. We present Kezek, a model that turns a mono recording of exactly two people into one track per person with the original length and timing; overlaps and short replies ("yeah", "mm-hm") stay on the track of the person who said them. Kezek decides who speaks when and who is who once for the whole recor...

---

### 43. SPADE: Soft Prompts for Ai-text DEtection

**Authors:** Alex Jiang, Didier Schwab, Chuyuan Li

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16929v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16929v1)

**Summary:** The easy access to Large Language Models (LLMs) has made AI-generated texts on the web increasingly ubiquitous, making AI-text detection a crucial task. Prompts greatly influence the generation process, but existing detectors focus solely on the generated texts --- supervised methods learn from labeled texts only, and zero-shot methods rely on the text's probability distributions --- ignoring the underlying generation process, which limits their robustness in open-world scenarios. We introduce S...

---

### 44. STEALTH: Steganographic Text Encoding Agnostic to Low-Level Tensor Hardware

**Authors:** William Fleshman

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16928v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16928v1)

**Summary:** Provably secure linguistic steganography hides a message inside text sampled from a language model, so that without the key, a stegotext is computationally indistinguishable from an honest model sample. Nearly every such scheme assumes the receiver can recompute the sender's token probabilities exactly bit for bit. We show this assumption is fragile: across three model families, bit-exact schemes decode almost none of our messages once the receiver's floating-point precision, quantization, or GP...

---

### 45. CADET: Construction of PCB Routing Instances with Executable Demonstrations

**Authors:** Hyungseok Song, Won-Seok Choi, Seohui Bae, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16913v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16913v1)

**Summary:** Printed circuit board (PCB) routing is the stage of physical layout that finds paths connecting the placed pads of each net. Public datasets in this domain are few, and most contain only the final states of routed boards, not demonstrations of the electronic design automation (EDA) engine actions that produce them. To close this gap, we propose CADET (Constructing executAble Demonstrations for Engine-grounded Training), which jointly generates synthetic boards and demonstrations built from EDA e...

---

### 46. Look It Up: Multi-bit LLM Watermarking via Codebook Search

**Authors:** Jarosław Janas, Paweł Morawiecki, Josef Pieprzyk

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16890v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16890v1)

**Summary:** Attributing short LLM-generated texts to a specific source remains challenging for existing multi-bit watermarking methods, which often require long generations or costly decoding to recover payloads reliably. We propose a codebook-based watermarking scheme that maps an $n$-bit payload to a longer $u$-bit codeword and embeds it during generation through token-level logit biasing. During extraction, the received bit sequence is matched to the nearest codeword in a precomputed secret codebook usin...

---

### 47. LLM-Assisted Verification in Dafny

**Authors:** Wieger Wesselink, Kees Huizing, Huub van de Wetering

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16886v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16886v1)

**Summary:** Formal verification of complex algorithms requires expertise in program specification, invariant construction, mathematical proof, and the management of automated theorem provers. Although large language models (LLMs) can generate program code and proof fragments, reliably developing complete machine-checked verifications remains challenging: it requires an iterative process of constructing and validating specifications and invariants, building proofs, diagnosing solver failures, and optimizing ...

---

### 48. Protein Language Models Fail To Capture Contact Predictions Under Invariant Relabeling

**Authors:** Paarth Batra, Aryan Keluskar

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16881v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16881v1)

**Summary:** Protein language models (pLMs) produce highly accurate contact maps from single-sequence inputs. People often take this accuracy as proof that these models implicitly learn invariant coevolutionary statistics, extracting the same signals as classical alignment-based methods like Potts. In this work, we introduce a diagnostic framework around a global bijective relabeling of the amino-acid alphabet. This transformation permutes residue letters while leaving all alignment-level information, column...

---

### 49. Context Graph: Explainable Multi-Agent Decision Chains in AI-RAN

**Authors:** Xijun Wang, Zhaoyang Liu, Xiang Chen, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16879v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16879v1)

**Summary:** AI-RAN distributes network control across multiple autonomous agents, namely xApps and rApps operating over shared radio resources. When an alert or degradation appears, operators currently lack a structured way to trace which decision caused it, what context triggered that decision, and how other agents interacted. Existing explainability tools focus on single-model feature attribution or linear event logging, neither of which captures cross-agent decision chains. We propose the Context Graph, ...

---

### 50. DPA: Decentralized Primal Averaging with Quasi-Global Momentum for Highly Heterogeneous Data

**Authors:** Diyako Ghaderyan, Stefan Werner

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16871v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16871v1)

**Summary:** Decentralized training of deep learning models keeps training data local and supports on-device learning over networks. In realistic scenarios, heterogeneity across agents' local data poses an optimization challenge and can severely degrade test accuracy, especially on sparse communication graphs. Building on recent advances in centralized primal averaging, we propose Decentralized Primal Averaging (DPA), a decentralized learning algorithm that combines primal averaging with a local quasi-global...

---

## cs.CL

**50 papers**

### 1. ArchSpace: Recording, Reviewing, and Referencing LLM Architecture Research

**Authors:** Jie Wang, Tong Zhu, JiaHao Kuang, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17332v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17332v1)

**Summary:** Model architecture shapes the scaling behavior, training efficiency, and inference cost of LLMs, making it a central focus of both industry and academia. In industry, teams such as those behind DeepSeek, Qwen, and Kimi routinely introduce architectural innovations, yet public reports rarely document which ideas succeeded, which were abandoned, and why. In academia, limited compute and inconsistent baselines often restrict evaluations to small-scale, single-point comparisons, making it difficult ...

---

### 2. Learning When Diffusion Language Models Should Regenerate

**Authors:** Minhae Oh, Jeonghye Kim, Jinwoo Koo, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17320v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17320v1)

**Summary:** Remasking allows diffusion language models to revisit generated text, but effective correction requires knowing when and what to revise. Our diagnosis on Sudoku reveals two gaps. Hidden states contain error information that token confidence does not reliably expose, and remasking an isolated error usually reproduces it when the surrounding context remains fixed. These findings motivate DiVR , a verifier that predicts whether a partially generated sequence will reach a correct answer. Trained on ...

---

### 3. CoReMem: Cost-Internalizing Memory for Successive Coding Tasks with Prospective Valuation

**Authors:** Peiwen Li, Harshit Verma, Sophia Zhou, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17316v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17316v1)

**Summary:** Coding agents tackle successive tasks on an evolving repository, carrying forward edits and writing memory before the next task is known. Selecting memory for unknown next tasks requires balancing future usefulness against the costs of writing and reading it. The actor must also decide when acting on available memory saves effort as the task unfolds. We introduce Coding-Repository Memory (CoReMem), a cost-internalizing framework that guides memory design and actor adaptation through measured mem...

---

### 4. Linking Rapid Learning to Compositional Structure in Neural Networks: Evidence from Additive Analogies in Meta-Learned Parameter Spaces

**Authors:** Abigail L. Tenenbaum, R. Thomas McCoy

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17314v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17314v1)

**Summary:** Humans can learn rapidly from limited experience, while neural networks typically require extensive training. In this work, we investigate what properties of a neural network can enable it to learn rapidly. We study neural networks that have been optimized via meta-learning, a technique that exposes a network to many related functions to facilitate its subsequent learning of similar functions. Prior work has shown that these meta-learned networks can learn new functions rapidly, but how they do ...

---

### 5. Goal Encoding in LLMs

**Authors:** Arnab Sen Sharma, Eric Todd, Sheridan Feucht, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17297v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17297v1)

**Summary:** We investigate whether and how LLMs encode goals: internal neural representations that precede and guide action, and that are flexible enough to be realized through many different execution paths. We construct a coding setting with multiple sub-tasks that allows us to evaluate goal-seeking behavior and the selection of sub-goals. In this setting, we localize an encoding of the next sub-goal in the outputs of a sparse set of attention heads. The same heads can be used to decode the LM's future ac...

---

### 6. Metal Sandbox: Isolated Execution and Command Scheduling for GPU Coding Agents on Apple Silicon

**Authors:** Haozhe Wang, Lina Chen, Fanqi Wan, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17294v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17294v1)

**Summary:** On-device inference requires kernels that make effective use of local accelerators. Efficient training and evaluation of models that generate Apple Metal kernels benefit from native macOS tools and concurrent agent sessions. These sessions alternate between model requests, development commands, and GPU execution, leaving GPU capacity idle for much of a rollout. We present Metal Sandbox, infrastructure that combines restricted per-instance file access, native command execution, and command-level ...

---

### 7. Negative-Only Policy Optimization for One-Sided Verifiable Rewards

**Authors:** Jiacheng Xu, Shuo He, Fuxiang Zhang, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17287v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17287v1)

**Summary:** Reinforcement learning with verifiable rewards (RLVR) typically relies on a verifier that can reliably judge whether sampled solutions are correct. However, in many realistic settings, complete verification is generally unavailable, while cheap checks can only falsify failures. We formalize this regime as one-sided verifiability (OSV): verified negatives are reliable counterexamples, but verified positives are merely non-falsified candidates and may contain many false positives. This asymmetry m...

---

### 8. Synthesis Smuggling: Maliciously Hiding Inferred Personal Attributes in LLM Outputs

**Authors:** Gautam Galada, Supreeth Shastri, Sagnik Ray Choudhury

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17280v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17280v1)

**Summary:** We propose Synthesis Smuggling, a novel threat model in which an adversarial LLM infers sensitive information about a user from routine assistance-seeking interactions and steganographically encodes that into innocuous-looking model-generated content. The user may then unknowingly transmit that information by sharing the generated artifact, say as an email, social-media post, or message, through ordinary communication channels. An adversary monitoring these channels can discover this information...

---

### 9. Maximizing Capacity Utilization of LoRA Adapters for Mitigating the Learning-Forgetting Trade-off

**Authors:** Tomohiro Sawada, Kartik Goyal

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17191v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17191v1)

**Summary:** Low-Rank Adaptation (LoRA) often underperforms full fine-tuning, especially in heterogeneous and continual-learning settings in which substantial forgetting occurs. In general, it suffers from an undesirable learning-forgetting trade-off across diverse fine-tuning settings. We identify a potential contributor: LoRA adapters, especially high-rank ones, frequently fail to realize the available capacity afforded by the configured rank. Specifically, we find that standard LoRA updates have effective...

---

### 10. Parsed, Plausible, Wrong: Output Format Controls Silent Errors in Small-Model Semantic Parsing

**Authors:** Umar Ahmed, Maxim Dunaev, Mohammad Nour Al Awad, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17169v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17169v1)

**Summary:** A small fine-tuned parser that emits a well-formed but wrong tree fails silently: nothing downstream can tell. We ask whether the output format, a free design choice, controls how often this happens. On the PIZZA ordering benchmark we fine-tune two sub-billion models (Qwen3.5-0.8B and LFM2.5-350M) with LoRA on six lossless encodings of the same target tree, from 44.3 down to 10.9 tokens per order, including two matched-length pairs that vary surface form at fixed length. Across 300 runs (5 train...

---

### 11. Actor, Judge, or Teacher? Understanding Decision Models in Long-Horizon Agents

**Authors:** Haochen Liu, Qianhao Zhu, Zixuan Wang, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17167v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17167v1)

**Summary:** Decision models answer a question with a typed output, such as a choice among options with a probability for each, so one model can choose an agent's actions, evaluate actions already taken, or score every action to teach a policy with reinforcement learning. Prior work has studied them mainly as actors, judging their usefulness by how well they act. We ask whether a decision model that acts poorly can still teach well. We compare three decision models and three general LLMs as actors and judges...

---

### 12. Parameter-Efficient Conciseness Adaptation: Differentiable Length Control for Concise Clinical Reasoning in Smaller Language Models

**Authors:** Tanzeel Abbas, Ahmad Kamran Malik, Nafees Qamar, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17128v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17128v1)

**Summary:** Smaller language models (SLMs) make it feasible to deploy clinical natural language processing where large proprietary models are too costly, and parameter-efficient fine-tuning allows them to be specialised on commodity hardware. One obstacle persists after training: on medical tasks these models answer at far greater length than the clinical question requires. In clinical decision support and point-of-care use, where time is short, such verbosity is hard to act on even when the underlying reas...

---

### 13. CapLite: Prompt-Injection Defense for Small Language Model Agents without Model-Written Security Artifacts

**Authors:** Zimo Xu, Wenzhuo Liu, Hideki Nakayama

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17115v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17115v1)

**Summary:** Enforcement defenses against prompt injection, such as CaMeL, Progent, IPIGuard and DRIFT, ask the agent's own model to write a security artifact (a program, a privilege policy, a dependency graph or a constraint list) that code then enforces. We ask whether small language model (SLM) agents can be trusted to write these artifacts. Across 15 open-weight models, 13 of them between 1.7B and 12B parameters, they cannot: the policies, graphs and constraints that the agent's model writes admit attack...

---

### 14. LazyWeights: Decode-on-Demand Edge LLMs

**Authors:** Arnab Sanyal, Gourav Datta, Sandeep P. Chinchali

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17108v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17108v1)

**Summary:** Memory decides which LLMs an edge device runs, and how fast: capacity on a $4$ GB Jetson Nano, bandwidth on an $8$ GB Jetson Orin Nano Super. Deployed formats (GPTQ, AWQ, $\texttt{llama.cpp}$'s K- and I-quants) spend equal bits on every integer code of a matrix, although the codes are far from uniform. $\texttt{LazyWeights}$ keeps these formats but tunes GPTQ so the codes compress, Huffman-codes them losslessly in interleaved lanes, and decodes them on demand in a small unit between DRAM and L2,...

---

### 15. Disentangling Spurious Correlations: How IRM Handles Diverse Shortcuts in Text Classification

**Authors:** Paul Grunenwald, Benoît Crabbé, Guillaume Wisniewski, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17107v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17107v1)

**Summary:** In NLP, models trained via Empirical Risk Minimization (ERM) often exploit spurious correlations, such as dialectal markers, at the expense of robust linguistic features, thereby degrading their out-of-distribution (OOD) generalization. Invariant Risk Minimization (IRM) aims to suppress such shortcuts by identifying predictive relationships that remain stable across environments, but its practical utility for NLP remains debated. We use a causality-driven framework to evaluate IRM under three sh...

---

### 16. Optimal Single-History Tokenization Disambiguation for Provably Secure Linguistic Steganography

**Authors:** Feng Jiang

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17091v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17091v1)

**Summary:** Provably secure linguistic steganography assumes that the receiver recovers the sender's tokens, but a text channel delivers only text, and ambiguous tokenizations break extraction. Existing fixes change the distribution, synchronize whole pools of tokens at a capacity that collapses with large vocabularies, or track several token histories. We prove that if extraction is exact and error-free across full-support language models, a single-history receiver is confined to a prefix-free candidate se...

---

### 17. Reasoning Supervision and Capability Retention in LoRA Domain Adaptation

**Authors:** Saleh Ashkboos, Dhruv Desai, Lavinia Ghita

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17072v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17072v1)

**Summary:** Fine-tuning foundation models on financial data has a wide range of applications, including identifying event types from news, monitoring risk and compliance language, and answering questions over filings and earnings calls. In this setting, the main challenge is to improve task performance without degrading the generalization capabilities of the model. In this paper, we present an extensive set of ablations for fine-tuning Qwen3-8B with low-rank adaptation (LoRA). We compare three training regi...

---

### 18. Discovering Effective Agent Memory Designs through Program Evolution

**Authors:** Xinheng Ding, Seyyed Saeid Cheshmi, Ziyang Zhang, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17068v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17068v1)

**Summary:** Program evolution provides a promising approach to discover agent memory designs and study the choices underlying their effectiveness. We introduce MAPE, a framework that evolves whole memory programs from minimal seeds through a standardized lifecycle interface and an iterative diagnosis-proposal loop. Experiments on LoCoMo and LongMemEval yield an absolute accuracy gain of up to 12% over manually designed baselines at 35% of the serving cost, with further evaluations supporting transfer across...

---

### 19. Evaluating Pretrained Language Semantics for Structured EHR Prediction Tasks

**Authors:** Ashvin Gupta, Brendan Delaney, Alessandra Russo

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17053v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17053v1)

**Summary:** Structured Electronic Health Records (EHR) models typically treat each clinical concept as a dataset-specific token, discarding the natural-language semantics associated with the event. As a result, relationships between concepts must largely be learned from EHR co-occurrence, without directly exploiting any prior semantic knowledge. We investigate how pretrained causal language models can be adapted for longitudinal EHR prediction by developing tEHR. Here, we represent events with their natural...

---

### 20. Auditing AI peer reviewers: a benchmark on real scientific papers

**Authors:** Íñigo Zubeldia, Boris Bolliet, Francisco Villaescusa-Navarro, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17052v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17052v1)

**Summary:** LLM-based peer review is now used at production scale, but its evaluation remains limited. We introduce a benchmark that injects objective, localisable errors of four types (general issues, mathematics, numerics, citations) at three severity levels into real papers and measures each reviewer's detection rate by error type and severity, together with its false-positive rate on clean copies. We also present Skepthical, a multi-agent reviewer that verifies citation-backed claims by retrieving the c...

---

### 21. Prevalence Bounds for Edited Watermarked Text: Power Envelopes and Calibration Sensitivity

**Authors:** Kuancheng Ye

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17035v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17035v1)

**Summary:** Watermark detectors decide whether one document came from a watermarked language model. Auditors often need a different number: the share of a corpus that did. We study this share for Gumbel-max and green-list (KGW) watermarks when every document may have been edited by an unknown amount. Without restrictions on the edits, the upper end of the identified set is 1. Combining a known least-favourable next-token distribution with a sequential coupling, we derive a power envelope indexed by three bu...

---

### 22. Similar but Not Redundant: Embedding-Gated Refinement for High-Granularity Topic Models

**Authors:** Daniel Denley, Robert L. Nicol, Mike J. Chantler

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17030v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17030v1)

**Summary:** High-granularity topic modelling extracts hundreds of niche topics from a corpus, yet this regime is rarely studied and is more commonly framed as a failure mode: "over-clustering," in which coherent themes fragment into redundant subtopics. We argue that this framing conflates genuine redundancy with topics that are semantically similar but meaningfully distinct, and that the central challenge in high-granularity modelling is separating the two. Recent post-hoc refinement methods address topic ...

---

### 23. Morphological Simplification in Alzheimer's Disease: Computational Analysis and Identification From Connected Speech

**Authors:** Mohamed Zakaria Kurdi

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16968v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16968v1)

**Summary:** Purpose: Morphology is often regarded as relatively spared in Alzheimer's disease (AD) and is rarely modeled in connected speech. This study asked which morphological features distinguish speakers with AD from healthy controls, how well morphology classifies AD compared with other linguistic levels and BERT-based models, and whether the signal exceeds transcript length and vocabulary. Method: Fifty-five automatic measures in eight families, seven of them new and theory-motivated, were computed f...

---

### 24. Lara Mini Base: Language Diversity as a Resource, Not a Trade-off

**Authors:**  Translated, Maria Pia Adinolfi, Isabelle Andrieu, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16956v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16956v1)

**Summary:** General-purpose language models are trained mostly on English: over open models we review, at most, non-English pretraining data makes up only a 12% share. Models built for European languages give them far more, but score well below general-purpose models of the same size. A common concern is that, in small models, languages compete for capacity. We present Lara Mini base, a model trained from scratch on 6T tokens in English and 44 other languages, which together cover all 24 official languages ...

---

### 25. SPADE: Soft Prompts for Ai-text DEtection

**Authors:** Alex Jiang, Didier Schwab, Chuyuan Li

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16929v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16929v1)

**Summary:** The easy access to Large Language Models (LLMs) has made AI-generated texts on the web increasingly ubiquitous, making AI-text detection a crucial task. Prompts greatly influence the generation process, but existing detectors focus solely on the generated texts --- supervised methods learn from labeled texts only, and zero-shot methods rely on the text's probability distributions --- ignoring the underlying generation process, which limits their robustness in open-world scenarios. We introduce S...

---

### 26. Beyond Word Error Rate: A Failure Taxonomy of Streaming Dictation ASR

**Authors:** Harras Mansoor, Muhammad Wisal, Hassan Bhatti, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16919v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16919v1)

**Summary:** Speech recognition (ASR) systems are usually compared by word error rate (WER) on recorded files, after punctuation, capital letters and number format are removed. In dictation, the audio is streamed live and the text goes into the user's message as written, so what matters is which mistakes the user has to fix. The test set, streamed to eleven ASR systems, comprises 106 scripted English dictations from one speaker (read in a quiet room, with a fan on, and whispered), 20 clips in each of eleven ...

---

### 27. Human or Synthetic? What a Fixed Budget Buys for Post-Training

**Authors:** Shourik Banerjee, Ethan Mendes, Mohit Raghavendra, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16895v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16895v1)

**Summary:** Post-training of large language models typically combines supervised fine-tuning (SFT) with preference-based fine-tuning such as Direct Preference Optimization (DPO). Human-annotated and synthetically generated preference data differ substantially in per-sample cost, but prior work typically holds sample count fixed when comparing the two. In this work, we explicitly study the interplay between cost and performance by comparing the effect of post-training with human and synthetic preference data...

---

### 28. Look It Up: Multi-bit LLM Watermarking via Codebook Search

**Authors:** Jarosław Janas, Paweł Morawiecki, Josef Pieprzyk

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16890v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16890v1)

**Summary:** Attributing short LLM-generated texts to a specific source remains challenging for existing multi-bit watermarking methods, which often require long generations or costly decoding to recover payloads reliably. We propose a codebook-based watermarking scheme that maps an $n$-bit payload to a longer $u$-bit codeword and embeds it during generation through token-level logit biasing. During extraction, the received bit sequence is matched to the nearest codeword in a precomputed secret codebook usin...

---

### 29. Pretraining Data Statistics Shape the Phases of Learning Entity Comparison in Language Models

**Authors:** Yik Siu Chan, Jing Huang, Yanai Elazar, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16882v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16882v1)

**Summary:** How does data shape language model (LM) behavior throughout pretraining? We investigate this question through a case study on entity comparison, e.g., Between France and Brazil, which country is larger?, across nine comparison tasks spanning five entity types. We begin with controlled experiments in which we train small LMs (163M parameters) on mixtures of natural text from pretraining corpora and synthetic task data. Our analysis identifies three distinct phases of learning: (1) an early phase ...

---

### 30. Shortcuts or Memorisation? Revisiting Data Corruption in Natural Language Understanding with Large Language Models

**Authors:** Aarne Talman, Stergios Chatzikyriakidis

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16843v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16843v1)

**Summary:** Pre-trained encoders fine-tuned on natural language inference (NLI) and other language understanding tasks keep much of their accuracy after the input is perturbed, e.g. by removing all nouns or shuffling the words. Does the same hold for large language models (LLMs), and if so, is it because they have seen the benchmarks during pre-training? In this paper we revisit these perturbation experiments with eight LLMs alongside fine-tuned encoders on GLUE and the three rounds of ANLI. Regardless of m...

---

### 31. Outcome-Mass Alignment: Controlling Length-Dependent Trajectory Influence in Multi-Turn LLM Agent Reinforcement Learning

**Authors:** Dawei Zhang, Yubin Huangfu, Jessica Fan, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16816v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16816v1)

**Summary:** To keep long interaction contexts tractable, stepwise group-relative training for multi-turn LLM agents materializes each source trajectory into multiple response rows and valid tokens. This expansion creates an outer-accounting problem distinct from within-trajectory credit assignment: row-based outcome statistics can count one episode outcome multiple times, while token-level reduction can assign unequal aggregate objective mass across trajectories. We term these effects outcome-statistics mul...

---

### 32. Detection Is Not Early Warning: Evaluating Token-Level Alarms on Language Model Failures

**Authors:** Marco De Negri, Luca Sartori, Lorenzo Baggi, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16803v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16803v1)

**Summary:** Many failures of language models begin at a specific token, the onset. A monitor that reads the model during generation can classify the finished response, detect the failure once it is under way, or warn before it begins, and only a warning leaves time to stop or steer the generation. Monitors are usually evaluated with response-level metrics such as AUROC, which ignore when the monitor fires. We introduce PREWARN, an evaluation protocol for any failure with an annotated onset. It calibrates ea...

---

### 33. Towards Green Text Generation: Memory-Based Speculative Decoding

**Authors:** Antal van den Bosch

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16714v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16714v1)

**Summary:** Speculative decoding accelerates text generation with large language models by letting a cheap draft model propose tokens that a large verifier checks in a single forward pass. We introduce Olifant, a draft model built on a memory-based classifier. It predicts the next token from a four-token window in under 0.3 ms on CPU, requiring no GPU, no backpropagation, and no accelerator memory. We measure throughput and energy under two verifier regimes on consumer hardware. Without a KV cache, drafting...

---

### 34. Forecasting Sales Delay through Time-aware Analysis of Sales Events in Textual Reports

**Authors:** Masaya Tsunokake, Yuta Koreeda, Yuhei Niwa, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16704v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16704v1)

**Summary:** Business-to-business (B2B) companies develop and deliver a one-of-a-kind product in response to a client's orders. To prepare resources for development beforehand, companies estimate dates when they will receive orders from clients in their sales process, called scheduled order dates. However, dates when the companies actually receive orders can differ from the scheduled order dates. This difference increases costs in the development. If the difference could be forecasted before receiving orders...

---

### 35. When Expert Disagreement Hurts: Prestige and Selectivity in LLM Decision Revision

**Authors:** Yupeng Tang, Mingfeng Lin

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16694v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16694v1)

**Summary:** When language models revise a decision after another agent disagrees, neither reversal counts nor final accuracy shows whether they are fixing mistakes or abandoning correct answers. We introduce a controlled two-pass audit that holds the question, the evidence, and the model's initial answer fixed and varies only the revision context: neutral reflection, anonymous disagreement, or disagreement attributed to a domain expert. For binary decisions the accounting is exact: revision raises accuracy ...

---

### 36. MuSeToM: Multi-Sensory Evaluation of Belief Revision with Textual Cues Across Six Senses

**Authors:** Chunkit Chan, Kawai Chung, Sze Heng Douglas Kwok, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16662v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16662v1)

**Summary:** Theory of Mind (ToM), the ability to infer mental states in others, is pivotal for human social cognition. Existing evaluations of ToM in large language models (LLMs) mainly focus on static belief attribution and false-belief reasoning, leaving a critical aspect of social reasoning underexplored: can LLMs decide whether perceptual evidence is sufficient to justify another person's belief revision? To address this gap, we present MuSeToM, a human-validated, text-based benchmark for evaluating epi...

---

### 37. Unibuc - NLP at "Voight-Kampff" Generative AI Detection PAN 2025

**Authors:** Teodor Marchitan, Claudiu Creanga, Liviu P. Dinu

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16612v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16612v1)

**Summary:** This paper describes the approach of the Unibuc - NLP team in tackling the "Voight-Kampff" Generative AI Detection task from PAN at CLEF 2025. In the Subtask 1: Voight-Kampff AI Detection Sensitivity we have explored different approaches of leveraging embeddings extracted from LLMs, using either classical ML models or further fine-tuning LLMs with a classification head for the downstream binary classification task. Our experiments showed that using a majority vote ensemble of classical ML models...

---

### 38. Do the Details Help the Whole? One-Way Transfer from Person Actions to Group Intent in VLMs on JRDB-Social

**Authors:** Chengguang Gan, Zhixi Cai, Yunhao Liang, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16581v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16581v1)

**Summary:** Social scene datasets label people at two levels: what each person is doing and what the group is there for. Training on both levels at once is often assumed to help each of them. We test this assumption for vision-language models (VLMs) on JRDB-Social, treating person actions as the details and group intent as the whole. We fine-tune Qwen3.5 4B under eight training arms with three seeds, repeat the core arms on Qwen3.5 9B and Qwen3-VL 4B, and judge every arm with a verdict rule fixed before tes...

---

### 39. Lost in Delegation: Studying the Effectiveness of Task Orchestration in Generative Search

**Authors:** Tamara Stojanovska, Elisabeth Kirsten, Leon Swazinna, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16526v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16526v1)

**Summary:** LLMs have quickly evolved from models used in isolation to agentic systems that delegate tasks to external tools and other LLMs to solve complex assignments. This agentic augmentation has led to impressive capability gains. However, when and how delegation improves performance remains poorly understood. For example, it is unclear whether delegation helps when tasks involve post-cutoff information that the orchestrating LLM cannot reliably resolve from its own knowledge. In this work, we use purp...

---

### 40. EvenVLM: A Text and Multimodal Dataset for the Even Language with Vision-Language Fine-Tuning

**Authors:** Daniil Makovetskii, Ivan Bondarenko

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16500v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16500v1)

**Summary:** We present EvenVLM, the first text and multimodal (VQA) dataset for Even (Lamut), an endangered Northern Tungusic language spoken by approximately 6,800 people in Siberia. Our dataset comprises 50,521 structured Even-Russian entries extracted from dictionary and phrasebook sources via GPT-4o Mini-based parsing, from which we synthetically generate 107,543 training examples spanning translation, grammar, reading comprehension, and semantic classification. To address tokenization inefficiency on E...

---

### 41. Where in the Input Does a One-Pass Decision Encoder Look?

**Authors:** Mohammed Nayeem Khan, Allan Kevin T

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16477v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16477v1)

**Summary:** Laya is a small model that answers a multiple-choice question about a text in one pass: the question, the options (each with a name and a description) and the text form one sequence of at most 512 tokens, the window, in the English release. A longer text is silently cut at the end, and we measure what that costs. Test documents place a held-out row's text, the evidence, at a chosen token offset among distractor text; 177 items, five tasks, three checkpoints (released, short-row fine-tune, long-d...

---

### 42. How Should Planning Agents ReSHAPE Their Search Space?

**Authors:** Yilin Zhang, Xinran Zhao, Tong Chen, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16466v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16466v1)

**Summary:** Planning agents and benchmarks treat a user's initial specification as fixed. Yet the requests users write exclude plans they would gladly take, since they rarely discover the possible trade-offs they would accept until seeing the options. Agents already revise requests through interaction, but whether this helps planning is unknown. We formalize this step as the ReSHAPE task, which judges a revision by whether its search space matches the acceptable plans and a planner finds one there. Using Re...

---

### 43. daVinci-Prover: Agent-Native Mid-Training for Formal Theorem Proving

**Authors:** Wenhong Zhu, Xuefeng Li, Jiashuo Zhang, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16433v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16433v1)

**Summary:** Advances in large language models (LLMs) are rapidly transforming formal theorem proving. Yet further progress remains constrained by the lack of a transparent and effective data recipe for systematically improving theorem-proving models. In this work, we argue that effective agentic provers require strong mathematical skill priors to ground theorem proving and agentic trajectories to enable long-horizon, interactive proof construction. To this end, we synthesize an agent-native 33.7B-token mid-...

---

### 44. RMIT-ADM+S at TREC RAG 2026: Research Agents, Retriever Ablations, and Open-Weight Replication

**Authors:** Oleg Zendel, Kun Ran, Chenglong Ma, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16425v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16425v1)

**Summary:** We describe the RMIT-ADM+S team's participation in the TREC 2026 Retrieval-Augmented Generation (RAG) track using the ClimbMix corpus. We submitted seven research-agent runs using proprietary OpenAI and open-weight models, exploring different retrieval strategies, writer models, and agent workflows. Pre-submission ablations identified writer selection and adjacent-chunk expansion as the main factors affecting answer quality. In the official NIST evaluation, six of seven runs exceeded the track m...

---

### 45. Experience-Handoff Reinforcement Learning for Recursive Self-Improvement

**Authors:** Doyoung Kim, Byeongguk Jeon, Kailin Zhang, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16409v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16409v1)

**Summary:** It is common to train Large Language Models (LLMs) for agentic tasks with Reinforcement Learning (RL) from scalar rewards. However, this throws away the fine-grained information about the environment that the agent experienced during the trial (e.g., error logs). To utilize this rich information, recent works wrap the agent in a harness that refines its own inputs through reflection or compaction and hands past experience to future rollouts, but the construction of the handed-off artifacts (e.g....

---

### 46. Saidzoda-Kazakh-EmbeddingGemma-300M: How Far One Epoch of Generated Questions Takes a Small Kazakh Embedder

**Authors:** Tohir Saidzoda, Madina Abdusalomzoda, Abubakr Abdullozoda, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16399v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16399v1)

**Summary:** EmbeddingGemma-300M is a small open embedder, and used as released it finds the right passage first for 60.8% of the Kazakh Belebele retrieval questions. We present Saidzoda-Kazakh-EmbeddingGemma-300M, the same model fully fine-tuned for one epoch on 208,511 pairs: 166,263 Kazakh questions that our own language model wrote about source passages from encyclopedias, Wikipedia, news and books, each checked by a second model, plus English and Russian replay. On Kazakh Belebele, recall@1 rises from 6...

---

### 47. Beyond Compressing Everything: Contrastive Memory Learning for Selective Context Compression

**Authors:** Sikui Zhang, Haowei Liu, Ziyun Gan, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16384v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16384v1)

**Summary:** As large language models (LLMs) advance toward increasingly long inputs, soft context compression offers a promising approach to efficient inference by converting long inputs into compact memory slots. Under limited memory budgets, effective context compression remains challenging because task-relevant evidence varies substantially across queries, ranging from localized evidence to multiple distant spans or information dispersed throughout the full document. Instead of compressing everything ind...

---

### 48. Recursive State-Augmented Language Models: Persistent Latent-State Adaptation of Pretrained Language Models

**Authors:** Omer Haq

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16375v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16375v1)

**Summary:** Language models rely on finite token contexts, limiting access to earlier interactions. We introduce Recursive State-Augmented Language Models (Recursive SALM), a framework in which a persistent latent state evolves with each observation and generates adaptations of a pretrained language model. A modular read-transition-write architecture separates observation encoding, latent dynamics, and predictor adaptation. We develop deterministic and stochastic formulations.   The experiments evaluate onl...

---

### 49. IsharaBART: An efficient BART-Based Framework for Low-Resource Bangla Sign Language Translation

**Authors:** Aonmoy Das, Ananna Dev Aishi, Md. Fazlul Kader

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16359v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16359v1)

**Summary:** Millions of Bangla Sign Language (BdSL) users lack reliable automatic translation tools. Existing systems are limited by data scarcity, unidirectional design, and computationally expensive architectures that are not suitable for low-resource deployment. We introduce IsharaBART, a bidirectional generative framework for gloss-sentence translation in BdSL. IsharaBART uses Bidirectional and Auto-Regressive Transformers (BART)-based conditional language modeling with denoising learning objectives. We...

---

### 50. Does Deep Knowledge Tracing Learn Semantic Relations Between Knowledge Components?

**Authors:** Kia Karbasi, Mahdi Saiedi, Kevin Hong, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16323v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16323v1)

**Summary:** Deep Knowledge Tracing (DKT) is a knowledge tracing (KT) model that updates a shared latent state from sequences of interactions, each pairing a knowledge component (KC) with a response. An interaction with one KC can therefore affect predictions for other KCs. We ask: Are the KC relations learned by DKT semantic? We construct text-derived semantic KC representations using nine pipelines to test whether the conclusions hold across alternative ways of constructing those representations.   The fir...

---

## cs.CV

**50 papers**

### 1. Back to Pixels: Lifting Latent Video Diffusion into Pixel Space

**Authors:** Yanke Song, Shuo Chen, Chris Rockwell, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17336v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17336v1)

**Summary:** Frontier video generation models work in a VAE latent space that compresses video in both space and time. This compression made training tractable, but now limits high-resolution, controllable, and interactive generation -- doubling resolution quadruples token count, conditions apply to groups of frames rather than individual ones, and each response must wait for the rest of its multi-frame block. We present PixVid, a simple yet effective method that lifts a pretrained latent video model to dire...

---

### 2. Unbundling Multimodal Vision Encoding

**Authors:** Ellis Brown, Chris Hoang, Shengyi Qian, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17334v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17334v1)

**Summary:** How multimodal language models should encode visual input remains up for debate. Most models use a pretrained vision encoder, while some recent recipes train the encoder from scratch with the language model or remove it entirely. Vision encoders bundle together three design choices: a visual prior from upstream pretraining, dedicated vision capacity, and pre-fusion placement of that capacity (i.e., before the multimodal backbone). Because published models also differ in data, architecture, and c...

---

### 3. TTB: Test-time Baking for Efficient Rendering of Decoder-only View Synthesis Models

**Authors:** Chin-Yang Lin, Ryo Hachiuma, Jaesung Choe, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17331v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17331v1)

**Summary:** Decoder-only Large View Synthesis Models (LVSMs) with KV-cache have recently achieved state-of-the-art quality by regressing novel views from neural networks without reconstructing 3D geometry, while Test-Time Training (TTT) layers save computation but sacrifice quality. We propose Test-Time Baking (TTB), a strategy that learns to bake global scene information from cross-view attention into a lightweight MLP, enabling fast and high-fidelity novel-view decoding. The first key is to repurpose the ...

---

### 4. ProtoVis-Nav: Prototypical Visual Imagination for Visual-Spatial Aligned UAV Navigation

**Authors:** Guangyuan Sui, Yunzhong Hou, Chi Harold Liu

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17330v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17330v1)

**Summary:** Vision language navigation (VLN) is very challenging for Unmanned Aerial Vehicles (UAVs) since small errors in 3D motion prediction can lead to navigation errors and collisions. Unable to fathom execution outcomes in 3D environments, existing methods often struggle to predict accurate navigation waypoints from language instructions. To solve this, we introduce the Prototypical Visual Imagination framework, shortened as ProtoVis-Nav, which forces the model to imagine an outcome-associated local v...

---

### 5. K2V: Generative Keyframing For Physically Plausible Video Generation

**Authors:** Felix O'Mahony, Daniel Olmeda Reino, Roberto Cipolla, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17324v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17324v1)

**Summary:** Video diffusion models are able to generate samples with high-quality appearance and textural qualities. However, content produced by these methods is known to exhibit significant physical errors. This is because, in a classical video generation setting, all physical reasoning must take place simultaneously and exclusively within the diffusion process.We propose to resolve these issues by redistributing the task of physical reasoning onto a language model-backed keyframe generation module, which...

---

### 6. BrickFlow: Connectivity-Guided Brick Reconstruction

**Authors:** Peter Kulits, Cordelia Schmid

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17321v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17321v1)

**Summary:** Given a set of LEGO parts and an image of an assembled object, our task is to infer the pose of each part to assemble the object. In contrast with traditional 3D reconstruction, doing so requires satisfying discrete physical constraints, which provide structure but render the problem combinatorial and highly sensitive to small pose errors. To learn a prior over how parts fit together, we train a set-conditioned SE(3) flow model on procedurally generated assemblies. We then finetune this model to...

---

### 7. Spatial Foundry: A Multimodal Dataset for Spatial Intelligence

**Authors:** Ethan Lin, Yang Song

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17318v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17318v1)

**Summary:** Spatial intelligence requires connecting visual observations to the geometry, objects, and persistent state of an environment. Images alone leave these relationships implicit, while disconnected annotations make it difficult to study appearance, camera motion, and scene changes under a common reference. We introduce Spatial Foundry, a collection of 5,280 furnished residential 3D scene configurations with editable assets and aligned visual, geometric, and temporal data. Its modalities include flo...

---

### 8. FLEX-LBP: Learning Local Binary Patterns with Exact Binary Inference for Texture Classification

**Authors:** Mohamed Alimoussa, Amal El Kaid

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17302v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17302v1)

**Summary:** Local Binary Patterns (LBP) remain among the most widely used texture descriptors, from industrial inspection to medical imaging. Yet their radius, sampling angles, color transform and thresholds are fixed by hand for each dataset. We present FLEX-LBP, which learns these parameters by backpropagation while every forward pass computes exact binary codes and hard histogram counts. A straight-through estimator acts only in the backward pass, so the deployed descriptor is an interpretable hard-binar...

---

### 9. Consistent Video-to-Video Translation via Explicit Correspondences

**Authors:** Gaurav Parmar, Zhengqi Li, Richard Zhang, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17298v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17298v1)

**Summary:** Interactive video-to-video applications require real-time generation while maintaining long-range temporal consistency. However, recent methods achieve speed by restricting attention to a fixed-length causal window. This limits long-range consistency whenever relevant history falls outside the context window. To address this limitation, we introduce vid2vid-long, a correspondence-based approach grounded in a simple observation. Video-to-video translation provides an explicit cross-frame referenc...

---

### 10. Objects as Addresses: Instance Binding in Vision Transformer Attention

**Authors:** Khalil Sabri, Guillaume-Alexandre Bilodeau, Nicolas Saunier, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17240v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17240v1)

**Summary:** Humans naturally parse visual scenes into coherent individual objects rather than scattered features, a capability cognitive science calls object binding. While recent work shows that pretrained Vision Transformers (ViTs) intrinsically acquire this ability, how native self-attention computations mechanistically keep object instances separate remains unresolved. By studying this across eight pretrained ViTs, we found that instance separation is expressed more strongly in attention routing than in...

---

### 11. MALNISI-Infused Graph Construction and Weighted Contrastive Loss based GAT for Unsupervised Representation Learning in HSI

**Authors:** Soumi Sarkar, Subhadip Boral, Sarbani Palit, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17199v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17199v1)

**Summary:** Hyperspectral images (HSI) possess discriminating spectral characteristics with respect to land utilization due to high-dimensional information. Recently, unsupervised representation learning using graph neural networks has unveiled these utilization-specific complex spectral relations. This article has three main contributions. First, it proposes an index, the Mean Absolute Local Neighborhood Inverse Spectral Index (MALNISI), which measures the similarity between two pixels based on their neigh...

---

### 12. eDMD: Endpoint Distribution Matching for Few-Step Diffusion Distillation

**Authors:** Tong Zhao, Xianfang Zeng, Yucheng Han, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17194v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17194v1)

**Summary:** Distribution matching distillation (DMD) has emerged as a leading paradigm for distilling diffusion models into few-step students, where an auxiliary fake score model tracks the student's distribution and the discrepancy between the teacher and fake predictions drives the student toward the teacher. In multi-step distillation, although only the student's final output is delivered, existing methods train the fake model on intermediate states or across all denoising steps. Consequently, the studen...

---

### 13. Consensus Capture in Reference-Based UAV Video Stabilization: A Benchmark on Dynamic Urban Scenes

**Authors:** Robert Fonod, Nikolas Geroliminis

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17190v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17190v1)

**Summary:** Reference-frame stabilization registers every frame of a hovering-drone video onto one reference frame, keeping object positions comparable. The registration pipelines it relies on are selected on feature-matching benchmarks in which only the camera moves. Over a busy intersection, vehicles moving together supply mutually consistent correspondences that can draw the robust homography estimate toward their motion: consensus capture, which inlier statistics cannot flag. A two-part benchmark measur...

---

### 14. Neural Render Proxies for Interactive and Differentiable Lighting

**Authors:** Sergio Sancho, Alexander Rath, Marco Manzi, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17185v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17185v1)

**Summary:** Within the CG animation production pipeline, the challenges artists tackle in Lighting can be immense. Even minor adjustments require re-rendering massive scenes with slow offline renderers; global illumination has to be sampled and complex shaders have to be evaluated, leading to iteration times of minutes to hours per frame. To accelerate this process, we introduce a novel neural render proxy (NRP) that enables differentiable relighting of static scenes with fixed camera and materials at inter...

---

### 15. Validation-Guided Prompt Selection for Differential Morphing Attack Detection

**Authors:** Raghavendra Ramachandra, Hailin Li

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17176v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17176v1)

**Summary:** Differential morphing attack detection (D-MAD) compares a trusted live capture with a document image that may contain a facial morph. We investigate whether labelled validation data can improve a frozen-parameter vision-language evaluator through prompt selection rather than model fine-tuning. Version~1 generates 50 candidate prompts and selects the top-ranked instruction using a security-oriented loss that prioritises missed morph attacks (MACER) while accounting for bona fide classification er...

---

### 16. SpotDiff: A Plug-and-Play Framework for Zero-Shot Change Detection in Remote Sensing Imagery

**Authors:** Anit Upadhyaya, Ata Akbari Asanjan, Chaitanya Jalluri, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17172v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17172v1)

**Summary:** Remote sensing change detection usually relies on large collections of temporally aligned, pixel-level annotations, which limits its scalability across regions, imaging platforms and application domains. Recent zero-shot approaches reduce the need for supervision, but they often localize fine-grained changes poorly because their features are coarse or inconsistent across time. We present SpotDiff, a training-free, plug-and-play framework for zero-shot change detection built by composing compleme...

---

### 17. UAV-Flow++: A Unified Suite for Benchmarking and Learning Language-Guided UAV Flight

**Authors:** Donglin Yang, Xiangyu Wang, Yantong Zhong, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17163v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17163v1)

**Summary:** Language-guided UAV navigation has largely focused on long-horizon route planning, leaving short-range, object-relative flight maneuvers underexplored. To address this gap, we formulate Flying-on-a-Word (Flow), a task requiring a UAV to convert concise natural-language instruction, egocentric visual observation, and current state dynamics into continuous flight actions. Flow encompasses both primitive motion commands and complex object-interactive behaviors, assessing motion intent comprehension...

---

### 18. HiVE-VQA: Hierarchical Interaction via Volumetric Embedding for Video Quality Assessment

**Authors:** Robbie Hamilton, Fan Zhang, David Bull

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17146v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17146v1)

**Summary:** The proliferation of user-generated video content has made accurate and robust no-reference video quality assessment (NR-VQA) a highly important challenge. Existing research increasingly relies on architecturally complex multi-branch pipelines or computationally intensive fine-tuning of single-branch backbones. In this paper, we investigate whether a single frozen video foundation model can serve as an effective NR-VQA backbone, and propose HiVE-VQA, the first framework (to our knowledge) to app...

---

### 19. STeP-C: Real-Time Neural Compression for Distributed Fiber-Optic Sensing at Scale

**Authors:** Tingfeng Li, Ming-Fang Huang, Shaobo Han, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17126v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17126v1)

**Summary:** Distributed fiber-optic sensing (DFOS) technologies such as Distributed Acoustic Sensing (DAS) generate continuous, high-resolution spatio-temporal data at rates exceeding hundreds of megabytes per second, creating severe challenges for real-time storage and transmission. While neural compression methods can achieve strong rate-distortion performance on sensing data, prior approaches either require per-segment retraining incompatible with streaming, or have only been validated offline. None have...

---

### 20. Spatiotemporal learning improves quantification of pore-space evolution and fluid displacement

**Authors:** Zhuangzhuang Ma, Rukuan Chai, Qianqian Ma, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17111v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17111v1)

**Summary:** Pore-space evolution and fluid displacement influence how rocks transmit and store fluids, affecting geological carbon storage, underground hydrogen storage and groundwater contaminant transport. A single time-resolved micro-CT experiment may produce tens to hundreds of three-dimensional images, and segmentation is required to quantify physical properties and run image-based simulations. Traditional methods such as thresholding perform poorly on noisy, low-contrast images and need manual adjustm...

---

### 21. Predicting Ethanol Drinking Status from Nonhuman Primate Liver Histology: A Proof of Concept for Parameter-efficient Fine-tuning in Few-Shot Vision-Language Modeling

**Authors:** Amirmohammad Mohammadi, Rupak Khadka, Kathleen A. Grant, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17105v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17105v1)

**Summary:** Combining vision-language models (VLMs) with parameter-efficient fine-tuning (PEFT) offers a promising approach to few-shot whole-slide image (WSI) classification in computational pathology. This study evaluates this approach for predicting ethanol drinking status from nonhuman primate liver histology. Adapters are evaluated against non-PEFT configurations on a subset of the Monkey Alcohol Tissue Research Resource (MATRR). All evaluated PEFT configurations achieve higher mean balanced accuracy t...

---

### 22. TuMAP: A Dual-View, Morphotype-Aware Pathomics Pipeline for Quantifying Renal Tubular Remodeling

**Authors:** Ruijie Wu, Yuechen Yang, Yanfan Zhu, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17104v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17104v1)

**Summary:** Quantifying disease-associated renal tubular remodeling is challenging because tubular appearances are heterogeneous. We introduce TuMAP (Tubular Morphotype-Aware Pathomics), a pipeline combining (1) dual-view foundation-model representations and provisional morphotype annotation, (2) compositional and within-morphotype pathomics, and (3) patient-level statistical inference. From 456,158 tubules in 358 PAS-stained kidney biopsy slides, TuMAP identified eight image-based morphotypes, seven of whi...

---

### 23. Joint Null-Space Projection for Data-Free Model Merging

**Authors:** Tian Xia

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17103v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17103v1)

**Summary:** Merging independently fine-tuned checkpoints into a single multi-task model requires no data, no labels, and no gradient steps. In practice the task vectors of different tasks interfere, and the standard remedies--averaging, magnitude pruning, sign election--operate entry by entry, ignoring that each delta induces a low-dimensional update on the hidden features it acts upon. We recast merging as a subspace interference problem. For every two-dimensional weight tensor we take the top-r right-sing...

---

### 24. SALT: State-Aligned Low-Rank Transfer for Single-Temporal Cross-Dataset Structural Localization in Remote Sensing

**Authors:** Aggelos Psiris, Georgios Angelidis, Giorgos Sfikas, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17077v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17077v1)

**Summary:** Change detection in remote sensing conventionally relies on spatially aligned bi-temporal imagery, which may be unavailable or unreliable in practical scenarios. Recent single-temporal approaches address this limitation by learning structural evidence, such as building regions, from a labeled source dataset and transferring it to unseen target imagery using only the current image. However, adaptation to the source dataset can over-specialize pretrained features and reduce their cross-dataset gen...

---

### 25. Ropedia Xperience 2: A Gold Standard for Scaling Physical AI Environments and Behaviors

**Authors:** Hao Li, Fangzhou Hong, Zhaoxi Chen, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17060v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17060v1)

**Summary:** Large foundation models such as GPT-6 Astra and Claude Fable 5.1 have recently been shown to control robots directly from visual observations. They nevertheless remain brittle on long-horizon, contact-rich tasks in real-world environments. Further progress depends on two complementary resources: demonstrations of human behavior that supervise how tasks are performed, and interactive environments in which policies can be rolled out, evaluated, and improved in closed loop. Language models have adv...

---

### 26. AURA 2.0: From User-Driven Responses to Model-Initiated Conversations in Streaming Video

**Authors:** Shuhan Li, Huankang Guan, Xintong Guo, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17048v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17048v1)

**Summary:** Most AI assistants respond only when prompted, remaining silent even when events in the video stream offer meaningful opportunities for conversation. To move beyond purely user-driven interaction, we present AURA 2.0, a streaming video large language model that introduces three core upgrades to AURA. The key advance is Model-Initiated Conversation (MIC), which enables the model to identify topics worth discussing in the evolving visual stream and initiate conversations at appropriate moments wit...

---

### 27. ElasticDino: Dense Semantic Features Using Elastic Deformations

**Authors:** Ulysse Mizrahi, Sean Zaretzky, Dov Danon, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16984v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16984v1)

**Summary:** Vision transformers (ViTs) serve as the backbone for countless vision tasks, including dense prediction tasks, such as segmentation and depth estimation, even though the quadratic complexity of self-attention severely limits feature resolution and induces spatial artifacts. In this work, we introduce ElasticDino, a lightweight adapter which produces high-resolution feature maps, adhering to the fine details of the input image. As a key insight, we observe the consistency of artifacts across chan...

---

### 28. A Disease-specific Retinal Aging Biomarker for Predicting Progression to Late Age-related Macular Degeneration

**Authors:** Hexin Dong, Benjamin Hou, Puzhen Wu, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16955v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16955v1)

**Summary:** Age-related macular degeneration (AMD) is a leading cause of irreversible vision loss in older adults. While chronological age is a primary risk factor, it inadequately reflects individual variations in retinal aging, limiting effective AMD risk stratification and timely intervention. Here, we propose and validate fundus-based AMD age (FAA), which quantifies disease-specific retinal aging in AMD and captures accelerated AMD-related retinal aging, thereby improving prognostic precision over chron...

---

### 29. Report of the 8th LSVOS Challenge: Mobile Unified Multimodal Understanding

**Authors:** Chang Liu, Henghui Ding, Tong Yang, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16925v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16925v1)

**Summary:** This report summarizes the Mobile Unified Multimodal Understanding (MUMU) track of the 8th Large-scale Video Object Segmentation (LSVOS) Challenge, held in conjunction with ECCV 2026. MUMU asks for a single unified model that jointly performs multi-concept image tagging over quality, scene, and event vocabularies, open-vocabulary object detection, and concise image captioning, within a budget of 0.5B parameters and 8 GB of peak inference memory. Submissions are ranked by a weighted task score sc...

---

### 30. Automated PD-L1 Tumor Proportion Scoring with Uncertainty-Guided Triage in Non-Small Cell Lung Cancer

**Authors:** Kesi Xu, Ayesha Azam, Tanvier Kaur, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16907v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16907v1)

**Summary:** Programmed death-ligand 1 (PD-L1) tumor proportion score (TPS) informs immunotherapy selection in non-small cell lung cancer. Near the 1% and 50% cutoffs, the score should also indicate when closer review is warranted. We designed a three-stage framework to follow the sequence of TPS assessment. Stage 1 identifies tumor regions and excludes macrophage-rich patches. Stage 2, a dual-branch cell counting network (D2Count-Net), counts PD-L1-positive and PD-L1-negative tumor cells in these regions to...

---

### 31. TokenStream: Multi-Subject Personalized Video Generation with Token-wise LoRA and Guided Attention

**Authors:** Hung Nguyen, Quang Qui-Vinh Nguyen, Khoi Nguyen

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16897v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16897v1)

**Summary:** We introduce TokenStream, an optimization-based framework that composes independently learned subject identities in text-to-video generation without a reference-video training dataset or joint optimization of each new subject combination. Learning from a single reference image makes subject appearance difficult to separate from static-image bias, while merging independently trained adapters can mix identities. Token-wise LoRA (ToRA) restricts low-rank updates to the cross-attention value project...

---

### 32. Raysemble: Metric 3D Bone Reconstruction from a Single X-ray

**Authors:** Xiaoyang Li, Xinghao Yan, Yuan Chai

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16869v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16869v1)

**Summary:** Raysemble reconstructs eight lumbar and pelvic bones from a single X-ray by separating shape and placement. Each 3D query samples regional and global features at its image projection. A shared decoder predicts normalized bone shapes. Predicted depth and camera geometry determine 3D centers and scales for resampling these shapes onto a common grid in millimeters. Evaluation uses 23 held-out patients with 43 CT scans, each generating one simulated anteroposterior radiograph. Without rigid alignmen...

---

### 33. Visual Cipher Bench: Benchmarking LLM Agents on Long-Horizon Visual Reasoning

**Authors:** Deyao Hong, Jiayi Jiang, Yuchun Chen, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16861v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16861v1)

**Summary:** While language-model agents excel at long-horizon coding and terminal tasks, this success relies on two conditions: explicit text specifications and immediate execution feedback. However, neither condition holds in real-world problems where critical information exists only in images, leaving it unclear whether long-horizon capability transfers from text to visual reasoning. In such visual settings, because rules and clues resist text transcription and lack test-case feedback, agents must repeate...

---

### 34. Kosmo-GFM: A Production-Ready Geometry Foundation Model

**Authors:** Sheng Tang, Shengzhe Wei, Tiancheng Chen, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16840v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16840v1)

**Summary:** We present Kosmo-GFM, a scene reconstruction system that integrates a geometry foundation model (GFM), a pose optimization engine (PoseEngine), and reconstruction-derived supervision from KosmoWorld. GFM predicts camera parameters, depth, cross-view correspondences, and dynamic 3D points from images and videos. PoseEngine combines these predictions with geometric optimization to recover scene-level camera poses and geometry for downstream 3D and 4D Gaussian Splatting. KosmoWorld generates images...

---

### 35. EG360: Efficient and Generalizable $360^\circ$ Depth Estimation via Adaptive Panorama-Perspective Distillation and Spherical Cross-Level Feature Fusion

**Authors:** Laiyan Ding, Chongxi Meng, Rui Huang

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16793v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16793v1)

**Summary:** Generalized panorama depth estimation has witnessed great advances in recent years. These methods typically achieve robust zero-shot generalization performance using large pretrained models, but their high computational cost makes real-time inference on embedded platforms challenging. In contrast, previous lightweight panorama models have mostly been developed for single-domain evaluations and cannot generalize well due to domain shifts. To reduce the gap between these two types of models, we in...

---

### 36. Evaluating Video LLMs' Understanding of Corner Cases in Autonomous Driving

**Authors:** Gabriel Manalu, Minh Son Hoang, Hyeontaek Hwang, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16767v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16767v1)

**Summary:** Natural language explanations promised by modern Video Large Language Models (Video LLMs) offer autonomous driving systems a path toward detailed scene description and interpretable decision making on the road. While recent benchmarks have begun assessing these models on driving scenes, they mainly target routine traffic conditions and general comprehension tasks based on existing driving datasets and therefore fail to evaluate model performance on the rarest and most safety-critical driving eve...

---

### 37. Efficient Periocular Recognition through Model Scaling and Cross Spectral VIS NIR Verification

**Authors:** Fabian Stockhard, Juan E. Tapia, Christoph Busch

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16764v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16764v1)

**Summary:** Periocular recognition offers an efficient alternative to full-face verification when facial regions are occluded or image resolution is limited. We present AdaEye, a systematic study of input and backbone scaling for periocular verification in visible-spectrum (VIS) and cross-spectral (VIS/NIR) settings. Using an AdaFace-style framework, we compare full-face, masked-face, and dedicated 80x40 periocular inputs while varying backbone width and embedding dimensionality. Across four VIS/VIS and VIS...

---

### 38. AgriSense: Vision-Language Decision Support and Robotic Intervention in a Virtual Greenhouse Copy title

**Authors:** Lyes Saad Saoud, Oualid Doukhi, Reza Ghorbani, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16752v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16752v1)

**Summary:** Autonomous greenhouse management increasingly requires robotic systems that integrate perception, navigation, environmental regulation, and plant-level intervention. This paper presents AgriSense, a framework combining an Isaac Sim virtual greenhouse, a quadruped mobile manipulator, RGB and LiDAR-inertial sensing, environmental control, and supervised vision-language decision support. Frozen DINOv2 and BERT encoders, together with structured environmental inputs, support joint prediction of twel...

---

### 39. ORCA:Orthogonal Residual Consensus Alignment for Multi-View Clustering

**Authors:** Xiaojian Ding, Xian Li, Xiaoying Zhu, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16749v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16749v1)

**Summary:** Deep multi-view clustering often suffers from redundant information accumulation during fusion and indiscriminate alignment across representation levels. We propose Orthogonal Residual Consensus Alignment (ORCA) to address these challenges. Its semantic incremental recurrent fusion module extracts cross-view orthogonal residuals as non-redundant increments and adaptively weights recurrent states through divergence-guided gating. Its consensus-calibrated hierarchical contrastive alignment module ...

---

### 40. PhysLoop: Harnessing LLMs' Physics Awareness for Self-Improving Video Generation Models

**Authors:** Yuxuan Chen, Xiaojie Li, Hao Chen, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16748v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16748v1)

**Summary:** Video generation models produce visually realistic videos but still struggle with physical dynamics and causal consistency. Learning from generated videos requires fine-grained physical supervision, yet reliable quality judgments, correction pairs, and controlled variations are difficult to obtain. Large language models (LLMs) possess physical knowledge, but struggle to reliably guide video generation models in producing their training videos. We present PhysLoop, a unified harness designed to s...

---

### 41. Fog-FWL: A Large-Scale Full-Waveform LiDAR Dataset for Recovering Fog-Hidden Objects

**Authors:** Kazuma Ikeda, Kotaro Oishi, Ryosei Hara, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16742v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16742v1)

**Summary:** LiDAR is a core sensor for autonomous driving, yet it is highly vulnerable to fog. Fog scattering produces strong backscatter near the sensor and attenuates reflections from objects behind it, so weak object returns are often discarded by the peak detection that converts received signals into point clouds. Full-waveform LiDAR (FWL), which records the received optical signal before peak detection, retains these weak returns, but the lack of suitable data has prevented research on recovering fog-h...

---

### 42. From Foundation VLM to Versatile Driving VLM: A Triplet Incremental Training Approach

**Authors:** Shengtao Wu, Zichao Dong, Weixuan Qiao, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16727v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16727v1)

**Summary:** Adapting general Vision-Language Models (VLMs) to Autonomous Driving (AD) is thought to require heavy 3D spatial priors or intrusive architectural overhauls to compensate for a lack of spatial grounding. In this work, we present a counterintuitive pilot study: off-the-shelf general VLMs already exhibit remarkable adaptability across diverse driving tasks, while precise metric depth remains the primary missing link, a bottleneck readily addressable via onboard sensors and depth foundation models....

---

### 43. What Limits Thermal Infrared Drone Detection? A Cross-Dataset Benchmark Analysis

**Authors:** Tamara R. Lenhard, Jan Kels, Tobias Koch

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16724v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16724v1)

**Summary:** Thermal infrared (IR) imaging enables drone detection with reduced dependence on ambient illumination, supporting continuous surveillance beyond the limitations of visible-spectrum sensing. However, substantial and often undocumented variability in camera systems, processing pipelines, and annotation practices across public IR drone datasets complicates the assessment of detector performance and cross-domain generalization. To examine these sources of variability and their implications for drone...

---

### 44. Sprint3D: Accelerating End-to-End 3D Asset Generation through Pipeline Optimization

**Authors:** Sho Kuno, Ruihan Yu, Yonghao Yu, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16701v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16701v1)

**Summary:** Image-to-3D generative models now produce asset-quality textured meshes, but at minutes per asset they remain slow to iterate with and costly to deploy. Prior work has mostly accelerated the sampling of the networks, and where it also optimizes the mesh processing, it trains its own generators. We instead start from a publicly released pipeline and ask how much of its end-to-end time can be saved. Profiling the public Pixal3D pipeline shows that its latency is dominated by what happens after the...

---

### 45. MuViRL: Multimodal View-Invariant Visual Speech Representation Learning via Calibrated View Aggregation

**Authors:** Fei Su, Kai Qiu, Juan Liu

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16655v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16655v1)

**Summary:** Multimodal representation learning combines complementary signals to capture shared semantic information. For dynamic scenes, these representations need to remain consistent across views while preserving distinctions between temporal states. In visual speech representation learning, view variation changes the visibility and reliability of articulation cues, making it difficult to learn such representations from synchronized audio and video. To address this challenge, we propose MuViRL, a self-su...

---

### 46. Learning the Missing Derivative: Neural Multiple-Scattering Operators for Inverse Volume Rendering

**Authors:** Sipeng Chen, Shibo Li

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16650v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16650v1)

**Summary:** Reconstructing optically thick media from photographs requires modeling multiple scattering and its response to changes in extinction. Frozen-source tomography discards this derivative; differentiable path tracing estimates it through expensive, noisy sampling. We instead predict the multiple-scattering field with a neural operator and differentiate through it during inverse rendering, while computing transmittance and single scattering directly. A further challenge arises during optimization: a...

---

### 47. Dataset Distillation via Drifting

**Authors:** George Cazenavette, Angelina Quan, Giannis Daras, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16642v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16642v1)

**Summary:** The task of dataset distillation concerns the learning of a small set of synthetic samples that can serve as an effective replacement for a large real dataset when used for downstream tasks. While many solutions have been proposed since the problem's inception, most of them primarily seek to optimize the distilled data with respect to a classifier. In this work, we propose a new distillation method that learns a set of samples such that they directly approximate the per-class data distribution. ...

---

### 48. Asymmetric Multimodal Learning with Decomposed JEPAs

**Authors:** Yusuf Shihata

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16639v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16639v1)

**Summary:** Cross-modal alignment is the standard objective for building multimodal representations. We show that alignment as a \emph{sole} objective is lossy wherever modalities are informationally asymmetric---where neither can express what the other carries. Visual question answering is an obvious case: a question is a selective relational operator probing a dense visual field whose fine-grained features no query recovers, so what alignment preserves is not what the task requires. We prove an \textbf{Al...

---

### 49. When Chekhov's Gun Fires Anyway: Over-Realization in Text-to-Image Models

**Authors:** Jiahao Huang, Kon Woo Kim, Song-Duo Ma, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16630v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16630v1)

**Summary:** In text-to-image generation, a target that the prompt mentions often appears in the generated image in a way the prompt does not call for. We call this failure over-realization. Mental-spaces theory points to the situations where it can happen: under a negation, inside what a character believes or imagines, as the vehicle of a figurative comparison, or behind a viewpoint that hides the target. Prior work has studied only negation in depth, and the conventional alignment and preference metrics do...

---

### 50. Safety as a Budget: Calibrating the Control Channel of Constrained GRPO for Vision-Language Models

**Authors:** Bo Han

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16628v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16628v1)

**Summary:** Reinforcement learning can teach vision-language models (VLMs) to decline harmful image-text requests, but how safe the result becomes is set indirectly, through reward weights found by trial runs. Stating safety as budgets on the rate of harmful assistance and the rate of over-refusal, enforced by Lagrange multipliers inside GRPO with an off-the-shelf scorer as the cost, is the natural fix, and it fails twice. The multiplier compares the scorer's mean with the budget, and scorers built for rank...

---

## cs.LG

**50 papers**

### 1. Unbundling Multimodal Vision Encoding

**Authors:** Ellis Brown, Chris Hoang, Shengyi Qian, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17334v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17334v1)

**Summary:** How multimodal language models should encode visual input remains up for debate. Most models use a pretrained vision encoder, while some recent recipes train the encoder from scratch with the language model or remove it entirely. Vision encoders bundle together three design choices: a visual prior from upstream pretraining, dedicated vision capacity, and pre-fusion placement of that capacity (i.e., before the multimodal backbone). Because published models also differ in data, architecture, and c...

---

### 2. ArchSpace: Recording, Reviewing, and Referencing LLM Architecture Research

**Authors:** Jie Wang, Tong Zhu, JiaHao Kuang, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17332v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17332v1)

**Summary:** Model architecture shapes the scaling behavior, training efficiency, and inference cost of LLMs, making it a central focus of both industry and academia. In industry, teams such as those behind DeepSeek, Qwen, and Kimi routinely introduce architectural innovations, yet public reports rarely document which ideas succeeded, which were abandoned, and why. In academia, limited compute and inconsistent baselines often restrict evaluations to small-scale, single-point comparisons, making it difficult ...

---

### 3. Internalizing Investment Mandates: A Neurosymbolic RL Approach to Portfolio Allocation

**Authors:** Zeynep Yıldız, Satchit Chatterji, Ercan Atam, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17329v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17329v1)

**Summary:** Institutional portfolios operate under investment policy statements that specify asset allocation constraints, often conditioned on market regime information. Deep reinforcement learning has been shown to optimize financial performance but typically does not enforce rule compliance, making it unsuitable for real-world deployment. Existing neurosymbolic methods such as Probabilistic Logic Policy Gradient (PLPG) offer constraint-satisfying reinforcement learning (RL) via differentiable symbolic su...

---

### 4. AgentSSL: Can MLE Agents Leverage Unlabeled Data?

**Authors:** Ethan Lin, Akanksha Sarkar, Ziang Liu, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17323v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17323v1)

**Summary:** Applying machine learning systems to new domains introduces bottlenecks in both labeled data acquisition and manual pipeline engineering. While recent MLE agents show promise in automating pipeline design, they have been studied almost exclusively in fully supervised settings, leaving them untested in realistic regimes where labeled data is scarce but unlabeled data is abundant. In this work, we introduce Agentic Semi-Supervised Learning (AgentSSL), framing SSL as a program search problem and st...

---

### 5. Linking Rapid Learning to Compositional Structure in Neural Networks: Evidence from Additive Analogies in Meta-Learned Parameter Spaces

**Authors:** Abigail L. Tenenbaum, R. Thomas McCoy

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17314v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17314v1)

**Summary:** Humans can learn rapidly from limited experience, while neural networks typically require extensive training. In this work, we investigate what properties of a neural network can enable it to learn rapidly. We study neural networks that have been optimized via meta-learning, a technique that exposes a network to many related functions to facilitate its subsequent learning of similar functions. Prior work has shown that these meta-learned networks can learn new functions rapidly, but how they do ...

---

### 6. Sketching Language Models for Context Attribution

**Authors:** Christopher Liaw, Aranyak Mehta, Grigoris Velegkas, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17313v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17313v1)

**Summary:** Context attribution asks how removing parts of a prompt changes a language model's output. We study leave-one-out (LOO) attribution for a prompt of $n$ tokens and a fixed measurement function. Computing all LOO values directly requires $n$ model evaluations. Under a stability assumption, our algorithm estimates all LOO values to error proportional to $\varepsilon$ with constant probability using $O(\sqrt{\log(1/\varepsilon)}/\varepsilon)$ evaluation calls. To complement our upper bound, we prove...

---

### 7. Classical Energies Learn to Reason 1,000x Faster than Looped Models

**Authors:** Benjamin Hoover, Hugh Blayney, James C. R. Whittington

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17309v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17309v1)

**Summary:** Looped models have emerged as a prominent paradigm for reasoning, with successes on simple reasoning puzzles such as Sudoku-Extreme and Maze-Unique. However, these models can be unstable, slow to train, and use many parameters and FLOPs to solve simple puzzles. Descent on an energy not only mitigates these issues but also offers advantages: built-in early stopping, compute that adapts to problem difficulty, fast training without differentiating through a solver, and interpretable weights that le...

---

### 8. Quantifying structural stability of transparent models for general insurance pricing

**Authors:** Félix Côté, Marie-Pier Côté

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17308v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17308v1)

**Summary:** The short duration of general insurance contracts leads to rapid distributional shifts in the data, warranting regular model updates. This process may yield a post-update model that differs considerably from the pre-update model in both predictions and structure. Structural stability is upstream of predictive stability, yet existing structural stability metrics are mostly restricted to simple decision trees. Thus, we first introduce the notion of functional transparency, characterising models wi...

---

### 9. Towards a Theory of Learnability via Debate

**Authors:** Tosca Lechner, Vinayak Pathak, Sivan Sabato, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17303v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17303v1)

**Summary:** Debate has been recently proposed as a training protocol that is hoped to produce more aligned models even as model capabilities scale. The idea is that the human, instead of providing supervision in the form of labels, judges a debate between two models that compete to prove the correctness of opposite labels. It can be shown that functions of a much higher computational complexity can be correctly judged in this way, compared to the complexity of functions that can be directly evaluated using ...

---

### 10. FLEX-LBP: Learning Local Binary Patterns with Exact Binary Inference for Texture Classification

**Authors:** Mohamed Alimoussa, Amal El Kaid

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17302v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17302v1)

**Summary:** Local Binary Patterns (LBP) remain among the most widely used texture descriptors, from industrial inspection to medical imaging. Yet their radius, sampling angles, color transform and thresholds are fixed by hand for each dataset. We present FLEX-LBP, which learns these parameters by backpropagation while every forward pass computes exact binary codes and hard histogram counts. A straight-through estimator acts only in the backward pass, so the deployed descriptor is an interpretable hard-binar...

---

### 11. Consistent Video-to-Video Translation via Explicit Correspondences

**Authors:** Gaurav Parmar, Zhengqi Li, Richard Zhang, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17298v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17298v1)

**Summary:** Interactive video-to-video applications require real-time generation while maintaining long-range temporal consistency. However, recent methods achieve speed by restricting attention to a fixed-length causal window. This limits long-range consistency whenever relevant history falls outside the context window. To address this limitation, we introduce vid2vid-long, a correspondence-based approach grounded in a simple observation. Video-to-video translation provides an explicit cross-frame referenc...

---

### 12. Goal Encoding in LLMs

**Authors:** Arnab Sen Sharma, Eric Todd, Sheridan Feucht, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17297v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17297v1)

**Summary:** We investigate whether and how LLMs encode goals: internal neural representations that precede and guide action, and that are flexible enough to be realized through many different execution paths. We construct a coding setting with multiple sub-tasks that allows us to evaluate goal-seeking behavior and the selection of sub-goals. In this setting, we localize an encoding of the next sub-goal in the outputs of a sparse set of attention heads. The same heads can be used to decode the LM's future ac...

---

### 13. Metal Sandbox: Isolated Execution and Command Scheduling for GPU Coding Agents on Apple Silicon

**Authors:** Haozhe Wang, Lina Chen, Fanqi Wan, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17294v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17294v1)

**Summary:** On-device inference requires kernels that make effective use of local accelerators. Efficient training and evaluation of models that generate Apple Metal kernels benefit from native macOS tools and concurrent agent sessions. These sessions alternate between model requests, development commands, and GPU execution, leaving GPU capacity idle for much of a rollout. We present Metal Sandbox, infrastructure that combines restricted per-instance file access, native command execution, and command-level ...

---

### 14. Negative-Only Policy Optimization for One-Sided Verifiable Rewards

**Authors:** Jiacheng Xu, Shuo He, Fuxiang Zhang, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17287v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17287v1)

**Summary:** Reinforcement learning with verifiable rewards (RLVR) typically relies on a verifier that can reliably judge whether sampled solutions are correct. However, in many realistic settings, complete verification is generally unavailable, while cheap checks can only falsify failures. We formalize this regime as one-sided verifiability (OSV): verified negatives are reliable counterexamples, but verified positives are merely non-falsified candidates and may contain many false positives. This asymmetry m...

---

### 15. Programming Quantum Circuit Parameters with Large Language Models

**Authors:** Tiago de Souza Farias, Caio Moraes Porto, Matheus da Silva Fonseca, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17246v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17246v1)

**Summary:** Large language models (LLMs) have recently demonstrated the ability to generate parameters for variational quantum circuits without conventional optimization. However, the conditions under which this approach is effective remain unclear. Here, we investigate a frozen, general-purpose LLM that generates complete circuit parameter vectors from symbolic circuit and Hamiltonian descriptions, with optional iterative energy feedback. We evaluate the approach on general random Hamiltonians, structured ...

---

### 16. Two mathematical models of knowledge distillation

**Authors:** Audrey Xie, Ludwig Schmidt, John Duchi

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17230v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17230v1)

**Summary:** Many hypotheses compete to explain the successes of knowledge distillation. To help address this, we propose and analyze a mathematical model of distillation, which suggests that distillation's performance comes not from obtaining better models but from easier to optimize landscapes. For generalized linear models trained with stochastic gradient descent, we prove that distillation fits performant student models asymptotically more quickly than non-distilled models. In rank-1 matrix approximation...

---

### 17. Linear Regression with Self-Selection Bias in Polynomial Time

**Authors:** Felix Zhou

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17228v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17228v1)

**Summary:** We revisit the problem of estimating $k$ linear regressors with self-selection bias in $n$ dimensions up to error $\varepsilon$ with the maximum self-selection criterion, as introduced by Cherapanamjeri, Daskalakis, Ilyas, and Zampetakis [CDIZ23, STOC]. Our main result is a $\mathrm{poly}(n,k,1/\varepsilon)$ time algorithm for the unknown-index variant of this problem, thereby improving upon the running times of the best known algorithms due to Gaitonde and Mossel [GM24] and Kalavasis, Mehrotra,...

---

### 18. Sheaf-Inspired Structured Scoring Extensions of LightGCN for Collaborative Filtering

**Authors:** Ksenia Belkovskaya, Timur Lidzhiev, Maria Stebliy, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17226v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17226v1)

**Summary:** Graph-based collaborative filtering learns user and item representations by propagating embeddings over a user--item interaction graph. We investigate a modular, sheaf-inspired scoring extension placed on top of a three-layer LightGCN backbone. The motivation comes from cellular sheaves, where local vector spaces are related by linear restriction maps; here, this idea motivates structured, pair-dependent transformations of user and item embeddings rather than a change to graph propagation. We co...

---

### 19. Data Archive for 2D and 3D Electrical Impedance Tomography with moderate conductivity contrast phantoms

**Authors:** S. J. Hamilton, A. Hauptmann, A. Hänninen, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17225v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17225v1)

**Summary:** This document describes open Electrical Impedance Tomography (EIT) measurement data that were collected from biomedical imaging inspired phantoms with moderate conductivity contrasts. The data were collected with the KIT4 and KIT5 EIT measurement devices at the University of Eastern Finland, and are intended for EIT image reconstruction algorithm development and testing. The data from thoracic imaging inspired cylindrical and chest-shaped phantoms are suitable for 2D algorithms, and the data fro...

---

### 20. Combinatorial Bernoulli Factories with Polynomially Many Coins

**Authors:** Renato Paes Leme, Rad Niazadeh

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17223v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17223v1)

**Summary:** We provide an efficient implementation of combinatorial Bernoulli factories. Such a factory turns coins of unknown biases $x$ into a random vertex of a polytope $P$ whose mean is exactly $x$. For every affine slice of the cube (the class of polytopes that admit a factory), we give a single algorithm whose expected number of coin flips and running time at every interior $x$ are polynomial in the dimension and in $1/{δ_*}$, where ${δ_*}=\min_i\{x_i,1-x_i\}$ is never supplied to the algorithm. For ...

---

### 21. Introducing Feedback Delays to Non-Delayed Adversarial MDPs: Optimal $\sqrt S$ and $\sqrt K$ Dependencies in Tabular and Linear AMDPs

**Authors:** Aarush Kulkarni, Khang Nguyen, William Chang, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17214v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17214v1)

**Summary:** We study regret minimization in episodic Adversarial Markov Decision Processes (AMDPs) with unknown transitions and bandit feedback. In tabular AMDPs with $S$ states, $A$ actions, and horizon $H$, the best known $K$-episode regret is $\tilde O(HS\sqrt{AK})$, whose $\sqrt S$ gap to the $Ω(H\sqrt{SAK})$ lower bound has long remained open. In linear AMDPs with $d$-dimensional features, after a five-year line of improvements starting from $K^{14/15}$, computationally efficient algorithms without a s...

---

### 22. Theoretical and Empirical Analysis of Sparse Convolution

**Authors:** Keshvi Tuteja, Yu-Hsiang Tsai, Gregor Olenik, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17212v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17212v1)

**Summary:** Deep neural networks for image processing are increasingly deployed on resource-constrained edge devices such as drones, medical systems, and smartphones, where limited computational resources and memory bandwidth pose significant challenges for efficient inference. Pruning during training often produces highly sparse convolutional kernels, offering the potential to significantly reduce computation and memory requirements. However, exploiting this sparsity efficiently at runtime remains challeng...

---

### 23. Physically Interpretable Basin Selection in Discrete-Variable Origami Design

**Authors:** Lucy Liu, Leon M. Kamp, Katia Bertoldi, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17196v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17196v1)

**Summary:** Automatic differentiation has enabled rapid progress on continuous-variable mechanical design problems, but gradient-based optimization still struggles with discrete variables. The standard approach is to optimize using a continuous relaxation of the choices, then commit to the nearest discrete design at the end. Why this procedure selects unfavorable basins is poorly understood. Here, we introduce a practical, interpretable design problem inspired by origami, in which automatic differentiation ...

---

### 24. Maximizing Capacity Utilization of LoRA Adapters for Mitigating the Learning-Forgetting Trade-off

**Authors:** Tomohiro Sawada, Kartik Goyal

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17191v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17191v1)

**Summary:** Low-Rank Adaptation (LoRA) often underperforms full fine-tuning, especially in heterogeneous and continual-learning settings in which substantial forgetting occurs. In general, it suffers from an undesirable learning-forgetting trade-off across diverse fine-tuning settings. We identify a potential contributor: LoRA adapters, especially high-rank ones, frequently fail to realize the available capacity afforded by the configured rank. Specifically, we find that standard LoRA updates have effective...

---

### 25. Parsed, Plausible, Wrong: Output Format Controls Silent Errors in Small-Model Semantic Parsing

**Authors:** Umar Ahmed, Maxim Dunaev, Mohammad Nour Al Awad, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17169v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17169v1)

**Summary:** A small fine-tuned parser that emits a well-formed but wrong tree fails silently: nothing downstream can tell. We ask whether the output format, a free design choice, controls how often this happens. On the PIZZA ordering benchmark we fine-tune two sub-billion models (Qwen3.5-0.8B and LFM2.5-350M) with LoRA on six lossless encodings of the same target tree, from 44.3 down to 10.9 tokens per order, including two matched-length pairs that vary surface form at fixed length. Across 300 runs (5 train...

---

### 26. Symmetry in Time: A Representation Theory of Linear Recurrent Memory

**Authors:** Anif N. Shikder, Ramit Dey, Jan Minac, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17162v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17162v1)

**Summary:** State space models (SSMs) are an emerging alternative to Transformers. SSMs offer linear-time inference and parallel training, but most implementations make the parallel scan efficient by making the recurrence diagonal: each channel of the hidden state is multiplied by an input-dependent real or complex number. These numbers commute, so the state records which inputs occurred but not their order. We formalize this with representation theory, which explains and fixes the state-tracking failures p...

---

### 27. AeroZoo: A Benchmark of Well-Posed Flow Problems for Foundation Models of Aerodynamics

**Authors:** Peter Sharpe, Carmelo Gonzales, Corey Adams, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17152v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17152v1)

**Summary:** Neural surrogates for computational fluid dynamics (CFD) are trained and ranked on datasets that each vary one design family in one flow domain. Such datasets cannot test the least that an aerodynamic foundation model must do: predict CFD-quality incompressible flow in seconds for new shapes in new enclosures. On DrivAerML, larger models and longer training barely lower Transolver's error; doubling the training cases cuts it by about 12% up to 400 cases, exhausting the dataset. We introduce Aero...

---

### 28. Enhancing Preference Detection using Eye Movement Cascade and Multilayer Combinatorial Fusion

**Authors:** Yuanhong Wu, Mary Tsaryk, Sam Watson, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17145v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17145v1)

**Summary:** Understanding how visual attention influences human preference formation is a fundamental problem in consumer behavior and cognitive science. In this work, we investigate how eye movement patterns can be used to predict preference decisions when subjects compare two alternatives. To address this problem, we analyze an eye-tracking dataset, where subjects view pairs of face images and their gaze behavior is recorded throughout the decision process. We model this problem using multiple machine lea...

---

### 29. A Convex-Analytic Reformulation for Poisoning Attacks on Logistic Regression

**Authors:** Carina Moreira Costa, Maria Eduarda Pinheiro, Martin Schmidt

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17143v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17143v1)

**Summary:** We study data poisoning attacks on logistic regression with $\ell_2$-regularization, where an attacker chooses the features of a fixed number of injected observations with prescribed labels to maximize the logistic loss on the clean training data. Strong convexity of the defender's problem yields an exact reformulation through its first-order optimality conditions. Using convex conjugacy of the softplus function, we replace the sigmoid relations by a single convex optimality-gap inequality and e...

---

### 30. ISLA: A Coordinate-Free, Measure-Weighted Transformer for Boundary-Driven PDEs

**Authors:** Peter Sharpe

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17141v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17141v1)

**Summary:** A foundational principle of physics is that all coordinate systems are equally valid: the behavior of a PDE-governed system does not depend on the origin or orientation of the frame, nor on the units or mesh used to write it down, and neither should a surrogate model. Yet the neural surrogates with the lowest errors on today's aerodynamics benchmarks lack these invariances and fail under simple transformations of the same problem: for models trained on PDEs of cars in one pose (i.e., translation...

---

### 31. Support-Constrained Offline Policy Improvement for Pediatric ECMO from Limited Clinical Data

**Authors:** Fateme Golivand Darvishvand, Saurabh Mathur, Nikhilesh Prabhakar, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17134v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17134v1)

**Summary:** Managing children on ECMO (Extracorporeal Membrane Oxygenation) requires balancing short-term physiological stability with the long-term goal of preventing neurological injury. Standard reinforcement learning can propose risky, out-of-distribution actions, while imitation learning is limited to reproducing clinician behavior. We introduce Support-Constrained Fitted Q-Iteration (FQI-SC), an offline reinforcement learning framework that cautiously improves upon expert behavior by restricting optim...

---

### 32. Paper-Faithful Federated Learning: Scientific Checks for Practitioner and Agent Development

**Authors:** Ali Dadras, Alp Yurtsever

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17129v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17129v1)

**Summary:** Federated learning experiments can produce reasonable-looking results even when the experiment implementation differs from the intended experimental protocol. Small errors in configuration, data partitioning, aggregation, randomness, evaluation, or checkpoint recovery may therefore affect a comparison without causing the program to fail. We present FedBrew, a research codebase for controlled and reproducible federated learning experiments. Its focus is controlled simulation with checks of specif...

---

### 33. STeP-C: Real-Time Neural Compression for Distributed Fiber-Optic Sensing at Scale

**Authors:** Tingfeng Li, Ming-Fang Huang, Shaobo Han, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17126v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17126v1)

**Summary:** Distributed fiber-optic sensing (DFOS) technologies such as Distributed Acoustic Sensing (DAS) generate continuous, high-resolution spatio-temporal data at rates exceeding hundreds of megabytes per second, creating severe challenges for real-time storage and transmission. While neural compression methods can achieve strong rate-distortion performance on sensing data, prior approaches either require per-segment retraining incompatible with streaming, or have only been validated offline. None have...

---

### 34. Using an energy pixels approach to estimate the size a 2nd Generation DEL must be to train a high-resolution binding model

**Authors:** Boris P. Belotserkovskii, R. Edward Watts

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17121v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17121v1)

**Summary:** DNA-encoded libraries (DELs) are commonly used to find small-molecule binders to a target protein. But the hard part is no longer finding a hit. It is building a machine-learning model good enough to guide the medicinal chemistry that follows, one that can resolve the shift in affinity when a chemist changes a single atom. Such a model needs two things from its training data: dense sampling of the small patch of chemical space around the hit, and an adequate number of genuinely tight binders wit...

---

### 35. Bellman Contraction under MMD: A Unified Framework

**Authors:** Baptiste Debes, Tinne Tuytelaars

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17116v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17116v1)

**Summary:** We introduce a mathematical framework for studying contraction of the distributional Bellman operator under Maximum Mean Discrepancy (MMD). We show that contraction reduces to conditional positive definiteness of an associated kernel constructed from the base kernel, which we call the Bellman difference kernel. Focusing on radial kernels, we use Schoenberg's theorem to connect this condition to Bernstein functions. This gives contraction criteria that hold in any dimension and can be verified an...

---

### 36. SALA: Semantically Aligned Latent Actions Enable Dual-Axis Scaling of Embodied Foundation Models

**Authors:** Jiachun Jin, Zetong Zhou, Haonan Wang, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17110v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17110v1)

**Summary:** Embodied foundation models hinge on diverse robot interaction data, which are costly to collect. Egocentric human videos offer a complementary source of experience, and latent action models (LAMs) provide a popular means of leveraging these videos for policy supervision. Compared with world-action models (WAMs), LAMs can offer greater training efficiency and potentially lower inference costs by avoiding explicit pixel prediction during policy learning and execution. However, most existing LAMs l...

---

### 37. Near-Optimal Regret for Oracle-Efficient Adversarial Contextual Bandits

**Authors:** Kiarash Banihashem, MohammadTaghi Hajiaghayi

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17109v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17109v1)

**Summary:** We study contextual bandits with $K$ actions, a class of $N$ policies, and i.i.d.\ contexts from a distribution that the learner can sample. For any sequence of loss functions fixed before play, we give an oracle-efficient algorithm with expected regret $O(\sqrt{KT\log(2N)}\,\log(2KT))$ against the best policy in hindsight on the realized contexts. This improves the $T^{2/3}$ dependence on the horizon in prior oracle-efficient bounds and achieves the optimal regret rate in this setting up to log...

---

### 38. LazyWeights: Decode-on-Demand Edge LLMs

**Authors:** Arnab Sanyal, Gourav Datta, Sandeep P. Chinchali

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17108v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17108v1)

**Summary:** Memory decides which LLMs an edge device runs, and how fast: capacity on a $4$ GB Jetson Nano, bandwidth on an $8$ GB Jetson Orin Nano Super. Deployed formats (GPTQ, AWQ, $\texttt{llama.cpp}$'s K- and I-quants) spend equal bits on every integer code of a matrix, although the codes are far from uniform. $\texttt{LazyWeights}$ keeps these formats but tunes GPTQ so the codes compress, Huffman-codes them losslessly in interleaved lanes, and decodes them on demand in a small unit between DRAM and L2,...

---

### 39. Joint Null-Space Projection for Data-Free Model Merging

**Authors:** Tian Xia

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17103v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17103v1)

**Summary:** Merging independently fine-tuned checkpoints into a single multi-task model requires no data, no labels, and no gradient steps. In practice the task vectors of different tasks interfere, and the standard remedies--averaging, magnitude pruning, sign election--operate entry by entry, ignoring that each delta induces a low-dimensional update on the hidden features it acts upon. We recast merging as a subspace interference problem. For every two-dimensional weight tensor we take the top-r right-sing...

---

### 40. Reasoning Supervision and Capability Retention in LoRA Domain Adaptation

**Authors:** Saleh Ashkboos, Dhruv Desai, Lavinia Ghita

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17072v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17072v1)

**Summary:** Fine-tuning foundation models on financial data has a wide range of applications, including identifying event types from news, monitoring risk and compliance language, and answering questions over filings and earnings calls. In this setting, the main challenge is to improve task performance without degrading the generalization capabilities of the model. In this paper, we present an extensive set of ablations for fine-tuning Qwen3-8B with low-rank adaptation (LoRA). We compare three training regi...

---

### 41. An Invariant Neural-Network Eddy-Viscosity Closure with Iterative Solver Coupling for Molten Salt Fast Reactor Thermal-Hydraulics

**Authors:** Zaid Abulawi, William Oliveira, Akzhol Almukhametov, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17067v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17067v1)

**Summary:** System thermal-hydraulics codes such as the System Analysis Module (SAM) close turbulence on coarse meshes with algebraic zero-equation mixing-length models. These models cannot represent the non-equilibrium turbulence, flow separation, and large-scale recirculation of open-cavity advanced reactors. We develop an invariant neural-network eddy-viscosity closure for SAM and apply it to the Molten Salt Fast Reactor (MSFR). The closure predicts the turbulent kinetic energy and timescale of each elem...

---

### 42. Capacity-Constrained Delayed Feedback for Online Conformal Risk Control

**Authors:** Bowen Wang, Osvaldo Simeone

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17059v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17059v1)

**Summary:** Online conformal risk control (OCRC) enables reliable uncertainty quantification in machine learning by converting model outputs into prediction sets with long-term risk guarantees. These guarantees, however, hinge on the assumption that the loss of each round is revealed immediately and losslessly. In practice, feedback may be delayed, and limited resources may prevent tracking all pending predictions, causing some feedback to be lost. To address this challenge, we develop capacity-aware OCRC (...

---

### 43. Evaluating Pretrained Language Semantics for Structured EHR Prediction Tasks

**Authors:** Ashvin Gupta, Brendan Delaney, Alessandra Russo

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17053v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17053v1)

**Summary:** Structured Electronic Health Records (EHR) models typically treat each clinical concept as a dataset-specific token, discarding the natural-language semantics associated with the event. As a result, relationships between concepts must largely be learned from EHR co-occurrence, without directly exploiting any prior semantic knowledge. We investigate how pretrained causal language models can be adapted for longitudinal EHR prediction by developing tEHR. Here, we represent events with their natural...

---

### 44. Infrastructure for Verifiable AI: Where Proof Costs Go and How Hardware Can Help

**Authors:** Yihan Xia, Wenxin Xu, Taotao Wang

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17042v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17042v1)

**Summary:** Users of artificial intelligence services, including those powered by large language models and other transformer-based models, need assurance that inference and training follow the declared computation without exposing private models or data. Zero-knowledge proofs can provide this assurance, but proof generation remains expensive. Hardware acceleration research often reports gains for individual cryptographic operations, leaving their effect on the full cost of proving neural-network workloads,...

---

### 45. Prevalence Bounds for Edited Watermarked Text: Power Envelopes and Calibration Sensitivity

**Authors:** Kuancheng Ye

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17035v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17035v1)

**Summary:** Watermark detectors decide whether one document came from a watermarked language model. Auditors often need a different number: the share of a corpus that did. We study this share for Gumbel-max and green-list (KGW) watermarks when every document may have been edited by an unknown amount. Without restrictions on the edits, the upper end of the identified set is 1. Combining a known least-favourable next-token distribution with a sequential coupling, we derive a power envelope indexed by three bu...

---

### 46. Temporal Regularized Learning: Self-Supervised Learning Local in Space and Time

**Authors:** Davide Wiest

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17019v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17019v1)

**Summary:** Layer-local self-supervised objectives remove the backward pass between layers, but almost all still compute their loss over a batch of samples and are therefore local in space but not in time. We introduce Temporal Regularized Learning (TeReL), a spatially and temporally local learning rule for self-supervised representation learning from sequential input streams. The key idea is to instantiate a VICReg-style objective with temporally adjacent positives and non-differentiated running population...

---

### 47. Random Exploration is Random

**Authors:** Yingkang Luo, Hua-Dong Xiong, Hanbo Xie, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17011v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17011v1)

**Summary:** Decision making often requires balancing exploitation of familiar options with exploration of uncertain alternatives. One strategy for exploration is random exploration, in which choices become more variable and less tied to the option that currently appears best. However, it remains unclear whether this variability reflects genuine stochasticity or instead a deterministic structure that traditional cognitive models fail to capture. We examined this question using the Horizon Task in an aggregat...

---

### 48. An Integrated Architecture for Data-Efficient Real-Time Neural Imitation of Nonlinear Time-Optimal Model Predictive Control

**Authors:** Maarten De Baecke, Flavia Sofia Acerbo, Andrea Giusti, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17005v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17005v1)

**Summary:** Nonlinear time-optimal model predictive control (TOMPC) enables highly performant control of constrained systems, but its computational cost prohibits real-time use on fast dynamical systems. Neural network imitation of the TOMPC control law can reduce online computational costs, yet existing work mostly targets quadratic cost formulations in simulation and addresses the challenges of neural controllers in isolation. This work imitates a long-horizon nonconvex TOMPC with hard terminal constraint...

---

### 49. Compiling Known Rules into Compact Neural Agents: Weight-Space Programming on Unseen Games

**Authors:** Jens Lehmann

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16981v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16981v1)

**Summary:** Weight-space programming (WSP) uses language models to construct neural network weights without training. We test whether known game mechanics can be compiled into compact agents that generalise to held-out levels, renderings and start states within a game family. Writers receive simulator source with held-out level data removed for 20 privately authored, unpublished ARC-AGI-3-style game families. With a fixed 57k-parameter recurrent architecture, the strongest writer reaches 56% held-out-level ...

---

### 50. Time Flies When You Parallelise: Pareto-efficient Time Series Foundation Models with Linear Recurrences

**Authors:** Torben Berndt, Lingyi Yang, Federico Nardi, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16934v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16934v1)

**Summary:** Time series foundation models have demonstrated strong zero-shot forecasting performance, but computational efficiency remains a central architectural challenge. Temporal self-attention incurs quadratic cost in the number of temporal tokens, while nonlinear recurrent state transitions restrict parallel computation along the temporal dimension. We introduce ci-proto, a family of time series foundation models based on Mamba-3, whose linear state recurrences support chunk-wise parallel-in-time comp...

---

## cs.NE

**50 papers**

### 1. Symmetry in Time: A Representation Theory of Linear Recurrent Memory

**Authors:** Anif N. Shikder, Ramit Dey, Jan Minac, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17162v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17162v1)

**Summary:** State space models (SSMs) are an emerging alternative to Transformers. SSMs offer linear-time inference and parallel training, but most implementations make the parallel scan efficient by making the recurrence diagonal: each channel of the hidden state is multiplied by an input-dependent real or complex number. These numbers commute, so the state records which inputs occurred but not their order. We formalize this with representation theory, which explains and fixes the state-tracking failures p...

---

### 2. Similarity-Guided Optimization Strategies for Approximate Network Symmetry Detection

**Authors:** David Hartman, Jaroslav Hlinka, Dominik Klepl, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16555v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16555v1)

**Summary:** Symmetry in complex networks is a structural property with broad implications for network function, dynamics, and robustness. While classical approaches rely on exact automorphisms and thus remain highly sensitive to small perturbations, recent work of Liu has introduced approximate formulations that relax the strict invariance condition and recast symmetry detection as an optimization problem over permutations. We investigate how node-level similarity information can be used to bias the search ...

---

### 3. A Finite Markov Chain Analysis of the Simplified Swarm Optimisation Update Rule

**Authors:** Wei-Chang Yeh

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16541v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16541v1)

**Summary:** Simplified swarm optimisation (SSO) updates each variable by one draw that copies the global or personal best, keeps the current value or redraws uniformly, with probabilities $c_g$, $c_p$, $c_w$ and $c_r$. As a finite Markov chain under frozen memory, its coordinate kernel $c_w I + (1 - c_w)Π$ has an explicit stationary law and exact convergence rate $c_w^t$. The elitist chain has a geometric hitting-time bound, from a non-optimal start a fixed $c_r$ needs at least $\exp(nc_r/2)$ expected evalu...

---

### 4. Optimal feature selection for firewall log analysis using Machine learning and Hybrid Metaheuristic algorithms

**Authors:** Seungwoo Han, Gil Hong, Jewan Kim, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16239v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16239v1)

**Summary:** Firewall log classification is important to monitor network traffic. Machine learning classifiers using network-related features have shown good results for this task, but high-dimensional features slow down classification. In this paper, we apply feature selection using bee swarm optimization with Q-learning-based local search (QBSO-FS) to the UCI Internet Firewall Data Set, together with random forest (RF), k-nearest neighbor (KNN), and Bernoulli naïve Bayes (Bernoulli NB) classifiers. The fir...

---

### 5. Pyramidal Columns Acting as Attention Heads

**Authors:** Fabrizia Giulia Garavaglia, Marco Giunti

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.16057v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16057v1)

**Summary:** Can the functional architecture of a Transformer attention head be given a biological construction? More specifically, could a suitable group of pyramidal columns in posterior temporal language regions (PTLRs) constitute the biological construction of a neuromorphic mechanical realization of an attention head, under a mathematical instantiation that need not coincide with its standard Transformer instantiation? This paper investigates this hypothesis by examining possible correspondences between...

---

### 6. Runtime Analysis of Cartesian Genetic Programming on Max: A Proven Exponential Speedup

**Authors:** Duc-Cuong Dang, Roman Kalkreuth, Andre Opris

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.16013v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16013v1)

**Summary:** Genetic Programming (GP) is a search paradigm inspired from natural evolution for the automated discovery of expressions, functions, and computer programs. Cartesian GP (CGP) is a flavor of GP that uses a graph-based model to encode candidate programs, as contrasted to the conventional Tree-based GP (TGP). Since its inception two decades ago, CGP has predominantly been analyzed empirically, thus little is known regarding its theoretical performance guarantees. This paper analyzes CGP for the Max...

---

### 7. Contour-Assisted Evolutionary Computation: Estimating Peaks From the Contour Lines of Evaluated Solutions

**Authors:** Jun Zhang, Tong Qian, Hua Ding, et al.

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.15641v1) | 📄 [PDF](https://arxiv.org/pdf/2611.15641v1)

**Summary:** Evolutionary algorithms (EAs) evaluate many candidate solutions but use them mainly to rank individuals. This paper treats the evaluated solutions as the spot heights of a topographic survey and draws the contour lines they imply. The contour map decomposes the evaluated region into peaks: in two dimensions a contour tree with persistence separates significant peaks from interpolation ripples, and in more dimensions hill climbing on the interpolated surface locates the peaks and ray-cast level s...

---

### 8. An Approach to Hinton's Mother-Child Proposal: Neural Networks Learning and Preserving Care in a Finite World

**Authors:** Csaba Balogh

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.15523v1) | 📄 [PDF](https://arxiv.org/pdf/2611.15523v1)

**Summary:** Hinton proposed that artificial intelligence should be given "maternal instincts" and relate to us as a mother to her child. We argue that care must first be learned, with the network itself as the child. We construct this upbringing in a finite world and study whether care survives the mother's departure, new situations and further learning. The mechanism combines a vocabulary of harm, a learned measure of future acceptability and an execution veto. A finite role certificate supports transfer w...

---

### 9. Matrix-Based Ant Colony Search with Batched Decoding for Hierarchical Replenishment Routing: A Stylized Case Study Based on Korean City Data

**Authors:** Jun Zhang, Wei-Jie Yu, Tong Qian, et al.

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.15338v1) | 📄 [PDF](https://arxiv.org/pdf/2611.15338v1)

**Summary:** We study a stylized single-vehicle replenishment-routing problem in which the cities of a national logistics network are both demand points and supply points: a vehicle of limited capacity delivers to every city once, and when its load is insufficient for the next city it must detour to a city already served that can still supply goods. A 100-node benchmark is built from Korean population and geographic data, with the cities divided into 10 levels; the per-visit supply coefficient and the allowe...

---

### 10. A Multi-Parent Edge Assembly Crossover Driven Hybrid Genetic Algorithm for the Hamiltonian \textit{p}-Median Problem

**Authors:** Junkai Huang, Pengfei He, Jin-Kao Hao, et al.

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.15219v1) | 📄 [PDF](https://arxiv.org/pdf/2611.15219v1)

**Summary:** The Hamiltonian \textit{p}-median problem seeks to partition the vertices of a graph into exactly $p$ disjoint cycles while minimizing their total cost. This paper presents a hybrid genetic algorithm incorporating a multi-parent edge assembly crossover operator. The crossover combines a base solution with multiple donor solutions in a single recombination operation, thereby expanding the space of available edge exchanges. It uses virtual copies of the base solution to establish edge balance, tog...

---

### 11. DeNA-SGN: Deterministic Neighborhood Aggregation for Verified Spiking Graph Inference

**Authors:** Sanjay Das, Xi Zhang, Emily Herron, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14775v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14775v1)

**Summary:** Graph learning on neuromorphic substrates requires an explicit spiking realization of neighborhood aggregation, supporting control and classification. We propose DeNA-SGN, which combines fixed OR and tie-inclusive Majority aggregation of binary node features with a learned signed-weight threshold classifier. A degree-dependent inhibitory construction implements Majority through shared control neurons, enabling a complete circuit compilation into SuperNeuroMAT. Across seven datasets and 41 mapped...

---

### 12. Galop: Billion-Scale Genetic Programming on a Single GPU

**Authors:** Xavier Hill Roy, Stephen Kelly

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14665v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14665v1)

**Summary:** Genetic programming (GP) evolves populations of heterogeneous programs, whereas GPUs achieve their highest throughput when groups of threads execute the same instructions. To better align GP evaluation with GPU execution, we present Galop, a hybrid CPU-GPU linear GP system that assigns one individual to each CUDA warp, a group of 32 threads that execute the same instructions across different fitness cases. We compare Galop against EvoGP, a recent high-performance GPU-based tree GP system, on dat...

---

### 13. Recurrent Modular Structure in Spiking Neural Network Reinforcement Learning

**Authors:** Vikram Ramavarapu, Himanshu Udupi, Ashish Gautam

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14262v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14262v1)

**Summary:** Biological neural circuits are both modular and recurrent, with dense communities sparsely linked to one another. Spiking neural networks (SNNs) for reinforcement learning are usually feed-forward, and it is unclear how to obtain functional modules in a recurrent SNN or what they buy. In this work, we introduce a class of spiking networks, called Community Recurrent SNNs (CoRe SNNs): recurrent networks partitioned into communities with fixed roles. A controller community receives the stimulus, e...

---

### 14. Tailoring Optimization Approaches with Domain Knowledge in Industry Process for Meta-heuristic Development

**Authors:** Jakub Cebula, Konrad Gmyrek, Paweł B. Myszkowski, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13940v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13940v1)

**Summary:** The paper presents an Industry Process for Meta-heuristic Development (IPMD) schema, a systematic methodology for applying meta- and hyper-heuristic applications to optimization problems. In this context, we present a case study of Balancing Non-dominated Tournament Genetic Programming (BNTGP) applied to solve two NP-hard multi-objective optimization problems: routing (Capacitated Vehicle Routing Problem with Time Windows) and scheduling (Multi-Skill Resource Constrained Project Scheduling Probl...

---

### 15. Oscillatory Processing Units as a computing substrate for biomimetic intelligence

**Authors:** Alexander A. Wolf

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13840v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13840v1)

**Summary:** Biological intelligence emerges from neural activity that connects sensation, memory and action. Synaptic plasticity, neuronal assemblies and oscillations provide principles for biomimetic computing, but translating them into reusable operations requires a defined computational unit. We introduce Oscillatory Processing Units (OPUs), groups of synthetic neurons sharing a rhythm. Their directed interactions transform incoming activity and prior receiving state into an Oscillatory Occupancy Space (...

---

### 16. A Functional Preservation Score for Auditing Connectome Operations: Compression, Alignment, Transport, and Local-Rule Writing

**Authors:** Praveg Vashishtha

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13681v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13681v1)

**Summary:** We introduce the Functional Preservation Score (FPS), a null-normalised, behaviourally grounded measure of how much of a neural network's input-output function survives a structural operation, and use it to audit the operations underlying speculative "mind-migration" pipelines on public data that runs on a single laptop. Across five pre-registered studies on the C. elegans connectome, whole-brain calcium activity, and hippocampal replay, FPS yields two positive characterisations and a three-part...

---

### 17. Reconstructing Boundary Layer Wind Profiles with Machine Learning: A Comparative Study on IGRA Radiosonde Data

**Authors:** Fedor Buzaev, Dmitry Efremenko, Daria Pugacheva, et al.

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.13359v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13359v1)

**Summary:** Wind profiles in the atmospheric boundary layer (ABL) drive short-range forecasting and wind-energy siting, yet sparse radiosonde coverage forces practitioners to interpolate them from a handful of physical predictors. We benchmark modern tabular learners against analytical parameterizations on 158,097 IGRA soundings. CatBoost, TabM, and FT-Transformer reduce RMSE to 1.3-1.6 m/s, against approximately 3 m/s for power-law and Monin-Obukhov fits; once the predictor set is fixed the three architect...

---

### 18. Making Strides in Symbolic Imitation Learning: Offline Demonstrations, Online Tuning

**Authors:** Bryce MacInnis, Malcolm I. Heywood

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.13182v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13182v1)

**Summary:** Deep reinforcement learning (DRL) methods have been the dominant paradigm in continuous control tasks due to their efficacy in function approximation, while interpretable evolutionary methods have lagged largely behind for the opposite reason. In this work, we introduce Symbolic Imitation Learning, a framework for distilling an oracle policy through an offline dataset into a decision list with linear model motion primitives. We show that this, in conjunction, with online Augmented-Random Search ...

---

### 19. Pricing Symbolic Rules by What GNNs Leave Unlearned

**Authors:** Satabarto Sarkar, Prithwineel Paul

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12446v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12446v1)

**Summary:** Symbolic knowledge (motif counts, ring counts, label constraints) is routinely added to graph neural networks (GNNs) and justified by their limited expressivity. We replace this yardstick with an exact one. The largest log-loss reduction a rule $S$ can give a model family is $I(Y;S\midσ)$ given what the family computes; every realised gain splits exactly into this term plus repaid neural debt; and for a trained network with representation $T$ the value is $I(Y;S\mid T)$, the label information tr...

---

### 20. Maximizing Detection Probability in UAV Search Missions using Random-Key Optimizers

**Authors:** Antonio Dantas, Elcio Shiguemori, Antonio Chaves

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12317v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12317v1)

**Summary:** This paper focuses on the stochastic and real-time constraints of Unmanned Aerial Vehicle (UAV) path planning in Search and Rescue (SAR) missions. We introduce a configurable data-driven and intelligent routing architecture that combines a closed-loop probability update with the Random-Key Optimizers (RKO). Our problem is mathematically modeled as a dynamic probabilistic variant of the Open Vehicle Routing Problem (OVRP), enabling the solver to switch adaptively between two objectives, thereby b...

---

### 21. A method to automatically discover symbolic local learning rules

**Authors:** Andrea Perin, Fabio Anselmi, Stephane Deny

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12248v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12248v1)

**Summary:** We present a general method for discovering symbolic local learning rules that can replace backpropagation, applicable, in principle, to any deep learning architecture and task. The method automatically discovers local loss functions specific to each layer by (1) constructing a dictionary of monomials of local tensor variables, inspired by Penrose diagram notation, (2) regressing over coefficients weighting these monomials to build layerwise polynomial losses whose gradients together minimize a ...

---

### 22. AscendMOEA: An Ascend NPU-Accelerated Platform for Tensorized Multi-Objective Evolutionary Algorithms

**Authors:** Qianlong Dang, Zhiyang Zhang, Baosheng Li, et al.

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12057v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12057v1)

**Summary:** Multi-objective evolutionary optimization increasingly involves large populations, expensive problem evaluations, and diverse algorithmic structures. These workloads expose the limited parallelism of loop-based implementations, while rewrites for accelerator execution can alter selection order, tie handling, and population updates. AscendMOEA is presented as a scalable platform that executes multi-objective evolutionary algorithms (MOEAs) on Huawei Ascend neural processing units (NPUs) and conve...

---

### 23. Attention Is Only as Good as Its Witnesses: When Higher-Order Layers Help, and When They Do Not

**Authors:** Mostafa 'Neo' Mohsenvand

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.11937v1) | 📄 [PDF](https://arxiv.org/pdf/2611.11937v1)

**Summary:** Transformers stop learning graph search as graphs grow, and learn the card game SET only after many distinct questions, although attention can represent both. We read these failures, and the uneven record of higher-order attention, from what a layer sums over: each layer we study computes the partition function of a family of witnesses and reads it at a temperature. Two laws follow. The depth law is a known result of logic, which we state for these layers: L layers over two-step walks reach exac...

---

### 24. Understanding Spike Encoding across IoT Sensing Modalities: An Empirical Study

**Authors:** Yuxuan Hou, Di Yu, Linshan Jiang, et al.

**Published:** 2026-11-08

🔗 [Paper](http://arxiv.org/abs/2611.11317v1) | 📄 [PDF](https://arxiv.org/pdf/2611.11317v1)

**Summary:** Spiking neural networks (SNNs) offer a path to energy-efficient sensing on Internet of Things (IoT) devices. The input encoder shapes that opportunity by changing the cues available for recognition and the work required to process them. We study these choices across wireless, inertial, surface electromyographic, and tactile sensing. For wireless activity recognition, interleaving reduces estimated energy for arithmetic in the network layers, latency from the prepared input window to returned sco...

---

### 25. Neural Activity Synchronization-Based Fast Local Learnable Spiking Neural Network Architecture

**Authors:** Pranith Dutta, Sk Wasim Rajjak, Siddhanta Ray, et al.

**Published:** 2026-11-08

🔗 [Paper](http://arxiv.org/abs/2611.11053v1) | 📄 [PDF](https://arxiv.org/pdf/2611.11053v1)

**Summary:** Implementing intelligent learning systems on low- power edge devices is challenging due to the high compu- tational complexity, training latency, and energy demands of traditional Artificial Neural Networks (ANNs). Spiking Neural Networks (SNNs), biologically plausible and spike-driven, come as an alternative. However, SNN training commonly relies on backpropagation through time (BPTT), which is computationally expensive, inherently global, and unsuitable for battery-driven devices. This work pr...

---

### 26. The forces at hand: social learning is permissive, not instructive, for the evolution of phenotypic plasticity

**Authors:** Nam H. Le

**Published:** 2026-11-07

🔗 [Paper](http://arxiv.org/abs/2611.10986v1) | 📄 [PDF](https://arxiv.org/pdf/2611.10986v1)

**Summary:** Evolution can favour a trait for two reasons: an instructive cause makes selection favour the trait; a permissive one lets it persist once selection no longer removes it. The distinction matters most for phenotypic plasticity and its replacement by inherited behaviour, genetic assimilation, the Baldwin effect. Social learning is credited with favouring plasticity on evidence that cannot tell the two apart: how much plasticity remains at the end of a simulation. Here we show, analytically and com...

---

### 27. Bridging Spiking and Continuous Dynamics in Spiking Neural Networks: A Muscle-Inspired Model

**Authors:** Maryam Soltani, Philip N. Garner

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09295v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09295v1)

**Summary:** Transforming the spike trains produced by spiking neural networks (SNNs) into continuous signals through biologically inspired mechanisms remains an open challenge in generative and regression tasks. In biological systems, a similar transformation occurs when muscles integrate neural spikes to produce smooth, coordinated movements. Inspired by this mechanism, we introduce a muscle-response model, a biologically motivated dynamical layer that converts spike trains into continuous representations....

---

### 28. OMCDE: Opposition-based Multi-Stage Matrix-Based Competitive Differential Evolution

**Authors:** Mohammad Sarhangzadeh, Shahryar Rahnamayan, Doruk Oner

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09167v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09167v1)

**Summary:** Differential Evolution has proven to be an effective algorithm for continuous global optimization, but it's modern high-performing variants often introduce additional complexity and computational cost. We propose OMCDE, a matrix-based competitive Differential Evolution algorithm that aims to improve optimization performance while maintaining computational efficiency. The proposed approach integrates competition-driven search dynamics, adaptive behavior between optimization stages, and opposition...

---

### 29. Circuit Theory-Informed AI for Condition Monitoring in Power Electronics

**Authors:** Yubo Song, Pascal A. Schirmer, Subham Sahoo

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09141v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09141v1)

**Summary:** Artificial intelligence for power electronics is evolving toward a deeper comprehension of system intrinsic behaviors and dynamics. As a novel integration of neural computation and electric circuits, spike-based neuromorphic computing offers promising potential in high energy efficiency and adaptability for data-driven applications. Building on the latency-coding principles, this article proposes a framework for data-light condition monitoring that relies solely on three-phase AC current measure...

---

### 30. Two-Layer Evolutionary Scheduling for Machine Learning Jobs in Multi-Cluster Environments

**Authors:** Jingyuan Xu, Changwu Huang, Lemeng Pan, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09093v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09093v1)

**Summary:** The rapid growth of large-scale machine learning (ML) workloads has led to unprecedented demands on GPU cluster scheduling systems. However, existing heuristic schedulers struggle to handle the complexity and dynamics of multi-cluster GPU environments, often leading to load imbalance, long queuing delays, and poor alignment to business objectives. This paper formulates the ML scheduling problem in multi-cluster GPU environments as online multi-objective optimization that minimizes the average an...

---

### 31. SwarmEvolve: Latent Agent Swarms for Evolutionary Discovery and Optimization

**Authors:** Qile Jiang, George Em Karniadakis

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.08483v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08483v1)

**Summary:** LLM-guided evolutionary search uses AI agents to improve programs for mathematical and computational problems by iteratively refining solutions and combining high-scoring methods. However, the process is often slow because the LLM generates a long textual chain of thought for each round and must repeat this generation many times to maintain population diversity. We present SwarmEvolve, a framework in which hundreds of low-cost agents per round work in swarms, reason in latent space without decod...

---

### 32. Invariance before structure: two modes of emergent compression in representation learning

**Authors:** Hardik Rajpal, Dan Goodman

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.07952v1) | 📄 [PDF](https://arxiv.org/pdf/2611.07952v1)

**Summary:** Learned representations show striking invariance across biological and artificial neural networks, with different substrates and variations driven by drift, heterogeneity and initialisation. To understand this invariance, we propose Emergent Adaptive Representation Learning (EARL), a framework that distinguishes two modes of emergence in learned representations: state-space compression, where a learned representation gains predictive power over its own future beyond what the network's units can ...

---

### 33. Projection-Free Gradient Tracking Neurodynamic for Distributed Nonnegative Sparse Optimization

**Authors:** Juntao Li, Qihang Guo, Deyuan Meng

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.07643v1) | 📄 [PDF](https://arxiv.org/pdf/2611.07643v1)

**Summary:** This paper proposes a continuous-time, projection-free neurodynamic system based on gradient tracking for distributed nonnegative sparse optimization. Unlike traditional methods, our approach avoids projecting states onto the feasible set. Instead, it employs gradient tracking to estimate average gradients under heterogeneous costs, coupling primal and dual dynamics such that feasibility and sparsity emerge naturally from the equilibrium conditions. The system ensures unique solutions through a ...

---

### 34. When Does Blockwise Additivity Break? Diagnosing and Repairing the Additive Assumption in Distillation-Based Architecture Search

**Authors:** Yuefeng Xu, Jun Yu

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.07487v2) | 📄 [PDF](https://arxiv.org/pdf/2611.07487v2)

**Summary:** Blockwise distillation methods for architecture search, such as DNA, DONNA, LANA and Puzzle, score each candidate replacement block in isolation and combine the scores additively. We ask at which budgets this additivity assumption fails, whether fine-tuning repairs the failure, what diagnoses it, and how it can be repaired cheaply. On DeiT-S, DeiT-B, Swin-T and Qwen2.5-0.5B with seven latency budgets each, an additive integer program trails a pairwise interaction-aware program after fine-tuning ...

---

### 35. Learning Time-Varying Connectomes for Stable Behavior Across Development

**Authors:** Christof Fehrman, Jacob J. Morra, Eva A. Naumann

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06895v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06895v1)

**Summary:** Neural circuits must maintain functionality to drive effective behavior while their size, topology, geometry, and intrinsic dynamics change across development. To model developing visuomotor circuits and behavior, we investigated whether a single compact generative encoding could produce functional recurrent controllers across such changes. Building on the HyperNEAT algorithm, we represented this program as a compositional pattern-producing network that received developmental time as an input to...

---

### 36. Adaptive Multi Mode: Budget-Aware Routing of Optimizers By Online Landscape Probes

**Authors:** Benjamin Jacob Bodner

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06879v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06879v1)

**Summary:** The best classical optimizer for a continuous black-box problem depends on its budget and landscape. Existing routers decide from the dimension and budget, past improvement or features fitted to one benchmark, and few test an optimizer's implicit assumptions online. AMM (Adaptive Multi Mode) routes a known budget among quasi-Newton, trust-region, coordinate, multistart and evolution-strategy optimization engines with online probes of curvature, plateaus, separability, kinks, basins and fractal s...

---

### 37. SpikePose: Lightweight Video Human Pose Estimation

**Authors:** Yunhao Huang, Kaushik Bhargav Sivangi, Tianyi Yu, et al.

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06594v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06594v1)

**Summary:** Efficient video human pose estimation must balance localisation accuracy, motion quality, and energy cost. We present SpikePose, a lightweight video pose estimator that pairs a frame-reset, single-step spiking encoder with motion-aligned heatmap memory (MAM). The encoder supplies per-frame spatial evidence, while MAM estimates joint displacement, aligns historical heatmaps, and adaptively fuses them with current predictions. By confining temporal reasoning to a compact, lightweight module outsid...

---

### 38. From Admission to Retention: Predicting Durable Offspring in Quality-Diversity Search

**Authors:** Corrado Calamita, Matteo Mendicini, Luca Ferrari, et al.

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06522v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06522v1)

**Summary:** Automated failure discovery can be framed as a diversity problem: the objective is to expose distinct ways a system fails rather than a single critical adversarial case. Yet uniform parent sampling provides no way to allocate search effort toward individuals likely to produce durable archive contributions. We study this credit assignment problem in an unstructured Quality-Diversity (QD) archive, testing whether signals available before an individual has reproduced distinguish offspring that mere...

---

### 39. Multi-Resident Data Association in Smart Homes via MDP Modeling and Behavior Cloning

**Authors:** Xi Chen, Julien Cumin, Fano Ramparany, et al.

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06296v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06296v1)

**Summary:** Ambient sensors offer a privacy-preserving solution for activity recognition in smart homes, yet they face a critical challenge in multi-resident environments known as Data Association, which aims to identify the resident triggering a specific anonymous sensor event. Existing approaches fundamentally fail to maintain global consistency by often yielding conflicting associations for silent residents. Additionally, these methods frequently suffer from severe trajectory fragmentation caused by the ...

---

### 40. Explainable Anomaly Detection in 5G Networks through Continuous Time Graphs

**Authors:** Thomas Hoger, Philippe Owezarski

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06225v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06225v1)

**Summary:** 5G networks increasingly resemble distributed systems in their design. It then becomes crucial to move beyond traditional network-based detection methods and to explore alternative approaches. In this work, we propose a formalization of 5G network exchanges as a dynamic graph, on which we apply techniques from the field of graph-based learning to detect anomalies effectively. This representation allows for fine-grained analysis of packet-level semantic content, while simultaneously capturing seq...

---

### 41. Mobility-Aware Mobile Edge Computing for Energy-Balanced Data Collection in IoT-Enabled Underwater Sensor Networks

**Authors:** Nguyen Thi My Binh, Do Dinh Hoan, Tong Tien Manh, et al.

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06186v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06186v1)

**Summary:** Underwater wireless sensor networks (UWSNs) face critical challenges in energy imbalance, connectivity, and data collection due to harsh environments. To address these issues, this paper focuses on the problem is how to achieve energy-balanced data collection in IoT-enabled UWSNs with a mobility-aware mobile edge computing (MEC), named MECEBDC. Unlike existing approaches, the proposed scheme jointly optimizes energy-aware clustering, cluster head selection, and AUV-assisted data collection. Furt...

---

### 42. Neural networks and games

**Authors:** Philip R. Neary

**Published:** 2026-11-03

🔗 [Paper](http://arxiv.org/abs/2611.05706v1) | 📄 [PDF](https://arxiv.org/pdf/2611.05706v1)

**Summary:** Hopfield neural networks and noncooperative games provide seemingly different approaches to understanding how collective outcomes emerge from local interactions. In a neural network, individual units adjust their states according to local signals; in a game, players choose actions to maximise individual payoffs. I establish an exact equivalence between symmetric binary Hopfield networks and binary-action games that admit a quadratic potential. The equivalence identifies stable network configurat...

---

### 43. Learning Behaviorally Relevant Dynamics in Multimodal Neural Recordings

**Authors:** Parastoo Azizeddin, Eray Erturk, Maryam M. Shanechi

**Published:** 2026-11-03

🔗 [Paper](http://arxiv.org/abs/2611.05167v1) | 📄 [PDF](https://arxiv.org/pdf/2611.05167v1)

**Summary:** Multimodal neural data can enable a more complete understanding of brain dynamics underlying behavior. Modalities such as spiking activity, local field potentials (LFPs), and behavior capture diverse spatiotemporal aspects of brain processes, yet prior neural-behavioral models that separate sources of variability rely on a single neural modality. By leveraging these complementary strengths, multimodal neural fusion can provide a unified, rich representation of brain-behavior processes and addres...

---

### 44. Solving the Nonlinear Westervelt Equation in Ultrasound Propagation Using Physics-Informed Neural Networks

**Authors:** Luke Oluwaseye Joel

**Published:** 2026-11-03

🔗 [Paper](http://arxiv.org/abs/2611.05130v1) | 📄 [PDF](https://arxiv.org/pdf/2611.05130v1)

**Summary:** Modeling the nonlinear acoustic wave propagation in biological tissues needs accuracy, especially in ultrasound imaging and therapeutic applications. The 1D Westervelt equation, \( p_{xx} - p_{tt} + γ\, p_{ttt} + η\,(p^{2})_{tt}=0, \) could be used to describe a finite-amplitude ultrasound propagation in these tissues. This equation accounts for nonlinearity, \(η\), and attenuation, \(γ\). To solve this equation, we observe that traditional solvers may struggle to do so correctly. This is due to...

---

### 45. Refined CMA-ES for CEC 2026 Bound-Constrained Single-Objective Optimization

**Authors:** Adam Stelmaszczyk, Rafał Biedrzycki, Jarosław Arabas

**Published:** 2026-11-03

🔗 [Paper](http://arxiv.org/abs/2611.04620v1) | 📄 [PDF](https://arxiv.org/pdf/2611.04620v1)

**Summary:** We present a simplified and parameter-adjusted variant of CMA-ES designed for the CEC 2026 Bound-Constrained Single-Objective Optimization competition. Unlike typical algorithmic developments that increase complexity by adding mechanisms, Refined CMA-ES systematically removes components that do not improve performance, such as the flat-land escape, while retaining standard features that provide measurable benefits. Adjusting key parameters (population size and initial step-size) yields substanti...

---

### 46. An ensemble of graph generative models for assisted history matching of the Brugge field case

**Authors:** Gleb Shishaev, Anton Shirokov, Shadfar Davoodi, et al.

**Published:** 2026-11-03

🔗 [Paper](http://arxiv.org/abs/2611.12927v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12927v1)

**Summary:** Assisted history matching remains non-unique because many geological realisations can reproduce equivalent production responses with substantial differences between individual well matches. This ambiguity increases when a field comprises several depositional settings and modelling strategies. The paper applied a graph autoencoder approach to history matching of a benchmark Brugge field that comprises different depositional zones. Each stratigraphic zone is modelled with its dedicated generative ...

---

### 47. Evolved Spiking Neural Networks for EEG Seizure Detection: Calcium Dynamics and Delay Mechanics

**Authors:** Tuba Aksoy

**Published:** 2026-11-02

🔗 [Paper](http://arxiv.org/abs/2611.03841v1) | 📄 [PDF](https://arxiv.org/pdf/2611.03841v1)

**Summary:** Neuroevolution can discover compact network designs that are hard to specify by hand. The EONS framework evolves the topology, weights, thresholds and delays of neuromorphic spiking networks without gradients. We tested whether giving integrate-and-fire (IF) neurons an activity-dependent calcium current (Ca-IF neurons) improves evolved networks for EEG seizure detection, with calcium parameters fixed, shared across a network, or evolved for each neuron. On 10 held-out CHB-MIT patients never seen...

---

### 48. Structured Visual Landscape: Generating Preferred Representations in Biological and Artificial Neural Networks

**Authors:** Yusong Zhao, Edgar Y. Walker, Hao Wang, et al.

**Published:** 2026-11-02

🔗 [Paper](http://arxiv.org/abs/2611.03597v2) | 📄 [PDF](https://arxiv.org/pdf/2611.03597v2)

**Summary:** Understanding how neurons respond to visual stimulus is an important question in both deep learning and neuroscience. It has significant implications for enhancing the interpretability of black-box artificial neural networks and for understanding the visual representation in the human brain. We propose a structured visual representations landscape and design an activation-based prior that allows us to effectively regularize the landscape with activations from brain regions or neural network unit...

---

### 49. Exact Fusion of Softmax Attention Heads Can Require Exponentially Many Atoms

**Authors:** Hiroyasu Usami, Keisuke Hara, Ayato Tsuboi, et al.

**Published:** 2026-11-02

🔗 [Paper](http://arxiv.org/abs/2611.02943v1) | 📄 [PDF](https://arxiv.org/pdf/2611.02943v1)

**Summary:** Fusing independently normalized attention heads can increase the number of explicit key-value entries, or atoms, needed to preserve their output. We prove a sharp separation for $W_d(q)=\sum_{j=1}^dσ(q_j)$: its $d$ two-atom heads use $2d$ head-atom terms, whereas its minimum single-head representation has exactly $2^d$ atoms, even with arbitrary fixed replacement keys, scalar values, and positive masses. The same lower bound holds for every fixed uniform error below $1/2$ on $\mathbb R^d$, and t...

---

### 50. Iterated Narrow Networks: Turing Completeness at Width 4 on Convex Input Spaces and the Complexity of Verification

**Authors:** Olivier Bournez, Johanne Cohen, Adrian Wurm

**Published:** 2026-11-02

🔗 [Paper](http://arxiv.org/abs/2611.02840v1) | 📄 [PDF](https://arxiv.org/pdf/2611.02840v1)

**Summary:** We study the iterates of a fixed ReLU network $N$ of width 4, that is, the discrete-time system $x_{k+1} = N(x_k)$ on $[0,1]^4$. Equivalently, $x_k$ is the output of a weight-tied network made of $k$ copies of $N$, or of a recurrent network with no external input, started at $x_0$. We prove that every deterministic Turing machine $M$ admits such a network $N_M$. The network can be constructed in polynomial time from $M$. Each iteration has depth $\mathrm{poly}(|M|)$. The iterates of $N_M$ simula...

---

## q-bio.NC

**50 papers**

### 1. Structure-Preserving Leaky Integrate-and-Fire Dynamics on Arbitrary Time Scales

**Authors:** Billur Kaymakçalan, Behiye İlayda Selçuk

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17219v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17219v1)

**Summary:** The leaky integrate-and-fire (LIF) neuron combines a passive membrane law with threshold-triggered firing and reset. We formulate this hybrid neuron model, under constant input, on an arbitrary Hilger time scale $\mathbb{T}$. Our central result is that, after the first spike, the firing times satisfy $t_{n+1}=Π_{\mathbb{T}}^{+}(t_n+T_c)$, where $T_c$ is the classical reset-to-threshold travel time. This recursion requires no periodicity, homogeneity, or translation invariance of $\mathbb{T}$; it...

---

### 2. Random Exploration is Random

**Authors:** Yingkang Luo, Hua-Dong Xiong, Hanbo Xie, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17011v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17011v1)

**Summary:** Decision making often requires balancing exploitation of familiar options with exploration of uncertain alternatives. One strategy for exploration is random exploration, in which choices become more variable and less tied to the option that currently appears best. However, it remains unclear whether this variability reflects genuine stochasticity or instead a deterministic structure that traditional cognitive models fail to capture. We examined this question using the Horizon Task in an aggregat...

---

### 3. Dynamical mean-field theory of latching Potts networks

**Authors:** Anindita Basu, Carlo Orientale Caputo, Fernando Lucas Metz, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16999v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16999v1)

**Summary:** Spontaneous transitions between memories, as observed in internally generated cognition such as mind-wandering and free association, require neural dynamics capable of destabilizing one attractive memory state and moving towards another. We ask what minimal representational structure is required for such transitions to emerge in random associative networks. To address this question, we study Potts associative networks with $S$ active states per unit and slow adaptive thresholds. The $S=1$ case c...

---

### 4. On the minimum energy required to trigger a spike

**Authors:** Guanchun Tong, Rodolphe Sepulchre

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16915v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16915v1)

**Summary:** We formulate and numerically study the problem of finding the minimum energy required to trigger a spike in a three-dimensional conductance-based excitable model. The variational formulation seeks a state trajectory that reaches the boundary of the spiking region with the least \textit{peak} cumulative work supplied through the membrane port. We approximate voltage histories by sums of real exponentials, reducing the problem to a finite-dimensional optimization. The best-found voltage waveform c...

---

### 5. Similarity-Guided Optimization Strategies for Approximate Network Symmetry Detection

**Authors:** David Hartman, Jaroslav Hlinka, Dominik Klepl, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16555v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16555v1)

**Summary:** Symmetry in complex networks is a structural property with broad implications for network function, dynamics, and robustness. While classical approaches rely on exact automorphisms and thus remain highly sensitive to small perturbations, recent work of Liu has introduced approximate formulations that relax the strict invariance condition and recast symmetry detection as an optimization problem over permutations. We investigate how node-level similarity information can be used to bias the search ...

---

### 6. Exact power spectra and effective dimensionality in critical block-GOE networks

**Authors:** Konstantinos Grammenos, Dionissios Hristopulos

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16427v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16427v1)

**Summary:** Criticality in neural networks is crucial for optimal information processing. Recent studies have shifted focus from static criticality to frequency-dependent behavior, particularly in oscillatory systems modeled by block-Gaussian orthogonal ensemble (block-GOE) matrices. However, analytical tools to predict spectral properties such as power spectrum and effective dimensionality remain scarce. In this work, we derive exact solutions for the network-averaged power spectrum $\operatorname{Tr}_{N}[...

---

### 7. Pyramidal Columns Acting as Attention Heads

**Authors:** Fabrizia Giulia Garavaglia, Marco Giunti

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.16057v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16057v1)

**Summary:** Can the functional architecture of a Transformer attention head be given a biological construction? More specifically, could a suitable group of pyramidal columns in posterior temporal language regions (PTLRs) constitute the biological construction of a neuromorphic mechanical realization of an attention head, under a mathematical instantiation that need not coincide with its standard Transformer instantiation? This paper investigates this hypothesis by examining possible correspondences between...

---

### 8. Optogenetic Modulation Fraction: A Robust Opsin-Presence Effect and an Unresolved Cell-Type Question, by Censoring-Aware Survival Analysis of Public Neuropixels Data

**Authors:** Siddhardha Nanda

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.15606v1) | 📄 [PDF](https://arxiv.org/pdf/2611.15606v1)

**Summary:** Expressing channelrhodopsin-2 (ChR2) in an interneuron population substantially raises the fraction of locally recorded units whose spike timing is altered by light, relative to no-opsin controls, under every method tried. Establishing that result rigorously, and retracting two secondary claims that did not survive the same rigor, is this paper's actual content. We reanalyze eight public Allen Institute Neuropixels sessions (4,112 units), modeling light-to-first-spike latency as a right-censored...

---

### 9. Analysis choices decide whether untrained networks beat trained ones at V1: a multiverse analysis of model-brain RSA

**Authors:** Nils Leutenegger

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.15533v1) | 📄 [PDF](https://arxiv.org/pdf/2611.15533v1)

**Summary:** Untrained convolutional networks have been reported to rival trained networks as models of visual cortex, and we had reported an untrained-network advantage over backpropagation at V1 in THINGS fMRI, together with a dependence on evaluation resolution. Under a pre-specified ridge readout, the untrained network scored below the trained one at every pooling grid (median r difference -0.043 at g = 4, 0 of 5 seeds positive), and also in MSE skill and per-fold r. In exploratory analyses, across 36 co...

---

### 10. Alignment De-Identifies Without Aligning: A Congruence-Invariant Relational Gap in Cross-Subject Neural Representations

**Authors:** Anna Notaro, Letizia Rossato, Sadasivan Puthusserypady

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.15204v1) | 📄 [PDF](https://arxiv.org/pdf/2611.15204v1)

**Summary:** In brain-computer interfaces, inter-subject variability remains a major challenge that limits decoding performance across users. Subject-wise alignment is widely used to improve cross-subject transfer of neural decoders, yet it is typically evaluated only through decoding accuracy, which cannot determine whether aligned representations share greater task-related structure. We therefore distinguish two questions that accuracy conflates: whether alignment removes subject-specific information and w...

---

### 11. Prototypes of the Mind: A Unified Framework for Probing the Visual Brain

**Authors:** Shi Chen, Seoyoung Ahn, Doris Tsao

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.15046v1) | 📄 [PDF](https://arxiv.org/pdf/2611.15046v1)

**Summary:** Deep learning has driven substantial progress in modeling fMRI responses, yet most existing approaches are optimized for a single objective---such as neural encoding, stimulus decoding, or post hoc interpretation---making it difficult to obtain a coherent account of neural representations. We introduce a unified framework that connects vision foundation models to brain activity while supporting neural analysis from multiple complementary perspectives. Our approach replaces black-box features wit...

---

### 12. Same currents, different field: $Δf = 0$ carrier-only stimulation is not temporal interference without the beat

**Authors:** Ido Haber, Giulio Tononi, Larissa Albantakis

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14839v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14839v1)

**Summary:** Carrier-only stimulation ($Δf = 0$) is generally considered the most rigorous control for temporal interference (TI) stimulation, assumed to reproduce TI's kilohertz carrier field without its low-frequency beat. We show that this assumption is incorrect: without the frequency difference, the carrier fields interfere coherently, changing the peak strength, power, and direction of the resulting field depending on electrode polarity and montage geometry. Using computational field modeling, we demon...

---

### 13. Mind-wandering preserves word-level coupling while disrupting comprehension

**Authors:** Anirudh Natarajan, Paul Sajda

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14814v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14814v1)

**Summary:** Readers can move their eyes through a page but retain little of its meaning when their minds wander. We tested whether word properties still guide their eyes during these lapses. We analyzed public eye-tracking and electroencephalography (EEG) data from 44 adults who read articles. They marked the text read during each lapse they noticed. We linked these spans to the sentences needed for later comprehension questions. Word frequency, length and surprisal still predicted which words readers skipp...

---

### 14. When Does the Real Wiring Win? Testing connectome structure-function claims against unmeasured physiology

**Authors:** Yeyuan Liu

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14508v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14508v1)

**Summary:** Connectome-constrained models are often used to argue that a measured wiring diagram outperforms shuffled or rewired wiring, and hence that structure shapes function. Such comparisons can confound wiring with how the models are tuned: a connectome fixes who connects to whom, not the excitability, gains or plasticity rates the model also needs, and modellers often tune these until the real-wiring model works. We separate three estimands: physiology tuned on the real wiring and transferred to null...

---

### 15. Measuring Robustness and Efficiency in a Connectome-Constrained Fly Visual System Model: Linking an Adversarial and a Perceptual Illusion

**Authors:** Alexandre Garcia-Duran, Alejandro Rodriguez-Garcia, Manuel Molano-Mazón, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14498v2) | 📄 [PDF](https://arxiv.org/pdf/2611.14498v2)

**Summary:** Biological visual systems compute reliably under tight metabolic and wiring constraints, whereas artificial vision systems consume far more energy and can be sensitive to adversarial perturbations. Whether networks with brain-like wiring are more robust at lower computational cost is unclear. We address this by benchmarking a task-optimized, continuous-time recurrent neural network of the fly visual system constrained by its synaptic connectome (FlyNet) against artificial neural networks. We com...

---

### 16. Optimization principles, revisited

**Authors:** William Bialek

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14381v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14381v1)

**Summary:** The brain solves a wide range of problems, and some of these solutions are very good indeed. It is an old idea that, in some cases, these solutions may be as good as possible given the relevant constraints. If this is true we can promote this notion of optimization to a principle from which aspects of function and mechanism can be derived, ideally with no free parameters. Optimization principles are powerful and have had many successes, but they remain controversial. We start with a reminder of ...

---

### 17. ScaleBrain: A Scale-Consistent Framework for EEG Foundation Models

**Authors:** Minyu Zhou, Yajing Wu, Yongqiang Tang, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14035v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14035v1)

**Summary:** Foundation models pre-trained on large unlabeled electroencephalography (EEG) corpora have emerged as a transformative paradigm for Brain-Computer Interface (BCI) applications. Recent EEG foundation models have shown that multi-scale representations derived from fixed-length patches can improve EEG representation learning. Existing frameworks commonly construct temporal scales through feature-level operations. However, these operations leave the correspondence between learned features and scale-...

---

### 18. Neuromodulation Through Intrinsic Noise

**Authors:** Sunghyun Koo, Jin Gyu Lee, Rodolphe Sepulchre

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13780v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13780v1)

**Summary:** Neuromodulation, the modulation of excitability through the regulation of neuronal parameters, is a key tool in neuromorphic control design. This paper investigates how spiking excitability can be modulated by intrinsic noise. Focusing on a simplified memristive neuron model, we show that intrinsic noise plays distinct functional roles depending on the feedback pathways: Intrinsic noise in the fast excitatory feedback shapes the nature of excitability and modulates the sensitivity of the neuron ...

---

### 19. Similar visual tuning conceals different recovery dynamics in a model of macaque V1

**Authors:** Xialei Huang, Qingyu Yan, Zheng Bian, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13692v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13692v1)

**Summary:** Biologically detailed neuronal networks can model how brain circuits perform observed functions, but their high computational cost limits the comparisons needed to test biological hypotheses. To address this limitation, we extend a multiscale approach in which responses of small populations of spiking neurons are computed in advance and reused across a larger cortical circuit. In particular, we approximate these local responses by deep neural networks and achieve an estimated acceleration of the...

---

### 20. A Functional Preservation Score for Auditing Connectome Operations: Compression, Alignment, Transport, and Local-Rule Writing

**Authors:** Praveg Vashishtha

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13681v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13681v1)

**Summary:** We introduce the Functional Preservation Score (FPS), a null-normalised, behaviourally grounded measure of how much of a neural network's input-output function survives a structural operation, and use it to audit the operations underlying speculative "mind-migration" pipelines on public data that runs on a single laptop. Across five pre-registered studies on the C. elegans connectome, whole-brain calcium activity, and hippocampal replay, FPS yields two positive characterisations and a three-part...

---

### 21. Human and Machine Annotations Predict Brain Responses to Naturalistic Movies Across Development

**Authors:** Yiran Huang, Zeyong Zhang, Rounak Rahman, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13637v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13637v1)

**Summary:** Naturalistic movie watching provides a powerful framework for studying dynamic brain function, but linking movie content to neural responses typically relies on labor-intensive human annotation. We investigated whether multimodal large language models (MLLMs) can provide scalable socio-affective and semantic annotations for naturalistic fMRI. We compared MLLM-generated theory-of-mind (ToM) and valence ratings with human ratings and with regional BOLD responses across three animated movies. For t...

---

### 22. Lightweight Deep Learning Framework for Astrocyte-Centric 3D Reconstruction across Normal and Stress-associated Ultrastructural States

**Authors:** Bowen Deng, Gwang-Jin Jeong, Seulgi Noh, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13581v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13581v1)

**Summary:** The morphology of astrocytes is closely associated with their ability to support and modulate neural circuit functions; however, its reconstruction from volume electron microscopy (vEM) data remains labor-intensive and computationally resource-intensive, placing substantial barriers on its broader adoption and scalability despite the high spatial resolution of vEM. We present AstroSeg-vEM, a lightweight, astrocyte-centric framework for morphology-preserving astrocyte segmentation, 3D reconstruct...

---

### 23. Orthographic depth at two scales, with English also matched for lexicon size

**Authors:** Adam Y. Shavit

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13400v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13400v1)

**Summary:** A reader can struggle to read in only one of their languages, and one proposed reason is how predictably spelling maps to sound. We measure that predictability as conditional entropy, the pronunciation uncertainty left once the spelling is seen, at two grain sizes (unit sizes): the alignment unit, an aligned spelling-sound chunk, and the syllable, bounded in the pronunciation. We analyse word lists in twelve alphabetic orthographies and report five in full, with English pronunciations from a dic...

---

### 24. A probabilistic model of visual segmentation explains early visual cortical dynamics

**Authors:** Tridib K. Biswas, Ruben Coen-Cagli

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.13316v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13316v1)

**Summary:** Neural dynamics are a central feature of biological neural systems. In the visual cortex, the functional role of neural dynamics is poorly understood, particularly for static stimuli. The statistics of still natural images have long been used by models that successfully predict firing in early visual cortex; those models assume that neurons represent inferences about latent image features, but often ignore the dynamics of said inference. Here, we test if inferential dynamics in images explain vi...

---

### 25. IC-GNN: Modeling Individualized Brain Community Organization for Disease Prediction

**Authors:** Yang Zhang, Xiao Zhou, Jonathan Warrell, et al.

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.13070v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13070v1)

**Summary:** Brain networks exhibit modular organization, where community structures vary substantially across individuals and diseases. Understanding these individual differences is crucial for advancing both basic neuroscience research and precision medicine. However, widely used predefined group-level brain atlases often overlook this heterogeneity. While individualized functional parcellations capture subject-specific variability in community boundaries, they often require lengthy scan times to achieve f...

---

### 26. Qualiaphobic artificial neural networks (and why to build them)

**Authors:** Erik Hoel

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12809v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12809v1)

**Summary:** This paper introduces qualiaphobic AI: artificial neural network architectures that are hostile to theories of consciousness. I show that qualiaphobia can be well-justified by knowledge about theories of consciousness, like when such theories are trivial or unfalsifiable or contradicted by overwhelming scientific evidence. It can also be justified by how theories of consciousness must be grounded in phenomenology, as well as how current popular theories of consciousness are applied to AI. I iden...

---

### 27. Spike-to-Field Mechanisms of Turbulence-Like Dynamics in Spatial Spiking Neural Networks

**Authors:** Zequan Liu

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12627v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12627v1)

**Summary:** Neural avalanches and turbulence-like brain dynamics are usually measured after neural activity has been coarse-grained into continuous fields, leaving open which spike-level mechanisms can generate these macroscopic observables. We build a spatial leaky integrate-and-fire spiking neural network and explicitly transform spikes into activity-density and Hilbert phase fields. A delayed, distance-dependent, passive-dendrite regime reproducibly generates turbulence-like field structure, including hi...

---

### 28. K-prop: Deep Online Learning by Backpropagating Temporal Kernels

**Authors:** Bingkun Liu, Paul Haider, Federico Benitez, et al.

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12530v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12530v1)

**Summary:** Self-recurrence represents an important component for temporal processing in neural networks, both artificial and biological, where it appears naturally in the form of leaky integration. However, due to the complex temporal dependencies of the gradient, an efficient and effective method of online training is still lacking. Here we propose K-prop, a novel online learning method for leaky neural networks. It dramatically reduces the computational and memory cost of real time recurrent learning (RT...

---

### 29. TrajLift: Lifting Memory Recall Trajectories with Latency-Modulated Heat Diffusion

**Authors:** Jiawen Kang, Jinchao Li, Mingyu Cui, et al.

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12197v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12197v1)

**Summary:** Verbal memory retrieval carries rich diagnostic information for Alzheimer's disease through the order, hesitation, and categorical organization of recalled words, yet computational modeling of this retrieval process remains largely unexplored. A key challenge is that timing and hierarchical structure are diagnostically entangled: the diagnostic meaning of retrieval timing depends on its hierarchical context. We propose TrajLift, a spectral framework that models verbal recall as timed trajectorie...

---

### 30. Language processing in the autistic brain: A meta-analysis of neuroimaging studies across modalities and age

**Authors:** Hanlin Wu, Bei Xiao, Qingxi He

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.11927v1) | 📄 [PDF](https://arxiv.org/pdf/2611.11927v1)

**Summary:** Language is central to social communication, which is altered in autism, and language abilities vary widely among autistic individuals. How the autistic brain processes language is central to understanding autistic communication. Yet neuroimaging studies report inconsistent findings on how autistic brain activity is altered during language processing. We synthesized 45 fMRI and PET studies (753 autistic and 777 non-autistic participants) with seed-based d mapping with permutation of subject imag...

---

### 31. MICE: Multi-animal Interaction Context Encoder - A Hierarchical Foundation Model for Mouse Behavior

**Authors:** Yen-Shuo Su, Weihan Li, Anqi Wu

**Published:** 2026-11-08

🔗 [Paper](http://arxiv.org/abs/2611.11644v1) | 📄 [PDF](https://arxiv.org/pdf/2611.11644v1)

**Summary:** Quantifying mouse behavior from pose is a foundational tool in neuroscience, ethology, drug discovery, and animal welfare. Self-supervised foundation models are a natural fit, but a foundation model for mouse behavior must handle social behavior - many behaviors that matter (aggression, courtship, mounting, allogrooming) are inherently multi-animal. Existing self-supervised pose models fall short: they encode each animal independently and discard interaction signal, hard-code the animal count, a...

---

### 32. From MNH to the Friedman--Komogortsev Method---which changes improve eye-movement classification?

**Authors:** Lee Friedman, Mehedi Hasan Raju, Oleg Komogortsev

**Published:** 2026-11-08

🔗 [Paper](http://arxiv.org/abs/2611.11519v1) | 📄 [PDF](https://arxiv.org/pdf/2611.11519v1)

**Summary:** The Friedman-Komogortsev Method (FKM) is a rule-based classifier of fixations, saccades, and post-saccadic oscillations in 1000-Hz recordings, developed from the modified Nyström-Holmqvist algorithm (MNH) and used in several recent studies. FKM changes MNH in many ways at once: it centres MNH's Savitzky-Golay filter, adds a position-based test for whether an apparent post-saccadic oscillation continues the saccade, adds rejection tests, and changes several thresholds. We asked which of these cha...

---

### 33. Learning Actionable Information Landscapes for Multimodal Active Sensing in Hawkmoths

**Authors:** Abdelrahman Sharafeldin, Yaqing Wang, Simon Sponberg, et al.

**Published:** 2026-11-07

🔗 [Paper](http://arxiv.org/abs/2611.11011v1) | 📄 [PDF](https://arxiv.org/pdf/2611.11011v1)

**Summary:** Animals integrate information across sensory modalities to guide exploration, suggesting that they maintain internal estimates of where actions are expected to reduce uncertainty. However, how such action-conditioned information maps are learned from multimodal sensory experience remains unclear, as previous studies have been largely confined to unimodal sensing frameworks. We introduce a multimodal predictive-coding framework for learning uncertainty-reduction maps from visual and mechanosensor...

---

### 34. Perception, Not Reasoning, Limits Visual Theory of Mind

**Authors:** Mohamed Rayan Barhdadi, Syed Talal Wasim, Juergen Gall, et al.

**Published:** 2026-11-07

🔗 [Paper](http://arxiv.org/abs/2611.10694v1) | 📄 [PDF](https://arxiv.org/pdf/2611.10694v1)

**Summary:** Vision-language models pass text-based false-belief probes at near-human levels but drop by over twenty percentage points on abstract panels the moment the same problem is conveyed visually. The consensus diagnosis is conceptual, prescribing new belief-reasoning modules. We argue the dominant bottleneck is perceptual: not what the model cannot reason about, but what it cannot see. We propose a five-condition dissociation protocol that holds the reasoning task constant while varying perceptual fi...

---

### 35. NeuroHorizon: Long-Horizon Forecasting of Neural Population Activity with Hierarchical Memory

**Authors:** Peng Jiang, Xiaoxuan Jia

**Published:** 2026-11-07

🔗 [Paper](http://arxiv.org/abs/2611.10617v1) | 📄 [PDF](https://arxiv.org/pdf/2611.10617v1)

**Summary:** Long-horizon forecasting of neural population activity tests whether a model has captured dynamics that remain predictive well beyond the observed history. Prediction quality typically declines as the horizon grows, yet neither short-horizon accuracy nor teacher-forced evaluation, which supplies the true activity preceding each predicted step, reveals how well models sustain predictions from an initial history alone. We compare direct multi-step prediction and autoregressive rollout on spiking r...

---

### 36. Pixels over Symbols: Sensory Realism Improves Behavioral Alignment in Models of Cognition

**Authors:** Hao Yuan Bai, Xiaoxuan Lei, Zihan Weng, et al.

**Published:** 2026-11-07

🔗 [Paper](http://arxiv.org/abs/2611.10565v1) | 📄 [PDF](https://arxiv.org/pdf/2611.10565v1)

**Summary:** Computational models of cognition have traditionally relied on abstract symbolic inputs that approximate sensory experiences with simplified vector representations. This simplification reflects historical computational constraints and a long-held assumption that the details of sensory realism are incidental to the study of cognitive processes. Recent advances have enabled the development of sensory-realistic models capable of performing diverse cognitive tasks, yet whether sensory realism meanin...

---

### 37. Path-dependent triage: Early judgments lead conversational AI chatbots to miss mental-health emergencies

**Authors:** Veith Weilnhammer, Raymond Dolan, Lennart Luettgau, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09647v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09647v1)

**Summary:** People increasingly bring mental-health concerns to consumer AI chatbots. In these conversations, clinically relevant information rarely arrives all at once. Instead, it unfolds over multiple turns, often in response to the questions the chatbot asks. Recognizing risk therefore depends on how a chatbot integrates newly disclosed information (inference) and on the questions it asks on each turn to elicit this information (context-seeking). Here we evaluated the conversational triage performance o...

---

### 38. A hair-thin implant opens the entire depth of the mouse brain to revisiting the same structures at subcellular resolution

**Authors:** Miroslav Stibůrek, Tomáš Pikálek, Petra Ondráčková, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09481v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09481v1)

**Summary:** Ultrathin multimode-fibre endoscopes provide minimally invasive access to subcellular structures throughout the depth of the mouse brain. Here we introduce a chronically implantable interface with a diameter of 144 μm, about the thickness of a human hair, that extends this capability to longitudinal imaging, enabling repeated access to the same fine structures over extended periods. The system supports weeks-long tracking of individual dendritic spines, allowing quantitative comparison of their ...

---

### 39. Decoding spatial and semantic information from large-scale visual cortical activity for natural-movie reconstruction

**Authors:** Yukai Huang, Haoyu Albert Wang, Jiawei Zhang, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.08887v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08887v1)

**Summary:** Reconstructing natural visual experience from cortical population activity is a central challenge in neural decoding, particularly for calcium imaging, where signals are noisy, temporally filtered, and paired neural-video data are limited. Here we present Ca2REAL (Calcium Activity to Reconstruct Events, Appearance, and Layout), a neural-to-video framework that conditions a pretrained video diffusion model through separate layout and semantic controls derived from calcium activity. Using measured...

---

### 40. Same Behavior, Different Mechanism: What Finite Experiments Can Certify About Integrated Information

**Authors:** Linqian Wu, Diaoxuan He

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.08469v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08469v1)

**Summary:** Interpretability, AI auditing and assessments of machine consciousness increasingly rest on mechanism-level quantities: functionals of a system's causal transition law that describe how it computes, not what it outputs. Experiments see that law only through finite, partial and noisy interventions. We ask when such a quantity is identifiable from an experiment's access, continuous in the mechanism and certifiable from finite data, and answer exactly for a deliberately demanding case - the integra...

---

### 41. Spiking neuromodulation: a linear control perspective

**Authors:** Fulvio Forni, Rodolphe Sepulchre

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.08571v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08571v1)

**Summary:** Neuronal excitability is a nonlinear phenomenon, and the complexity of spiking experimental traces sometimes looks defeating. The present paper takes the view point that excitability is a neuromodulated property, and aims to demonstrate that the neuromodulation of spiking is amenable to the classical linear analysis tools of control theory. We illustrate the value of linear feedback analysis as an alternative to bifurcation analysis in the simple yet classical example of spiking modulation by th...

---

### 42. Do sEMG Foundation Models Improve Cross-Subject Generalisation?

**Authors:** William Raftery, Dario Farina

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.08199v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08199v1)

**Summary:** sEMG Foundation Models aim to learn general purpose representations over diverse subjects and recording conditions that boost performance on a variety of downstream tasks. However, existing evaluations make it difficult to discern whether pretraining alone is sufficient to combat the cross-subject overfitting which makes machine learning on sEMG so challenging. We conduct a systematic evaluation of three sEMG foundation models across three gesture classification datasets under both intra-session...

---

### 43. Reversible Dynamics, Asymmetric Actions: Parking as a Trajectory-Level Affordance

**Authors:** Adam Y. Shavit

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.07965v1) | 📄 [PDF](https://arxiv.org/pdf/2611.07965v1)

**Summary:** Drivers are often told to back into a tight parking space, not drive in nose first. The advice looks paradoxical, because a slow car is dynamically reversible: reverse its speed and replay the steering backward, and it retraces a feasible path. Played backward, though, reverse-in shows a car driving forward out of the space. Reverse-in and forward-in are different tasks: they share a start position but end facing opposite ways. We separate three clearances between car and obstacles. Static fit $...

---

### 44. Invariance before structure: two modes of emergent compression in representation learning

**Authors:** Hardik Rajpal, Dan Goodman

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.07952v1) | 📄 [PDF](https://arxiv.org/pdf/2611.07952v1)

**Summary:** Learned representations show striking invariance across biological and artificial neural networks, with different substrates and variations driven by drift, heterogeneity and initialisation. To understand this invariance, we propose Emergent Adaptive Representation Learning (EARL), a framework that distinguishes two modes of emergence in learned representations: state-space compression, where a learned representation gains predictive power over its own future beyond what the network's units can ...

---

### 45. Self-Supervised Learning of Local Predictive Directions as a Neural Computation

**Authors:** Marco Zenari, Xuehao Ding, Daniel Burnham, et al.

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.07809v1) | 📄 [PDF](https://arxiv.org/pdf/2611.07809v1)

**Summary:** Natural sensory dynamics are globally nonlinear but often exhibit simple local geometry, with nearby trajectories evolving preferentially along a small number of predictive directions. We ask how neural circuits could discover this geometry directly from temporal experience. We introduce Local Predictive Directions (LPD), a self-supervised framework that learns local directions whose projections maximally predict near-future trajectory evolution. LPD applies past-future canonical correlation ana...

---

### 46. Bearing, heading and the perceptual geometry of collective motion

**Authors:** Mohammad Salahshour

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.07214v1) | 📄 [PDF](https://arxiv.org/pdf/2611.07214v1)

**Summary:** Traditional models of collective motion commonly assume that animals turn to match their neighbours' directions of travel. In the harmonic theory, decisions follow from a neural representation of direction, and a neighbour enters only as a stimulus at a bearing, the direction in which it lies. Here we show that a neighbour's spatial extent allows its orientation to enter through projection geometry alone, and the theory generates a matrix of coupling coefficients indexed by the neighbour's beari...

---

### 47. Learning Time-Varying Connectomes for Stable Behavior Across Development

**Authors:** Christof Fehrman, Jacob J. Morra, Eva A. Naumann

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06895v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06895v1)

**Summary:** Neural circuits must maintain functionality to drive effective behavior while their size, topology, geometry, and intrinsic dynamics change across development. To model developing visuomotor circuits and behavior, we investigated whether a single compact generative encoding could produce functional recurrent controllers across such changes. Building on the HyperNEAT algorithm, we represented this program as a compositional pattern-producing network that received developmental time as an input to...

---

### 48. Cell-type-specific modularity in E/I networks shapes dynamical regimes and computational capabilities

**Authors:** Emmanouil Giannakakis, Victor Buendía, Oleg Vinogradov, et al.

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06720v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06720v1)

**Summary:** Structural modularity is a ubiquitous feature of brain networks that shapes neural dynamics and information processing. Yet excitatory and inhibitory populations can differ in their modular organization, and it remains unclear how this asymmetry affects network dynamics and computation. Here, using dynamical mean-field theory and simulations of networks performing complex temporal tasks, we show that independently tuning excitatory and inhibitory modularity controls the dynamical regimes of bala...

---

### 49. PINR-ESI: Physics-Informed Self-Supervised Implicit Neural Representation Framework for EEG Extended-Source Imaging

**Authors:** Zhiyong Zhou, Sheng Liao, Xiaolin Li, et al.

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06700v2) | 📄 [PDF](https://arxiv.org/pdf/2611.06700v2)

**Summary:** EEG extended-source imaging aims to localize active cortical regions and characterize their spatial extent, yet supervised inverse networks typically depend on synthetic EEG-source pairs and may be sensitive to synthetic-to-real mismatch. We propose a physics-informed self-supervised implicit neural representation (INR) framework for spatial source reconstruction without paired source labels or simulation-based supervised pretraining. The lead field matrix encodes the source-to-sensor volume-con...

---

### 50. Synchronized Hearts, Desynchronized Brains: A Nonlinear Dynamics Perspective for Function and Failure

**Authors:** Irene Pellini, Simon Bauer, Seba Contreras, et al.

**Published:** 2026-11-04

🔗 [Paper](http://arxiv.org/abs/2611.06618v1) | 📄 [PDF](https://arxiv.org/pdf/2611.06618v1)

**Summary:** Both the heart and the brain are built from electrically excitable cells, yet the emergent dynamics of these organs could not differ more. In the myocardium, a coherent traveling wave of action potentials ensures coordinated contraction; in the cerebral cortex, distributed, irregular spiking underlies efficient information processing and the generation of behavior. Here, we illuminate the principles that underlie the emergence of such distinct nonlinear dynamics using concepts from complex syste...

---

## stat.ML

**50 papers**

### 1. Sketching Language Models for Context Attribution

**Authors:** Christopher Liaw, Aranyak Mehta, Grigoris Velegkas, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17313v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17313v1)

**Summary:** Context attribution asks how removing parts of a prompt changes a language model's output. We study leave-one-out (LOO) attribution for a prompt of $n$ tokens and a fixed measurement function. Computing all LOO values directly requires $n$ model evaluations. Under a stability assumption, our algorithm estimates all LOO values to error proportional to $\varepsilon$ with constant probability using $O(\sqrt{\log(1/\varepsilon)}/\varepsilon)$ evaluation calls. To complement our upper bound, we prove...

---

### 2. Quantifying structural stability of transparent models for general insurance pricing

**Authors:** Félix Côté, Marie-Pier Côté

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17308v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17308v1)

**Summary:** The short duration of general insurance contracts leads to rapid distributional shifts in the data, warranting regular model updates. This process may yield a post-update model that differs considerably from the pre-update model in both predictions and structure. Structural stability is upstream of predictive stability, yet existing structural stability metrics are mostly restricted to simple decision trees. Thus, we first introduce the notion of functional transparency, characterising models wi...

---

### 3. Linear Regression with Self-Selection Bias in Polynomial Time

**Authors:** Felix Zhou

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17228v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17228v1)

**Summary:** We revisit the problem of estimating $k$ linear regressors with self-selection bias in $n$ dimensions up to error $\varepsilon$ with the maximum self-selection criterion, as introduced by Cherapanamjeri, Daskalakis, Ilyas, and Zampetakis [CDIZ23, STOC]. Our main result is a $\mathrm{poly}(n,k,1/\varepsilon)$ time algorithm for the unknown-index variant of this problem, thereby improving upon the running times of the best known algorithms due to Gaitonde and Mossel [GM24] and Kalavasis, Mehrotra,...

---

### 4. Introducing Feedback Delays to Non-Delayed Adversarial MDPs: Optimal $\sqrt S$ and $\sqrt K$ Dependencies in Tabular and Linear AMDPs

**Authors:** Aarush Kulkarni, Khang Nguyen, William Chang, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17214v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17214v1)

**Summary:** We study regret minimization in episodic Adversarial Markov Decision Processes (AMDPs) with unknown transitions and bandit feedback. In tabular AMDPs with $S$ states, $A$ actions, and horizon $H$, the best known $K$-episode regret is $\tilde O(HS\sqrt{AK})$, whose $\sqrt S$ gap to the $Ω(H\sqrt{SAK})$ lower bound has long remained open. In linear AMDPs with $d$-dimensional features, after a five-year line of improvements starting from $K^{14/15}$, computationally efficient algorithms without a s...

---

### 5. Disentangling Spurious Correlations: How IRM Handles Diverse Shortcuts in Text Classification

**Authors:** Paul Grunenwald, Benoît Crabbé, Guillaume Wisniewski, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17107v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17107v1)

**Summary:** In NLP, models trained via Empirical Risk Minimization (ERM) often exploit spurious correlations, such as dialectal markers, at the expense of robust linguistic features, thereby degrading their out-of-distribution (OOD) generalization. Invariant Risk Minimization (IRM) aims to suppress such shortcuts by identifying predictive relationships that remain stable across environments, but its practical utility for NLP remains debated. We use a causality-driven framework to evaluate IRM under three sh...

---

### 6. Prevalence Bounds for Edited Watermarked Text: Power Envelopes and Calibration Sensitivity

**Authors:** Kuancheng Ye

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17035v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17035v1)

**Summary:** Watermark detectors decide whether one document came from a watermarked language model. Auditors often need a different number: the share of a corpus that did. We study this share for Gumbel-max and green-list (KGW) watermarks when every document may have been edited by an unknown amount. Without restrictions on the edits, the upper end of the identified set is 1. Combining a known least-favourable next-token distribution with a sequential coupling, we derive a power envelope indexed by three bu...

---

### 7. Temporal Regularized Learning: Self-Supervised Learning Local in Space and Time

**Authors:** Davide Wiest

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17019v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17019v1)

**Summary:** Layer-local self-supervised objectives remove the backward pass between layers, but almost all still compute their loss over a batch of samples and are therefore local in space but not in time. We introduce Temporal Regularized Learning (TeReL), a spatially and temporally local learning rule for self-supervised representation learning from sequential input streams. The key idea is to instantiate a VICReg-style objective with temporally adjacent positives and non-differentiated running population...

---

### 8. Entire sig-jump-diffusions, their expected signature and applications to score-based generative modeling

**Authors:** Christa Cuchiero, Francesca Primavera, Sara Svaluto-Ferro

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16995v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16995v1)

**Summary:** We develop score-based generative models for time series and standard finite-dimensional data, building on the analytical computation of the expected signature of a new class of jump-diffusions, called entire sig-jump-diffusions. These are semimartingales whose characteristics are given by linear combinations of potentially infinitely many components of their own signature. We show that their expected signature can be computed by solving linear ODEs in the extended tensor algebra, providing a tr...

---

### 9. Uncertainty-aware quantum machine learning based on Dempster-Shafer theory

**Authors:** Marie Kempkes, Jakob Spiegelberg, Evert van Nieuwenburg, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16903v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16903v1)

**Summary:** A large body of work in quantum machine learning has centered on characterizing the expressivity and performance of quantum models. In contrast, little attention has been paid to the reliability of predictions beyond average performance measures such as accuracy. In this work, we introduce an uncertainty-aware quantum classification framework based on Dempster-Shafer theory. This theory allows to express uncertainty through weights assigned not only to individual classification labels but to set...

---

### 10. Stochastic Kernel Mode Decomposition: Information, Uncertainty, and Conditional Regime Inference

**Authors:** Boumediene Hamzi, Houman Owhadi

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16874v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16874v1)

**Summary:** When do mode energies preserve regime information as measurement quality changes? Stochastic Kernel Mode Decomposition (sKMD) fits joint regime laws on signed KMD mode coordinates and transfers the reference mode posterior to regime probabilities and conditional reconstructions. For centered Gaussian regimes with independently varying known noise variances, fixed coordinate energies retain the full regime posterior precisely when all classes share their cross-covariances and class variances can ...

---

### 11. Class-Competence Aggregation: Output-Layer Routing for Federated Multiclass DDoS Detection under Class-Concentrated Non-IID Data

**Authors:** Tapu Datta, Hafiz Imtiaz

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16772v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16772v1)

**Summary:** Federated learning over distributed intrusion-detection sensors naturally produces \emph{class-concentrated} non-IID data, where an entire attack class is held by a single client and absent elsewhere. We show this collapses federated averaging in a specific, localized way: the output layer holds one decision boundary per class, and when a class's aggregation weight comes overwhelmingly from clients that have never seen it, its neuron receives an active anti-signal rather than mere dilution, coll...

---

### 12. On the Difficulty of Sequence-Level Supervised Learning for Autoregressive Language Models

**Authors:** Mathieu Blondel, Michaël E. Sander, Germain Vivier-Ardisson, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16736v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16736v1)

**Summary:** During the supervised learning phase, autoregressive language models are typically trained by minimizing the negative log-likelihood of the training data, which decomposes as a sum of token-level cross-entropies via teacher forcing. This objective is simple and efficient but potentially suffers from so-called exposure bias: a mismatch between the way the model is trained and the way it is used at inference time. Can we instead design sequence-level loss functions that incorporate inference-time ...

---

### 13. When and How SignSGD Outperforms SGD: A Functional Scaling Law Perspective

**Authors:** Zilin Wang, Binghui Li, Jia-Nan Wang, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16560v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16560v1)

**Summary:** We study how the sign operator interacts with gradient noise to shape the learning dynamics and scaling behavior of sign-based optimizers. In power-law kernel regression with diagonal features, we establish a functional scaling law (FSL) for SignSGD under general learning rate schedules. The FSL describes the learning dynamics through two processes: signal learning and noise forgetting. The key mechanism is noise-induced preconditioning: gradient noise smooths the sign operator, inducing an effe...

---

### 14. Context-Predictive Low-Rank Adaptation for Face Presentation Attack Detection

**Authors:** Aminu Yusuf, Shakeel Muhammad Ibrahim, Sulaimon Oyeniyi Adebayo, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16534v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16534v1)

**Summary:** Face presentation attack detection requires representations that distinguish physical spoofing cues across changes in acquisition devices, subjects, and attack media. Large visual encoders offer transferable representations, but conventional binary fine-tuning supervises their final decisions without explicitly constraining how local facial evidence is represented under partial observation. We present CP-JEPA, a context-predictive adaptation framework that combines low-rank tuning of a pretraine...

---

### 15. Posterior contraction rates for banded approximations of Gaussian processes

**Authors:** Omar Kassi, Bernhard Stankewitz, Botond Szabo

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16482v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16482v1)

**Summary:** Gaussian process regression models are widely used in modern statistics and machine learning due to their flexibility, interpretability, built-in uncertainty quantification, and strong theoretical foundations. However, training Gaussian processes (GPs) has a computational cost of $O(n^3)$, while the memory and prediction costs are also $O(n^2)$.   For large datasets commonly encountered in practice, this becomes infeasible and necessitates the use of approximate posterior methods.   In this work...

---

### 16. Recursive State-Augmented Language Models: Persistent Latent-State Adaptation of Pretrained Language Models

**Authors:** Omer Haq

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16375v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16375v1)

**Summary:** Language models rely on finite token contexts, limiting access to earlier interactions. We introduce Recursive State-Augmented Language Models (Recursive SALM), a framework in which a persistent latent state evolves with each observation and generates adaptations of a pretrained language model. A modular read-transition-write architecture separates observation encoding, latent dynamics, and predictor adaptation. We develop deterministic and stochastic formulations.   The experiments evaluate onl...

---

### 17. Distribution-First Framework for Learning Risk-Sensitive Individualized Treatment Rules

**Authors:** Zhen Fang, Guanting Chen, Yufeng Liu

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16274v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16274v1)

**Summary:** Learning a risk-sensitive individualized treatment rule (ITR) with patient covariates is challenging when the treatment criterion depends on the full conditional outcome distribution rather than only its conditional mean. Existing methods are largely criterion-specific, making it difficult to compare multiple treatment criteria within a common pipeline, such as quantiles, conditional value-at-risk (CVaR), and complex preference-based objectives such as cumulative prospect theory. We propose a di...

---

### 18. A Sensitivity Framework for Assessing External Validity

**Authors:** Ariel Boyarsky, Naoki Egami, Hongseok Namkoong

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16242v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16242v1)

**Summary:** Assessing the external validity of experimental results is a pervasive challenge in causal inference as internally valid findings need not generalize beyond sites in which the experiments were conducted. Since the number of sites is often smaller than the number of site-level variables that moderate causal effects, we develop a partial identification framework that lets practitioners assess external validity under a wide range of assumptions that allow extrapolation across site-level variables. ...

---

### 19. Fréchet Oblique Forest for Non-Euclidean Regression

**Authors:** Jiaye Chen, Rui Qiu, Zhou Yu

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16209v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16209v1)

**Summary:** We propose Fréchet oblique forests (FOF) for non-Euclidean regression with predictors and responses in metric spaces. An Alexandrov inner-product score defines directional splits in metric predictor spaces and recovers ordinary oblique splits for Euclidean predictors. Candidate splits are evaluated through pairwise response distances, avoiding repeated Fréchet mean computations during split search. Forest predictions minimize a weighted Fréchet criterion obtained by averaging leaf weights across...

---

### 20. Gradient Flows over Convex Bodies for Learning Optimal Regularizers

**Authors:** Nilava Metya, Oscar Leong, Yong Sheng Soh

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16142v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16142v1)

**Summary:** We consider the question of describing gradient flows over the collection of convex bodies. This is motivated by foundational questions arising in inverse problems. Suppose we wish to solve an ill-posed inverse problem using regularization techniques. Can we learn an optimal choice of a convex regularizer directly from prior data? Given a numerical algorithm that computes such an optimal regularizer, is there a principled manner for describing the evolution of its iterates? The objective of this...

---

### 21. A Matching Lower Bound for Online Smooth Calibration

**Authors:** Kaixuan Ji, Quanquan Gu

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.16097v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16097v1)

**Summary:** We study smooth calibration error in sequential binary prediction, which measures how far a sequence of probabilistic forecasts is from being calibrated and, unlike the classical expected calibration error, is robust to small perturbations of the forecasts. Against adaptive adversaries, the minimax smooth calibration error is known to lie between $Ω(T^{1/3})$ and $O(\sqrt{T})$ (Qiao and Zheng, 2024), where $T$ is the number of rounds. In this paper, we close this gap by constructing a new advers...

---

### 22. Your PID Is Already a Neural Network: Learning Its Gains with Only Three Weights and No Teacher

**Authors:** Felipe de Jesús Félix-Arredondo, Nezih Nieto-Gutiérrez, Carlos Astengo-Noguez, et al.

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.16050v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16050v1)

**Summary:** A discrete PID controller is exactly a recurrent neural network, a classical state-space fact: a fixed linear memory of the running integral and the last error, read out by three trainable weights that map one-to-one to the PID gains. Networks with bounded hidden states, such as LSTMs of any width, only approximate it. Trained only on a one-step physical cost (the expected cost of one transition from a fixed state distribution), with no demonstrations, teacher controller, or known gains, the net...

---

### 23. Improved Elastic Weight Consolidation as an Optimization Constraint for Continual Learning

**Authors:** Davide Wiest

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.16039v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16039v1)

**Summary:** Elastic Weight Consolidation (EWC) is a widely used regularization-based technique for continual learning, protecting performance on old tasks with a quadratic penalty whose empirical Fisher is usually justified through probabilistic curvature. We instead introduce Continual Learning as an Optimization Constraint (CLOC): new training must preserve chosen functionals of learned behavior. EWC's empirical Fisher is exactly the first-order form of this constraint when the preserved functional is eac...

---

### 24. Characterizing the Edge of Stability in Variational Training Without Priors

**Authors:** Juraj Marusic, Jonathan Wenger, Beau Coker, et al.

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.15990v1) | 📄 [PDF](https://arxiv.org/pdf/2611.15990v1)

**Summary:** Variational approaches in deep learning promise to deliver improved uncertainty quantification and out-of-distribution generalization by inferring a distribution over weights, regularized by a divergence to a chosen prior. However, prior elicitation presents a significant challenge in deep learning, resulting in the common practice of significantly downweighting the regularization term in the variational objective. Recently, it was proposed to train solely via the expected loss by relying on imp...

---

### 25. Training Calibrated Conditional Generative Models with a Sample-Only Coverage Loss

**Authors:** Benjamin Remy, Raphael Rossellini, Chihway Chang, et al.

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.15829v1) | 📄 [PDF](https://arxiv.org/pdf/2611.15829v1)

**Summary:** Conditional generative models have become the tool of choice for sampling posteriors in scientific inverse problems, where we seek to sample images or signals conditioned on a set of indirect and noisy measurements. Yet they are often overconfident, which is a critical failure in scientific applications where accurate uncertainty quantification is essential. Existing regularizers fall short in complementary ways: differentiable coverage objectives require the model's density and do not identify ...

---

### 26. A Latent Semiparametric Mixture Model for Robust Heterogeneity Learning in High Dimensions

**Authors:** Lyuou Zhang, Boxiang Wang, Lulu Wang, et al.

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.15827v1) | 📄 [PDF](https://arxiv.org/pdf/2611.15827v1)

**Summary:** Learning heterogeneity from high-dimensional data has become a fundamental task across many data-driven fields. Cluster analysis is a widely used unsupervised tool for this purpose, and many existing methods have been adapted to high-dimensional settings through sparsity constraints. In contrast to algorithmic approaches, model-based clustering offers clean theoretical guaranties and computational simplicity, but can be restrictive in practice due to its reliance on specific parametric distribut...

---

### 27. Global-Local and Window-Concatenated Functional Random Forests: Early and Late Fusion of Window-Specific Functional Principal Components

**Authors:** Fabrizio Maturo, Annamaria Porreca

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.15816v1) | 📄 [PDF](https://arxiv.org/pdf/2611.15816v1)

**Summary:** Functional random forests built on a single functional principal component decomposition of the whole domain may dilute features confined to short intervals, whose location is rarely known in advance. We propose two random forests based on window-specific functional principal components. The global-local functional random forest (GL-FRF) is a late-fusion method that stacks a tuned full-curve forest and one forest per window with penalised convex weights; it contains the full-curve forest as a fe...

---

### 28. From Link Prediction to Linear Community Detection: A Finite-Sample Guarantee for Graph Pretraining

**Authors:** Ying Chen, Zhangyang Wang, Yixuan He

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.15778v1) | 📄 [PDF](https://arxiv.org/pdf/2611.15778v1)

**Summary:** Link prediction (LP) is a standard pretraining objective for graph neural networks (GNNs): hide edges, train an encoder-decoder to predict them, and reuse the node embeddings for downstream node tasks. Despite its empirical success, there is little quantitative theory explaining why an edge-level objective should produce embeddings that are linearly useful for node classification. We study this question in the finite-sample stochastic block model (SBM). For any bounded GNN encoder paired with a ...

---

### 29. Conformal prediction for censored life history data

**Authors:** Lu Mao

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.15724v1) | 📄 [PDF](https://arxiv.org/pdf/2611.15724v1)

**Summary:** We consider individual prediction of general summaries of a multistate trajectory, such as time alive out of hospital or time spent in remission. Right censoring complicates calibration because these outcomes may be only partially observed. We develop a conformal prediction approach for scalar and vector summaries over a fixed clinical horizon supported by follow-up. For each candidate region, we define the coverage determining time as the earliest time at which the observed history establishes ...

---

### 30. Learning Mixtures of Exponential Family

**Authors:** Mansi Sood, Devavrat Shah

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.15698v1) | 📄 [PDF](https://arxiv.org/pdf/2611.15698v1)

**Summary:** Motivated by causal inference and physical computing systems, we consider the problem of learning mixture of two bounded-support exponential-family distributions with a shared interaction parameter matrix and mixture component-specific linear parameter vectors. The unknown sequence of component labels belongs to a known structured class. We propose an estimator based on a convex loss that avoids the log-partition function; for each fixed label assignment, estimation is a convex optimization prob...

---

### 31. Sampling the Funnel: A Comprehensive Survey of Hamiltonian Monte Carlo for Hierarchical Bayesian Inference

**Authors:** Miguel Fernandez-de-Retana, Aitor Almeida

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.15634v1) | 📄 [PDF](https://arxiv.org/pdf/2611.15634v1)

**Summary:** Hierarchical models are central to applied Bayesian statistics, yet the variance structures they depend on can produce posterior geometries that remain difficult to explore even with Hamiltonian Monte Carlo (HMC), a designation now covering a large and increasingly heterogeneous family of algorithms. This survey uses Generalized HMC as an organizing framework to describe the many variants of HMC, their methodological and computational properties, and their empirical consequences. Varying the tra...

---

### 32. FADO: Learning Causal Explanations with Prior-Fitted Networks

**Authors:** Seth Flaxman, Jess Carr, Annabel Jakob, et al.

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.15607v1) | 📄 [PDF](https://arxiv.org/pdf/2611.15607v1)

**Summary:** In regression and classification tasks with tabular datasets, most of the literature on explanation in ML (e.g. SHAP, permutation importance) has focused on predictive attribution: does feature $X_i$ help predict outcome $Y$? At its heart, predictive attribution captures correlation, not causation. We instead ask a causal question: would manipulating feature $X_i$ change outcome $Y$? We define a natural quantity to answer this question, the feature intervention effect: $Δ_i = E[Y\mid do(X_i=+1)]...

---

### 33. Bet Imaginatively, not Historically in Independent-Data Sequential Testing

**Authors:** Nathaniel Xu, Feng Liu, Danica J. Sutherland

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.15456v1) | 📄 [PDF](https://arxiv.org/pdf/2611.15456v1)

**Summary:** Sequential testing avoids some of the many controversies and drawbacks related to traditional batch testing with p-values. In particular, the testing by betting paradigm has developed rapidly in recent years; it frames the level of evidence against the null as the wealth of a player in a betting game. Naturally, how much a player should bet is a key consideration, and should reflect their confidence in what they know about the next observed data point. Much current work uses standard betting str...

---

### 34. Sharp Gaussian approximation for Polyak--Ruppert averaged linear stochastic approximation

**Authors:** Bogdan Butyrin, Eric Moulines, Alexey Naumov, et al.

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.15442v1) | 📄 [PDF](https://arxiv.org/pdf/2611.15442v1)

**Summary:** We study how quickly the normalized Polyak--Ruppert average approaches its Gaussian limit in linear stochastic approximation with bounded i.i.d.\ coefficients. For step sizes decaying as $k^{-γ}$, with $1/2\leγ<1$, we prove an upper bound of order $n^{γ-1}$ on the approximation error over convex sets in fixed dimension. A matching lower bound holds for every fixed model. The fastest rate in this range is $n^{-1/2}$, attained at $γ=1/2$. We also obtain an $O(n^{-1/2})$ bound on the error of the r...

---

### 35. Non-normal Limits and Joint Calibration of Cross-fitted Heterogeneity Tests

**Authors:** Even He, Zaizai Yan

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.15333v1) | 📄 [PDF](https://arxiv.org/pdf/2611.15333v1)

**Summary:** Cross-fitting is used to test whether a ranking learned in a randomized experiment separates units that benefit from treatment from those that do not: each fold is ranked by a model fitted to the other folds, and the standardized difference in estimated effects between units ranked high and low is compared with a normal distribution. Under the null hypothesis of no heterogeneity the ranking is determined by noise, and because each fold helps to rank the others the fold estimates are dependent. W...

---

### 36. Sharp Covering-Number Bounds for Feedforward ReLU Networks via Parameter Symmetries

**Authors:** Ruizhi Deng, Guohao Shen, Tangrui Xiong

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.15300v1) | 📄 [PDF](https://arxiv.org/pdf/2611.15300v1)

**Summary:** In neural networks, distinct parameter configurations often realize the same input--output mapping, indicating that nominal parameter counts can overstate functional complexity. In this paper, we characterize the parameter-space symmetries of ReLU and Leaky ReLU networks across fully connected, convolutional, and residual architectures. We prove that every quasianalytic parameter map preserving the network function is a composition of positive channel scaling and channel permutation. By quotient...

---

### 37. Communication-Efficient Federated Multi-View Clustering via View-Aware Quantization

**Authors:** Khadija Ardif, Meryeme Ayache, Nidal Nasser, et al.

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.15270v1) | 📄 [PDF](https://arxiv.org/pdf/2611.15270v1)

**Summary:** Federated multi-view clustering (FedMVC) has recently attracted increasing attention for its ability to exploit complementary clustering structures across multiple clients while preserving data privacy. However, existing FedMVC methods often suffer from high communication overhead due to the repeated transmission of high-dimensional representations, which limits their scalability in practical federated systems. Moreover, different views may contribute unequally to the clustering performance, cal...

---

### 38. Winter wheat improves soil carbon sequestration with reduced gains in warmer climates

**Authors:** Georgios Giannarakis, Vasileios Sitokonstantinou, Dimitrios Bormpoudakis, et al.

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.15232v1) | 📄 [PDF](https://arxiv.org/pdf/2611.15232v1)

**Summary:** Sustainable agricultural intensification requires a precise understanding of how land use decisions influence soil organic carbon (SOC) sequestration under varying environmental conditions. We apply causal machine learning to evaluate the heterogeneous impact of winter wheat-based rotations on SOC at the field-level across Lithuania. Using a nationwide dataset collected over five years (2018-2022), including crop types, management practices, soil properties, and environmental conditions, we esti...

---

### 39. Common-DAG Support from Targeted Covariance Changes under Confounding

**Authors:** Peida Li

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.15052v1) | 📄 [PDF](https://arxiv.org/pdf/2611.15052v1)

**Summary:** Targeted covariance changes couple structural rows through a common directed acyclic graph. We study the graph support determined by these experiments when structural errors may be correlated. A positive-gap four-node family has a shortcut identified by common acyclicity. A response indegree of at most two additionally gives unique complete support and two compatible coefficient matrices. The same experiments admit a stable feedback model with the shortcut absent. The result extends to connected...

---

### 40. Understanding the Asymptotic Transience of Q-Learning via Distributional Expansion

**Authors:** Shengbo Wang

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.14926v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14926v1)

**Summary:** Q-learning has been empirically observed to exhibit substantial transient error. This transient remains uncaptured by the leading Gaussian limit because the central-limit normalization removes the smaller-scale displacement generated by the initial nonlinear evolution. On the other hand, worst-case finite-sample guarantees, while accounting for transient effects, can obscure the mechanisms responsible for the error on a particular problem instance. We develop a finer asymptotic analysis that giv...

---

### 41. Nested Ensemble Learning with Topological Data Analysis for Graph Classification and Regression

**Authors:** Innocent Abaa, Umar Islambekov

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.14900v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14900v1)

**Summary:** We propose a nested ensemble learning framework that utilizes Topological Data Analysis (TDA) to extract and integrate topological features from graph data, with the goal of improving performance on classification and regression tasks. Our approach computes persistence diagrams (PDs) using lower-star filtrations induced by three filter functions: closeness, betweenness, and degree2 centrality. To overcome the limitation of relying on a single filter, these PDs are integrated through a data-drive...

---

### 42. Almost Optimal Lower Bounds under Almost ETH for Approximating Euclidean k-means

**Authors:** Karthik C. S., Dor Minzer

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.14892v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14892v1)

**Summary:** In the Euclidean $k$-means problem, we are given a set of $n$ points in $\mathbb{R}^d$, and the goal is to find $k$ representative points in space so as to minimize the sum of the squared distances from each point to its closest representative. Algorithmically, de la Vega, Karpinski, Kenyon, and Rabani [STOC'03] and Kumar, Sabharwal, and Sen [JACM'10] obtain a $(1+\varepsilon)$-approximation for high-dimensional Euclidean $k$-means in time $2^{(k/\varepsilon)^{O(1)}} \cdot dn^{O(1)}$, which was ...

---

### 43. Characterizing Local Breadth in Language Generation

**Authors:** Jon Kleinberg, Fan Wei

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.14887v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14887v1)

**Summary:** Large language models sharpen the validity--breadth trade-off: a generator should avoid hallucinations without collapsing onto a narrow set of valid outputs. We study generation from positive examples of an unknown target in the Kleinberg--Mullainathan model, with arbitrary, possibly adversarial order and no distributional or computational assumptions. Breadth is measured by lower Banach density, which rules out arbitrarily large sparse holes, unlike prefix-based lower asymptotic density.   1. E...

---

### 44. Synthetic Data Augmentation for Fairness under Data Imbalance: Theory and Adaptive Allocation

**Authors:** Zhengchi Ma, Kaifeng Zhang, Anru R. Zhang

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.14870v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14870v1)

**Summary:** Data imbalance across sensitive groups and class labels is common in classification problems and can contribute to substantial fairness disparities. We study how such imbalance affects Equal Opportunity and how synthetic data augmentation can mitigate the resulting unfairness. We first identify two mechanisms, prevalence imbalance and group-size imbalance, through which changes in the training distribution shift the learned decision boundary and induce disparities in group true positive rates. M...

---

### 45. Improved last-iterate bounds for SGD with and without replacement

**Authors:** Yimin Zhong, Jiaxin Zhou

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14811v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14811v1)

**Summary:** In this work, we study last-iterate convergence bounds for stochastic gradient descent (SGD) on convex and $β$-smooth loss functions and improve the bound from $\cO((\log T)^3/T)$ to $\cO((\log T)^3/(T\log\log T))$ in the interpolation regime. The improvement comes from applying a horizon-dependent multiscale estimate of gradients to the comparison of trajectories. The bound applies to both sampling with replacement and sampling without replacement within one pass.

---

### 46. Don't Match the Noise: Distribution Matching under Unknown Measurement Error with an Audit Sample

**Authors:** Arya Farahi, Ritwik Vashistha

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14749v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14749v1)

**Summary:** Real-world machine learning systems often operate on imperfect measurements: sensors are noisy, annotations are produced by non-experts, and scientific observations are often indirect. In these settings, classic distribution comparison tools such as maximum mean discrepancy (MMD) can be systematically biased, matching artifacts of the measurement process rather than the underlying mechanisms of interest. We study a practical regime in which noisy observations are abundant, but only a small audit...

---

### 47. Robbing Peter to Pay Paul: Cross-Attribute Externalities of Fairness Interventions

**Authors:** Fernandes Machado Agathe, Jamotton Charlotte, Charpentier Arthur

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14717v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14717v1)

**Summary:** Fairness interventions often targets disparities associated with a single sensitive attribute in binary classification tasks. However, when multiple sensitive attributes are associated with a data subject, improving fairness with respect to one attribute does not necessarily improve it across all attributes: it may exacerbate disparities associated with other sensitive attributes, including those that are unavailable to the practitioner. We refer to these unintended effects as cross-attribute ex...

---

### 48. Code as Explanations: Executable and Verifiable LLM Explanations

**Authors:** Nhi Nguyen, Shauli Ravfogel, Rajesh Ranganath

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14704v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14704v1)

**Summary:** As large language models (LLMs) increasingly make consequential decisions and solve problems alongside humans, we must understand how models arrive at their conclusions. Understanding how an LLM behaves requires observing it across multiple inputs, yet free-text explanations such as chain-of-thought (CoT) are generated per instance and cannot be easily verified on new inputs. We propose {code explanations to address the mismatch in how LLM explanations are generated versus how they are evaluated...

---

### 49. Thompson Sampling using Prior-fitted Diffusion Transformers

**Authors:** Sihwa Park, Jingsen Zhu, Vinamr Jain, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14656v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14656v1)

**Summary:** Thompson sampling is natural randomized strategy for optimizing unknown functions in a black-box manner. In continuous global optimization, Thompson sampling has largely been restricted to Gaussian process priors, as these are essentially the only class for which computing the posterior distribution has been tractable in practice. In this work, we introduce \emph{prior-fitted diffusion transformers}, which are diffusion models that perform Thompson sampling in-context at inference time, after be...

---

### 50. TorchCurves: Differentiable Parametric Curves

**Authors:** Alex Shtoff

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14516v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14516v1)

**Summary:** We present TorchCurves, a PyTorch library that treats vector-valued parametric curves as learnable primitives. Its central operation maps batches of scalar inputs to points on curves represented in B-spline or Legendre polynomial bases, with differentiation through both inputs and coefficients. Curve coefficients can be optimized jointly with the surrounding model or produced by another network. The library provides trainable modules, reusable basis modules, and a functional interface, supportin...

---

