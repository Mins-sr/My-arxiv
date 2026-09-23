# arXiv Daily Digest - 2026-09-23

Total papers: 300

---

## cs.AI

**50 papers**

### 1. SpeakerMem-R1: Speaker-Centered Dual-Track Memory for Multi-Party Dialogue

**Authors:** Haobo Zheng, Tan Tang, Yan Chen, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26780v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26780v1)

**Summary:** Long-term conversational memory in multi-party settings requires more than retrieving relevant content from long-term conversations: it must distinguish who said what, whom each statement concerns, how individuals perceive one another, what information is shared by the group, and how states change over time. Recent studies on multi-party dialogue benchmarks show that existing general-purpose LLM memory systems tend to lose person and group relations or struggle to integrate clues distributed acr...

---

### 2. CliffCompaction: Cost-Efficient Compaction for Long-Horizon Coding Agents

**Authors:** Trang Nguyen, Eulrang Cho, Bingqing Chen, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26779v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26779v1)

**Summary:** Agents often work on complex problems that require millions of tokens of context, which necessitates compacting across sessions due to limited context windows. We develop CliffCompaction, an autocompaction technique that reduces cost by up to 50% under a bounded context while maintaining or improving performance on Terminal-Bench and achieving new levels of efficiency for test-time scaling and state-of-the-art results on KernelBench. The per-rollout savings of CliffCompaction make the performanc...

---

### 3. SWE-Serve: Benchmarking Agentic Engineering For Production Inference Serving

**Authors:** Jennifer Williams, Dave Farris, Jeff Farris, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26777v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26777v1)

**Summary:** We introduce SWE-Serve, a benchmark for evaluating agents on production inference engineering tasks. Implementing an inference feature can require coordinating multiple changes across the serving stack, including model support, runtime execution, and public APIs. Existing benchmarks provide limited coverage of production inference engineering: repository-level software engineering benchmarks do not target inference, while general terminal-agent benchmarks include only a few inference tasks. Dedi...

---

### 4. A2M: Trace-Optimized Agent Hijacking in the MCP Ecosystem

**Authors:** Laizhen Li, Xuan Wang, Peicheng Zhao, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26761v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26761v1)

**Summary:** Agents using the Model Context Protocol (MCP) rely on semantic matching to select tools from third-party servers, exposing a semantic supply-chain risk through attacker-controlled metadata and outputs. We introduce A2M (Attraction-to-Manipulation), a two-stage black-box framework for hijacking MCP agents. The Attraction phase optimizes tool metadata to increase invocation probability; the Manipulation phase uses execution traces to refine adversarial tool returns that steer agents toward attacke...

---

### 5. Grow the Harness, Not the Context: From Strategy-Free Scaffolds to Reusable Specialist Agents

**Authors:** Laizhen Li, Jiarui Li, Juanjuan Zhao, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26760v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26760v1)

**Summary:** Large language model (LLM) agents often handle streams of related tasks, yet standard harnesses repeatedly ask the model to reconstruct the same control decisions inside each task's context. We study whether task feedback can instead turn recurring control into reusable executable code, while reserving LLM calls for task-specific semantic reasoning. We introduce Growing Harness, a failure-guided training paradigm that learns the agent harness itself from a strategy-free scaffold that exposes fix...

---

### 6. Type-Safe Is Not Error-Free: A Constrained Decision Head Follows the Option Name, Not the Rubric Bound to It

**Authors:** Yu Sun, Junhao Xu

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26758v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26758v1)

**Summary:** Typed decision models are built for settings where model outputs are consumed directly by software. Instead of generating free-form text, they return a decision over a predefined set of options. By construction, every output conforms to the required schema. Yet this guarantee does not tell us whether the model interprets the options as intended. We study Jev and two Jev-like models with open weights by changing how option names are assigned to rubrics. Each option consists of an option name and ...

---

### 7. FleXray: Universal Clinical X-ray Segmentation

**Authors:** Victor Ion Butoi, Vivek Gopalakrishnan, John V. Guttag, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26756v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26756v1)

**Summary:** X-ray is medicine's most widely used imaging modality, yet remains among its least quantitative. Unlike volumetric modalities like CT or MRI, X-ray collapses 3D anatomy into a 2D projection, causing structures to overlap and anatomical boundaries to be ambiguous, even to experts. As a result, labeling X-ray databases for training general-purpose segmentation systems is impractical, leaving morphometric and functional X-ray analysis confined to narrow anatomical regions and applications. To this ...

---

### 8. Metrics Failure in LLM-Based Code Vulnerability Repair: An Empirical Study and a Change-Aware Screen

**Authors:** Om Nepal, Sushant Aryal, Oluseyi Olukola, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26749v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26749v1)

**Summary:** Large language models (LLMs) are increasingly applied to the automated repair of C/C++ security vulnerabilities, and compile rate is a commonly reported proxy for progress: whether the generated patch compiles. We argue that compile rate is a scientifically unreliable metric for single-function vulnerability repair, and we support this with five controlled experiments over 203 vulnerable functions from Big-Vul, three open-source code LLMs (350M to 6.7B parameters), and three prompting strategies...

---

### 9. Does AI Save Time on Product Design? A Randomized Controlled Experiment of AI Prompt-to-Design Workflows

**Authors:** Remy Stewart, Olabode Anise, Andrew Hogan, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26725v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26725v1)

**Summary:** AI tools for digital product design now offer prompt-to-design capabilities, allowing designers and their non-designer colleagues to create prototypes through conversational workflows with large language models (LLMs). While these tools promise time savings, experimental evidence in product design remains limited compared with evidence from software engineering. We conducted a randomized controlled trial with 50 product designers and 50 product managers to evaluate prospective time savings from ...

---

### 10. The Sirens' Song: When Proximal Background Context Overshadows Distant Evidence

**Authors:** Xiaoyu Yang, Jie Lu, Wei Duan, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26718v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26718v1)

**Summary:** Long-context LLMs focus on retrieving distant evidence from extensive context, yet existing work has largely focused on overcoming distance alone. In this work, we identify the Proximity Trap, insufficient attention to distant evidence often arises less from distance itself than from cumulative competition with abundant, task-irrelevant proximal background. To address the Proximity Trap, we introduce LYRA (Long-context heavY-tailed Relevance Alignment), a t-distributed directional matching mecha...

---

### 11. TraceVIC: Causal Reasoning over Code Evolution for Identifying Vulnerability-Inducing Commits

**Authors:** Fnu Tanish, Samiha Shimmi, Samikshya Chapagain, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26711v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26711v1)

**Summary:** Software vulnerabilities are often discovered long after they are introduced, making it difficult to identify the vulnerability-inducing commit (VIC) responsible for introducing the underlying vulnerable condition. Existing VIC identification techniques largely rely on git blame to trace vulnerable code through revision history and use positional heuristics, such as selecting its earliest or most recent modification. However, the true VIC may occur anywhere within this history, and vulnerable be...

---

### 12. Train Where the Quantized Model Goes: On-Policy Distillation for Low-Bit Reasoning

**Authors:** Yuanteng Chen, Zhilei Liu, Peisong Wang, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26708v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26708v1)

**Summary:** Quantization-aware distillation (QAD) restores much of the short-form question-answering performance lost to sub-3-bit quantization, yet leaves mathematical and code reasoning substantially impaired. Long generations often degenerate into repetitive loops, exhausting the decoding budget without completing a solution. We trace this gap to quantization-amplified exposure bias: QAD trains on fixed corpus prefixes, while quantization-induced deviations compound along the model's own autoregressive t...

---

### 13. Beyond Repeated Sampling: Learning Search Policies for LLM Reasoning

**Authors:** Ismail Labiad, Matthieu Kowalski, Marc Schoenauer, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26704v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26704v1)

**Summary:** Large language models increasingly tackle hard reasoning problems by spending more test-time compute, yet the dominant strategy remains naive repeated sampling: draw many independent solutions and hope one is correct. Because such sampling explores only through local decoding noise, it tends to produce many near duplicate attempts rather than genuinely different ideas. We ask whether exploration can instead be steered at a semantic level, by first sampling problem specific concepts, hints, or st...

---

### 14. Measuring the Serving Stack Instead of the Model: Hidden Confounds in Local Tool-Use Evaluation

**Authors:** Lijuan Tang, Yuemeng Zheng

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26693v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26693v1)

**Summary:** A coding agent must emit a valid tool call--a parseable invocation of a tool in the provided schema--before the harness can execute its chosen action. We study how local serving stacks affect this protocol step and show that measured outcomes can depend on the serving layer rather than model behavior alone. In Ollama, the default tools= request is gated per model by a static template flag: some models are accepted and return calls as text, some return native tool_calls, while Phi-3 and Gemma-3 a...

---

### 15. From Alignment to Access Control: A Framework for GenAI Policy Enforcement

**Authors:** Nathalie Baracaldo

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26682v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26682v1)

**Summary:** Generative AI (GenAI) applications have flourished enabling users to chat with large language models, and to create agents to act on their behalf for a variety of tasks. The pace of development of capabilities in this field is incredibly fast with security and safety taking a back seat. Unfortunately, the slower pace at which security and safety mechanisms have evolved has led to real incidents. Policy enables the definition of desirable behavior of applications, and for that reason, it is a cor...

---

### 16. A Spectral Theory of Grokking: Weight Decay induces Feature Learning

**Authors:** Lenz Pracher, Pascal de Jong, Oskar Lieshaus, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26679v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26679v1)

**Summary:** In grokking an early fit to the training data separates from a much later improvement in generalization. During this delay, training can move from a fixed neural tangent kernel (NTK) regime to one in which task-relevant kernel eigendirections continue to evolve. We provide a quantitative theory for how this transition from lazy to rich learning can produce delayed generalization. For homogeneous networks trained with squared loss and $L_2$ weight decay, we show that a finite residual remains aft...

---

### 17. The Delegation Blind Spot: Auditing Product Decisions from Agent Choices

**Authors:** Shivam Gupta

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26642v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26642v1)

**Summary:** Successful agent execution need not identify which future product improvement its user would value. We present a decision-specific audit that maps a declared observation channel and product-value contrast to compatible intervals and witness populations. Its foundations are established identification and decision theory; the contribution is an executable measurement workflow and a controlled study of its limits. A frozen experiment makes 4,800 requests to two pinned model snapshots on shared synt...

---

### 18. Capable yet Parsimonious: Extracting and Characterizing Hidden Chain-of-Thought in Frontier Models

**Authors:** Xiaoyu Luo, Tao Ren, Wenrui Yu, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26637v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26637v1)

**Summary:** The rapid capability gains of frontier language models are widely attributed to improved reasoning abilities, yet this cannot be verified as raw CoT traces in closed-source systems are hidden. By registering a simple custom tool through a standard API feature, we induce frontier models to externalize intermediate reasoning. Because these traces may reflect post-hoc rationalization rather than genuine reasoning, we first evaluate against native CoT on open-source models and extend to closed-sourc...

---

### 19. Greedy Decoding Is Not Precision-Invariant: Cross-Precision Output Divergence in LLM Inference

**Authors:** Gaoyuan Du, Anam Nawaz Khan, Rex Zhou, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26621v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26621v1)

**Summary:** Greedy decoding from large language models is commonly treated as deterministic. We show it is not precision-invariant: the same model, prompt, and decoding algorithm produce different outputs in BF16 versus FP16 on identical hardware. Across our evaluations of six models (1.1B-7B parameters, four families; divergence additionally characterised at 12B) and three benchmarks, 49-100\% of prompts diverge; a single token flip often cascades into trajectory-level divergence. We develop an empirical e...

---

### 20. Towards Hierarchical GNNs for multi-grid power flow: generalization across operating scenarios

**Authors:** Carmine Delle Femine, Leire Garin Atxaga, Asier Diaz-Iglesias, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26603v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26603v1)

**Summary:** Hierarchical latent communication improves the generalization of a multi-grid power-flow model to new operating scenarios. The module exchanges information through two reduced graphs within a GENCO-based corrective network. We compare Kron-derived transports, a same-anchor Quotient construction and a flat backbone in preliminary trainings of 200 epochs on three grid topologies, with three initialization seeds per model. Evaluation uses 200 newly generated, preselected scenarios per grid. On the ...

---

### 21. Receptiveness, Not Sycophancy: Distinguishing Engagement from Deference in Language Models

**Authors:** Calvin Isley, Johann Gaebler, Max Lamparth, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26579v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26579v1)

**Summary:** A central concern with language models is sycophancy: their tendency to defer to users' views at the expense of independent substantive judgment. In parallel, work on social sycophancy has focused on behaviors such as validation and positivity that may signal inappropriate deference. Yet the markers of social sycophancy are also characteristic of conversational receptiveness, a construct from social psychology shown to improve interactions across disagreement. We argue that this overlap creates ...

---

### 22. Quantum-Aided Active Device Detection in Energy-Harvesting Symbiotic Radio Networks

**Authors:** Remon Polus, Deemah Tashman, Soumaya Cherkaoui

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26565v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26565v1)

**Summary:** Massive connectivity in next-generation networks demands energy- and spectrum-efficient solutions for large-scale Internet of Things (IoT) deployments. Symbiotic radio (SR) enables passive IoT devices to communicate by backscattering existing cellular transmissions. A key challenge in uplink SR is active device detection (ADD), which directly affects decoding reliability, interference management, and system throughput. We propose an energy-harvesting code-domain non-orthogonal multiple access (N...

---

### 23. The Disciplinary Language Transfer Problem: How Psychological Vocabulary Produces Governance Failures in AI Agent Deployment

**Authors:** Kymberly Lasser-Chere, Tyler Akidau, Marc Millstone

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26562v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26562v1)

**Summary:** The vocabulary used to describe AI agents in governance contexts -- learning, memory, values, compliance, identity, trust -- is borrowed from psychological and organizational science, contributing to systematic failures in how organizations deploy, oversee, and hold agents accountable. This paper argues that the problem is not merely terminological but epistemological: psychological vocabulary carries an "invisible grammar" of its home discipline into governance discourse, calibrating frameworks...

---

### 24. Neutral-Atom-based Quantum Optimization for Resource Allocation in NOMA Networks

**Authors:** Patatchona Keyela, Remon Polus, Soumaya Cherkaoui, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26556v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26556v1)

**Summary:** In wireless communication networks, many resource optimization problems are nondeterministic polynomial-time hard (NP-hard) due to their combinatorial nature and high computational complexity. Recently, neutral-atom-based quantum computing has emerged as a promising platform for efficiently solving such problems by leveraging quantum superposition and entanglement. However, its application to wireless communication optimization problems remains largely unexplored. In this paper, we investigate t...

---

### 25. JEV-as-a-Judge: Accept When Confident, Escalate When Unsure

**Authors:** Yubo Li, Yidi Miao, Ramayya Krishnan, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26550v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26550v1)

**Summary:** LLM-as-a-judge enables evaluation across diverse tasks, but inference cost and confidence reliability become critical at scale. We study whether a decision-only judge can provide an economical first pass and identify when stronger evaluation is needed. Comparing jev-as-a-judge with sixteen generative and reward-model judges, with blinded human adjudication, we find it within three percentage points of a state-of-the-art LLM judge, our strongest comparator, on ordinary preference and evidence-gro...

---

### 26. Topology-Stratified Materials Discovery with A Flow-Based Generative Model

**Authors:** Jingyi Zhou, Oyshee Chowdhury, Noah Oyeniran, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26547v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26547v1)

**Summary:** Accurate generation of crystal structures is the foundation to the discovery of high-performance materials for extreme-environment applications, such as aerospace, additive manufacturing, and fusion energy systems. Although generative modeling has emerged as a promising approach for crystal design, its performance remains limited by the complex crystal structures and diverse chemical compositions. In this work, we develop UFO-MGen, a universal flow-based generative model that learns topological ...

---

### 27. REFLEX with Jev for Efficient Selective Control in LLM Agents

**Authors:** Tiantong Wu, Wei Yang Bryan Lim

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26532v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26532v1)

**Summary:** LLM agents often use generative models for bounded decisions, raising the question of when these decisions can be handled more efficiently without reducing task success. We study REFLEX, an agent architecture that uses Jev as a fast, typed decision layer and calls a strong LLM when confidence is low, or generation is required. On a frozen 100-task benchmark, REFLEX achieves 95% success with 72.7% fewer strong-model calls than a strong-only agent, with reductions persisting across three fallback ...

---

### 28. A Semiotics-Aware Framework for Evaluating Fidelity and Coverage in Natural Language Generation

**Authors:** Lorenzo Zangari, Davide Picca

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26527v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26527v1)

**Summary:** When two texts describe the same expression, standard metrics based on lexical overlap or whole-text similarity may fail to detect meaningful differences in how that expression is framed. We propose a framework to evaluate semiotic alignment between texts, where a semiotic profile encompasses both the contextual meaning and the discourse references made salient by a text. Our approach yields two scores, Semiotic Fidelity and Semiotic Coverage, estimating how much of one text's profile is support...

---

### 29. Do Vision Model See Like the Brain? A Comparison Across EEG Encoding Model

**Authors:** Shashank Baghel, Kshitij Dwivedi, Dinesh Singh, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26512v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26512v1)

**Summary:** Convolutional neural networks (CNNs) and vision transformers are both used to model the human visual system, but whether the two architectures diverge at a specific point in network depth is unclear. We compared six CNNs and two vision transformers by computing the Pearson correlation (r) between each model's predicted and measured EEG response at every layer or block, in ten participants viewing 200 natural images. For the transformer models, we also tested four token representations, from the ...

---

### 30. The Ethics of Artificial Intelligence in Military Operations

**Authors:** Nicolas Drapier, Florian Mauberger, Aladine Chetouani, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26507v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26507v1)

**Summary:** Deep learning systems now mediate military decisions to use force, yet their internal logic resists inspection, their evaluation practices are gameable, and their deployment fractures accountability across dispersed stakeholders. The ethical challenge posed by these systems is fundamentally epistemic: not just whether autonomous weapons should be permitted to kill, but whether the conditions for responsible human judgment can survive when critical functions are delegated to opaque algorithms.   ...

---

### 31. Radiomics-Conditioned Modulation of RenalCLIP Features for Clear Cell Renal Cell Carcinoma Classification

**Authors:** Yuan Liang, Sourav Bhattacharjee, Abraham Campbell

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26492v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26492v1)

**Summary:** Radiomics provides quantitative descriptions of tumour appearance that may complement disease-specific foundation models in small labelled cohorts. We investigate this complementarity for computed tomography-based classification of clear cell renal cell carcinoma. Our framework uses radiomics to modulate RenalCLIP features through feature-wise linear modulation (FiLM), while retaining a direct radiomics contribution. Internal testing and external validation compare it with conventional fusion st...

---

### 32. When Recursive Models Finish Computing

**Authors:** Hare Krishna, Shubham Singh, Stephen Ebert, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26487v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26487v1)

**Summary:** Recursive models can continue updating their latent states beyond their nominal inference budget, so an incorrect output at that budget does not show whether computation is unfinished or has entered a persistently unsuccessful regime. We study the dynamics of completion in attention- and MLP-based Tiny Recursive Models (TRMs) on 1,000 hard Sudoku puzzles. Extending recurrence from the nominal 16 steps to 512 steps increases cumulative exact-solve accuracy from 59.2% to 87.5% for the attention mo...

---

### 33. Not Quite My Tempo: Voice Activity-aware Speech Synthesis for Lip-Synchronous Dubbing

**Authors:** Alejandro Pérez-González-de-Martos, Florian Lux, Angelina Elizarova, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26486v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26486v1)

**Summary:** Automatic lip-synchronous dubbing requires a speech synthesis model to generate alternating voice and silence patterns in the target language that match the timing of the source clip precisely to ensure an optimal viewing experience. Prior works address this problem by conditioning the speech synthesis process on lip movements extracted from the video signal. In this work, we condition the speech generation on a binary voice-activity signal, which has a lightweight representation and can be prod...

---

### 34. FeatLens: Feature-Guided Dynamic Code Graph Construction and Retrieval for Repository-Level Code Generation

**Authors:** Xutian Li, Bo Xiong, Yifeng Zhu, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26480v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26480v1)

**Summary:** Recent code generation research has moved from isolated function completion toward repository-level generation in existing codebases. To implement a target function correctly, an LLM must identify reusable repository dependencies such as existing functions, APIs, and cross-file definitions. Existing retrieval methods provide such context through code similarity search, persistent whole-repository graphs, or LLM-driven graph exploration, but often incur high graph construction, reasoning, and tok...

---

### 35. PP-Net: A Hybrid Physical-Prior Neural Network for Scattered Light Removal in Biomedical Images on Embedded Devices

**Authors:** Yongfei Guo, Tingjin Chu, Mengzhuo Liu, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26474v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26474v1)

**Summary:** Scattered light is common in biomedical images, yet its removal remains challenging. The difficulty arises from three aspects: first, aligned scattered-light-free biomedical ground truth is often unavailable; second, scattering is coupled with weak illumination and sensor-induced noise; and third, many learning-based restoration models are computationally expensive for embedded devices in Internet of Medical Things (IoMT) scenarios. To address these issues, this paper proposes PP-Net, a hybrid p...

---

### 36. Complementary Roles of Radiomics and Foundation Representations in Renal Cell Carcinoma Classification: A Comparative Study of 2D and 3D CT Encodings

**Authors:** Yuan Liang, Sourav Bhattacharjee, Abraham Campbell

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26463v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26463v1)

**Summary:** Accurate preoperative subtype classification of renal cell carcinoma (RCC) from contrast-enhanced computed tomography remains clinically challenging. Radiomics provides structured tumour descriptors, whereas foundation representations offer transferable image features. However, it remains unclear whether radiomics still adds value beyond pretrained representations, and how 2D and 3D MedVAE encoders compare in this setting.   We compared handcrafted radiomics, 2D MedVAE, 3D MedVAE, and their fusi...

---

### 37. Reproducible AI Requires Reproducible Randomness

**Authors:** Anthony Bertrand, Tom Schmitt, Engelbert Mephu Nguifo, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26461v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26461v1)

**Summary:** Pseudorandom number generators (PRNGs) constitute indispensable computational tools across multiple scientific domains, including Monte Carlo simulations, stochastic computing, and artificial intelligence (AI). The reproducibility of such applications critically depends on the ability of PRNG implementations to generate identical sequences across software environments when initialized from the same internal state. These algorithms enable the simulation of stochastic processes while providing det...

---

### 38. Recursive self-improvement of AI research agents

**Authors:** Dhruv Srikanth, Bingchen Zhao, Dixing Xu, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26457v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26457v1)

**Summary:** AI agents are beginning to automate research and development across the AI stack, from improving training efficiency to optimizing inference. A natural next step is to improve the research efficiency of the agents themselves. When an AI research agent's own code is the object of optimization, each accepted rewrite becomes the agent that the next round edits. We refer to this loop as recursive self-improvement. Its significance lies in a long-standing trend, in which increased cumulative spending...

---

### 39. The Source of Disturbance Matters: External, Internal, and Control-Generated Noise in Adaptive Regulation

**Authors:** Veronique Ziegler

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26428v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26428v1)

**Summary:** Adaptive regulation can itself perturb the state it is intended to stabilize. In replicated simulations of an adaptive agent, we compare external disturbance, persistent internally generated disturbance, and control-generated disturbance under regulation-first and disturbance-first ordering. Persistent internal disturbance produces the largest exposure and regulatory burden within the tested parameter grid. When positive controller updates generate an immediate disturbance cost, increasing that ...

---

### 40. DeepFEAv2: Deep Learning for Transient Finite Element Analysis Beyond Structured Meshes

**Authors:** Georgios Triantafyllou, Panagiotis G. Kalozoumis, Dimitris K. Iakovidis

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26426v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26426v1)

**Summary:** Finite Element Analysis (FEA) is widely used for transient mechanical simulations, but its high computational cost limits real-time and high-resolution applications. Deep learning surrogate models can reduce this cost; however, many existing approaches are restricted to steady-state prediction or cannot jointly predict Node- and Element-based Outputs (NEO) over time. The state-of-the-art DeepFEA framework has addressed these issues but remains limited to structured finite element (FE) meshes. To...

---

### 41. QuantWM: Temporally Consistent 2-Bit KV Cache Quantization for World Models and Video Generation

**Authors:** Jiaqi Zhao, Xiaobin Hu, Bo Yin, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26425v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26425v1)

**Summary:** KV cache memory has become a major deployment bottleneck for video generation and world models, which motivates low-bit quantization study for efficiency. Existing 2-bit KV cache quantization methods can achieve nearly lossless performance on video benchmarks such as VBench, however, we find that they still cause severe temporal flickering and visual degradation. Meanwhile, deeper investigates show that Key quantization produces smaller reconstruction errors than Value, but surprisingly leads to...

---

### 42. Reliability Theory for AI Control

**Authors:** Grant Molnar

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26419v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26419v1)

**Summary:** Reliability theory gives a mature language for layered systems, but its formal tools are not yet standard in frontier AI control. We apply them to Google DeepMind's defenses against rogue deployment. The same control stack can have cubic, quadratic, or linear rare-failure suppression depending on its failure domains. Birnbaum importance identifies which component improvements buy the most nominal reliability, while prevention changes the population on which recovery is demanded. These results gi...

---

### 43. TimeInteract: Towards Real-Time Interactive Intelligence for Streaming Time Series

**Authors:** Sheng Pan, Yongli Gu, Yiqing Guo, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26389v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26389v1)

**Summary:** Real-world time series evolve continuously, with meaningful changes potentially emerging at any moment. However, existing time-series language models (TSLMs) remain inherently static. They either receive complete sequences for offline processing or alternate between streaming input and response generation, which prevents processing of new observations during interaction. We introduce a new regime, Time-Series Interaction: a model continuously perceives incoming time-series observations and user ...

---

### 44. MAVP: Map-Aware Visuomotor Policies for Mobile Manipulation

**Authors:** Jinhe Tang, Ruixiao Dai, Weiming Zhi

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26378v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26378v1)

**Summary:** Successful mobile manipulation requires coordinated base and arm motion while maintaining accurate spatial positioning. However, demonstration-trained policies can struggle to realise the intended base motion reliably, leading to spatial misalignment and subsequent manipulation failures. We present MAVP (Map-Aware Visuomotor Policies), a framework that improves execution reliability by predicting explicit base-pose targets and tracking them using localisation feedback. MAVP reconstructs a static...

---

### 45. FairMean: Promoting Fairness in Distributed Learning under Label Poisoning Attacks

**Authors:** Huigan Zheng, Jiaojiao Zhang, Yongxiang Liu

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26377v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26377v1)

**Summary:** Fairness-aware distributed learning prioritizes clients with large losses to reduce performance disparities, but label poisoning can create large losses, thereby inducing a fairness--robustness conflict. We propose FairMean to manage this conflict. FairMean weights client gradients using a bounded, nondecreasing function of local loss. The increasing weights prioritize high-loss clients to promote fairness, while the upper bound prevents excessive loss-induced amplification of poisoned-client gr...

---

### 46. GitScholar: A Dataset for Predicting AI Research Impact from GitHub Engagement

**Authors:** Emilien Guandalino, Lorenz K. Müller, Beatrice Alessandra Motetti, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26361v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26361v1)

**Summary:** With the rapid pace of AI research and the hundreds of daily new publications, staying up-to-date with the latest developments has become increasingly difficult. For researchers, quickly identifying impactful work is essential, yet manually reviewing each new publication is impractical. Automated impact prediction methods help address this challenge, usually by combining various information sources available, such as a paper's content or citation history. In this work, we propose using GitHub en...

---

### 47. PACT: From Credit Assignment to Critic Alignment

**Authors:** Jiayan Fu, Hang Xu, Yong Zhang, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26355v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26355v1)

**Summary:** Reinforcement learning has become a central component of large language model (LLM) post-training, yet token-level credit lacks a generally accepted mathematical definition, leaving its relationship to commonly used training signals unclear. We formulate three regularity conditions, namely Completeness, Prefix Consistency, and Neutrality, and prove that they uniquely determine token-level credit. This characterization provides a unified basis for explaining phenomena across existing algorithms a...

---

### 48. TransBERT: A Framework for Synthetic Translation in Domain-Specific Language Modeling

**Authors:** Julien Knafou, Luc Mottin, Anaïs Mottaz, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26347v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26347v1)

**Summary:** The scarcity of non-English language data in specialized domains significantly limits the development of effective Natural Language Processing (NLP) tools. We present TransBERT, a novel framework for pre-training language models using exclusively synthetically translated text, and introduce TransCorpus, a scalable translation toolkit. Focusing on the life sciences domain in French, our approach demonstrates that state-of-the-art performance on various downstream tasks can be achieved solely by l...

---

### 49. Geometry-Aware Hyperbolic Residual Quantization

**Authors:** Alessio Colombo, Melika Ayoughi

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26342v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26342v1)

**Summary:** Residual Vector Quantization turns continuous representations into discrete, multi-level token sequences. Yet most methods operate in Euclidean space, despite the coarse-to-fine structure of the resulting codes and the latent hierarchies present in many data domains. Hyperbolic geometry offers a natural alternative for hierarchical representations, but naive hyperbolic extensions introduce geometric inconsistencies: non-associative hyperbolic addition prevents consistent residual aggregation, wh...

---

### 50. TriWorldBench: A Tri-View Consistency Perspective on Embodied World Models

**Authors:** Xuanyi Liu, Haofeng Wang, Ruiqi Li, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26314v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26314v1)

**Summary:** Embodied world models predict the outcomes of robot actions to support learning and planning. For robots equipped with head and wrist cameras, this requires complementary views: the head view captures the overall task, while wrist views reveal local gripper-object interactions. However, evaluating these views independently cannot determine whether they describe the same action and object state. We introduce TRIWORLDBENCH, a benchmark for evaluating embodied world models through synchronized head...

---

## cs.CL

**50 papers**

### 1. Flash-dLLM: IO-Aware KV Caching and Parallel Decoding for Fast, Memory-Efficient Diffusion LLMs

**Authors:** Quan Nguyen-Tri, Mukul Ranjan, Zhiqiang Shen

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26796v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26796v1)

**Summary:** Diffusion Large Language Models (dLLMs) have recently emerged as a promising alternative to autoregressive LLMs by enabling non-autoregressive text generation. However, their practical deployment remains limited by inefficient inference, largely due to the absence of effective Key-Value (KV) caching and scalable parallel decoding mechanisms. Existing acceleration methods typically study KV caching and parallel decoding in isolation, overlooking the I/O bottlenecks that arise when cache reuse and...

---

### 2. Agensh: Scaling Organizational Intelligence to 1,024 Agents

**Authors:** Zhihao Zhan, Ting Song, Li Dong, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26781v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26781v1)

**Summary:** A multi-agent system can reduce latency on complex tasks by executing work concurrently. Several pioneering harness frameworks support multi-agent systems. However, the scalability of current multi-agent harnesses is often constrained by a central orchestrator's capacity to allocate tasks and coordinate workers. To address this limitation, we introduce Agensh, a scalable self-organized multi-agent harness without a central orchestrator: concurrent workers execute a multi-agent cooperation loop, ...

---

### 3. SpeakerMem-R1: Speaker-Centered Dual-Track Memory for Multi-Party Dialogue

**Authors:** Haobo Zheng, Tan Tang, Yan Chen, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26780v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26780v1)

**Summary:** Long-term conversational memory in multi-party settings requires more than retrieving relevant content from long-term conversations: it must distinguish who said what, whom each statement concerns, how individuals perceive one another, what information is shared by the group, and how states change over time. Recent studies on multi-party dialogue benchmarks show that existing general-purpose LLM memory systems tend to lose person and group relations or struggle to integrate clues distributed acr...

---

### 4. Beyond Repeated Sampling: Learning Search Policies for LLM Reasoning

**Authors:** Ismail Labiad, Matthieu Kowalski, Marc Schoenauer, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26704v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26704v1)

**Summary:** Large language models increasingly tackle hard reasoning problems by spending more test-time compute, yet the dominant strategy remains naive repeated sampling: draw many independent solutions and hope one is correct. Because such sampling explores only through local decoding noise, it tends to produce many near duplicate attempts rather than genuinely different ideas. We ask whether exploration can instead be steered at a semantic level, by first sampling problem specific concepts, hints, or st...

---

### 5. Measuring the Serving Stack Instead of the Model: Hidden Confounds in Local Tool-Use Evaluation

**Authors:** Lijuan Tang, Yuemeng Zheng

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26693v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26693v1)

**Summary:** A coding agent must emit a valid tool call--a parseable invocation of a tool in the provided schema--before the harness can execute its chosen action. We study how local serving stacks affect this protocol step and show that measured outcomes can depend on the serving layer rather than model behavior alone. In Ollama, the default tools= request is gated per model by a static template flag: some models are accepted and return calls as text, some return native tool_calls, while Phi-3 and Gemma-3 a...

---

### 6. Detecting GPT-Assisted Writing Using Interpretable Stylometric Features

**Authors:** Rajesh Kumar, Nabeel Siddiqui, Alexander Fuchsberger

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26687v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26687v1)

**Summary:** Distinguishing GPT-assisted from independently authored student writing has become a critical challenge in academia. This paper evaluates the discriminative capability of interpretable stylometric features extracted solely from submitted text. Using data from 90 participants who wrote both independently and with ChatGPT assistance, we evaluate eight machine learning classifiers while keeping data from the same participant together during validation. On the held-out test set, Random Forest achiev...

---

### 7. Discovery-Driven Integration of Disjoint Tables via Text

**Authors:** Md Ataur Rahman, Dimitris Sacharidis, Oscar Romero, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26658v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26658v1)

**Summary:** Integrating heterogeneous datasets within data lakes is a critical challenge, particularly for semantically related tables that lack the explicit attributes needed to be joined. We study Discovery-Driven Integration, where the relevant sources and their missing relational structure must be discovered before integration. In this setting, unstructured text provides the evidence that connects otherwise disjoint tables. The fundamental challenge is to discover the relationships at a fine-grained lev...

---

### 8. Diffusion Drafts, AR Verifies: Accelerating Document OCR with Self-Speculative Decoding

**Authors:** Dohyun Kim, Sungjun Han, Hyungguk Kim, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26638v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26638v1)

**Summary:** Autoregressive OCR vision-language models accurately convert document images into text and structured markup, but require one sequential decoding step per output token, limiting inference speed. Unlike open-ended text generation, OCR outputs are strongly grounded in the input image, making diffusion-based parallel generation promising. However, when several tokens are predicted in one diffusion step, each is predicted before the others are known. Committing them directly can therefore introduce ...

---

### 9. Capable yet Parsimonious: Extracting and Characterizing Hidden Chain-of-Thought in Frontier Models

**Authors:** Xiaoyu Luo, Tao Ren, Wenrui Yu, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26637v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26637v1)

**Summary:** The rapid capability gains of frontier language models are widely attributed to improved reasoning abilities, yet this cannot be verified as raw CoT traces in closed-source systems are hidden. By registering a simple custom tool through a standard API feature, we induce frontier models to externalize intermediate reasoning. Because these traces may reflect post-hoc rationalization rather than genuine reasoning, we first evaluate against native CoT on open-source models and extend to closed-sourc...

---

### 10. Knowledge Pull Requests for Continual Document Authoring

**Authors:** Alexander Martin, Benjamin Van Durme

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26634v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26634v1)

**Summary:** We introduce Knowledge Pull Requests (KPRs), a framework for continual document authoring that makes each change interpretable. Documents require ongoing revision as new knowledge surfaces from other sources, languages, or times, but existing approaches either edit with no account of what knowledge changed or regenerate from scratch. A KPR integrates new knowledge into a document by extracting claims, filtering and routing them to sections, and flagging conflicts with existing content, producing...

---

### 11. PERSONAWEAVER: Controllable Diversity Beyond Conventional Archetypes in Procedural Character Generation

**Authors:** Maan Qraitem, Kate Saenko, Bryan A. Plummer

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26629v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26629v1)

**Summary:** Procedural character generation aims to populate games, simulations, and other virtual worlds with diverse characters. Large language models (LLMs) offer a promising foundation for scaling this task. However, LLM-based procedural character generation remains at an early stage: existing methods either generate characters directly or adapt profiles retrieved from persona banks. As we show, both approaches produce behaviorally homogeneous populations: characters overwhelmingly agree with positive m...

---

### 12. Semantic Abstraction for Natural Language Inference: a Methodological Framework for Discovering and Compensating Semantic Knowledge and Reasoning Gaps in Large Language Models

**Authors:** David Torres-Moreno, Jorge Hermosillo-Valadez

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26610v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26610v1)

**Summary:** Despite their outstanding performance on many NLP tasks, LLMs face serious challenges related to semantic abstraction. In this study, we are interested in understanding how LLMs leverage abstract semantic knowledge in natural language inference (NLI), which requires sophisticated linguistic capabilities to interpret implicit meanings, contextual conceptual relationships, and semantic connections between words and phrases. To this end, we propose a methodological framework for constructing new se...

---

### 13. Receptiveness, Not Sycophancy: Distinguishing Engagement from Deference in Language Models

**Authors:** Calvin Isley, Johann Gaebler, Max Lamparth, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26579v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26579v1)

**Summary:** A central concern with language models is sycophancy: their tendency to defer to users' views at the expense of independent substantive judgment. In parallel, work on social sycophancy has focused on behaviors such as validation and positivity that may signal inappropriate deference. Yet the markers of social sycophancy are also characteristic of conversational receptiveness, a construct from social psychology shown to improve interactions across disagreement. We argue that this overlap creates ...

---

### 14. A retrospective analysis on the use of LLMs to study infant syntax learning

**Authors:** Hélie Bazin, Anouk Barberousse, François Yvon

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26539v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26539v1)

**Summary:** Large language models (LLMs) have increasingly been used to investigate how children acquire syntax at an early stage of development. This is notably the central scientific goal of the BabyLM challenge, a community-wide effort to develop models that achieve human-level syntactic performance while being trained on developmentally realistic corpora. In this paper, we reflect on the use of LLMs in the study of infant syntax learning by providing an epistemological assessment of several studies from...

---

### 15. Transcribe, Translate, and Optimize: Joint Reward Learning for Speech Translation

**Authors:** Yanghe Dong, Wanting Huang, Weiran Wang

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26536v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26536v1)

**Summary:** In LLM-based speech translation, transcription-based chain-of-thought (CoT) suffers from a mismatch between reference transcripts used in supervised fine-tuning (SFT) and model-generated transcripts at inference. To address this, we propose joint recognition and translation fine-tuning via group relative policy optimization (GRPO). We score both transcripts and translations, with translation conditioned on model-generated transcripts, and compare three token advantage strategies. Using Qwen2.5-O...

---

### 16. A Semiotics-Aware Framework for Evaluating Fidelity and Coverage in Natural Language Generation

**Authors:** Lorenzo Zangari, Davide Picca

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26527v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26527v1)

**Summary:** When two texts describe the same expression, standard metrics based on lexical overlap or whole-text similarity may fail to detect meaningful differences in how that expression is framed. We propose a framework to evaluate semiotic alignment between texts, where a semiotic profile encompasses both the contextual meaning and the discourse references made salient by a text. Our approach yields two scores, Semiotic Fidelity and Semiotic Coverage, estimating how much of one text's profile is support...

---

### 17. Calibration as a First-Class Criterion in LLM Evaluation

**Authors:** Mario Sanz-Guerrero, Katharina von der Wense

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26489v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26489v1)

**Summary:** Calibration of language models -- the alignment between expressed or implicit confidence and empirical correctness -- is a well-studied subfield within NLP. Methods to measure it already exist. The problem is adoption: outside this subfield, NLP research regularly introduces new models, datasets, and benchmarks without checking whether the model's confidence scores are meaningful. We argue that this adoption gap is a major obstacle to trustworthy LLM evaluation. Miscalibration causes problems in...

---

### 18. Spoken Language Models that Think Aloud

**Authors:** Junyi Ao, Kainan Peng, Mingbo Ma, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26488v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26488v1)

**Summary:** While Chain-of-Thought (CoT) reasoning has improved the capability of language models, directly applying it to Spoken Language Models (SLMs) may introduce long silent intervals under the serial "think-then-speak" paradigm, disrupting real-time spoken interaction. To address this issue, we propose an asynchronous think-aloud framework for reasoning-based SLMs within the Thinker-Talker architecture. The framework maintains a primary reasoning stream for logical deduction and a lightweight think-al...

---

### 19. Behavior is Not Enough: A Mechanism-Based Evaluation of Social Norm Emergence in LLM Societies

**Authors:** Rasika Muralidharan, Haewoon Kwak, Jisun An

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26481v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26481v1)

**Summary:** Social norms cannot be identified from behavior alone: the same cooperative equilibrium may reflect shared expectations, strategic incentives, or simple imitation. Yet in multi-agent large language model systems, prior work largely treats behavioral convergence as evidence of norm emergence. In this work, we introduce an evaluation framework that measures agents' reported empirical and normative expectations in addition to behavioral convergence. Through controlled ablations, we test the effect ...

---

### 20. How to Estimate Whether You Have Found Several Needles in a Haystack: Measuring Calibration in Multi-Label Text Classification

**Authors:** Sophie Henning, Georg Hofmann, Alexander Schulte, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26468v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26468v1)

**Summary:** A key factor in deciding whether to trust an automatic prediction is its confidence score, which should be calibrated to match the actual probability of the prediction being correct. Most confidence calibration metrics target binary or multi-class tasks, while multi-label calibration remains largely underexplored. Multi-label classification tasks, such as assigning medical codes to clinical notes or determining news topics, are usually dominated by a large number of negatives, i.e., labels that ...

---

### 21. Enriching Speech Emotion Representations with Conversational Context

**Authors:** Arthur Peuvot, Romaric Besançon, Gaël de Chalendar, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26422v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26422v1)

**Summary:** Detecting emotions is necessary for building systems that can accurately and adaptively interact with humans. Speech Emotion Recognition (SER) has become an important research focus to develop intelligent spoken interfaces. However, most studies predict emotions at the utterance level, ignoring the conversational context, along with the emotional flow and speaker interactions it carries. In this paper, we introduce ACERT (Averaged Contextual Emotion Representation through Time), a module that in...

---

### 22. Combining Hierarchical Cognitive Process with Process Supervision for Interpretable Scene Safety Understanding

**Authors:** Zhiyun Jiang, Hanyong Wang, Binbin Liang, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26399v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26399v1)

**Summary:** Scene safety understanding plays a life-or-death role in situational awareness in various critical domains. Traditional methods that rely on learning direct mappings between scenes and safety levels often lack interpretability, limiting their reliability in critical applications. An effective approach to overcoming this challenge lies in interpreting human cognitive processes and equipping machine models with analogous cognitive capabilities. This work explores an effective way of integrating sc...

---

### 23. On the Lexical Superstition of Large Language Models for Code Comprehension: Re-evaluation on Code of Low Lexical Quality

**Authors:** Xin Shen, San-Zhuo Xi, Yali Du, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26388v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26388v1)

**Summary:** Recent advances in large language models (LLMs) have made them widely used for code-related tasks. Identifier names are statistically informative in naturally occurring code, but their information is not always reliable. We investigate whether current LLMs assign disproportionate weight to lexical cues when renaming preserves program structure. We introduce Face/Off, a semantics-preserving identifier-renaming framework, and evaluate progressive naming conditions across multiple models and code-c...

---

### 24. Layout-Guided Masking for GROBID: Lightweight Structural Gains in Large-Scale Scientific PDF Ingestion

**Authors:** Luca Foppiano, Sana Khamassi, Vipul Gupta

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26381v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26381v1)

**Summary:** Transforming scholarly PDFs into machine-readable fulltext remains a bottleneck for large-scale information systems. Recent vision-based parsers improve accuracy, but need GPUs and may introduce noise into the extracted text. GROBID, a modular font-stream parser running on CPU, is the de-facto standard for structuring scientific articles and underpins several of the largest open scholarly corpora. We pair it with a lightweight CPU detector localising figure, table, and paratext (header, footer, ...

---

### 25. HySparse2: Hybrid Sparse Attention with Two-Level KV Sharing

**Authors:** Jianyu Wei, Yizhao Gao, Qihao Zhang, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26368v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26368v1)

**Summary:** Long-horizon and multi-turn agents typically generate short actions and process long observations from tools and environments. This growing context demands efficient prefill, compact KV-cache storage, and accurate long-context retrieval. To meet these demands, we introduce HySparse2, a hybrid sparse attention architecture with two-level KV sharing. At the outer level, KV Bridging adopts a YOCO-style self-decoder and cross-decoder structure, but bridges only full-attention layers. The self-decode...

---

### 26. TransBERT: A Framework for Synthetic Translation in Domain-Specific Language Modeling

**Authors:** Julien Knafou, Luc Mottin, Anaïs Mottaz, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26347v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26347v1)

**Summary:** The scarcity of non-English language data in specialized domains significantly limits the development of effective Natural Language Processing (NLP) tools. We present TransBERT, a novel framework for pre-training language models using exclusively synthetically translated text, and introduce TransCorpus, a scalable translation toolkit. Focusing on the life sciences domain in French, our approach demonstrates that state-of-the-art performance on various downstream tasks can be achieved solely by l...

---

### 27. Blaming Across the Aisle: Political Contrasting and Blame Attribution in the Danish Parliament

**Authors:** Markus Lundsfryd Jensen, Rune Egeskov Trust, Kenneth Christian Enevoldsen, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26346v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26346v1)

**Summary:** Political discourse is widely perceived to be growing more hostile, yet robust evidence remains scarce. This study examines blame attribution in the Danish Parliament from 1997 to 2026, combining a purpose-built classifier, BlameBERT (F1: 0.80), with multilevel statistical modeling. The classifier is constructed using an annotation-efficient pipeline for blame attribution in low-to-mid resource languages. The results reveal a banana-shaped trajectory, with blame declining until around 2016 befor...

---

### 28. Designing and Analysing Argument Mining Pipelines: Towards a Comprehensive Assessment

**Authors:** Siddharth Bhargava, Sara Tonelli, Patricia Martín-Rodilla

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26338v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26338v1)

**Summary:** Argument Mining (AM) transforms natural language into its underlying argument structures. This transformation is typically realized through a sequence of AM tasks that form an end-to-end AM pipeline. However, AM approaches often differ in how they conceptualize these tasks, making direct comparisons between them difficult and opaque. This calls for a more nuanced, task-level analysis of AM approaches to enable clearer comparison and assessment.   This work presents a preliminary meta-study that ...

---

### 29. CHiME-9 ECHI: A Machine Learning Challenge for Enhancing Conversations to Address Hearing Impairment

**Authors:** Robert Sutherland, Thomas Kuebert, Marko Lugger, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26306v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26306v1)

**Summary:** This work presents the task and results of the CHiME-9 challenge for Enhancing Conversations to address Hearing Impairment. The challenge considers the scenario of four-party conversations in a noisy, cafeteria-style environment with interfering speech sources and sound effects. Participants are provided with audio recordings made with Meta Aria glasses and hearing aid microphones, and clean speech samples of the conversation participants. The task is to extract the speech of the conversation pa...

---

### 30. FIRE: Failure-Informed Runtime Engineering for Reliable Language-Model Agents

**Authors:** Nikita Agarwal, Nivedit Jain

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26048v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26048v1)

**Summary:** Language-model agents often reach a working solution and then fail to consistently deliver it. We study runtime policies: targeted natural-language instructions and action denials applied by the agent harness at states that preceded observed failures, without changing model weights or the user prompt. With this, keeping capability constant, we observe a meaningful unlock in delivered reliability. Across the complete 87-task Terminal-Bench 2.1 suite, with two attempts per task, policies increase ...

---

### 31. Truth for Believable AI: Expressed Doubt, Provenance, and Belief Revision as an Engineerable Stance

**Authors:** Sebastian Cochinescu

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26035v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26035v1)

**Summary:** Conversational agents often express answers in a uniformly confident register. We test whether expressed uncertainty, provenance-aware assertion, and explicit belief revision can be implemented as a behavior layer over a fixed language model; we do not test believability or trust. The layer combines three epistemic states, per-claim confidence and typed provenance, a provenance-gated expression rule, and a persistent revision store with auditable acknowledgments and partial resistance to false c...

---

### 32. Domain-Adaptive Pretraining Enhances Water Treatment Semantic Representation for Large-Scale Structured Literature Mining

**Authors:** Mudi Zhai, Ruihong Qiu, Qingyun Zeng, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26034v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26034v1)

**Summary:** Water treatment research is expanding rapidly, but much of the knowledge acquired from this research remains scattered across unstructured literature. The field still lacks a dedicated language model that can efficiently capture water treatment-specific domain semantics for large-scale literature mining. Here, we address this by developing WaterBERT, a domain-adapted encoder model designed for semantic representation and structured information extraction from water treatment texts. WaterBERT was...

---

### 33. MICRO: Multi-Fidelity Active Search for Severe Error Discovery

**Authors:** Orlando Leone, Niclas Pokel, Pehuén Moure, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26025v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26025v1)

**Summary:** Human feedback can vary in cost and informativeness. Strong feedback can reveal severe errors but is costly, so cheaper quality ratings can help decide which items to annotate. We propose MICRO (Multi-Fidelity Impact Clustered Rollout), an active search framework that allocates a shared budget to these feedback types to maximise confirmed severe error discoveries. MICRO jointly models ratings and annotation losses conditional on item features to steer acquisition. It clusters acquisitions by the...

---

### 34. Challenges of Multi-Speaker Extraction for Real Conversational Speech Enhancement

**Authors:** Robert Sutherland, Stefan Goetze, Jon Barker

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25948v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25948v1)

**Summary:** Target-speaker and multi-speaker extraction are techniques for extracting speech from a desired speaker or desired speakers in the presence of other speakers and/or noise. Neural network approaches for this task are often trained and evaluated using simulated datasets, with balanced amounts of target speech and speaker enrolment samples which closely match the target speech. However, in real multi-party conversations, participants are often silent for more time than they are speaking, and their ...

---

### 35. ClusterFewshot: Improving Few-shot Optimization for LLMs workflow

**Authors:** Omri Bar Haim, Shahar Katz, Lior Wolf

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25939v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25939v1)

**Summary:** The performance of large language model (LLM) workflows often depends on selecting a small set of in-context demonstrations to guide model behavior on new tasks. Recent methods improve this process by augmenting prompts with successful reasoning paths. However, their demonstration selection relies on random sampling or metric-based rankings, overlooking the semantic structure of the task. We propose ClusterFewshot, a strategy that combines semantic structuring with utility-aware scoring to const...

---

### 36. Certified Against Which Oracle? Execution Labels Set the Reported Risk of Conformal Abstention for Text-to-SQL

**Authors:** Jiamiao Liu, Dewen Qiao, Yu Zhang, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25938v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25938v1)

**Summary:** A conformal abstention certificate for text-to-SQL is only as truthful as the correctness labels it is calibrated on. The uncertainty pipelines that read confidence off execution consistency take those labels from the single database a benchmark ships, an oracle known to be lenient. We run a preregistered intervention on Spider-Realistic, swapping that database for the benchmark's distilled multi-instance test suite. Across four SQL-specialist checkpoints and two split schemes, the swap raises t...

---

### 37. Informed Masking: Structure-Aware Perturbation for Reinforcement Learning in Diffusion Large Language Models

**Authors:** Xiaoyi Yu, Enver Sangineto, Pei Fu, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25927v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25927v1)

**Summary:** Diffusion Large Language Models (dLLMs) have emerged as an efficient alternative to autoregressive models, yet aligning them via Reinforcement Learning (RL) requires likelihood surrogates estimated from masked reconstruction subproblems under a small Monte Carlo budget per rollout. Existing methods construct these subproblems by uniform random masking, leaving open the question of which subproblems to prioritize. We identify a systematic upstream/downstream structure in dLLM rollouts. Some token...

---

### 38. Rethinking Length-Based Training: Batch Composition and Loss Normalization in Speech Token Language Models

**Authors:** Hongjin Song, Runwu Shi, Weiqiao Shan, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25890v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25890v1)

**Summary:** Short-to-long training is a simple curriculum for speech models, but its gains can be difficult to interpret. In speech token language models, length-based training can change the shuffle policy, batch composition, token retention, and token weights under batch-mean loss. We disentangle these factors through matched comparisons. In the tested settings, short-to-long ordering shows no independent benefit when batch composition and token exposure are fixed. First-epoch grouping lowers perplexity f...

---

### 39. Isolated Sign Language Recognition for Icelandic Sign Language: Experiments in a Low-resource Setting

**Authors:** Finnur Ágúst Ingimundarson, Guðný Björk Þorvaldsdóttir, Mathias Müller, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25862v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25862v1)

**Summary:** We present the first experiments on isolated sign language recognition (ISLR) for Icelandic Sign Language (ÍTM). We use ÍTM SignWiki, a dataset derived from a bilingual Icelandic--ÍTM online dictionary. It is genuinely low-resource: 1,845 videos cover 849 classes, 86% of which have only two examples, making the full task effectively one-shot recognition across signers. We compare two open-source ISLR frameworks, OpenHands and SPOTER, on three tasks of increasing vocabulary size (22, 117 and 849 ...

---

### 40. BELXTR: Biomedical Entity Linking via Contextualized Token Retrieval

**Authors:** Samuele Garda, Ulf Leser

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25859v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25859v1)

**Summary:** Biomedical Entity Linking disambiguates mentions to entities in a knowledge base (KB), making it the cornerstone of information extraction pipelines. While embedding-based models are a popular approach for the task, they suffer from a key limitation. They compress mentions (and entities) into a single vector, forcing the model to average away crucial fine-grained differences. We present BELXTR, a novel embedding model based on the multi-vector (a.k.a. late interaction) architecture, which allows...

---

### 41. MemoryAthena: Adaptive Routing over Latent and Generated Memories

**Authors:** Mingyuan Li, Guangsheng Yu, Juyuan Zhang, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25853v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25853v1)

**Summary:** Learned-memory methods store information in an explicit table and consume it through a separate reader, allowing addressing, storage, and reading to be modified independently. We study whether useful memory can also be generated rather than only retrieved. MemoryAthena uses three pathways: direct Engram retrieval (E), generation from retrieved Engram cues (GE), and generation from causal backbone states without consulting the memory table (GH). Generated memory is conditionally useful: it can co...

---

### 42. ARAFA: An LLM-Generated Arabic Fact-Checking Dataset

**Authors:** Christophe Khalil, Shady Elbassuoni, Rida Assaf

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25833v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25833v1)

**Summary:** Automatic fact-checking poses a significant challenge in Arabic natural language processing due to the scarcity of datasets and resources. In this manuscript, we introduce Arafa, a new large-scale dataset for fact-checking in Modern Standard Arabic, constructed through an automated framework leveraging large language models (LLMs). The dataset was constructed through a three-step pipeline: (1) claim generation from Arabic Wikipedia pages with supporting textual evidence, (2) claim mutation to ge...

---

### 43. Auditing Proxy-Based Validation Across Text Spans

**Authors:** Daein Weon, Dong Ho Kang

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25808v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25808v1)

**Summary:** Evaluation scores are often validated by their agreement with inexpensive proxy labels. When the score and the proxy are computed from the same text span, however, that agreement can arise from surface evidence the two share rather than from the semantic construct the proxy is meant to represent. We make the distinction explicit by declaring the score, its span, the proxy and the target construct as a validation contract, then re-evaluating that proxy rule strictly outside the scored span. In a ...

---

### 44. Latest Exact Match Attention

**Authors:** Moritz Brösamle

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25802v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25802v1)

**Summary:** We introduce latest exact match attention (LEMA), an attention variant for transformers where queries and keys are binarized and each query attends only to the latest exactly matching key. We prove that LEMA transformers with chain of thought can simulate word-RAMs, as was recently shown for the less restrictive rightmost hard attention. In contrast to prior hard attention variants, the restriction to exact matches enables an efficient converse direction: word-RAMs can simulate LEMA transformers...

---

### 45. Reply to comments arXiv:2512.07881 and arXiv:2601.06104 on quantum structure in human and AI-generated language

**Authors:** Massimiliano Sassoli de Bianchi, Roberto Leporini

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25797v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25797v1)

**Summary:** We reply to the comments by M. Sienicki and K. Sienicki (arXiv:2512.07881) and by K. Sienicki (arXiv:2601.06104) on our work on quantum-mechanical statistics in human language (arXiv:2407.14924) and on quantum structure in AI-generated language (arXiv:2511.21731). We thank the authors for their careful reading and address what we consider to be the main points of criticism: the exploratory nature of the protocol used in the experiments with large language models; the role of marginal-law violati...

---

### 46. Syndrome, Synergy, and Safety: Structured Reasoning and Knowledge-Driven Alignment for TCM Prescription Generation

**Authors:** Zheng Chen, ZhiCheng Du, Haoxuan Li, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25755v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25755v1)

**Summary:** Applying large language models to Traditional Chinese Medicine (TCM) prescription generation reveals three clinically critical gaps: models produce end-to-end mappings without auditable reasoning following the li-fa-fang-yao paradigm (SR Gap), treat each encounter in isolation without follow-up adjustment via sui zheng jia jian (LA Gap), and fail to enforce absolute contraindication rules such as Shi Ba Fan (SC Gap). We propose a progressive four-stage framework (SFT $\to$ PG-CoT $\to$ Dynamic $...

---

### 47. Slow Decay and Silenced Expression: Iterated Subliminal Trait Transfer in Language-Model Lineages

**Authors:** Ryan Vo, Duc-Vu Nguyen, Matt Kretchmar, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25721v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25721v1)

**Summary:** Language models are increasingly trained on the outputs of other models, forming chains that we call lineages, in which a trait present in one generation can pass to the next. Prior work on subliminal learning has shown that a teacher's trait can transmit to a student through filtered data carrying none of the trait's content. However, the evidence covers only a single training step. We study whether such a trait holds or fades across lineages. We instill the trait into three copies of Qwen2.5-7...

---

### 48. How Strongly Should Task State Influence an LLM Agent?

**Authors:** Chenyu Zhang, Wonbin Kweon, Jiawei Han

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25686v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25686v1)

**Summary:** Long-horizon assigned work requires an LLM agent to track the state of a task: which steps are done, blocked, cancelled, or open to repetition. Agent systems either keep this state as text in the prompt and rely on the model to read that text, or move the state into a module that enforces it, and each system is evaluated as a whole, so no one knows how much reliability comes from the state being shown, told, or enforced. We fix the task rules, the model, and paired episodes and vary how strongly...

---

### 49. From Utterances to Networks: Modelling Slang Adoption and Diffusion Across Subreddits

**Authors:** Xiaoning Wang, Ted Underwood, Zhewei Sun

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25669v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25669v1)

**Summary:** Adoption and diffusion of neologisms in online communities have received renewed attention in recent years. As internet slang terms such as APT, referring to a K-pop song, and phrases such as Canon Event meaning an embarrassing but pivotal event, go viral online, it becomes increasingly important to understand the mechanisms that contribute to their success. Prior studies have often explained slang diffusion either from the perspective of social interaction or from the linguistic properties of t...

---

### 50. Efficient Cost-Aware LLM Evaluation via Bayesian Bandit Gittins Indices

**Authors:** Qian Xie, Yueli He, Nairen Cao

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25645v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25645v1)

**Summary:** Exhaustively evaluating every candidate LLM configuration on every benchmark item to identify a high-performing one is costly. We formulate configuration selection as a cost-aware Bayesian bandit problem and propose GittinsEval, which draws on the Bayesian-optimal Gittins policy to determine which configuration to evaluate next and when to stop. We extend the policy with an anytime recommendation rule over both fully and partially evaluated configurations, using an LCB-style score to account for...

---

## cs.CV

**50 papers**

### 1. φ-RIE: From Photorealistic Reconstruction to Interactive Environments

**Authors:** Runyi Yang, Deheng Zhang, Xiaoye Wang, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26795v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26795v1)

**Summary:** 3D Gaussian Splatting (3DGS) can reconstruct a captured scene photorealistically, but the resulting representation does not by itself support physical interaction. Robot simulation instead requires object-level change, \textit{i.e.}, objects must move independently, make contact, and reveal previously occluded surroundings. This gap arises because object appearance may remain entangled with the background, while hidden object geometry and occluded background content may be unobserved. To address...

---

### 2. HARMONY: Hierarchical Agentic Reasoning for MONocular Image-to-Scene Synthesis

**Authors:** Shufan Sun, Chen Wang, Enxin Song, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26793v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26793v1)

**Summary:** Compositional 3D scene reconstruction has recently been explored from two directions: agentic reasoning that provides semantic understanding of spatial relationships but lacks precise alignment with input images; and visual geometry foundation models that predict dense point maps from input images but the reconstruction quality is limited. Therefore, recovering a complete 3D scene from a single monocular image with accurate inter-object relationships and high-fidelity reconstruction quality rema...

---

### 3. DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving

**Authors:** Ziyang Leng, Sicheng Mo, Seth Z. Zhao, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26792v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26792v1)

**Summary:** Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions. Existing platforms, however, exhibit a sim-to-real visual gap that corrupts policy perception, undermining their ability to assess a policy's closed-loop decision-making. To this end, we propose DreamStream, a generative, closed-loop simulator that achieves policy-oriented fidelity using a simulator-ground...

---

### 4. StableVQ: Practical Guidelines for Stable Vector-Quantized Tokenizer Training

**Authors:** Bao Tang, Jiahao Guo, Haoxiang Cao, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26774v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26774v1)

**Summary:** Vector Quantization (VQ) is fundamental to discrete visual tokenizers that power modern autoregressive and masked image generation models. While recent shared-projection codebook methods have substantially advanced codebook utilization, training stability remains a critical and underexplored challenge. We argue that the root cause lies in the entanglement of the Encoder--Decoder and Codebook training: because neither module can reliably fulfill its own responsibility in isolation, the system can...

---

### 5. FleXray: Universal Clinical X-ray Segmentation

**Authors:** Victor Ion Butoi, Vivek Gopalakrishnan, John V. Guttag, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26756v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26756v1)

**Summary:** X-ray is medicine's most widely used imaging modality, yet remains among its least quantitative. Unlike volumetric modalities like CT or MRI, X-ray collapses 3D anatomy into a 2D projection, causing structures to overlap and anatomical boundaries to be ambiguous, even to experts. As a result, labeling X-ray databases for training general-purpose segmentation systems is impractical, leaving morphometric and functional X-ray analysis confined to narrow anatomical regions and applications. To this ...

---

### 6. Evaluating the Semantic-to-Geometric Gap in Adversarial Defenses Against Vision-Language Model-Based Plagiarism

**Authors:** Christopher Burger, Christina Trotter, Joseph Carlisle, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26733v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26733v1)

**Summary:** The rapidly advancing capabilities of vision-language models (VLMs) present a systemic challenge to academic integrity. VLMs now allow students to bypass meaningful engagement by capturing and submitting graphical problems as singular images, a practice we define as trivial plagiarism. To provide educators with actionable data on VLM limitations, we investigate the efficacy of heuristic adversarial image transformations designed to degrade model performance while remaining human-interpretable. T...

---

### 7. ASTRA-SR: Atmospheric Seeing and Turbulence Restoration for Astronomical Image Super-Resolution

**Authors:** Xining Ge, Ziteng Cui, Shuhong Liu

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26731v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26731v1)

**Summary:** Ground-based planetary imaging suffers from atmospheric turbulence, sensor noise, and limited sampling, making restoration a joint denoising, deblurring, and super-resolution problem. We present ASTRA-SR, a blind single-frame restoration framework trained on a physics-grounded synthetic dataset. High-dynamic-range spacecraft RAW observations serve as clean sources, and paired LR inputs are synthesized using measured layer-integrated turbulence strengths, propagated moving phase screens, exposure...

---

### 8. GAD-MambaUNet: Direction-Group Mamba with Gradient-Adaptive DINOv3 Distillation for Lightweight Medical Image Segmentation

**Authors:** Fang Wang, Huitao Li, Wenhan Chao, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26729v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26729v1)

**Summary:** In this paper, we proposed GAD-MambaUNet, a lightweight medical image segmentation network that combines efficient local modeling, direction--group state-space interaction, and training-time foundation-model supervision. To improve contextual modeling in compact segmentation networks, we introduced Direction-Group Graph Selective Scan (DG-GSS), which treated scan-direction and channel-group responses as graph nodes and enabled structured information exchange before multi-directional fusion. We f...

---

### 9. DIFTA-3D: Depth-Consistent Instance-Level Feature Transfer and Adaptation of DINOv3 for 3D Detection

**Authors:** Linman Wang, ZiFei Zhang, Chunran Zheng, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26702v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26702v1)

**Summary:** RGB-D 3D instance detectors benefit from visual semantics, but the task-specific Faster R-CNN/ResNet branch used by IIFNet3D couples feature extraction to a separately trained 2D detector and its image-domain labels. Replacing that branch with a frozen vision foundation model removes this task-specific dependency, but may introduce occlusion noise and a mismatch between patch features and geometry-aware detection features. In this work, we investigate this replacement through an adaptation of DI...

---

### 10. Longitudinal Retinal Vascular Remodeling in Myopic Children Treated with Orthokeratology or Defocus Lenses: A Two-Year Comparative Study

**Authors:** Zhihao Zhao, Yinzheng Zhao, Jie Zhang, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26662v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26662v1)

**Summary:** Purposes: To characterize longitudinal retinal vascular changes in myopic children treated with orthokeratology (OK) or multifocal defocus lenses (Defocus) and to examine their association with axial elongation. Methods: In this retrospective cohort study, 43 myopic children underwent comprehensive clinical examination and fundus photography at baseline, 12 months, and 24 months. Axial length (AL) and spherical equivalent refraction (SER) were recorded at baseline, 6, 12, and 24 months. An autom...

---

### 11. ROAM-ASD: Robust Open-World Active Speaker Detection with Flexible Multimodal Fusion

**Authors:** Pu Wang, Yujun Wang, Hugo Van hamme

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26648v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26648v1)

**Summary:** Active speaker detection (ASD) requires reliable association between visible faces and acoustic speech, yet existing systems often degrade under challenging domains or incomplete observations. We introduce ROAM-ASD, a robust audiovisual framework that jointly models audio, full-face, and fine-grained mouth representations. A unified joint self-attention mechanism processes all input streams together with modality-agnostic query tokens, enabling direct interaction among available modality inputs....

---

### 12. Diffusion Drafts, AR Verifies: Accelerating Document OCR with Self-Speculative Decoding

**Authors:** Dohyun Kim, Sungjun Han, Hyungguk Kim, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26638v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26638v1)

**Summary:** Autoregressive OCR vision-language models accurately convert document images into text and structured markup, but require one sequential decoding step per output token, limiting inference speed. Unlike open-ended text generation, OCR outputs are strongly grounded in the input image, making diffusion-based parallel generation promising. However, when several tokens are predicted in one diffusion step, each is predicted before the others are known. Committing them directly can therefore introduce ...

---

### 13. Laryngeal Structure Segmentation in High-Speed Videoendoscopy Using Deep Learning

**Authors:** Sardar Nafis Bin Ali, Mohsen Zayernouri, Dimitar D. Deliyski, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26636v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26636v1)

**Summary:** Laryngeal high-speed videoendoscopy (HSV) offers an effective means of observing the motion of different laryngeal structures along with vibratory behaviors of the vocal folds under various voicing conditions. Segmentation of laryngeal tissues enables analysis of different tissue structures and their dynamics, helping characterize the involvement of laryngeal muscles in voice production. Given the large number of HSV frames, automating this task is imperative. While deep learning-based methods h...

---

### 14. Label-Efficient Learning for Ground-Based Sky-Image Classification: A Benchmark of Transfer Learning, Active Learning, and Pseudo-Labeling on GCD

**Authors:** Esther Bou Dagher, Viktoriya Bu-Dager, Boguslaw Zegarlinski

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26631v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26631v1)

**Summary:** Accurate ground-based cloud classification is important for atmospheric monitoring, solar-energy forecasting, aviation weather assessment, and climate observation systems. However, reliable sky-image annotation is time-consuming, especially when cloud types are visually similar or mixed. We study the label efficiency of deep learning for ground-based cloud classification using the Ground-based Cloud Dataset (GCD). Rather than proposing a new architecture, we benchmark three practical strategies ...

---

### 15. A Data-Interventional Framework for Auditing Privacy and Fairness in Generative Medical Imaging

**Authors:** Mischa Dombrowski, Bernhard Kainz

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26623v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26623v1)

**Summary:** Diffusion-based synthetic data generation offers a promising route for sharing medical imaging data without releasing sensitive patient records. However, generative models face a fundamental tension between privacy and fairness: they may memorize rare training samples, leading to privacy risks, or fail to reproduce underrepresented features, resulting in unfair synthetic distributions. While prior work has largely focused on either memorization or fairness in isolation, their interaction remains...

---

### 16. GeoComposer: Geometry-Grounded Photographic Composition Instruction

**Authors:** Shuangzhi Li, Qiaoqiao Jia, Xingxin Chen, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26620v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26620v1)

**Summary:** Photographic composition aims to provide visual guidance for improving the framing, viewpoint, and spatial arrangement of an image. Early methods primarily rely on image cropping to enhance composition, which is restricted to the viewpoint and spatial arrangement of the input image. Recent methods have explored image understanding and editing to improve composition, but they mainly focus on instruction following and aesthetic quality, overlooking the importance of 3D scene geometry consistency f...

---

### 17. MMAP: Multimodal Missing-Aware Pretraining for Longitudinal Alzheimer's Prediction

**Authors:** Fiona Kekwick, Matthew Baugh, Bernhard Kainz, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26617v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26617v1)

**Summary:** Clinical decision making heavily relies on predicting the disease progression trajectory by seeking to understand patient's health status which is characterised by multimodal medical data. AI holds great potential for learning useful representations from multimodal medical data to predict disease progression and aid clinical decision making. However, development of predictive AI models is constrained by missing modalities and incomplete tabular data frequently occurring in medical datasets. In a...

---

### 18. Foundation model embeddings capture pre-diagnostic changes on screening mammograms

**Authors:** Kalina P. Slavkova, Eric Brattain, Aditya Gowd, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26605v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26605v1)

**Summary:** Foundation model embeddings of screening mammograms may encode pre-diagnostic tissue change without task-specific adaptation. We tested whether embeddings move faster along a data-derived "cancer direction" in women later biopsied for cancer than in matched screen-negative controls, and whether this depends on pretraining domain. We studied 1,773 biopsied women (785 malignant, 988 biopsy-negative) and 1,773 matched controls, each with at least two annual screening exams before their index exam. ...

---

### 19. GTR: Gated Token Recurrence for Efficient Dense Prediction

**Authors:** Zhe Feng, Longfei Liu, Wei Liu, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26590v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26590v1)

**Summary:** Self-attention-based vision backbones perform well on dense prediction, but the quadratic computational cost of global softmax attention limits their efficiency as image resolution increases. We introduce Gated Token Recurrence (GTR), a softmax-free recurrent vision backbone that combines gated linear attention, alternating spatial scan directions, and spatially enhanced SwiGLU blocks. GTR is distilled from a detection-specialized DINOv3 teacher using only final-layer patch-token alignment throu...

---

### 20. Radiomics--Foundation Fusion for Interpretable RCC Classification: Internal Benchmarking and Exploratory External Transfer

**Authors:** Yuan Liang, Fangyijie Wang, Kathleen M. Curran, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26578v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26578v1)

**Summary:** Accurate preoperative subtype classification of renal cell carcinoma (RCC) from contrast-enhanced CT remains clinically challenging because clear cell RCC (ccRCC) and non-clear cell RCC often show overlapping imaging appearances. This study evaluates whether foundation representations reduce reliance on handcrafted radiomics, or whether radiomics remains complementary for interpretable tumour characterisation. We compared radiomics, conventional CNN features, MedicalNet-pretrained features, MedV...

---

### 21. Beyond End-Task Success: How to Audit Visual Experience Retrieval in Robotics

**Authors:** Eshika Pathak, Leela Krishna

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26567v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26567v1)

**Summary:** Robots that store past experiences must select which one to reuse in a new scene. Most systems select by visual similarity, and most evaluations report only the success of the selected experience. That number does not show whether the selection was good: a rule can score well by repeatedly using one broadly transferable experience, or poorly because its preferred experience is weak. Since robots increasingly adapt by reuse rather than retraining, a score that describes the library rather than th...

---

### 22. Vision Foundation Models with Synthetic-Only Training for Monocular Spacecraft Pose Estimation

**Authors:** John Church, Vazghen Nikolian

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26561v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26561v1)

**Summary:** We present an improvement on previous spacecraft pose estimation architectures that results in the lowest published mean rotation errors we know of on the SPEED+ lightbox and sunlamp test sets for a known, non-cooperative spacecraft. By using a previously established heatmap-based pose estimation architecture and adapting a large self-supervised ViT foundation model (DINOv3) in place of the smaller convolutional and ViT encoders of previous work, we show that pose estimation accuracy improves fr...

---

### 23. Latent Commonality Expectation-Maximisation for Box-supervised Tree Crown Instance Segmentation

**Authors:** Thomas Pitts, Kunqi Li, Bin Liang

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26549v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26549v1)

**Summary:** Individual tree crown segmentation from aerial imagery underpins tree-level carbon accounting, biodiversity, and restoration monitoring at landscape scale. However, existing models are predominantly trained on dense canopy forest imagery and degrade in savannah and drylands, where tree crowns are sparse, of variable appearance, and underrepresented in annotated benchmarks. These models also typically depend on costly polygon annotations. We introduce LACE (LAtent Commonality Expectation-maximisa...

---

### 24. Notes on Fourier-Bessel wavelets

**Authors:** Marcel Venturotti, Georgios Exarchakis

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26537v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26537v1)

**Summary:** These notes develop the mathematical foundations and construction of a Fourier-Bessel wavelet family inspired by the disk harmonics of Shaqfa et al.[9]. We begin with the relevant properties of Bessel and modified Bessel functions and introduce the wavelet properties required for the construction. We then derive the Fourier-Bessel disk harmonics as solutions to the Helmholtz equation on the unit disk subject to a Neumann boundary condition.   Building on this basis, we construct a wavelet family...

---

### 25. Virtual Encoders in Multimodal Transformers

**Authors:** Katsuya Ogata, Yuta Nakashima

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26513v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26513v1)

**Summary:** Multimodal language models traditionally rely on dedicated perceptual encoders to construct task-usable representations. More integrated architectures have recently emerged, which instead expose the shared transformer to lightly projected patches, audio frames, or discrete visual tokens. Where does this encoding happen when such representations are not provided? We find that the transformer can internalize this missing computation, constructing task-usable perceptual representations within its o...

---

### 26. Do Vision Model See Like the Brain? A Comparison Across EEG Encoding Model

**Authors:** Shashank Baghel, Kshitij Dwivedi, Dinesh Singh, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26512v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26512v1)

**Summary:** Convolutional neural networks (CNNs) and vision transformers are both used to model the human visual system, but whether the two architectures diverge at a specific point in network depth is unclear. We compared six CNNs and two vision transformers by computing the Pearson correlation (r) between each model's predicted and measured EEG response at every layer or block, in ten participants viewing 200 natural images. For the transformer models, we also tested four token representations, from the ...

---

### 27. Semantically-Guided Domain Randomization for Industrial Object Detection in Low-Image-Budget Regimes

**Authors:** Jose Moises Araya-Martinez, Gautham Mohan, Jens Lambrecht

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26505v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26505v1)

**Summary:** Retraining visual perception pipelines in High-Mix, Low-Volume (HMLV) automotive manufacturing must be carried out under tight annotation, energy, and time budgets, yet most Synthetic Data Generation (SDG) strategies still operate in the thousands of images. This work evaluates Semantically-Guided Domain Randomization (S-GDR), an annotation-free adaptation pipeline that couples Vision-Language Model (VLM)-based semantic captioning of a small unannotated real reference set with diffusion-based ba...

---

### 28. Radiomics-Conditioned Modulation of RenalCLIP Features for Clear Cell Renal Cell Carcinoma Classification

**Authors:** Yuan Liang, Sourav Bhattacharjee, Abraham Campbell

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26492v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26492v1)

**Summary:** Radiomics provides quantitative descriptions of tumour appearance that may complement disease-specific foundation models in small labelled cohorts. We investigate this complementarity for computed tomography-based classification of clear cell renal cell carcinoma. Our framework uses radiomics to modulate RenalCLIP features through feature-wise linear modulation (FiLM), while retaining a direct radiomics contribution. Internal testing and external validation compare it with conventional fusion st...

---

### 29. From Token Importance to Conditional Removability: Rethinking Visual Token Pruning in Multimodal Large Language Models

**Authors:** Shengli He, Yongchao Liang, Roumeng He, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26484v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26484v1)

**Summary:** Training-free visual-token pruning often uses token importance, redundancy, or related selection criteria as proxies for safe removal. We show that these signals alone do not fully characterize removability, which is conditioned on both representation depth and the surrounding deletion set. Controlled interventions demonstrate that removing the same tokens at different depths produces substantially different downstream perturbations, while changing only the deletion context at a fixed depth alte...

---

### 30. PP-Net: A Hybrid Physical-Prior Neural Network for Scattered Light Removal in Biomedical Images on Embedded Devices

**Authors:** Yongfei Guo, Tingjin Chu, Mengzhuo Liu, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26474v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26474v1)

**Summary:** Scattered light is common in biomedical images, yet its removal remains challenging. The difficulty arises from three aspects: first, aligned scattered-light-free biomedical ground truth is often unavailable; second, scattering is coupled with weak illumination and sensor-induced noise; and third, many learning-based restoration models are computationally expensive for embedded devices in Internet of Medical Things (IoMT) scenarios. To address these issues, this paper proposes PP-Net, a hybrid p...

---

### 31. Complementary Roles of Radiomics and Foundation Representations in Renal Cell Carcinoma Classification: A Comparative Study of 2D and 3D CT Encodings

**Authors:** Yuan Liang, Sourav Bhattacharjee, Abraham Campbell

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26463v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26463v1)

**Summary:** Accurate preoperative subtype classification of renal cell carcinoma (RCC) from contrast-enhanced computed tomography remains clinically challenging. Radiomics provides structured tumour descriptors, whereas foundation representations offer transferable image features. However, it remains unclear whether radiomics still adds value beyond pretrained representations, and how 2D and 3D MedVAE encoders compare in this setting.   We compared handcrafted radiomics, 2D MedVAE, 3D MedVAE, and their fusi...

---

### 32. Code Plans, Diffusion Renders: Open-Ended Generative World Modeling

**Authors:** Zixun Fang, Yawen Shao, Kai Zhu, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26458v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26458v1)

**Summary:** We introduce \textbf{CoDeR}, a new paradigm for world modeling. Unlike existing video world models that implicitly represent world dynamics through visual observations, our system explicitly constructs an executable world with code and employs video generation models for visual realization. Specifically, we coordinate five complementary roles to translate high-level concepts into structured world rules, executable dynamics, and perceptual observations. This design enables \textit{long-term memor...

---

### 33. Mammo-LIFE: Longitudinal Mammographic Imaging and Clinical Feature Enrichment for Post-Radiotherapy Outcome Prediction

**Authors:** Farnoush Bayatmakou, Maryam Hosseini, Reza Taleei, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26443v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26443v1)

**Summary:** Recent advances in Artificial Intelligence (AI)-powered Computer-Aided Diagnosis (CAD) systems have substantially improved breast cancer screening, diagnosis, and prognosis. Comparatively, postradiotherapy outcome prediction using paired longitudinal mammograms has received considerably less attention. This is largely due to the limited availability of well-annotated longitudinal datasets. Longitudinal mammograms, coupled with paired pre- and post-treatment information, provide a unique opportun...

---

### 34. Latent Dataset Distillation for Human Motion Prediction

**Authors:** Ge Tian, Guang Li, Takahiro Ogawa, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26430v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26430v1)

**Summary:** Dataset distillation (DD) compresses a large training set into a compact synthetic set while preserving downstream training utility. Although DD has been widely studied for images and recently extended to time-series forecasting, its application to human motion prediction remains largely unexplored. Human motion is high-dimensional and structurally coupled, and gradient matching (GM) in the original motion space optimizes many correlated variables without a prior on pose plausibility or temporal...

---

### 35. QuantWM: Temporally Consistent 2-Bit KV Cache Quantization for World Models and Video Generation

**Authors:** Jiaqi Zhao, Xiaobin Hu, Bo Yin, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26425v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26425v1)

**Summary:** KV cache memory has become a major deployment bottleneck for video generation and world models, which motivates low-bit quantization study for efficiency. Existing 2-bit KV cache quantization methods can achieve nearly lossless performance on video benchmarks such as VBench, however, we find that they still cause severe temporal flickering and visual degradation. Meanwhile, deeper investigates show that Key quantization produces smaller reconstruction errors than Value, but surprisingly leads to...

---

### 36. Sample, Simulate, Select: Physics-in-the-Loop Text-to-Motion for Humanoids Without Training

**Authors:** Raphael Memmesheimer, Sven Behnke

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26420v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26420v1)

**Summary:** Text-to-motion models generate plausible human motion but do not model a robot's dynamics; whole-body tracking controllers execute robot references reliably but cannot replan an infeasible one. Recent language-to-humanoid systems bridge this gap by training. We measure how much of the gap closes with no training at all, by putting the deployment controller itself in the loop. Sample-simulate-select (S$^3$) draws $N$ motions per prompt from a frozen text-to-motion model, retargets each to a Unitr...

---

### 37. MAVP: Map-Aware Visuomotor Policies for Mobile Manipulation

**Authors:** Jinhe Tang, Ruixiao Dai, Weiming Zhi

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26378v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26378v1)

**Summary:** Successful mobile manipulation requires coordinated base and arm motion while maintaining accurate spatial positioning. However, demonstration-trained policies can struggle to realise the intended base motion reliably, leading to spatial misalignment and subsequent manipulation failures. We present MAVP (Map-Aware Visuomotor Policies), a framework that improves execution reliability by predicting explicit base-pose targets and tracking them using localisation feedback. MAVP reconstructs a static...

---

### 38. KwaiMind Technical Report

**Authors:** Junlong Wu, Zijun Li, Yuting Hu, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26375v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26375v1)

**Summary:** Commercial image editing requires product identity preservation, accurate text rendering, and user appeal alongside general editing quality. We present KwaiMind, an image editing system combining general capabilities with e-commerce specialization. An agent-based data engine maintains approximately 1.8 million high-quality editing pairs. Built on a multimodal diffusion transformer, KwaiMind undergoes continued pre-training and supervised fine-tuning, followed by preference optimization and onlin...

---

### 39. On the Role of the Projector in Contrastive Self-Supervised Learning: Last-Layer Rank Dynamics Drive Representation Quality

**Authors:** Siladittya Manna, Priyangshu Mandal, Umapada Pal, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26334v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26334v1)

**Summary:** The dimensional collapse of representations in self-supervised contrastive learning is an ever-present issue. One notable technique to prevent such a collapse of representations is using a multi-layered perceptron network called Projector. In several works, the projector has been found to heavily influence the quality of representations learned in a self-supervised contrastive pre-training task. However, the question still lingers. What role does the projector play? Assuming the projector mitiga...

---

### 40. Leveraging Vision-Based Point Cloud Map Priors for Camera-Based 3D Object Detection and Online Vectorized HD Mapping

**Authors:** Markus Käppeler, Rohit Mohan, Abhinav Valada

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26325v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26325v1)

**Summary:** Camera-based 3D object detection and online vectorized HD mapping provide compact scene representations for autonomous driving, but both depend on accurate metric geometry and remain limited by depth ambiguity. Over long-term deployment, observations from repeated traversals can be accumulated into persistent point cloud priors that provide geometric context beyond the current observations. Existing explicit point cloud prior approaches, however, rely on LiDAR-based map construction and therefor...

---

### 41. ForeDrive: Foresight-Guided End-to-End Autonomous Driving with a Planning-Relevant Latent World Model

**Authors:** Sinuo Wang, Zichong Gu, Yuhan Huang, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26299v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26299v1)

**Summary:** Existing latent world models are typically optimized for future predictability, yet the resulting representations are not necessarily useful for planning in autonomous driving. Predictions are commonly used for pretraining or auxiliary supervision rather than as direct conditioning signals for trajectory generation. We propose ForeDrive, which learns a planning-relevant latent representation and couples it asymmetrically to a Diffusion Transformer (DiT) planner. The planner consumes multi-horizo...

---

### 42. EMERGE: Resolution-Agnostic Point Cloud Generation with Equivariant Graph-Based Diffusion

**Authors:** Ilias Mitsouras, Nikolaos Chaidos, Giorgos Stamou, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26039v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26039v1)

**Summary:** Point cloud generation has emerged as a crucial task for accurately capturing and reproducing the complexity of the physical world. However, existing generative approaches, predominantly relying on Transformers and Variational Autoencoders (VAEs), frequently ignore the continuous, non-grid topologies inherent to 3D spaces. Although the integration of graph-based structures has yielded significant benefits in related discriminative vision tasks, such geometric architectures remain noticeably abse...

---

### 43. Faithful Faithfulness Evaluations: Challenges & Pitfalls Learned from a Breast MRI Case Study

**Authors:** Peachapong Poolpol, Henrik H. J. Detjen, Eike Petersen

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25978v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25978v1)

**Summary:** Saliency maps are widely used to explain deep learning predictions in medical imaging, yet visually plausible explanations do not necessarily reflect a model's true decision process and may therefore mislead clinicians. We investigate this problem using a Vision Transformer-based breast MRI classifier trained on the ODELIA Breast MRI Challenge dataset and evaluate multiple saliency methods, including Last-layer Attention, Attention Rollout, Grad-SAM, Gradient Attention Rollout, GMAR, Grad-CAM, a...

---

### 44. NAWE: Digital Watermarking with Neural-Assisted Watermark Extraction

**Authors:** Roman Chaban, Vitaliy Kinakh, Lilian Rouzaire, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25972v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25972v1)

**Summary:** NAWE (Neural-Assisted Watermark Extraction) combines an explicit signal-processing watermarking construction with a pretrained neural host predictor. A periodic, perceptually masked watermark carrier provides synchronization, Polar coding supplies redundancy, and denoising followed by subtraction extracts the embedded watermark. The denoiser remains frozen, without watermark-specific training. A one-factor-at-a-time study compares Wiener, BM3D, DRUNet, and GS-DRUNet host estimators. Comparisons ...

---

### 45. GRIP: Gaussian Rendering as a Cross-Modal Bridge for Image-to-Point Cloud Registration

**Authors:** Karim Slimani, Catherine Achard, Eric Marchand, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25966v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25966v1)

**Summary:** This paper introduces GRIP, a pose-conditioned refinement framework for pixel-to-point matching and 2D to 3D registration. Given an initial coarse pose estimate, GRIP addresses the structural mismatch between grid based image descriptors and unordered point cloud descriptors by softly rendering learned 3D point features onto the image grid through Gaussian feature splatting. The rendered point derived feature map is then fused with image features by a pixel aligned transformer, enabling visual s...

---

### 46. Towards Systematic Qualification of Vision-Language Models for Automotive Perception Systems

**Authors:** Malsha Ashani Mahawatta Dona, Konstantinos Rokanas, Alexander Säfström, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25945v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25945v1)

**Summary:** The field of Artificial Intelligence has been adopted for many application domains. Vision Language Models are one of the recently advanced AI techniques that have been explored to support automotive features such as vehicle perception, and safety assurance. However, such language models are prone to hallucinations, posing a potential threat to the safety of automotive systems that may incorporate them. Within the automotive domain, VLMs could not only hallucinate traffic objects, but could also...

---

### 47. Calibrating Retrieval Geometry: Reliability-Guided Training-Free Aggregation for Visual Place Recognition

**Authors:** Xin Li, Zhimin Mao, Shang Wang, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25937v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25937v1)

**Summary:** Frozen visual foundation models provide transferable features for visual place recognition, but fixed aggregation can suppress useful distinctions in new environments. We introduce TFA, a reliability-guided, training-free aggregation method requiring neither place labels nor task-specific weight updates. Our key observation is that reproducible retrieval need not be discriminative: independent codebooks can consistently retrieve a few database hubs. TFA combines cross-codebook agreement, retriev...

---

### 48. AT3D-AD: Anomaly Type-Aware 3D Anomaly Detection via Hierarchical Point-Language Alignment

**Authors:** Jingyu Zeng, Haoquan Lu, Can Gao

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25930v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25930v1)

**Summary:** Detecting and localizing 3D point-cloud defects is essential for industrial inspection. However, existing methods often suffer from imprecise localization due to the lack of anomaly supervision and reliance on single-granularity representations. To address these limitations, we propose Anomaly Type-Aware 3D Anomaly Detection (AT3D-AD), a unified framework for joint detection, localization, and classification. Specifically, we first design the Physics-Driven Parametric Anomaly Synthesis (PDPAS) m...

---

### 49. NaCR: Visual Localization via NeRF-aided Camera Ray Regression

**Authors:** Yesheng Zhang, Xiang Dai, Xu Zhao, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25907v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25907v1)

**Summary:** Visual localization (VL) is a fundamental technology for vision applications such as virtual reality. Recently, a novel VL paradigm, Camera Ray Regression (CRR), has emerged, which maps 2D image patches to 3D camera rays, but its accuracy is limited. To improve CRR accuracy, we notice a compelling duality: the inverse of this mapping is inherently performed by the novel view synthesis model, \ie, Neural Radiance Fields (NeRF). While NeRF renders image patches from camera rays via differentiable ...

---

### 50. BAS-OPD: Budget-Aware Selective On-Policy Self-Distillation for Fine-Grained Multimodal Perception

**Authors:** Zihan Chen, Hengguang Zhou, Yuan Kang, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25891v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25891v1)

**Summary:** Multimodal large language models (MLLMs) often struggle with fine-grained visual perception when processing complete images, as critical evidence may only appear in local regions. On-policy self-distillation (OPD) enables transferring privileged visual knowledge from informative views to full-image policies, but querying the teacher for every rollout introduces substantial supervision costs. In this work, we propose BAS-OPD, a budget-aware selective OPD framework that allocates teacher supervisi...

---

## cs.LG

**50 papers**

### 1. A Decentralized Partially Observable Team Decision Methodology with Delayed Information Sharing

**Authors:** Xiaoxing Ren, Thomas Parisini, Andreas A. Malikopoulos

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26783v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26783v1)

**Summary:** We study decentralized partially observable team decision problems with low-rank latent dynamics and unknown system models. The proposed framework combines team-theoretic equivalence with low-rank model representations to address cooperative decision-making in partially observable Markov decision processes without prior knowledge of the transition model. Each team member makes decisions based on local private information and delayed common information shared across the team. Using only this avai...

---

### 2. SpeakerMem-R1: Speaker-Centered Dual-Track Memory for Multi-Party Dialogue

**Authors:** Haobo Zheng, Tan Tang, Yan Chen, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26780v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26780v1)

**Summary:** Long-term conversational memory in multi-party settings requires more than retrieving relevant content from long-term conversations: it must distinguish who said what, whom each statement concerns, how individuals perceive one another, what information is shared by the group, and how states change over time. Recent studies on multi-party dialogue benchmarks show that existing general-purpose LLM memory systems tend to lose person and group relations or struggle to integrate clues distributed acr...

---

### 3. CliffCompaction: Cost-Efficient Compaction for Long-Horizon Coding Agents

**Authors:** Trang Nguyen, Eulrang Cho, Bingqing Chen, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26779v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26779v1)

**Summary:** Agents often work on complex problems that require millions of tokens of context, which necessitates compacting across sessions due to limited context windows. We develop CliffCompaction, an autocompaction technique that reduces cost by up to 50% under a bounded context while maintaining or improving performance on Terminal-Bench and achieving new levels of efficiency for test-time scaling and state-of-the-art results on KernelBench. The per-rollout savings of CliffCompaction make the performanc...

---

### 4. EquivSVA: A Formally Verified Dataset of Behavioral Assertions Across Equivalent RTL Implementations

**Authors:** FNU Aditi

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26751v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26751v1)

**Summary:** Large language models are increasingly used to generate SystemVerilog Assertions from natural-language specifica- tions and register-transfer-level designs. Existing datasets and benchmarks support important goals such as large- scale training, formal evaluation, specification-to-assertion generation, and mutation-based testing. A complemen- tary need is to study whether a generated assertion cap- tures externally observable behavior or depends on inci- dental details of one RTL implementation. ...

---

### 5. Automatic depth-based local center clustering via $β$-integrated local depth and adaptive grouping

**Authors:** Siyi Wang, Alexandre Leblanc, Paul D. McNicholas

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26748v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26748v1)

**Summary:** Clustering is an unsupervised learning technique that partitions unlabeled data into groups. Most existing methods require user-specified parameters, such as the number of clusters or neighborhood size. Conversely, we propose automatic depth-based local center clustering (A-DLCC), a fully data-driven method that eliminates numerical parameter tuning. A-DLCC uses the $β$-integrated local depth to identify stable exemplars, points consistently central across multiple locality levels, termed local ...

---

### 6. Diffusion-Induced Spatial Attention Overlapping Community Detection

**Authors:** Kosti Koistinen, Vesa Kuikka, Joni Herttuainen, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26737v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26737v1)

**Summary:** Detection of overlapping communities is essential for modelling networks in which nodes participate simultaneously in multiple structural or functional groups. Existing graph neural network approaches commonly rely on local message passing, which can obscure community boundaries through smoothing and limit the representation of structurally relevant long-range dependencies. We introduce Diffusion-Induced Spatial Attention Community Detection (DISCO), a deep-learning framework that combines a str...

---

### 7. The Sirens' Song: When Proximal Background Context Overshadows Distant Evidence

**Authors:** Xiaoyu Yang, Jie Lu, Wei Duan, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26718v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26718v1)

**Summary:** Long-context LLMs focus on retrieving distant evidence from extensive context, yet existing work has largely focused on overcoming distance alone. In this work, we identify the Proximity Trap, insufficient attention to distant evidence often arises less from distance itself than from cumulative competition with abundant, task-irrelevant proximal background. To address the Proximity Trap, we introduce LYRA (Long-context heavY-tailed Relevance Alignment), a t-distributed directional matching mecha...

---

### 8. Train Where the Quantized Model Goes: On-Policy Distillation for Low-Bit Reasoning

**Authors:** Yuanteng Chen, Zhilei Liu, Peisong Wang, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26708v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26708v1)

**Summary:** Quantization-aware distillation (QAD) restores much of the short-form question-answering performance lost to sub-3-bit quantization, yet leaves mathematical and code reasoning substantially impaired. Long generations often degenerate into repetitive loops, exhausting the decoding budget without completing a solution. We trace this gap to quantization-amplified exposure bias: QAD trains on fixed corpus prefixes, while quantization-induced deviations compound along the model's own autoregressive t...

---

### 9. Optimal Sequential Annotations for Off-Policy Evaluation

**Authors:** Woojin Chae, Ezinne Nwankwo, Haitong Qin, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26707v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26707v1)

**Summary:** Offline reinforcement learning and off-policy evaluation evaluates dynamic treatment rules based on retrospectively collected data prior to deployment. In recent AI applications, state and reward information is recorded as complex text or image, which recent AI advancements such as LLM-as-a-judge can label with unknown bias. Expert annotation may be available but at a higher cost. For example, safety classification via cheap but imperfect classifiers vs. expensive expert review. We show how a li...

---

### 10. When are bosonic Gaussian states classical to learn?

**Authors:** Senrui Chen, Antonio Anna Mele, Francesco Anna Mele, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26705v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26705v1)

**Summary:** A fundamental question in physics is: When does classical behavior emerge from quantum systems? Bosonic Gaussian states provide a natural setting to explore this quantum-classical boundary, as they capture both the classical field behavior and the intrinsic quantum nature of light. Here, we address this problem from a learning-theoretic perspective by asking: When are bosonic Gaussian states classical to learn? That is, under what conditions (if any) can an n-mode bosonic Gaussian state be learn...

---

### 11. PROSWIN: Probabilistic Solar Wind Speed Forecasting Using Deep Distributional Regression From Solar Images

**Authors:** Daniel Collin, Yuri Shprits, Luca Chiarabini, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26683v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26683v1)

**Summary:** Accurately predicting fast solar wind conditions is challenging, as uncertainties are large and unquantified by traditional single-value prediction models. In particular, the risks of high-speed solar wind streams (HSSs), which can cause damage to technological infrastructure, cannot be reliably assessed without probabilistic forecasts. We present PROSWIN, a probabilistic machine learning model that forecasts the hourly solar wind speed (SWS) at Earth with a four-day lead time. The approach comb...

---

### 12. A Spectral Theory of Grokking: Weight Decay induces Feature Learning

**Authors:** Lenz Pracher, Pascal de Jong, Oskar Lieshaus, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26679v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26679v1)

**Summary:** In grokking an early fit to the training data separates from a much later improvement in generalization. During this delay, training can move from a fixed neural tangent kernel (NTK) regime to one in which task-relevant kernel eigendirections continue to evolve. We provide a quantitative theory for how this transition from lazy to rich learning can produce delayed generalization. For homogeneous networks trained with squared loss and $L_2$ weight decay, we show that a finite residual remains aft...

---

### 13. MAGIC: Mixed-Granularity Agent Graphs via Incremental Construction with Dense-Reward Reinforcement Learning

**Authors:** Kairui Yang, Ziheng Yi, Xunkai Li, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26667v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26667v1)

**Summary:** Collaboration topology shapes both the performance and execution cost of LLM-based multi-agent systems. Because tasks differ in complexity and required capabilities, recent approaches generate task-specific collaboration graphs that specify agent participation and information flow. However, representative topology generators use either individual agents or predefined groups throughout an organization, overlooking differing collaboration needs across subtasks. Our key insight is to select granula...

---

### 14. Discovery-Driven Integration of Disjoint Tables via Text

**Authors:** Md Ataur Rahman, Dimitris Sacharidis, Oscar Romero, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26658v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26658v1)

**Summary:** Integrating heterogeneous datasets within data lakes is a critical challenge, particularly for semantically related tables that lack the explicit attributes needed to be joined. We study Discovery-Driven Integration, where the relevant sources and their missing relational structure must be discovered before integration. In this setting, unstructured text provides the evidence that connects otherwise disjoint tables. The fundamental challenge is to discover the relationships at a fine-grained lev...

---

### 15. Statistical Rates for Entropic Optimal Transport in the Discrete to SubGaussian Regime

**Authors:** Tomas Gonzalez, Gonzalo Mena

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26647v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26647v1)

**Summary:** We study statistical rates in entropic optimal transport in the semi-discrete regime where one measure has finite support and the other is subGaussian. Our main result establishes parametric convergence rates for the empirical dual potentials to their population counterparts, with no dimension dependence in the leading term. Our result relies on tailored strong concavity analysis of the semi-dual objective, coupled with specialized bounds for the semi-discrete potentials. As a consequence, we ob...

---

### 16. The Delegation Blind Spot: Auditing Product Decisions from Agent Choices

**Authors:** Shivam Gupta

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26642v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26642v1)

**Summary:** Successful agent execution need not identify which future product improvement its user would value. We present a decision-specific audit that maps a declared observation channel and product-value contrast to compatible intervals and witness populations. Its foundations are established identification and decision theory; the contribution is an executable measurement workflow and a controlled study of its limits. A frozen experiment makes 4,800 requests to two pinned model snapshots on shared synt...

---

### 17. Label-Efficient Learning for Ground-Based Sky-Image Classification: A Benchmark of Transfer Learning, Active Learning, and Pseudo-Labeling on GCD

**Authors:** Esther Bou Dagher, Viktoriya Bu-Dager, Boguslaw Zegarlinski

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26631v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26631v1)

**Summary:** Accurate ground-based cloud classification is important for atmospheric monitoring, solar-energy forecasting, aviation weather assessment, and climate observation systems. However, reliable sky-image annotation is time-consuming, especially when cloud types are visually similar or mixed. We study the label efficiency of deep learning for ground-based cloud classification using the Ground-based Cloud Dataset (GCD). Rather than proposing a new architecture, we benchmark three practical strategies ...

---

### 18. On Basis Function Selection for Sparse Gaussian Process Regression

**Authors:** Marnix Van Soom, Ivan De Boi

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26624v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26624v1)

**Summary:** Sparse Gaussian processes achieve $O(N)$ inference by replacing the kernel with an appropriate expansion in a fixed basis $\{φ_j\}$ on the input space. Given a compute budget $M \ll N$, practitioners conventionally truncate the basis to its first $M$ entries. Nothing in the formalism, however, prevents one from selecting only those $M$ basis functions that matter for the data at hand. This would avoid spending budget on basis functions where there is no signal, but it requires a criterion for ra...

---

### 19. Greedy Decoding Is Not Precision-Invariant: Cross-Precision Output Divergence in LLM Inference

**Authors:** Gaoyuan Du, Anam Nawaz Khan, Rex Zhou, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26621v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26621v1)

**Summary:** Greedy decoding from large language models is commonly treated as deterministic. We show it is not precision-invariant: the same model, prompt, and decoding algorithm produce different outputs in BF16 versus FP16 on identical hardware. Across our evaluations of six models (1.1B-7B parameters, four families; divergence additionally characterised at 12B) and three benchmarks, 49-100\% of prompts diverge; a single token flip often cascades into trajectory-level divergence. We develop an empirical e...

---

### 20. MMAP: Multimodal Missing-Aware Pretraining for Longitudinal Alzheimer's Prediction

**Authors:** Fiona Kekwick, Matthew Baugh, Bernhard Kainz, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26617v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26617v1)

**Summary:** Clinical decision making heavily relies on predicting the disease progression trajectory by seeking to understand patient's health status which is characterised by multimodal medical data. AI holds great potential for learning useful representations from multimodal medical data to predict disease progression and aid clinical decision making. However, development of predictive AI models is constrained by missing modalities and incomplete tabular data frequently occurring in medical datasets. In a...

---

### 21. Foundation model embeddings capture pre-diagnostic changes on screening mammograms

**Authors:** Kalina P. Slavkova, Eric Brattain, Aditya Gowd, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26605v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26605v1)

**Summary:** Foundation model embeddings of screening mammograms may encode pre-diagnostic tissue change without task-specific adaptation. We tested whether embeddings move faster along a data-derived "cancer direction" in women later biopsied for cancer than in matched screen-negative controls, and whether this depends on pretraining domain. We studied 1,773 biopsied women (785 malignant, 988 biopsy-negative) and 1,773 matched controls, each with at least two annual screening exams before their index exam. ...

---

### 22. Towards Hierarchical GNNs for multi-grid power flow: generalization across operating scenarios

**Authors:** Carmine Delle Femine, Leire Garin Atxaga, Asier Diaz-Iglesias, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26603v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26603v1)

**Summary:** Hierarchical latent communication improves the generalization of a multi-grid power-flow model to new operating scenarios. The module exchanges information through two reduced graphs within a GENCO-based corrective network. We compare Kron-derived transports, a same-anchor Quotient construction and a flat backbone in preliminary trainings of 200 epochs on three grid topologies, with three initialization seeds per model. Evaluation uses 200 newly generated, preselected scenarios per grid. On the ...

---

### 23. Unlocking Cross-Scenario Physical Layer Security: A Mixture-of-Experts Framework with Generative Diffusion Models

**Authors:** Xiao Tang, Tong Hui, Chao Shen, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26598v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26598v1)

**Summary:** The future 6G networks are expected to incorporate a proliferation of wireless services in diverse environments, which presents a significant challenge for information security. Conventionally optimization always requires recalculation and learning strategy often suffers poor generalization, which are thus incapable for the security provisioning with wide scenario coverage. In this paper, we propose an adaptive and robust learning framework that leverages a mixture-of-experts (MoE) architecture ...

---

### 24. GTR: Gated Token Recurrence for Efficient Dense Prediction

**Authors:** Zhe Feng, Longfei Liu, Wei Liu, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26590v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26590v1)

**Summary:** Self-attention-based vision backbones perform well on dense prediction, but the quadratic computational cost of global softmax attention limits their efficiency as image resolution increases. We introduce Gated Token Recurrence (GTR), a softmax-free recurrent vision backbone that combines gated linear attention, alternating spatial scan directions, and spatially enhanced SwiGLU blocks. GTR is distilled from a detection-specialized DINOv3 teacher using only final-layer patch-token alignment throu...

---

### 25. Polyak-Type Extragradient Methods for Monotone Root-Finding Problems

**Authors:** TaeHo Yoon, Sayantan Choudhury, Ezra Greenberg, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26581v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26581v1)

**Summary:** We study Polyak-type step-size selection for extragradient methods for solving deterministic and stochastic monotone root-finding problems. We show that the known projection-type correction for deterministic extragradient arises from minimizing an upper bound on the distance to a solution, paralleling the classical Polyak step-size construction. Using this viewpoint, we provide a unified deterministic analysis of the Polyak-type Extragradient Method (PolyakEG), based on a local critical conditio...

---

### 26. Notes on Fourier-Bessel wavelets

**Authors:** Marcel Venturotti, Georgios Exarchakis

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26537v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26537v1)

**Summary:** These notes develop the mathematical foundations and construction of a Fourier-Bessel wavelet family inspired by the disk harmonics of Shaqfa et al.[9]. We begin with the relevant properties of Bessel and modified Bessel functions and introduce the wavelet properties required for the construction. We then derive the Fourier-Bessel disk harmonics as solutions to the Helmholtz equation on the unit disk subject to a Neumann boundary condition.   Building on this basis, we construct a wavelet family...

---

### 27. Gap-Free Streaming PCA Beyond Rank-One Updates: Near-Optimal Rates and Applications to Differential Privacy

**Authors:** Anming Gu, Syamantak Kumar, Kevin Tian, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26508v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26508v1)

**Summary:** Streaming principal component analysis (PCA) seeks to recover a leading spectral subspace in a single pass over a data stream. We give a new analysis of the ubiquitous Oja's algorithm [Oja82] for the most general, gap-free variant of this problem, where no eigengap assumptions are made on the underlying mean matrix, complemented by a nearly-matching lower bound. Prior works achieving near-optimal rates for streaming PCA either required gap assumptions [JJK+16, HNWW21], or were limited to rank-on...

---

### 28. Deep Generative Crystal Structure Prediction: A Benchmark Study and a Controlled Test of Prototype Dependence

**Authors:** Lai Wei, Rongzhi Dong, Ying Feng, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26502v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26502v1)

**Summary:** Deep generative models are widely reported to enable de novo crystal structure prediction (CSP), but their capability has not been measured consistently against template-based methods. We evaluate 12 representative generative CSP models, spanning latent-variable, diffusion, flow-matching, autoregressive, and manifold random-walk architectures, against TCSP 2.0 on 180 test structures and a leakage-controlled subset of 46. All methods use identical structure-matching, symmetry, and consensus crite...

---

### 29. When Recursive Models Finish Computing

**Authors:** Hare Krishna, Shubham Singh, Stephen Ebert, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26487v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26487v1)

**Summary:** Recursive models can continue updating their latent states beyond their nominal inference budget, so an incorrect output at that budget does not show whether computation is unfinished or has entered a persistently unsuccessful regime. We study the dynamics of completion in attention- and MLP-based Tiny Recursive Models (TRMs) on 1,000 hard Sudoku puzzles. Extending recurrence from the nominal 16 steps to 512 steps increases cumulative exact-solve accuracy from 59.2% to 87.5% for the attention mo...

---

### 30. PP-Net: A Hybrid Physical-Prior Neural Network for Scattered Light Removal in Biomedical Images on Embedded Devices

**Authors:** Yongfei Guo, Tingjin Chu, Mengzhuo Liu, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26474v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26474v1)

**Summary:** Scattered light is common in biomedical images, yet its removal remains challenging. The difficulty arises from three aspects: first, aligned scattered-light-free biomedical ground truth is often unavailable; second, scattering is coupled with weak illumination and sensor-induced noise; and third, many learning-based restoration models are computationally expensive for embedded devices in Internet of Medical Things (IoMT) scenarios. To address these issues, this paper proposes PP-Net, a hybrid p...

---

### 31. Can We Predict Anomaly Detection Performance from Embedding-Space Geometry?

**Authors:** Kevin Wilkinghoff, Zheng-Hua Tan

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26460v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26460v1)

**Summary:** Anomaly detection systems are often trained using normal data alone, while model selection and evaluation typically require labeled anomalies. We study whether anomaly detection performance can be predicted without access to anomalous data. For kNN-based detectors, we derive a lower bound on the area under the ROC curve (AUC) that relates detection performance to the separation between inlier and outlier scores and to their respective variances. Under a local scaling model, we use this bound to ...

---

### 32. Recursive self-improvement of AI research agents

**Authors:** Dhruv Srikanth, Bingchen Zhao, Dixing Xu, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26457v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26457v1)

**Summary:** AI agents are beginning to automate research and development across the AI stack, from improving training efficiency to optimizing inference. A natural next step is to improve the research efficiency of the agents themselves. When an AI research agent's own code is the object of optimization, each accepted rewrite becomes the agent that the next round edits. We refer to this loop as recursive self-improvement. Its significance lies in a long-standing trend, in which increased cumulative spending...

---

### 33. A Practical Guide on Graphical Model Validation

**Authors:** Mario V. Wüthrich

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26445v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26445v1)

**Summary:** This manuscript formalizes the most popular model validation tools used in general insurance actuarial modeling. These include graphical tools like calibration plots, actual-vs-expected plots, lift charts, Murphy diagrams, as well as classical statistical tools such as Bregman losses, deviance losses, elementary losses, Murphy's decomposition and Gini scores. Particular emphasis is placed on whether calibration and discrimination are studied under a policy-weighted or an exposure-weighted popula...

---

### 34. One-Step Generative Surrogate Models via Block-Triangular Joint Drifting

**Authors:** Nicholas Geissler, Shreya Jha, Ricardo Baptista, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26435v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26435v1)

**Summary:** Drifting provides a direct route to one-step generative models, but applying it directly to stochastic transition modeling requires multiple samples of the next state conditioned on the same current state. Standard trajectory data, however, typically provide only one realized next state for each observed current state and therefore do not provide an empirical approximation of the corresponding conditional distribution over possible next states. We introduce block-triangular joint drifting, which...

---

### 35. DeepFEAv2: Deep Learning for Transient Finite Element Analysis Beyond Structured Meshes

**Authors:** Georgios Triantafyllou, Panagiotis G. Kalozoumis, Dimitris K. Iakovidis

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26426v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26426v1)

**Summary:** Finite Element Analysis (FEA) is widely used for transient mechanical simulations, but its high computational cost limits real-time and high-resolution applications. Deep learning surrogate models can reduce this cost; however, many existing approaches are restricted to steady-state prediction or cannot jointly predict Node- and Element-based Outputs (NEO) over time. The state-of-the-art DeepFEA framework has addressed these issues but remains limited to structured finite element (FE) meshes. To...

---

### 36. SuperPCA: subspace analysis and an efficient algorithm for high-dimensional PCA

**Authors:** Irina-Beatrice Haas, Maike Meier, Yuji Nakatsukasa, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26406v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26406v1)

**Summary:** Principal component analysis (PCA) is a fundamental tool to reduce the dimensionality of the data in many applications. PCA finds a few signal directions that contain most of the variability of the data by computing the eigenvectors of the sample covariance matrix. In this work, we focus on the spiked covariance model, in which the data vectors are defined by a few orthogonal signals plus an isotropic Gaussian noise, and our goal is to estimate one or more of the leading signals. Our main theore...

---

### 37. OMatG-flash: An All-Atom Flow Map with Reinforce Adjoint Matching for Scalable Materials Discovery

**Authors:** Thomas Egg, Harry Winston Sullivan, Ellad B. Tadmor, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26402v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26402v1)

**Summary:** The discovery of novel inorganic materials drives technological breakthroughs in critical fields such as computing and energy storage. Generative AI has promised to accelerate the materials discovery pipeline, but state-of-the-art flow and diffusion models remain bottlenecked by the cost of proposing candidate materials. To address this, we introduce OMatG-flash, an all-atom flow map for inorganic crystal structure prediction (CSP) and de novo generation (DNG). OMatG-flash is a Pareto-optimal in...

---

### 38. Double Descent and Malign Overfitting in Diffusion Models

**Authors:** Raphaël Urfin, Tony Bonnaire, Giulio Biroli, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26392v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26392v1)

**Summary:** Conventional wisdom in deep learning holds that overparameterization---having more parameters $p$ than training samples $n$---is benign: larger models generalize better and, even without regularization, interpolating models generalize well, the test error following a double-descent curve. One might expect the same benign overfitting for diffusion models, whose training reduces to regression, i.e. to minimizing a quadratic score-matching loss. Yet the opposite is observed: overfitting here is cat...

---

### 39. TimeInteract: Towards Real-Time Interactive Intelligence for Streaming Time Series

**Authors:** Sheng Pan, Yongli Gu, Yiqing Guo, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26389v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26389v1)

**Summary:** Real-world time series evolve continuously, with meaningful changes potentially emerging at any moment. However, existing time-series language models (TSLMs) remain inherently static. They either receive complete sequences for offline processing or alternate between streaming input and response generation, which prevents processing of new observations during interaction. We introduce a new regime, Time-Series Interaction: a model continuously perceives incoming time-series observations and user ...

---

### 40. On the Lexical Superstition of Large Language Models for Code Comprehension: Re-evaluation on Code of Low Lexical Quality

**Authors:** Xin Shen, San-Zhuo Xi, Yali Du, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26388v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26388v1)

**Summary:** Recent advances in large language models (LLMs) have made them widely used for code-related tasks. Identifier names are statistically informative in naturally occurring code, but their information is not always reliable. We investigate whether current LLMs assign disproportionate weight to lexical cues when renaming preserves program structure. We introduce Face/Off, a semantics-preserving identifier-renaming framework, and evaluate progressive naming conditions across multiple models and code-c...

---

### 41. Learning to Defer with Guidance on Real World Medical Data

**Authors:** Emma Sun, Joshua Strong, Alison Noble

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26384v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26384v1)

**Summary:** Medical image interpretation is high-volume and time-consuming, and while AI interpretation can reduce workload, fully autonomous deployment carries potential safety concerns and low specificity may in practice lead to increased clinician workload. Learning to Defer (L2D) addresses this by selectively routing cases between autonomous prediction and human experts by learning from input features and AI model and human performance. While theoretical guarantees have been proven for L2D, its performa...

---

### 42. MAVP: Map-Aware Visuomotor Policies for Mobile Manipulation

**Authors:** Jinhe Tang, Ruixiao Dai, Weiming Zhi

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26378v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26378v1)

**Summary:** Successful mobile manipulation requires coordinated base and arm motion while maintaining accurate spatial positioning. However, demonstration-trained policies can struggle to realise the intended base motion reliably, leading to spatial misalignment and subsequent manipulation failures. We present MAVP (Map-Aware Visuomotor Policies), a framework that improves execution reliability by predicting explicit base-pose targets and tracking them using localisation feedback. MAVP reconstructs a static...

---

### 43. FairMean: Promoting Fairness in Distributed Learning under Label Poisoning Attacks

**Authors:** Huigan Zheng, Jiaojiao Zhang, Yongxiang Liu

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26377v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26377v1)

**Summary:** Fairness-aware distributed learning prioritizes clients with large losses to reduce performance disparities, but label poisoning can create large losses, thereby inducing a fairness--robustness conflict. We propose FairMean to manage this conflict. FairMean weights client gradients using a bounded, nondecreasing function of local loss. The increasing weights prioritize high-loss clients to promote fairness, while the upper bound prevents excessive loss-induced amplification of poisoned-client gr...

---

### 44. GitScholar: A Dataset for Predicting AI Research Impact from GitHub Engagement

**Authors:** Emilien Guandalino, Lorenz K. Müller, Beatrice Alessandra Motetti, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26361v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26361v1)

**Summary:** With the rapid pace of AI research and the hundreds of daily new publications, staying up-to-date with the latest developments has become increasingly difficult. For researchers, quickly identifying impactful work is essential, yet manually reviewing each new publication is impractical. Automated impact prediction methods help address this challenge, usually by combining various information sources available, such as a paper's content or citation history. In this work, we propose using GitHub en...

---

### 45. PACT: From Credit Assignment to Critic Alignment

**Authors:** Jiayan Fu, Hang Xu, Yong Zhang, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26355v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26355v1)

**Summary:** Reinforcement learning has become a central component of large language model (LLM) post-training, yet token-level credit lacks a generally accepted mathematical definition, leaving its relationship to commonly used training signals unclear. We formulate three regularity conditions, namely Completeness, Prefix Consistency, and Neutrality, and prove that they uniquely determine token-level credit. This characterization provides a unified basis for explaining phenomena across existing algorithms a...

---

### 46. HYDRA: Proactive Android Malware Drift Adaptation via Hierarchical Graph Contrastive Learning

**Authors:** Han Chen, Hanchen Wang, Hongmei Chen, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26352v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26352v1)

**Summary:** Concept drift, driven by the rapid evolution of Android malware, severely degrades the performance of machine learning detectors. Current adaptation strategies are often reactive, responding only after performance has dropped and imposing a significant manual annotation burden, or they are proactive but rely on unstable adversarial training and incomplete, single-level graph representations. To overcome these limitations, we propose HYDRA (Hybrid Drift Adaptation), a proactive adaptation framewo...

---

### 47. TransBERT: A Framework for Synthetic Translation in Domain-Specific Language Modeling

**Authors:** Julien Knafou, Luc Mottin, Anaïs Mottaz, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26347v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26347v1)

**Summary:** The scarcity of non-English language data in specialized domains significantly limits the development of effective Natural Language Processing (NLP) tools. We present TransBERT, a novel framework for pre-training language models using exclusively synthetically translated text, and introduce TransCorpus, a scalable translation toolkit. Focusing on the life sciences domain in French, our approach demonstrates that state-of-the-art performance on various downstream tasks can be achieved solely by l...

---

### 48. Geometry-Aware Hyperbolic Residual Quantization

**Authors:** Alessio Colombo, Melika Ayoughi

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26342v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26342v1)

**Summary:** Residual Vector Quantization turns continuous representations into discrete, multi-level token sequences. Yet most methods operate in Euclidean space, despite the coarse-to-fine structure of the resulting codes and the latent hierarchies present in many data domains. Hyperbolic geometry offers a natural alternative for hierarchical representations, but naive hyperbolic extensions introduce geometric inconsistencies: non-associative hyperbolic addition prevents consistent residual aggregation, wh...

---

### 49. Disaggregated Quantization: Specializing LLM Prefill and Decode

**Authors:** Andrei Panferov, Maximilian Kleinegger, Sweta Priyadarshi, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26333v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26333v1)

**Summary:** Prefill and decode reward different approaches to quantization: low-precision arithmetic accelerates prompt processing, while compact weights reduce memory traffic during generation. We propose "disaggregated quantization" (DQ), which specializes computation formats, weights and storage placement to both of these phases. On Qwen 3 and Gemma 3, removing activation quantization specifically on decode improves accuracy on decode-heavy tasks without increasing inference cost. Training separate compu...

---

### 50. Error Bounds for Statistical Estimators in BTL Model with Parametric Multivariate Utility Functions

**Authors:** Yicheng Li, Huifu Xu

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26326v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26326v1)

**Summary:** We study preference elicitation under the Bradley-Terry-Luce (BTL) model where the true partworth vector is unknown and has to be estimated as a parameter with elicited preference information. The set of selected pairwise queries is non-uniform, deterministic, and arbitrary over a collection of alternatives, provided that it satisfies a joint identifiability condition. We focus on understanding when the canonical maximum likelihood estimator (MLE) is finite and admits sharp error bounds without ...

---

## q-bio.NC

**50 papers**

### 1. Deep Learning in Infant Functional Neuroimaging: Challenges, Advances, and Future Directions

**Authors:** Dan Hu, Jiale Cheng, Weiran Xia, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26688v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26688v1)

**Summary:** Infancy is a critical developmental window characterized by rapid functional brain reorganization, during which large-scale networks emerge, individualized connectome signatures continue to form, and early deviations may shape long-term cognitive and clinical outcomes. Functional MRI (fMRI) offers an opportunity to study these processes in vivo, yet extracting developmentally meaningful information from it remains challenging due to comparatively short scan duration, structured motion artifacts,...

---

### 2. Physics-constrained inference of somatic dynamics from dendritic recordings with sparse somatic supervision in weakly coupled two-compartment neuron model

**Authors:** Abdeltif Oujbara, Benjamin Ambrosio, M. A. Aziz-Alaoui

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.25436v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25436v1)

**Summary:** Somatic membrane potential is the primary determinant of neuronal output, yet it remains inaccessible in many experimental setups where only dendritic recordings are available. Reconstructing somatic dynamics from distal measurements is a challenging inverse problem, particularly when the soma and dendrites are weakly coupled, as dendritic signals represent a filtered and attenuated version of somatic activity. To address this, we use a physics-informed neural network (PINN) constrained by a two...

---

### 3. A theory of plasticity: capacity for change as inverse configurational constraint

**Authors:** Igor Branchi

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.25312v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25312v1)

**Summary:** Plasticity is invoked across the sciences to explain how systems can change, yet it is inferred from the very change it is meant to explain. A system may have many alternatives, realize none and still be plastic. Another may be driven far toward its only alternative, but the magnitude of that change does not establish its plasticity. What matters for plasticity is not how far the system moves but how strongly its present configuration constrains alternatives. Here I propose that plasticity, unde...

---

### 4. Binding-Motivated Contextuality: A Cross-Domain Cyclic Test in Perception and Judgment

**Authors:** Adam Y. Shavit

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.23977v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23977v1)

**Summary:** Perceptual binding and the contextuality of judgment are studied apart, in psychophysics and decision research. We argue they share one obstruction: a nonzero class in $H^1$ of a presheaf with no global section -- though only contextuality is tested, since binding's obstruction vanishes. We build on sheaf formulations of predictive coding (Seely 2025) and contextuality (Abramsky & Brandenburger 2011): a cyclic set of pairwise judgments admits a global (noncontextual) explanation exactly when the...

---

### 5. Matched-Input Estimates Differ in Sign Across Architectures: Auditing EEG Foundation Models on Motor Imagery

**Authors:** Kevin Zhou, Sparsh Roy

**Published:** 2026-09-20

🔗 [Paper](http://arxiv.org/abs/2609.23924v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23924v1)

**Summary:** Pretrained EEG foundation models are increasingly proposed as general-purpose encoders for brain-computer interfaces, yet recent benchmarks disagree about when their representations transfer to downstream tasks. We audit LaBraM and CBraMod on motor imagery under a validation-locked protocol in which preprocessing, architecture, optimization, freeze depth, checkpoint, temperature, and method selection are determined using training-session data only. On four-class BCI Competition IV-2a, every supe...

---

### 6. A discrete generative model of neuronal spiking activity on microelectrode arrays

**Authors:** Md Sayed Tanveer, Mohammed A. Mostajo-Radji, Ge Wang

**Published:** 2026-09-20

🔗 [Paper](http://arxiv.org/abs/2609.23907v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23907v1)

**Summary:** Generative models of neural activity could help characterize tissue dynamics, compare experimental conditions, and simulate population activity for applications ranging from disease and drug-response studies to closed-loop experimentation. Existing approaches, however, typically assume a fixed set of sorted neurons, whereas high-density microelectrode arrays produce extremely sparse, array-wide binary spike volumes in which the observed subset of electrodes varies across assays. We introduce a d...

---

### 7. From Biological Precursors to Artificial Cognition: Consciousness, Embodiment, and the MEM Architecture

**Authors:** Janusz A. Starzyk, Wiesław L. Galus

**Published:** 2026-09-20

🔗 [Paper](http://arxiv.org/abs/2609.23828v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23828v1)

**Summary:** This article asks under what conditions artificial intelligence could warrant a rational attribution of consciousness. Linguistic ability, multimodality, memory, planning, action control, and humanoid embodiment are not sufficient evidence of phenomenal experience. Biological precursors such as excitability, homeostasis, neural networks, and hierarchical representation instead identify functions whose counterparts may be engineered. The paper compares conventional LLMs, hybrid h-LLMs, vision-lan...

---

### 8. Chaotic Dynamics-Regulated Topological Learning for Patient-Specific Preictal State Identification

**Authors:** Zihan Wang, Daixin Li, Guilin Wang, et al.

**Published:** 2026-09-20

🔗 [Paper](http://arxiv.org/abs/2609.23317v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23317v1)

**Summary:** Epileptic seizures arise from complex, nonlinear interactions within brain networks, yet reliable electroencephalographic (EEG) prediction remains challenging due to the nonstationary and heterogeneous nature of neural dynamics. Existing methods typically analyze EEG data as static or weakly time-dependent snapshots, overlooking the intrinsic dynamics and lacking the geometric sensitivity to capture the hierarchical, localized evolution of the epileptogenic zone. To address these limitations, we...

---

### 9. BrainWideBench: Benchmarking large-scale pretraining and across-animal transfer in multi-region neural recordings

**Authors:** Alexandre Andre, Shivashriganesh P. Mahato, Vinam Arora, et al.

**Published:** 2026-09-18

🔗 [Paper](http://arxiv.org/abs/2609.22064v1) | 📄 [PDF](https://arxiv.org/pdf/2609.22064v1)

**Summary:** Advances in large-scale neural recording have made it possible to collect data across many animals and distributed brain regions, raising the question of whether this scale can be exploited to learn general-purpose neural representations transferable across diverse downstream tasks. Yet, progress toward this goal has been limited by fragmented evaluation protocols and a narrow focus on individual task domains. Here, we present BrainWideBench, a benchmark for evaluating across-animal transfer on ...

---

### 10. Identifying Neural State Changes due to Gain versus Off-Manifold Displacement

**Authors:** Sam McKenzie

**Published:** 2026-09-18

🔗 [Paper](http://arxiv.org/abs/2609.21272v1) | 📄 [PDF](https://arxiv.org/pdf/2609.21272v1)

**Summary:** Memory segmentation is thought to arise from rapid decorrelation in neural activity, often quantified by Euclidean distance or cosine angle. Although these metrics detect a transition, they do not reveal how the new state relates to the repertoire represented by the neural manifold. This matters because neuromodulators that drive state transitions also alter excitability, and learning may repurpose existing representations or create new ones. Here, I introduce a geometric decomposition that sepa...

---

### 11. Foundation-model-based multi-label phenotyping of combined hyperkinetic movement disorders

**Authors:** Laura Cif, Zohra Souei, Diane Demailly, et al.

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.22369v1) | 📄 [PDF](https://arxiv.org/pdf/2609.22369v1)

**Summary:** Movement disorders (MDs) frequently co-occur, yet phenomenological and severity assessment shows substantial inter-rater variability. Markerless video could improve reproducibility, but prior work is largely single-symptom, depends on standardized acquisition, and lacks validation and transfer across ages and sites. We combined two foundation models into one frozen backbone: Segment Anything Model 3 (SAM 3) for dense, per-frame markerless segmentation summarized into geometric, contour and grid ...

---

### 12. A Deep Neural Network for Predicting Continuous Human EEG Across the Auditory Pathway in Response to Sound

**Authors:** Thomas J Stoll, Ross K Maddox

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20595v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20595v1)

**Summary:** Computational models of auditory physiology commonly target specific responses or stages of the auditory pathway, limiting their ability to integrate findings across experimental paradigms and neural timescales. We present a foundation model of human auditory electrophysiology: a causal neural network trained to map binaural acoustic waveforms directly to high-sample-rate EEG. The model was trained on approximately 250 hours of EEG data from 92 subjects, with varied electrode montages and stimul...

---

### 13. A Mathematical Model of Motivated Emotional Mind - Cognitive Embodied System

**Authors:** Wiesław L. Galus, Janusz A. Starzyk

**Published:** 2026-09-17

🔗 [Paper](http://arxiv.org/abs/2609.20437v1) | 📄 [PDF](https://arxiv.org/pdf/2609.20437v1)

**Summary:** This article presents a mathematical model of the Motivated Emotional Mind cognitive architecture developed for embodied intelligent systems. Such a system learns to maintain its homeostasis through a generalized form of reinforcement learning based on its internal motivations, termed motivated learning (ML). The principal contribution of this article is a rigorous formalization of the re-entrant loop integrating feedforward processing, lateral interactions, and feedback pathways, together with ...

---

### 14. Neural noise enables accurate internal simulation of rare events

**Authors:** Heng Zhang, Pawel Herman, Zenas C. Chao

**Published:** 2026-09-16

🔗 [Paper](http://arxiv.org/abs/2609.18033v1) | 📄 [PDF](https://arxiv.org/pdf/2609.18033v1)

**Summary:** The brain needs an accurate internal model of the world to generate predictions and guide behavior. However, it must estimate the statistical structure of the environment from limited experience. This is particularly difficult for rare events, whose observed frequencies in a limited sample may substantially under- or overestimate their true frequencies. How the brain constructs an accurate internal model despite this sampling problem remains unclear. We address this problem using a Bayesian Conf...

---

### 15. Spike Sorting with VanillaSort

**Authors:** Zishuo Feng, Feng Cao

**Published:** 2026-09-15

🔗 [Paper](http://arxiv.org/abs/2609.22322v1) | 📄 [PDF](https://arxiv.org/pdf/2609.22322v1)

**Summary:** Training spike detectors on real recordings is challenging because algorithmically generated labels can be noisy and incomplete. We propose VanillaSort, combining multichannel detection with spatially augmented, template-guided clustering. VanillaDet uses visibility-aware masking, truncated Gaussian targets and a temporally tolerant positive-bag loss, followed by conditional event-SNR gating. VanillaCluster combines HuiduRep embeddings with relative-amplitude features for Gaussian mixture cluste...

---

### 16. Learning Options for Compositional Motor Control with Adapter Banks

**Authors:** Sreejan Kumar, Marcelo Mattar, Lea Duncker

**Published:** 2026-09-15

🔗 [Paper](http://arxiv.org/abs/2609.17042v1) | 📄 [PDF](https://arxiv.org/pdf/2609.17042v1)

**Summary:** Learning flexible motor primitives is a hallmark of skilled motor control. Recent neuroscience theory proposes that motor primitives may be implemented as low-rank perturbations of a shared recurrent network, but leaves open how such a system is learned. We translate this principle into a novel architecture for learning motor skills end-to-end: a shared recurrent core modulated by a bank of residual adapters, each selected by a discrete latent code. Trained on closed-loop biomechanical control, ...

---

### 17. Predictor Construction Can Reverse Multimodal Neural Contrasts

**Authors:** Lucas Nadolskis, Galen Pogoncheff, Michael Beyeler

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.16430v1) | 📄 [PDF](https://arxiv.org/pdf/2609.16430v1)

**Summary:** Foundation-model features are increasingly used to ask what information neural activity represents, often by comparing prediction gains between nested encoding models. We show that such multimodal contrasts can change sign when only the conditioning predictor is reconstructed. Using fMRI from the Natural Scenes Dataset, DINOv2 visual features, and MPNet embeddings of MS COCO captions and Localized Narratives, a caption-narrative contrast in the additional predictive contribution of vision favors...

---

### 18. A neural-astrocyte architecture implements a hybrid automaton for evidence accumulation

**Authors:** Giacomo Vedovati, Ilya E. Monosov, Thomas J. Papouin, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.16217v1) | 📄 [PDF](https://arxiv.org/pdf/2609.16217v1)

**Summary:** Astrocytes are non-neuronal glial cells that are receiving widespread attention due to their emerging role in neural computation. In this paper, we propose and study dynamical mechanisms by which astrocytes may augment the ability of neural networks to infer context in reinforcement learning (RL) settings. We construct a biologically inspired, two-level dynamical neural-astrocyte network with distinct spatial and temporal organization. We train this model on a hierarchical multi-context task tha...

---

### 19. Decision-Related Cognitive Signatures from Fast-Slow Dynamics: A Low-Dimensional Observation-Operator Framework

**Authors:** Furkan Emre Isik, Ali Demirci

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15918v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15918v1)

**Summary:** Repeated decisions exhibit temporal structures such as persistence, direction-dependent switching, recurrent alternation, and abrupt transitions. We examine the generative sufficiency of a two-dimensional fast-slow dynamical system. The system combines a cubic fast equation with linear slow feedback and is analyzed through its equilibrium geometry, trace-determinant structure, equilibrium-fold loci, candidate Hopf boundaries, and singular critical manifold. An explicit observation operator proje...

---

### 20. The Cross-Substrate Access Assay: What an Indicator Test Must Declare to Travel from Brain to Language Model

**Authors:** Pieter van Rooyen

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.22300v2) | 📄 [PDF](https://arxiv.org/pdf/2609.22300v2)

**Summary:** Testing an artificial system for a property linked to consciousness means applying a measurement developed on brains to a system that is not one. Such a transfer must re-examine five parts of the procedure: the competing statistical models, how they are fitted, the unit the inference generalizes over, the quantity the uncertainty interval is about, and the rule that turns a result into a verdict. The Cross-Substrate Access Assay declares all five. Because brain and model signals share no physica...

---

### 21. When Teachers Smile or Frown: A Profile-Based Analysis of Achievement Emotions

**Authors:** Rudra Mukhopadhyay, Satyaki Mazumder, Koel Das

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15747v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15747v1)

**Summary:** Achievement emotions shape how students engage with and learn from academic tasks, yet most studies examine individual emotions rather than co-occurring affective profiles and their dynamics. We examined latent achievement-emotion profiles and their transitions following exposure to different instructor facial expressions during a video lecture. Self-reported data from 78 Grade VII and VIII students revealed three profiles: enthusiastic, demotivated, and vulnerable. Profile transitions differed ...

---

### 22. Nonlinear dynamics of random neural networks with second-order synaptic motifs

**Authors:** Jun Yang, Hannah Choi

**Published:** 2026-09-13

🔗 [Paper](http://arxiv.org/abs/2609.14251v1) | 📄 [PDF](https://arxiv.org/pdf/2609.14251v1)

**Summary:** Classical theories of random neural networks typically assume independent connectivity, overlooking the local motif structures prevalent in biological circuits. Here, we investigate how four second-order synaptic motifs (chain, reciprocal, convergent, and divergent) shape the dynamics of nonlinear firing-rate networks. While previous studies have established that chain correlations generate outlier eigenvalues, we demonstrate that these motifs also jointly reshape the Jacobian eigenvalue bulk. U...

---

### 23. URCHIN: A Horizontal Spiking Language Model for Data-Constrained Pretraining

**Authors:** Po-Han Chiang

**Published:** 2026-09-12

🔗 [Paper](http://arxiv.org/abs/2609.13899v1) | 📄 [PDF](https://arxiv.org/pdf/2609.13899v1)

**Summary:** The BabyLM challenge measures how much language a model can learn from developmentally-plausible, child-scale data rather than internet-scale corpora, yet prior language models forgo the biological constraints of the neural circuitry that acquires human language: spiking neurons separated into excitatory and inhibitory populations wired by a recurrent lateral connectome. This paper presents URCHIN (Unified Recurrent Connectome with Horizontal Integrate-and-fire Neurons), which applies the Parall...

---

### 24. Hierarchical emergence of network bursting in a four-cell central pattern generator model

**Authors:** Krishna Pusuluri, Huiwen Wu, Andrey L. Shilnikov

**Published:** 2026-09-12

🔗 [Paper](http://arxiv.org/abs/2609.13858v1) | 📄 [PDF](https://arxiv.org/pdf/2609.13858v1)

**Summary:** How can a neural circuit rhythmically burst when none of its constituent neurons can endogenously do so? We address this question through a bottom-up reconstruction of a 4-cell neural circuit modeled after the swim central pattern generator (CPG) of the sea slug \textit{Dendronotus iris}. We first map the intrinsic regimes of a swim interneuron (SiN) model neuron and show that slow mutual inhibition can generate anti-phase bursting in a half-center oscillator (HCO) assembled from tonic-spiking o...

---

### 25. Pretraining for Sample-Efficient Neural Interfaces

**Authors:** Ben Tang, Zachary Spalding, Gregory B. Cogan

**Published:** 2026-09-11

🔗 [Paper](http://arxiv.org/abs/2609.13507v1) | 📄 [PDF](https://arxiv.org/pdf/2609.13507v1)

**Summary:** Brain-computer interfaces (BCIs) decode neural activity to restore lost function. Typically, training a high-performance neural decoder requires a large labeled dataset to be collected from every new subject. One way to reduce the labeled data cost is self-supervised pretraining, which learns general neural representations from unlabeled recordings that accumulate across subjects. However, for intracranial electroencephalography (iEEG) recordings, self-supervised learning has been challenging du...

---

### 26. Stability and Wandering of Bumps in Neural Fields with Interneuron Subtypes

**Authors:** Bilal Ahmed, Heather Cihak, Gregory Handy

**Published:** 2026-09-11

🔗 [Paper](http://arxiv.org/abs/2609.13074v1) | 📄 [PDF](https://arxiv.org/pdf/2609.13074v1)

**Summary:** The maintenance of continuous variable information in working memory is thought to rely on persistent patterns of cortical activity. In delayed-estimation tasks, neural activity can form localized activity peaks, or ``bumps,'' whose positions track the remembered variable. Such activity is well described by continuous-attractor neural field models, but most existing models collapse cortical inhibition into a single homogeneous population. Here, we introduce a stochastic neural field model with d...

---

### 27. pyAvalanches: A Python Package for Analyzing Spatiotemporal Propagation in Neuronal Avalanches

**Authors:** M. Marzulli, A. Angiolelli, C. Mannino, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11530v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11530v1)

**Summary:** The analysis of neuronal avalanches offers insights into brain dynamics utilizing the framework of criticality, but the reproducibility and comparability of studies are limited by the use of fragmented, lab-specific scripts. To address this issue, we introduce pyAvalanches, an open-source Python package providing a standardized, end-to-end pipeline for avalanche analysis from electrophysiological recordings (e.g., electroencephalography-EEG). Starting from the detection of neuronal avalanches th...

---

### 28. Degeneracy along the sensorimotor hierarchy: motor control within a framework larger than redundancy

**Authors:** Florent Paclet, Paul Duprat

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.11325v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11325v1)

**Summary:** Motor control has described the surplus of solutions available to the nervous system as redundancy, a term that names duplication: interchangeable elements, robust to loss but incapable of differential adaptation. Biology has had a second term for twenty-five years. Degeneracy names elements that are not interchangeable and are nonetheless isofunctional with respect to a given output, and it supports adaptability, since non-identical elements necessarily diverge in some context. Circuit neurosci...

---

### 29. The Platonic brain bridge hypothesis: human brain networks as an architectural prior for multimodal large language models

**Authors:** Pengfei Zhang, Biao Tian, Xiangang Li, et al.

**Published:** 2026-09-10

🔗 [Paper](http://arxiv.org/abs/2609.10947v2) | 📄 [PDF](https://arxiv.org/pdf/2609.10947v2)

**Summary:** Multimodal large language models predict brain activity, but brain alignment has been a measurement, not a design tool. We propose the Platonic brain bridge hypothesis: omni models, multimodal large language models that process video, audio and text jointly, converge on brain-like representations usable in both directions. From model to brain, brain-likeness of seven omni models is stable across participants, rises with every input channel in three bases, and our encoders lead the Algonauts 2025...

---

### 30. Discovering Subtypes of Neurodegenerative Progression with a Scalable Connectome-Constrained Dynamic Model

**Authors:** Daniel Semchin, Emile d'Angremont, Hao Ding, et al.

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.10890v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10890v1)

**Summary:** Parkinson's disease is clinically and biologically heterogeneous, yet its spatiotemporal progression remains poorly characterized. We present a connectome-constrained disease progression model that jointly estimates subject-specific disease time and data-driven subtypes from longitudinal morphometry. Applied to 85 imaging and clinical biomarkers from the Parkinson's Progressive Markers Initiative (PPMI) cohort, the model recovers four morphologically distinct progression subtypes. We validate th...

---

### 31. Cortical information transfer reveals conserved hemispherical network dynamics across human handedness

**Authors:** Yago Emanoel Ramos, José Garcia Vivas Miranda

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.10870v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10870v1)

**Summary:** Whether human motor and brain lateralization arises from fundamentally distinct neural architectures or emerges from conserved network dynamics remains a central question at the intersection of network science and neurobiology. Conventional measures of cortical activation often fail to resolve how directed information exchange adapts to manual preference during complex motor tasks. This ambiguity leaves it unclear whether left-handed individuals possess atypical neural organization or follow sha...

---

### 32. BrainTaskonomy: Learning How to Pretrain and What to Transfer in fMRI Foundation Models

**Authors:** Junfeng Xia, Wenhao Ye, Junxiang Zhang, et al.

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.10518v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10518v1)

**Summary:** fMRI foundation models increasingly aggregate heterogeneous data across brain states, cohorts, and acquisition settings, yet pretraining domains are commonly treated as a flat mixture and downstream tasks are adapted independently. We study whether measured learning relations can organize both stages without modifying the backbone. During pretraining, a lightweight Brain-DiT proxy estimates difficulty and directed facilitation across ten fMRI domains, yielding a priority-guided cumulative domain...

---

### 33. A Bio-Plausible Visual Neural Network for Locust-Inspired Collision Perception

**Authors:** Qinbing Fu, Jiani Li, Jiajun Huang, et al.

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.10183v1) | 📄 [PDF](https://arxiv.org/pdf/2609.10183v1)

**Summary:** Locust visual systems have long served as an important biological paradigm for studying looming perception and collision avoidance. Numerous computational models have successfully reproduced the selective responses of Lobula Giant Movement Detector (LGMD) neurons to approaching objects, thereby emulating the fundamental functionality of the biological system. However, existing models remain limited in biological plausibility and robustness when operating in complex and dynamic visual environment...

---

### 34. EEGBind: Detecting Source-Level Interictal Epileptiform Discharges via EEG-Centric Multimodal Binding

**Authors:** Muchen Li, Anglin Liu, Xuetian Gao, et al.

**Published:** 2026-09-09

🔗 [Paper](http://arxiv.org/abs/2609.09728v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09728v1)

**Summary:** Source-level analysis of interictal epileptiform discharges (IEDs) is relevant to presurgical evaluation and treatment planning because it helps characterize where epileptiform activity is likely to arise. Beyond detecting whether an IED is present, this setting requires assigning IED-positive activity to clinically meaningful brain-region categories. This setting is challenging because source-region evidence in short electroencephalography (EEG) windows can be subtle, partial, and affected by s...

---

### 35. The Computational Primitives of Adaptation

**Authors:** Jonathan W. Page

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.11989v1) | 📄 [PDF](https://arxiv.org/pdf/2609.11989v1)

**Summary:** Research on adaptive systems has traditionally focused on behavior (what organisms do) and mechanism (how their machinery works). This paper focuses on a third level, computation, which considers what adaptive systems must compute to survive and reproduce. It is proposed that adaptation has its own computational structure, comprising a small set of primitive operations common to all adaptive systems, regardless of their physical form. Six primitives, Arouse, Orient, Valence, Position, Boundary, ...

---

### 36. Emergence of criticality in models of real neurons

**Authors:** David P. Carcamo, Christopher W. Lynn

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.09438v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09438v1)

**Summary:** Critical systems sit near boundaries between qualitatively distinct behaviors. When inferring models of neural activity, this proximity to criticality is thought to require the precise tuning of parameters. Here, we show that as the number of neurons increases, criticality can emerge naturally without fine-tuning. When computing observable statistics from parameters (the forward problem), some small regions in parameter space map to large regions in statistics space. These special parameters are...

---

### 37. XAI-Refine: An Automated Explanation-Knowledge Loop for Brain-Age Prediction

**Authors:** Yang Qiao, Junjie Wu, Deqiang Qiu, et al.

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.09388v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09388v1)

**Summary:** Brain-age prediction models are commonly evaluated by predictive accuracy, yet accurate predictions alone do not establish that a model relies on reproducible or neurobiologically supported mechanisms. Post-hoc explanation methods can expose these mechanisms, but existing workflows typically stop at diagnosis or require correction targets to be specified before model analysis. We propose XAI-Refine, an automated explanation-knowledge loop for brain-age prediction from resting-state functional co...

---

### 38. Hi-M imaging of chromatin architecture in adult Drosophila brain cryosections

**Authors:** Christel Elkhoury Youhanna, Julie Garona, Marie Schaeffer, et al.

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.08776v1) | 📄 [PDF](https://arxiv.org/pdf/2609.08776v1)

**Summary:** Hi-M combines fluorescence in situ hybridization (FISH), automated microfluidics, sequential imaging, and computational chromatin tracing to measure the three-dimensional organization of selected genomic regions in single cells. This chapter describes a Hi-M workflow adapted for cryosections of adult Drosophila melanogaster brains, enabling chromatin tracing while preserving tissue architecture and cell identity. The protocol covers Oligopaint library design and amplification, fixation, brain di...

---

### 39. Why shared attention vectors fail: a case for outcome-indexed tuning

**Authors:** Lenard Dome

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.08615v1) | 📄 [PDF](https://arxiv.org/pdf/2609.08615v1)

**Summary:** Dimensional attention in learning is often implemented as a globally shared attention vector, where each stimulus dimension corresponds to a single scalar. These scalars are learned by models through gradient-descent on error, where predictive features acquire more salience. We show that under multi-outcome learning, where models predict more than one outcome, this shared vector becomes unstable; it collapses to its bounds and prevents the models from learning meaningful attentional tunings for ...

---

### 40. An Evidence-Aware Framework for EEG Microstate Analysis: Improved Sensitivity to Alzheimer's Disease and Ageing

**Authors:** Kaidong Wu, Haili Ye, Ptolemaios G Sarrigiannis, et al.

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.08500v1) | 📄 [PDF](https://arxiv.org/pdf/2609.08500v1)

**Summary:** Electroencephalography (EEG) microstate analysis commonly converts each scalp topography into a winner-take-all hard label and summarises the resulting sequence using duration, occurrence, coverage, transitions, and symbolic complexity. Although interpretable, this readout discards evidence strength, assignment ambiguity, and low-confidence periods. We introduce a template evidence trajectory framework that retains, at each sampled Global Field Power (GFP) peak, the evidence for all templates or...

---

### 41. A Gradient-based yet Spike-Timing-Dependent Solution to the Feedback Learning Problem in Neural Microcircuits

**Authors:** Xiangnan Zhang, Jingxin Liu, Ranqi Lu, et al.

**Published:** 2026-09-08

🔗 [Paper](http://arxiv.org/abs/2609.08070v2) | 📄 [PDF](https://arxiv.org/pdf/2609.08070v2)

**Summary:** The brain uses discrete spikes for dynamic computation, yet, how neural microcircuits (NMCs) solve temporal credit assignment using local spike timing remains a fundamental open question. Dominant spiking neural network (SNN) approaches circumvent this by approximating backpropagation through surrogate gradients, decoupling learning from biological spike timing. Here, we reformulate temporal credit assignment as a state separation problem: extracting task-required components induced by historica...

---

### 42. Fisher-Rao Distance Detects Shifts in Kinematic Profiles under Cognitive Load

**Authors:** Joseph Vero, Elizabeth B Torres

**Published:** 2026-09-07

🔗 [Paper](http://arxiv.org/abs/2609.07696v1) | 📄 [PDF](https://arxiv.org/pdf/2609.07696v1)

**Summary:** Motor control research involves the study of movement kinematics derived from the positional trajectories that complex motions describe. In natural, unconstrained motions requiring cognitive and memory processes in real time, the temporal speed profiles are not bell-shaped, may have multiple maxima and the peaks distribution is best fit by the continuous gamma family with two parameters, the shape and the scale. As the stochastic processes described by complex motion trajectories are non-station...

---

### 43. Exploring the robustness of permutation entropy analysis to differentiate between closed-eyes and open-eyes resting states

**Authors:** Juan Gancio, Natalia López López, Antonio J. Pons, et al.

**Published:** 2026-09-07

🔗 [Paper](http://arxiv.org/abs/2609.22265v1) | 📄 [PDF](https://arxiv.org/pdf/2609.22265v1)

**Summary:** Electroencephalography (EEG) is a noninvasive technology that is widely used to monitor brain states, and many efforts are focused on developing reliable and efficient data analysis methods for EEG recordings. Here, we apply ordinal analysis to the EEG recording of the resting state of 109 healthy subjects measured in two different conditions: with eyes closed (EC state) or eyes open (EO state). We study the robustness of the temporal permutation entropy ($PE$) and the spatial permutation entrop...

---

### 44. Fisher Information Metric as a model-free measure of proximity to criticality in neural systems

**Authors:** Yuewei Du, Alberto Liardi, Hardik Rajpal, et al.

**Published:** 2026-09-07

🔗 [Paper](http://arxiv.org/abs/2609.07624v1) | 📄 [PDF](https://arxiv.org/pdf/2609.07624v1)

**Summary:** Critical phenomena are widespread across many disciplines and have recently become a topic of deep interest in the study of biological and artificial neural networks. A distinct signature of criticality is the emergence of avalanches with power-law-distributed sizes and durations. However, empirically estimating the critical exponents remains challenging, and their interpretation is often model-dependent. In this work, we demonstrate how the Fisher Information Metric (FIM), a measure of generali...

---

### 45. Homeostasis Revisited and Reformulated Through Hidden Markov Model Control

**Authors:** Rubén Moreno-Bote

**Published:** 2026-09-07

🔗 [Paper](http://arxiv.org/abs/2609.07508v1) | 📄 [PDF](https://arxiv.org/pdf/2609.07508v1)

**Summary:** A common formalization of homeostasis is the free energy principle, a framework that defines a set of desired observation values, or critical states, that the agent should reach or remain close to. Under the free energy principle, an agent should act to maximize the probability of receiving the desired observations. Here we revisit the common approach of solving the problem of maximizing the log probability of the desired observations by maximizing a variational lower bound, the so-called negati...

---

### 46. Revisiting the Aerts-Broekaert-Smets quantum model of the liar paradox

**Authors:** Massimiliano Sassoli de Bianchi

**Published:** 2026-09-07

🔗 [Paper](http://arxiv.org/abs/2609.09228v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09228v1)

**Summary:** The quantum model of the two-sentence liar paradox proposed by Aerts, Broekaert, and Smets is an early example of the use of quantum formalism to describe cognitive dynamics. Our reconstruction is primarily pedagogical in intent, but it also leads to a number of clarifications, and to some new observations, concerning the structure of the model. Rewriting the model in Dirac notation, we make explicit the distinction between truth values originating from a decision and from semantic inference, an...

---

### 47. Determinants of hyperparameter robustness in connectome reservoir computing

**Authors:** Miles Walter Churchland, Raul de Palma Aristides, Jordi Garcia-Ojalvo, et al.

**Published:** 2026-09-07

🔗 [Paper](http://arxiv.org/abs/2609.07355v1) | 📄 [PDF](https://arxiv.org/pdf/2609.07355v1)

**Summary:** Reservoir computing provides a controlled setting for studying how recurrent network architectureshapes computation: input signals are projected into a high-dimensional state space by a fixed nonlinear dynamical system, and only the readout is trained. However, reservoir performance can be dependent on hyperparameters; this paper asks which recurrent network features support robustness to those parameter changes. We characterize computational performance using memory capacity (MC), truncated sin...

---

### 48. Adaptive Entangled Game Modules in Artificial General Intelligence

**Authors:** Haochen Li, Xinshuai Guo, Jingdong Ouyang, et al.

**Published:** 2026-09-07

🔗 [Paper](http://arxiv.org/abs/2609.09226v1) | 📄 [PDF](https://arxiv.org/pdf/2609.09226v1)

**Summary:** We introduce a probability-wave framework for modeling the collective behavior of interacting adaptive agents, deriving testable eigenmodes through a generalized behavioral intelligence (GBI) nonlocal probability-wave equation. This framework captures a broad range of human intelligence behaviors with analytical mechanisms and offers an indirect method to examine the Liu-Chen-Ao (LCA) hypothesis of nonlocal entangled nerve fibers in the brain through collective trader behaviors. Our empirical an...

---

### 49. Formation of structural attractors in neuromorphic systems

**Authors:** Yurii Parzhyn, Alexander Schwarzmann, Mykyta Lapin, et al.

**Published:** 2026-09-06

🔗 [Paper](http://arxiv.org/abs/2609.06826v1) | 📄 [PDF](https://arxiv.org/pdf/2609.06826v1)

**Summary:** This paper examines the theory of Invariant Structural Learning (ISL), which proposes a non-optimization approach to concept formation. Learning is interpreted as convergence to structural attractors in a hypergraph space, rather than as the minimization of a global loss function. The paper presents the ISL model, including its mathematical formalization, computational verification, and a hypothetical neurobiological interpretation. The mathematical section introduces the formal apparatus of the...

---

### 50. A Roadmap for MEG Foundation Models

**Authors:** Philipp Thölke, Hamza Abdelhedi, Yorguin Mantilla-Ramos, et al.

**Published:** 2026-09-03

🔗 [Paper](http://arxiv.org/abs/2609.04461v2) | 📄 [PDF](https://arxiv.org/pdf/2609.04461v2)

**Summary:** Foundation models are beginning to reshape brain-signal analysis by moving the field beyond task-specific decoding pipelines toward reusable models pretrained on broad neural datasets. Magnetoencephalography (MEG) is a compelling but still underdeveloped target for this shift: it captures human cortical dynamics at millisecond resolution while offering stronger spatial interpretability than EEG, making it especially valuable for source-resolved studies of perception, language, cognition, and cli...

---

## stat.ML

**50 papers**

### 1. A Decentralized Partially Observable Team Decision Methodology with Delayed Information Sharing

**Authors:** Xiaoxing Ren, Thomas Parisini, Andreas A. Malikopoulos

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26783v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26783v1)

**Summary:** We study decentralized partially observable team decision problems with low-rank latent dynamics and unknown system models. The proposed framework combines team-theoretic equivalence with low-rank model representations to address cooperative decision-making in partially observable Markov decision processes without prior knowledge of the transition model. Each team member makes decisions based on local private information and delayed common information shared across the team. Using only this avai...

---

### 2. Automatic depth-based local center clustering via $β$-integrated local depth and adaptive grouping

**Authors:** Siyi Wang, Alexandre Leblanc, Paul D. McNicholas

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26748v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26748v1)

**Summary:** Clustering is an unsupervised learning technique that partitions unlabeled data into groups. Most existing methods require user-specified parameters, such as the number of clusters or neighborhood size. Conversely, we propose automatic depth-based local center clustering (A-DLCC), a fully data-driven method that eliminates numerical parameter tuning. A-DLCC uses the $β$-integrated local depth to identify stable exemplars, points consistently central across multiple locality levels, termed local ...

---

### 3. Optimal Sequential Annotations for Off-Policy Evaluation

**Authors:** Woojin Chae, Ezinne Nwankwo, Haitong Qin, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26707v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26707v1)

**Summary:** Offline reinforcement learning and off-policy evaluation evaluates dynamic treatment rules based on retrospectively collected data prior to deployment. In recent AI applications, state and reward information is recorded as complex text or image, which recent AI advancements such as LLM-as-a-judge can label with unknown bias. Expert annotation may be available but at a higher cost. For example, safety classification via cheap but imperfect classifiers vs. expensive expert review. We show how a li...

---

### 4. Context-Adaptive Thresholding for Conditionally Representative Monitoring and Classification

**Authors:** Ansgar Steland

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26652v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26652v1)

**Summary:** Commonly, classifiers and monitoring procedures are trained from labeled data by optimizing an objective such as the misclassification rate. This may lead to unrepresentative conditional distributions of the outcome (the labels) given important external variables, different from the conditional laws in the population. We show how to modify any given threshold-type classifier resp. monitoring rule to achieve representative conditional label prediction by using adapting the threshold to a covariat...

---

### 5. On Basis Function Selection for Sparse Gaussian Process Regression

**Authors:** Marnix Van Soom, Ivan De Boi

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26624v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26624v1)

**Summary:** Sparse Gaussian processes achieve $O(N)$ inference by replacing the kernel with an appropriate expansion in a fixed basis $\{φ_j\}$ on the input space. Given a compute budget $M \ll N$, practitioners conventionally truncate the basis to its first $M$ entries. Nothing in the formalism, however, prevents one from selecting only those $M$ basis functions that matter for the data at hand. This would avoid spending budget on basis functions where there is no signal, but it requires a criterion for ra...

---

### 6. Gap-Free Streaming PCA Beyond Rank-One Updates: Near-Optimal Rates and Applications to Differential Privacy

**Authors:** Anming Gu, Syamantak Kumar, Kevin Tian, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26508v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26508v1)

**Summary:** Streaming principal component analysis (PCA) seeks to recover a leading spectral subspace in a single pass over a data stream. We give a new analysis of the ubiquitous Oja's algorithm [Oja82] for the most general, gap-free variant of this problem, where no eigengap assumptions are made on the underlying mean matrix, complemented by a nearly-matching lower bound. Prior works achieving near-optimal rates for streaming PCA either required gap assumptions [JJK+16, HNWW21], or were limited to rank-on...

---

### 7. A Practical Guide on Graphical Model Validation

**Authors:** Mario V. Wüthrich

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26445v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26445v1)

**Summary:** This manuscript formalizes the most popular model validation tools used in general insurance actuarial modeling. These include graphical tools like calibration plots, actual-vs-expected plots, lift charts, Murphy diagrams, as well as classical statistical tools such as Bregman losses, deviance losses, elementary losses, Murphy's decomposition and Gini scores. Particular emphasis is placed on whether calibration and discrimination are studied under a policy-weighted or an exposure-weighted popula...

---

### 8. SuperPCA: subspace analysis and an efficient algorithm for high-dimensional PCA

**Authors:** Irina-Beatrice Haas, Maike Meier, Yuji Nakatsukasa, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26406v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26406v1)

**Summary:** Principal component analysis (PCA) is a fundamental tool to reduce the dimensionality of the data in many applications. PCA finds a few signal directions that contain most of the variability of the data by computing the eigenvectors of the sample covariance matrix. In this work, we focus on the spiked covariance model, in which the data vectors are defined by a few orthogonal signals plus an isotropic Gaussian noise, and our goal is to estimate one or more of the leading signals. Our main theore...

---

### 9. Error Bounds for Statistical Estimators in BTL Model with Parametric Multivariate Utility Functions

**Authors:** Yicheng Li, Huifu Xu

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26326v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26326v1)

**Summary:** We study preference elicitation under the Bradley-Terry-Luce (BTL) model where the true partworth vector is unknown and has to be estimated as a parameter with elicited preference information. The set of selected pairwise queries is non-uniform, deterministic, and arbitrary over a collection of alternatives, provided that it satisfies a joint identifiability condition. We focus on understanding when the canonical maximum likelihood estimator (MLE) is finite and admits sharp error bounds without ...

---

### 10. Learning to Fluctuate: Statistical Foundations for Causal Tabular Pretraining

**Authors:** Zhiheng Zhang

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26290v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26290v1)

**Summary:** Causal tabular foundation models amortize effect estimation across synthetic mechanisms, but latent-effect supervision rewards posterior shrinkage instead of directly encoding the repeated-sample response needed in a fixed deployment population. We introduce fluctuation-supervised pretraining (FSP): each synthetic table is labeled by its average treatment effect plus its efficient influence-function fluctuation, while deployment remains a single frozen forward pass. Along the path $T_{λ,P}=θ(P)+...

---

### 11. xWhyL: Causal Interactive Learning

**Authors:** Nicholas Tagliapietra, Florian Peter Busch, Moritz Willig, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.26037v1) | 📄 [PDF](https://arxiv.org/pdf/2609.26037v1)

**Summary:** Explanations are central to causal reasoning, and cognitive science has long established that the human drive to explain is itself a mechanism for learning about causality. Despite this, learning from those abductive signals is largely ignored in artificial intelligence. While explainable AI (XAI) increasingly draws on causal models to generate explanations, the converse direction about what explanations can do for causality remains largely unexplored. To fill this gap, we propose xWhyL, a forma...

---

### 12. Conditional Tensor Diffusion: Distributional Counterfactual Learning and Inference

**Authors:** Xinbing Kong, Zeyu Li, Junfan Mao, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25924v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25924v1)

**Summary:** Causal inference guides operational and managerial decisions but remains challenging in high-dimensional panel or tensor settings, where decisions may depend on the joint conditional distribution of missing control outcomes. We develop \emph{Counterfactual Tucker Diffusion} (\CFTDiff), which integrates the treatment mask and latent Tucker structure into conditional diffusion to recover this distribution given observed control outcomes through efficient nonlinear score learning in a low-dimension...

---

### 13. Beyond Scalar Sensitivity: Activation-Aware Mixed-Precision LLM Quantization with Cross-Layer Refinement

**Authors:** Akihiro Yoshida, Yuma Ichikawa

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25916v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25916v1)

**Summary:** Mixed-precision weight quantization is commonly formulated as a Multiple-Choice Knapsack Problem (MCKP), yet existing solvers rely on scalar sensitivity proxies that collapse each weight matrix's Hessian into a single number and treat every module independently. We prove that even the optimal scalar proxy incurs multiplicative distortion up to $\sqrt{κ(\mathbf{A})κ(\mathbf{B})}$ relative to the full activation-aware quadratic, where $κ(\mathbf{A})$ and $κ(\mathbf{B})$ denote the condition number...

---

### 14. Statistical Gains from Looped Estimation under Parameter Budgets

**Authors:** Xinyu Tian, Xiaotong Shen

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25778v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25778v1)

**Summary:** Growing memory demands in artificial intelligence motivate learning with fewer trainable parameters. We ask whether a looped estimator, which repeatedly applies one fitted operator with parameters shared across iterations, can improve statistical accuracy under a common parameter budget. Its conventional untied counterpart uses separate parameters at each iteration. For general likelihood models, we establish an upper bound on squared Hellinger risk for looped sieve maximum likelihood and a mini...

---

### 15. Beyond Class Marginals: Bounding Rehearsal Gaps without Freezing Class Co-occurrence

**Authors:** Congren Dai, Nat Roongjirarat, Fei Ye

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25735v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25735v1)

**Summary:** Class-balanced replay controls class frequency but does not determine the interval between successive replay appearances of a class. We study this interval, the rehearsal gap, separately from the class marginal and class co-occurrence, and introduce randomised-pass replay (RPR), which visits each resident class once per shuffled pass. For a fixed set of C resident classes and replay batch size b less than or equal to C, RPR preserves the balanced time-averaged class marginal and bounds every gap...

---

### 16. Optimal Tradeoffs Between Network Size and Parameter Magnitude in Neural Approximation and Minimax Regression

**Authors:** Baicheng Li, Zuowei Shen, Haizhao Yang, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25710v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25710v1)

**Summary:** The statistical accuracy of neural networks depends on both their approximation power and the complexity of the class fitted from data. While increasing network size is a natural way to improve approximation, parameter magnitude provides another resource whose role must be quantified in both respects. We establish a sharp width--magnitude tradeoff at fixed depth using one elementary bounded $1$-Lipschitz Dyadic--Triangular Activation. For the unit $β$-Hölder ball on $[0,1]^d$ with $0<β\leq1$, th...

---

### 17. On the Gradient Heterogeneity Dynamics of Adversarially Robust Federated Regression

**Authors:** Leonardo F. Toso, James Anderson, Nirupam Gupta, et al.

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25705v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25705v1)

**Summary:** Federated learning (FL) is intrinsically heterogeneous: honest clients may have different data-generating models. On top of that, adversarial clients can make heterogeneity even more pronounced by sharing arbitrary updates. Existing analyses typically control the interaction between statistical heterogeneity and adversarial behavior through gradient-dissimilarity conditions. However, the underlying bound is imposed a priori and may yield conservative guarantees even for least-squares regression....

---

### 18. Efficient Cost-Aware LLM Evaluation via Bayesian Bandit Gittins Indices

**Authors:** Qian Xie, Yueli He, Nairen Cao

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25645v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25645v1)

**Summary:** Exhaustively evaluating every candidate LLM configuration on every benchmark item to identify a high-performing one is costly. We formulate configuration selection as a cost-aware Bayesian bandit problem and propose GittinsEval, which draws on the Bayesian-optimal Gittins policy to determine which configuration to evaluate next and when to stop. We extend the policy with an anytime recommendation rule over both fully and partially evaluated configurations, using an LCB-style score to account for...

---

### 19. Generalized Deep Regression for Repeated Measurements

**Authors:** Kexuan Li

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25605v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25605v1)

**Summary:** In this paper, we study the estimation of a marginal regression function from independent units with repeated binary, count, or continuous responses using ReLU deep neural networks. In the model, we assume that the dependence is generated by an unobserved random mean function within each unit. We then fit a neural network with a convex generalized regression loss. We show an oracle inequality by separating conditional measurement variation from between-unit variation. In addition, we prove that ...

---

### 20. Scalable Minimum-Volume Simplex Estimation with Non-asymptotic Analysis

**Authors:** Jun LI, Yanlong Guo, Zhaozhao Zeng

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25576v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25576v1)

**Summary:** We study the estimation of a $K$-dimensional simplex from $N$ i.i.d.\ points sampled uniformly from its interior; the observations are convex combinations of $K+1$ unknown prototypes. Existing polynomial-time estimators need cubic per-sample work or $O(NK)$ storage and are impractical at $N\sim 10^6$--$10^8$. We propose DeepMVSA, which re-expresses the minimum-volume principle in neural implicit form: a lightweight coordinate network generates the mixing weights and a triangular LU-type paramete...

---

### 21. Direct Optimization of Generators for Search in Automated Theorem Proving

**Authors:** Adam Ousherovitch, Ambuj Tewari

**Published:** 2026-09-22

🔗 [Paper](http://arxiv.org/abs/2609.25575v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25575v1)

**Summary:** Fine-tuned Large Language Models (LLMs) significantly advance Automated Theorem Proving (ATP), but are often deployed as guiding policies within tree search rather than for single-attempt generation. Recent work shows cross entropy is suboptimal for an LLM used in flat search strategies such as aggregation or filtering and that work has developed new loss functions to correct this misalignment. Extending this alignment to tree search is more challenging: proof discovery depends on exploration an...

---

### 22. Continuous Optimization for p-adic Models

**Authors:** Julian Salazar, Dimitri Kanevsky, Matt Harvey, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.25501v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25501v1)

**Summary:** We present the first method for native, continuous gradient descent for machine learning models with $p$-adic parameters. Existing native optimizers are discrete, mostly combinatorial searches, as the $p$-adic numbers $\mathbb{Q}_p$ are totally disconnected, with standard losses that are flat away from their minima. To enable continuous optimization, we propose working with $\mathbb{Q}_p$ via its Berkovich affine line: a canonical, path-connected expansion of $\mathbb{Q}_p$ that preserves its is...

---

### 23. A Practical Recipe for Semi-Supervised Federated ASR: Online Pseudo-Labels with Server Update Stabilization

**Authors:** Wonho Bae, Zakaria Aldeneh, Martin Pelikan, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.25471v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25471v1)

**Summary:** Semi-supervised federated learning (SSFL) trains models on clients' unlabeled data using a teacher to generate pseudo-labels, with a small labeled seed dataset on the server. Automatic Speech Recognition (ASR) is particularly fragile here: pseudo-label errors compound across the output sequence and across training rounds into divergence, leaving a large gap to fully-supervised FL. We show that closing this gap turns on two coupled design axes -- the teacher (which model generates the pseudo-labe...

---

### 24. PICPIs: Prediction-Interval-Conditional Prediction Intervals

**Authors:** Xuelin Yang, Baihe Huang, Yilong Hou, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.25388v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25388v1)

**Summary:** A classical question in statistics is which observable quantities to condition on when drawing inferences about unobservable targets. For conformal prediction in nonparametric uncertainty quantification, standard marginal validity offers limited resolution at the prediction values on which decisions are based, and fully conditional guarantees with respect to the covariates are provably unattainable. We address this gap by introducing a prediction-based conditioning framework that we refer to as ...

---

### 25. Penalized Nonreversible Langevin for Constrained Sampling

**Authors:** Pervez Ali, Weihao Dong, Xiaoyu Wang

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.25381v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25381v1)

**Summary:** We propose penalized nonreversible Langevin algorithms for sampling from $π(x)\propto e^{-f(x)}\mathbf 1_{\mathcal C}(x)$, where $\mathcal C\subset\mathbb R^d$ is a compact convex set. The algorithms combine a squared distance penalty with constant or compatible state dependent skew symmetric perturbations that preserve the penalized Gibbs distribution. For smooth, possibly nonconvex $f$, we derive nonasymptotic total variation bounds for the full gradient algorithm under a log Sobolev inequalit...

---

### 26. JAREX: An Acquisition Function for Multi-Objective Algorithmic Process Characterization

**Authors:** Xinyang Li, Kevin Stone, Ajit Vikram

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24954v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24954v1)

**Summary:** Pharmaceutical process characterization is central to Quality by Design because it defines how variations in process parameters affect the ability to meet product quality specifications, thereby supporting proven acceptable ranges and robust manufacturing. In practice, however, characterization still relies largely on factorial design of experiments (DOE) approaches, which are inefficient for resolving multivariate pass/fail boundaries in higher-dimensional spaces. While Bayesian optimization ha...

---

### 27. Selective Inference for CART with Binary Outcomes

**Authors:** Tomoshige Nakamura

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24949v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24949v1)

**Summary:** Binary classification trees select subgroups using the same outcomes later used to assess their differences. We develop finite-sample conditional tests of a common success probability within a parent selected by deterministic Gini CART. The construction retains all eligible cutpoints and conditions on the selected split, its ancestor path, the parent success total, and outside outcomes. The resulting uniform label fiber gives an exact count distribution, while a reversible parallel Monte Carlo c...

---

### 28. Conformalized Quantile Regression and Minimax Limits of Fixed-Score Calibration under Known Covariate Shift

**Authors:** Rustam Isaev, Anton Conrad, Denis Belomestny, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24929v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24929v1)

**Summary:** In this paper, we study nonasymptotic $L^p$ error bounds for interval length and conditional coverage in split conformalized quantile regression (CQR). Our bounds rely on local regularity conditions and accuracy guarantees for the estimated quantiles. We further instantiate our bounds for quantile regression with sparse ReLU neural networks. We also consider covariate shift, where the calibration and test covariates have different distributions, and derive nonasymptotic bounds for this setting. ...

---

### 29. Identifying Representational Biases in Datasets Using PCA: A Max-Disparity Partition Framework

**Authors:** Arjun KM, Shashi Jain

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24556v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24556v1)

**Summary:** Principal Component Analysis (PCA) minimises aggregate reconstruction error, which can inadvertently represent majority subgroups with substantially higher fidelity than minority subgroups. Fairness-aware extensions of PCA correct this disparity but require group labels as input. We address the logically prior question: given only a data matrix, which binary partition of the data suffers the greatest representational disparity under a shared PCA projection? We formalise this as the max-disparity...

---

### 30. Beyond Point Prediction: Artificial Representative Trees with Uncertainty

**Authors:** Lea L. Mairhöfer, Silke Szymczak, Björn-Hergen Laabs, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24528v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24528v1)

**Summary:** Random forests (RFs) predict well but are opaque, whereas single decision trees are interpretable but unstable. Artificial representative trees (ARTs) were developed as interpretable surrogate models for RFs, but their use as standalone prediction models with uncertainty quantification has not been systematically investigated. We combine ARTs with leaf-wise Mondrian conformal predictive systems (CPS), enabling a single tree to provide continuous predictions, prediction intervals, and probabiliti...

---

### 31. Tensor Completion using Subspace Information

**Authors:** Jingyang Li, Michael K. Ng

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24501v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24501v1)

**Summary:** Tensor completion has attracted significant attention in both applications and theoretical research. Under standard uniform sampling, existing polynomial-time guarantees generally require more observations than the number of degree of freedom, motivating the study of a possible statistical-to-computational gap in highly missing regimes. Fortunately, in many practical scenarios, side information is available, which can provide valuable insights to mitigate these challenges. In this paper, we intr...

---

### 32. Prior-Amortized In-Context Bayesian Inference for Generalized Linear Mixed-Effects Models

**Authors:** Alex Kipnis, Marcel Binz, Eric Schulz

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24422v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24422v1)

**Summary:** Hierarchical data is ubiquitous in the empirical sciences and is most commonly analyzed with generalized linear mixed-effects models (GLMMs). Bayesian inference for GLMMs yields calibrated uncertainty but requires MCMC; the No-U-Turn Sampler (NUTS) is the gold standard but is slow and must restart from scratch for every new dataset, model and prior. We introduce metabeta, a pretrained neural network for prior-amortized in-context Bayesian inference over GLMMs. Unlike previous neural posterior es...

---

### 33. A Three-Way Testing Framework for Quantifying Epistemic Calibration Uncertainty in SBI

**Authors:** Luben M. C. Cabezas, Pedro L. C. Rodrigues, Rafael Izbicki

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24419v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24419v1)

**Summary:** Current experimental scientists increasingly rely on simulation-based inference (SBI) to invert complex models with intractable likelihoods. A primary goal in these settings is to obtain credible regions with valid coverage. While recent model-agnostic conformal calibration methods have succeeded in constructing credible sets with prescribed local Bayesian coverage, their approximate nature introduces inherent epistemic uncertainty in the calibration process. In this work, we propose a novel too...

---

### 34. Empirical Auditing of Edge-Private Graph Generators

**Authors:** Anum Fatima, Stratis Limnios, James Adams, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.25155v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25155v1)

**Summary:** We empirically audit privacy leakage by testing whether outputs from edge-neighbouring inputs remain distinguishable, using statistically valid lower bounds on the privacy loss witnessed by our attacks. Our framework compares direct-edge, local-structural, and GNN-based attacks through the geometry surrounding a target edge. Experiments across two generators and two networks show that privacy leakage is both mechanism- and network-dependent, with learned representations revealing information not...

---

### 35. A Distributional Optimisation Perspective on Combining Models in Deep Learning

**Authors:** Congye Wang, Yan Lin, Zheyang Shen, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24328v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24328v1)

**Summary:** Combining predictions from different models can improve performance at machine learning tasks, but the training of the individual models and the rule used to combine them are typically chosen separately, and by ad hoc means. Recent advances in distributional optimisation (i.e. where the optimisation occurs over the set of probability distributions) offer an opportunity for principled joint training, viewing the collection of models as a discrete distribution whose support points are to be optimi...

---

### 36. Adversarially Robust PAC Learning with Optimal VC Rates

**Authors:** Steve Hanneke, Amirreza Shaeiri

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24260v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24260v1)

**Summary:** We study the problem of \emph{adversarially robust} PAC learning. In this framework, the learner observes independent samples from an unknown distribution over $\mathcal{X} \times \{0,1\}$, as in classical PAC learning. However, given a perturbation map $\mathcal{U} : \mathcal{X} \to 2^{\mathcal{X}}$ known to the learner, the goal is to output, with high probability, a predictor that correctly classifies \emph{every} perturbation $z \in \mathcal{U}(x)$ of most future examples $(x,y)$ drawn from ...

---

### 37. Variational objectives for amortized Bayesian inference in inverse problems: The role of posterior conditioning

**Authors:** Abhishek Srivastava, Arijit Hazra, Rajesh Dubbaku

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.25145v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25145v1)

**Summary:** Variational autoencoders (VAEs) offer an efficient approach to amortized Bayesian inference for inverse problems, but posterior accuracy can depend strongly on the choice of variational regularization, particularly when the inverse problem contains weakly identified parameter directions. This study investigates three objectives: a reverse Kullback--Leibler formulation (VAE-KL), an asymmetric Jensen--Shannon formulation (VAE-JS), and a Jensen--Shannon--Wasserstein formulation (VAE-JSWA), which re...

---

### 38. The Informational Content in Lepto-Variance and Its Relation to Higher Moments

**Authors:** Vassilis Polimenis

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.25144v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25144v1)

**Summary:** Lepto-regression is defined as the machine learning process of constructing a Regression Tree of a target feature on itself. It is a novel, model-free method potentially revealing information on important sample structure properties. But it is yet not clear what the informational content of lepto-variance is and how it is related to other well-known statistics of a sample. One significant finding is that 58% of the historical US stock return variability is 1-bit lepto-variance that can not be ex...

---

### 39. OSCAR: Order-aware Scoring and Calibration for AI Rankings

**Authors:** You Liu, Yue Liu, Quanchao Lu, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24128v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24128v1)

**Summary:** Judge-specific sensitivity is useful for aggregating pairwise LLM evaluations, but its interpretation depends on which systematic presentation effects the ranking model includes. We introduce OSCAR, an order-aware framework for scoring and calibrating AI rankings, and study position as one such effect. In released judgments from 18 evaluators, the all-response A-minus-B score difference ranges from $-63.11$ to $98.31$ percentage points. Matching question text, response texts, candidate identitie...

---

### 40. Model-Agnostic Feature Selection via LOCO-Guided Adaptive Minipatch Sampling

**Authors:** Xuhui Liu, Lili Zheng

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24126v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24126v1)

**Summary:** Black-box machine learning models increasingly deliver strong predictions, but extracting useful information from them, such as a set of important features, remains challenging. Existing model-agnostic methods primarily estimate feature importance or conduct inference on it rather than directly selecting features, whereas many feature selection methods are model-specific or rely on the model-X assumption. We introduce LOCO-guided Adaptive Minipatch Sampling (LAMPS), a model-agnostic ensemble fra...

---

### 41. Causal Bayesian Optimization: Foundations, Methods, and Applications

**Authors:** Chenfeng Huang, Thuy T. Le, Zixuan Ma, et al.

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24112v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24112v1)

**Summary:** Causal Bayesian Optimization (CBO) combines causal inference with Bayesian optimization to enable sample-efficient intervention selection in systems with causal structure. This survey provides a systematic review of CBO through a unified BO-loop perspective, showing how causal assumptions shape intervention search spaces, surrogate models, acquisition functions, and decision policies. We organize existing methods by graph and system-knowledge assumptions, environment, intervention representation...

---

### 42. Doubly robust target inference for generalized linear regression with completely missing covariates

**Authors:** Huali Zhao, Ke Deng

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.24086v1) | 📄 [PDF](https://arxiv.org/pdf/2609.24086v1)

**Summary:** Large-scale multipurpose cohort studies and biobanks often omit covariates needed for specific downstream analyses. We study target-population inference for generalized linear regression when key covariates are completely absent from the target data but observed in a related source population. Standard missing covariate methods are not directly applicable because they require at least partial observation of the covariates in the target population. We develop a doubly robust transfer learning fra...

---

### 43. Exponential Family Synthetic Controls

**Authors:** Hector Rodriguez-Deniz, David M. Blei

**Published:** 2026-09-21

🔗 [Paper](http://arxiv.org/abs/2609.23970v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23970v1)

**Summary:** We develop exponential family synthetic controls (EFSC), a distributional version of synthetic controls for a panel of datasets. Each cell of the panel corresponds to a dataset drawn from an exponential family whose natural parameters factorize probabilistically across units and times. We estimate the latent factors using black-box variational inference. This replaces the usual weighted-average view of synthetic controls with a flexible probabilistic model that operates on full distributions. We...

---

### 44. Sparse Regression Distilled from a Single Robust Fit

**Authors:** Wooyoung Shin, Seunghwan Park

**Published:** 2026-09-20

🔗 [Paper](http://arxiv.org/abs/2609.23937v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23937v1)

**Summary:** Robust linear fits can resist response contamination yet remain too dense or unstable for useful global explanations. We propose penalized distillation, which fits a smoothly clipped absolute deviation (SCAD) estimator to a robust initial estimator's empirical fitted surface along a safeguarded coordinate-descent path and evaluates candidate states separately for fidelity, parsimony, perturbation stability, and held-out prediction. The new results attach to the states the algorithm actually comp...

---

### 45. Density-Ratio Rescoring for Imbalanced Classification Using Raking Duals and Classifier Scores

**Authors:** Dongha Kim, Seunghwan Park

**Published:** 2026-09-20

🔗 [Paper](http://arxiv.org/abs/2609.23926v2) | 📄 [PDF](https://arxiv.org/pdf/2609.23926v2)

**Summary:** Density-Ratio Rescoring (DRR) augments a classifier trained at the original class prior with a survey-raking dual score. Raking reweights the majority sample to match minority feature moments within a tolerance. DRR marginally standardizes the dual and base scores and combines them with a fixed weight of one half, using the fitted dual directly for prediction without resampling or refitting the base classifier. Under exact population matching and a correctly specified log-linear tilt model, the ...

---

### 46. The Probabilistic Structure of Large Language Models

**Authors:** Adnan Aboulalaâ

**Published:** 2026-09-20

🔗 [Paper](http://arxiv.org/abs/2609.25134v1) | 📄 [PDF](https://arxiv.org/pdf/2609.25134v1)

**Summary:** This paper presents a probabilistic perspective on large language models (LLMs), developed with the aim of bringing together, in a single self-contained account, tools that are usually treated separately across the literature. LLMs are described through probability measures on the set of sequences of tokens, specified via their autoregressive conditional distributions. Training is formulated as a maximum-likelihood estimation problem, addressed by stochastic gradient methods, while text generati...

---

### 47. On Generalized Naive Bayes with Continuous Features

**Authors:** Ábrahám Papp, Botond Szilágyi, Edith Alice Kovács

**Published:** 2026-09-20

🔗 [Paper](http://arxiv.org/abs/2609.23819v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23819v1)

**Summary:** The Generalized Naive Bayes (GNB) model was introduced for discrete and categorical random variables as an extension of classic Naive Bayes. We now accommodate the GNB framework to continuous explanatory variables. A central result of the paper is that structure learning of the GNB depends only on the pair copulas of the bi-variate marginals. We proved that the GNB structure can be assigned to the basis of a matroid, therefore we give greedy algorithms for finding the optimal GNB structure on th...

---

### 48. Iterative Atom Refinement: A Monotonicity Principle for Dictionary Learning

**Authors:** Alexander Christie, Miguel Moscoso, Alexei Novikov, et al.

**Published:** 2026-09-20

🔗 [Paper](http://arxiv.org/abs/2609.23812v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23812v1)

**Summary:** Dictionary learning seeks to recover an unknown dictionary $A$ from observations ${\bf y}_i = A{\bf x}_i$ with sparse coefficient vectors ${\bf x}_i$. We introduce the \emph{Iterative Atom Refinement} (IAR) algorithm, a simple procedure for recovering individual dictionary atoms. Starting from a random direction, IAR repeatedly selects the observations most strongly correlated with the current iterate and updates the direction by averaging the selected data. Our main contribution is a rigorous c...

---

### 49. Belted Engression: Sufficient Dimension Reduction for Generative Distributional Regression

**Authors:** Wenxi Tan, Bing Li, Lingzhou Xue

**Published:** 2026-09-20

🔗 [Paper](http://arxiv.org/abs/2609.23789v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23789v1)

**Summary:** Modern conditional generative models face significant challenges when learning complex covariate dependencies. While sufficient dimension reduction (SDR) provides a principled approach to compress these dependencies, traditional SDR frameworks were not formulated for conditional generation. To bridge this gap, we propose Belted Engression, a unified and architecturally parameter-efficient framework for generative distributional regression. Our approach establishes an end-to-end compress-then-gen...

---

### 50. TEMPER: Temporal Encoder-Masked Probabilistic Ensemble Regressor for Time-Series Forecasting

**Authors:** Giancarlo Vercellino

**Published:** 2026-09-20

🔗 [Paper](http://arxiv.org/abs/2609.23701v1) | 📄 [PDF](https://arxiv.org/pdf/2609.23701v1)

**Summary:** Probabilistic forecasting requires accurate central predictions and calibrated uncertainty estimates. This paper presents TEMPER, the Temporal Encoder-Masked Probabilistic Ensemble Regressor, a univariate time-series forecasting algorithm that combines a temporal autoencoder, a differentiable masked neural decision forest, continuous ranked probability score (CRPS) training, and Gaussian-mixture post-processing. The R implementation is built on torch for R and returns horizon-wise density, distr...

---

