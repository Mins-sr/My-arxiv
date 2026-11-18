# arXiv Daily Digest - 2026-11-18

Total papers: 350

---

## cs.AI

**50 papers**

### 1. Ambient LLMs: Data-Efficient Supervised Fine-tuning via Temperature Matching

**Authors:** Giannis Daras, Marios Papachristou, Adam Klivans, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23229v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23229v1)

**Summary:** Collecting large-scale, diverse, and high-quality post-training datasets for autoregressive language models is challenging. Consequently, Supervised Fine-Tuning (SFT) is typically applied to datasets significantly smaller than those used for pre-training, which leads to overfitting and the catastrophic forgetting of the tails of the data distribution. To prevent this collapse, we introduce Ambient SFT, a principled framework for leveraging imperfect predictions to augment the fine-tuning set. In...

---

### 2. StringQFT: A Multiuse Textbook Resource for AI-Assisted Theoretical Physics

**Authors:** Xingyang Yu

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23225v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23225v1)

**Summary:** We present StringQFT as a textbook collection for string constructions of quantum field theory and as infrastructure for AI-assisted theoretical physics. The collection comprises 18 volumes, 190 chapters and 3,795 pages, covering brane probes, brane webs, geometric engineering, F-theory constructions, wrapped M5-branes and exact worldsheet constructions. Its open-book benchmark inventory contains 1,073 items, including 499 with automatic finite-answer checking. For retrieval-augmented generation...

---

### 3. Do LLM Agents Still Need to Be Told How to Self-Improve?

**Authors:** Shobhita Sundaram, Cansu Sancaktar, Phillip Isola

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23219v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23219v1)

**Summary:** LLM agents increasingly drive their own learning. Self-improvement methods delegate various components of model optimization to the models themselves. As models become more capable, this motivates a basic question: do these increasingly capable models still need us to specify how they should self-improve? In this paper we study an autonomous paradigm in which, given basic primitives, resources, and a general goal for self-improvement, agents construct their own self-learning algorithm for contex...

---

### 4. Higher-Scoring Coding Models Did Not Get More Work Done

**Authors:** Yining Hua

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23216v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23216v1)

**Summary:** New coding models advertise themselves on score improvements of coding benchmarks. Yet no study has tested if a model that scores higher on these benchmarks gets more real work done. On June 12, 2026, a U.S. export control directive banned access to Claude Fable 5 for 19 days, which forced users to switch to other models. During this time, most former Fable 5 users switched to Opus 4.8 (11 points lower on SWE-Bench Pro compared to Fable 5). We treat this suspension as a natural experiment, where...

---

### 5. Reading Scene States: Uncovering Safety Failures in Vision-Language Models

**Authors:** Tongxi Wu, Yuyang Cheng, Jiacheng Xian, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23206v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23206v1)

**Summary:** Vision-language models (VLMs) can provide harmful assistance by interpreting visual events, even without an explicit request for the underlying harmful objective. We identify this \textbf{scene-state safety vulnerability} and introduce \textbf{SceneSafetyBench}, comprising 375 image--question pairs spanning Initial, Medium, and Ultimate scene states and five visual presentations. Across eight VLMs, scene-state inputs elicit harmful assistance with attack success rates (ASRs) of 45.6--72.3\%. Com...

---

### 6. Fine-Tuning Gemma 4 Edge Models for MATLAB Signal-Processing Code with SFT and QLoRA on a Laptop iGPU

**Authors:** Mehmet Altan Toksöz

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23205v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23205v1)

**Summary:** Small language models that run on a laptop are attractive for writing signal-processing code offline, but they make systematic errors on digital signal processing (DSP) conventions. We apply supervised fine-tuning (SFT) to the Gemma 4 edge models E2B and E4B with 66 checked examples covering 11 signal-processing MATLAB subtasks, using low-rank adaptation (LoRA) and quantized LoRA (QLoRA) on the integrated GPU (iGPU) of a laptop, and deploy the 8-bit integer (int8) models with the adapters throug...

---

### 7. Agent Trust Infrastructure (ATI): A Federated Identity, Trust, Attestation, and Accountability Architecture for Cross-Organization Autonomous AI Agents

**Authors:** Viet K. Nguyen, Mohammad I. Husain

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23202v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23202v1)

**Summary:** AI agents increasingly collaborate across organizational boundaries, invoking tools and interacting with agents operated by independent entities. Although existing agent frameworks support planning and coordination, they lack a common mechanism for verifying cross-organizational agent identity, execution integrity, and authorization. We propose the Agent Trust Infrastructure (ATI), a framework-independent security architecture built on Public Key Infrastructure (PKI), Zero Trust Architecture (ZT...

---

### 8. Structure--Residual Inductive Biases for Language Model Pretraining

**Authors:** Hai Huang, Bartosz Żuk, Rassul Magauin, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23197v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23197v1)

**Summary:** Next-token prediction is relied upon to learn both predictive behavior and internal representations. We ask whether representation structure itself should be an explicit inductive bias. Motivated by the two-part coding view of Kolmogorov complexity, we study a structure--residual principle in which a representation separates structure from realization detail. We instantiate this principle in two complementary ways. Boundary Bottleneck Concept (BBC) routes information from token segments through ...

---

### 9. WoRD: Diffusion-Based Posterior Inference for Online Goal Recognition

**Authors:** Almog Anschel, Sarah Keren

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23192v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23192v1)

**Summary:** Goal recognition is the task of inferring an agent's intended goal from its observed behavior. Most existing work focuses on high-level symbolic recognition, abstracting away the continuous motion through which agents reach their goal. Methods that do reason over continuous trajectories rely on an explicit dynamics model that is hard to acquire and rarely transfers across settings. Neither approach explicitly learns how agents move toward each candidate goal, limiting accuracy on ambiguous traje...

---

### 10. Retrieval-Augmented Correction for Generalist Medical Image Segmentation

**Authors:** Vincenzo Marcianò, Xiaoming Zhang, Michela Antonelli, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23189v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23189v1)

**Summary:** Automated segmentation is routinely used as the first step in quantitative image-based clinical workflows, where predicted masks are subsequently reviewed and corrected by human operators. Automated correction of the residual structural errors is currently addressed one anatomy at a time, so the number of trained correctors scales with the number of segmentation targets. We present GRACE, a retrieval-augmented refiner that edits an input mask under context drawn from a shared knowledge base of v...

---

### 11. Say Less, Hallucinate Less? Diagnosing and Restoring Object Coverage in Preference-Optimized Vision-Language Models

**Authors:** Hansang Lee

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23179v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23179v1)

**Summary:** Preference optimization (PO) is the standard way to reduce object hallucination in large vision-language models. We find that four public PO checkpoints of LLaVA-1.5-7B also lower object coverage. They name fewer object categories, and their lower hallucination rates bring no significant gain in set-level object F1 on CHAIR. We therefore ask how much of the PO gain the base model can reproduce by stopping earlier. A positive end-of-sequence (EOS) logit bias lets the base model reach the recall o...

---

### 12. Inference after coding agents

**Authors:** Florian Gunsilius, David Van Dijcke, Kaspar Wüthrich

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23174v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23174v1)

**Summary:** Empirical research is changing rapidly as AI coding agents are becoming increasingly proficient in every step of it, from writing code to manipulating data. We argue that while the potential of coding agents for science is vast, their use in hypothesis testing poses a substantial threat to classical inference, as these agents enable a supercharged form of selective inference. In particular, we argue that coding agents carrying out empirical research introduce a new type of post-selection inferen...

---

### 13. Attribution Through the Decoder: Prediction-Space Explanations for Structured Outputs

**Authors:** Zaer Bin Zaqy, Brinnae Bent

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23161v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23161v1)

**Summary:** Networks that predict angles, gaze directions, and rotations do not output these quantities directly: they emit raw coordinates that a fixed decoder, such as normalization, maps to the final prediction. Attribution methods are usually applied to the raw coordinates, so they can credit inputs for changes the decoder discards, such as rescaling a vector when only its direction matters. The resulting explanation can highlight inputs that have no effect on the prediction. We instead attribute throug...

---

### 14. Learning Stratified Policies for Inference-Time Objectives

**Authors:** Mridul Mahajan, Xuezhou Zhang, Aldo Pacchiano

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23154v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23154v1)

**Summary:** Inference-time scaling improves the performance of large language models by sampling multiple responses and evaluating their collective utility. However, many existing approaches obtain these samples by repeatedly sampling from a single policy. In this work, we study if the sample budget at inference time can instead be allocated across a population of policies. We introduce stratified policies, where each of $k$ learned policies contributes one response to a $k$-sample inference-time objective....

---

### 15. Mind the Gap: A Deployed Multi-Agent System for Documentation Maintenance

**Authors:** Lorenzo Masoero

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23142v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23142v1)

**Summary:** The "AI revolution" has enabled teams across the technology industry to deliver software features at unprecedented velocity. While code evolves faster than ever, customer-facing documentation often struggles to stay up to speed. As users increasingly rely on LLM-based agents that consume documentation as their primary interface, the impact of this documentation gap worsens: stale information propagates and is treated as authoritative. Signals for identifying where documentation has fallen behind...

---

### 16. RSI-Prime: Training Models to Train Models

**Authors:** Dewu Zheng, Yang Ye, Hongyu Zhang, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23138v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23138v1)

**Summary:** Enabling large language models (LLMs) to autonomously conduct training and improve target models is an important foundation for recursive self-improvement (RSI). As LLMs expand their role from being trained to conducting training, their model-training capability warrants dedicated study and systematic development. To this end, we construct RSI-Prime, a dataset for improving model-training capability, comprising 350 complete experimental trajectories across seven task categories. To help LLMs lea...

---

### 17. Natural Language Programming: Rethinking Language, Memory, and Cognition in the Era of Generative AI

**Authors:** Giovanni Adorni, Daniele Grosso

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23106v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23106v1)

**Summary:** Generative Artificial Intelligence is transforming the role of natural language in computational systems. In classical Natural Language Processing (NLP), language was treated as an object of computation: something to analyse, classify, translate, or generate. Large Language Models (LLMs) challenge this perspective, enabling natural language to function increasingly as an executable cognitive medium through which humans structure reasoning, orchestrate problem solving, and regulate hybrid human/A...

---

### 18. Hidden-State Similarity Predicts Re-Elicitation After Inoculation Prompting

**Authors:** Rose N. Kwon, Samy Mammeri, Sabyasachi Sahoo, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23096v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23096v1)

**Summary:** Fine-tuning on narrow harmful tasks can cause emergent misalignment, where models generalize harmful behavior beyond the training distribution. Inoculation prompting can reduce this effect by explicitly eliciting the undesired behavior during training, but recent work shows that the behavior can reappear when evaluation prompts contain cues from the training context. We study what makes such prompts effective triggers. We find that, surprisingly, textual similarity to the inoculation prompt is a...

---

### 19. What's in a Tree ? Hierarchical $n$-gram models as controlled approximators of language

**Authors:** Aritra Das, Francesco Cagnetta, Darshil Doshi, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23093v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23093v1)

**Summary:** Hierarchical models have been proposed as synthetic settings for studying language. However, their relevance to realistic language corpora remains underexplored. In this work, we introduce tree-grams, autoregressive generative $n$-gram models that build the conditional probability tensor $p(x_n \mid x_{1:n-1})$ through a hierarchical composition of order-2 and order-3 tensors. $n$ controls the maximal context window, whereas a rank hyperparameter $d$ controls model capacity, yielding an interpre...

---

### 20. BugGen 2.0: Rethinking the Roles of LLMs for Scalable RTL Bug Synthesis

**Authors:** Minh Luu, Michael Quinn, Aakash Tyagi, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23091v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23091v1)

**Summary:** AI-assisted RTL localization and debugging need ground-truth bug datasets with known locations and observable failures, while testbench grading uses injected bugs to measure detection capability. Creating such datasets at scale remains a major EDA challenge. BugGen 1.0 shows that Large Language Models (LLMs) can generate context-aware RTL mutations. Still, it relies on the model for both choosing where to mutate and generating the edit, which increases inference costs and can lead to invalid cho...

---

### 21. Learning to Undo: Transfer Reinforcement Learning under State Space Transformations

**Authors:** Mridul Mahajan, Aldo Pacchiano, Xuezhou Zhang

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23081v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23081v1)

**Summary:** Transfer learning in reinforcement learning (RL) has shown strong empirical success. In this work, we take a more principled perspective by studying when and how transferring knowledge between MDPs (a source and a target) can be provably beneficial. Specifically, we consider the case where there exists an undo map such that applying this map to the target's state space recovers the source exactly. We propose an algorithm that learns this map by matching state feature statistics gathered from bot...

---

### 22. Colombo: A Frontier-to-Frontier Autoresearch System for Oracle-Based Optimization

**Authors:** Haihan Zhang, Wendao Wu, Chenheng Zhang, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23080v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23080v1)

**Summary:** Science advances from frontier to frontier as discoveries reshape what is known and create the basis for further discovery. We present Colombo, a self-organizing AI researcher that drives this renewal, first instantiated in oracle-based optimization. Here, the central question is how efficiently a problem class can be solved through a prescribed information interface and what costs no admissible algorithm can avoid. The gap between achievable guarantees and unavoidable limits defines the frontie...

---

### 23. Runtime Verification of Multiple Natural Language Criteria for Agent Governance

**Authors:** Silviu Pitis, Parand A. Alamdari, Jessica Tang, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23074v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23074v1)

**Summary:** AI agents are governed by hundreds of natural language criteria, yet existing verifiers cannot efficiently evaluate an agent's output against a large set of such criteria and report which are satisfied, violated, or inapplicable. We introduce the VFM, a tree-attention verifier that encodes the shared context and target text, and scores N natural language criteria in parallel, returning independent per-criterion ternary verdicts. The VFM is pretrained on CriteriaBank, a corpus of 394K (context, t...

---

### 24. The Resolution Hypothesis: Agent Evolution's Key Is Identifying Improvements

**Authors:** Yuanhao Zeng, Shaocheng Lan, Ao Lu, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23068v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23068v1)

**Summary:** Agent evolution follows a simple loop: a proposer writes candidate artifacts (prompts, skills, memories) and selection accepts those that score higher. This loop has shown promise, yet practitioners face a puzzle: methods trade wins across papers, and evolution often fails to bootstrap on certain tasks. We trace this puzzle to the Resolution Hypothesis: agent evolution stalls not because methods fail to propose better artifacts, but because noisy evaluations cannot reliably identify them. Across...

---

### 25. Values Shape What Self-Improving Coding Agents Build

**Authors:** Jason Liang, Dylan Waldner, Risto Miikkulainen

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23067v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23067v1)

**Summary:** Self-improving agents are typically optimized for the results they produce, with less attention to how they produce them. Their instructions give designers limited ways to shape how they work, especially when the task is open-ended. This paper studies whether a short value statement in an agent's persistent instruction file changes not only how well the agent performs but also what it builds. Four higher-order value types in Schwartz's theory of basic human values were evaluated: openness to cha...

---

### 26. Deep Reinforcement Learning for Heat Pump and Underfloor Heating Control: An End-to-End Case Study

**Authors:** Antonio Manjavacas, David Suárez-Caro, Alejandro Campoy-Nieves, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23063v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23063v1)

**Summary:** Efficient control of underfloor heating (UFH) systems coupled with heat pumps (HPs) is challenging due to the high thermal inertia of buildings and the slow dynamic response of UFH systems. Deep Reinforcement Learning (DRL) offers a data-driven control approach capable of simultaneously optimizing energy consumption and thermal comfort. However, the application of DRL-based controllers in occupied buildings under real operating conditions remains limited. This work presents and end-to-end case s...

---

### 27. FrameRouter: Frame Budget Routing for Long-Video Understanding on Video-MME-v2 and Beyond

**Authors:** Bingjun Luo, Jialin Guo, Siqi Li

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23055v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23055v1)

**Summary:** Long-video question answering benchmarks like Video-MME-v2 typically evaluate systems under a uniform frame budget for every question, despite stark variation in the evidence each query actually demands. We analyze this mismatch on Video-MME-v2 and find that different question subsets prefer different frozen frame-budget policies, while uniformly increasing the frame count does not reliably improve all metrics. These findings motivate fixed-mean frame-budget routing, a controlled inference setti...

---

### 28. ReTouchGS: Ultralight Render-free Aesthetic Color Enhancement and Transfer for 3D Gaussian Splatting

**Authors:** Chuanzhi Xu, Boyu Wei, Chengkun Yue, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23054v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23054v1)

**Summary:** 3D Gaussian Splatting (3DGS) enables photorealistic scene reconstruction. Existing 3DGS color transfer and interactive editing methods are guided by reference images and user-specified color adjustments. However, in many applications, users simply want aesthetically guided color enhancement that automatically makes the scene more visually appealing while maintaining consistent colors and tones across viewpoints. We present ReTouchGS, to our knowledge the first framework for reference-free aesthe...

---

### 29. ForecastGym: A Live, Controlled, and Replayable Benchmark for Forecasting Agents

**Authors:** Yicheng Tao, Yuante Li, Zipei Fan

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23045v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23045v1)

**Summary:** Agents built on large language models (LLMs) increasingly forecast real-world events by searching the Web and reasoning over what they find. How well such an agent forecasts depends on both the retrieved evidence and the model, making control over that evidence essential for evaluation. Live evaluations can mix retrieval with reasoning when each system searches on its own, while retrospective search can leak later information through date filters or today's ranking of historical pages. Comparing...

---

### 30. Check Your Blind Spots: Decision-Guided Perception by Probing the Planner with Hypothetical Objects

**Authors:** Hoang Pham Cong, Long D. Nguyen, Ho Viet Duc Luong, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23030v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23030v1)

**Summary:** Not every perception error changes the planner's action. Yet adaptive-resolution perception chooses where to spend high-resolution computation from image cues, which can neither reliably point to an object that low resolution missed nor tell which objects matter to the planner. We observe that the planner can say where an object would matter before anything is seen: inserting a hypothetical object at a location tests whether its action would change. Decision-Guided Speculative Perception (DGSP) ...

---

### 31. PeriaTrace: Tooth-Level Grounding Diagnosis and Patient-Facing Explanations from Periapical Radiographs

**Authors:** Zhenhuan Zhou, Yuchen Zhang, Jingbo Zhu, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23012v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23012v1)

**Summary:** Periapical radiographs (PRs) are central to endodontic diagnosis, but interpreting them and preparing reports are time-consuming. Technical language can limit patients' understanding, while existing automated methods often lack tooth-level links between findings and image evidence. We present PeriaTrace, a three-stage framework integrating tooth-level diagnosis, visually grounded report generation, and patient-friendly explanations and care recommendations. PeriaTrace was developed and evaluated...

---

### 32. PhysScope: Agentic Multimodal Physics Reasoning with Grounded Visual Memory

**Authors:** Haoyang Liu, Kecheng Liang, Xinyu Li, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23010v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23010v1)

**Summary:** Vision-language models (VLMs) can correctly interpret physics diagrams yet apply constraints outside the states or conditions in which they hold, causing premise errors to propagate through subsequent calculations. We introduce PhysScope, an inference-time visual harness that supports self-correction of these scope mismatches without updating model weights. PhysScope enables the model to link physical scopes directly to its visual observations and explicitly constructs derived views to support r...

---

### 33. Residual-Guided Lightweight Reinforcement Learning for Risk-Aware Trajectory Selection with a Frozen World Model

**Authors:** Jiaqi Wu, Yongqi Dong, Yijie Zhong, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22998v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22998v1)

**Summary:** In automated driving, world models provide future scene predictions for evaluating candidate trajectories, but fixed selection rules may not capture scene-dependent trade-offs. We propose a residual-guided reinforcement learning (RL) framework for lightweight trajectory selection with a frozen world model and a fixed candidate bank. The framework uses proximal policy optimization (PPO) to fine-tune a joint policy over candidate selection and bounded trajectory residuals. A context-conditioned ra...

---

### 34. RagHarnessDebugger: Jev-Guided Agentic RAG in Contract Inference Repair Auditing

**Authors:** Moriya Dechtiar, Daniel Martin Katz, Michael J. Bommarito, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22991v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22991v1)

**Summary:** Agentic systems using retrieval-augmented generation (RAG) must repair their own answers by gathering more evidence, testing alternative policies and deciding if, when, and what repairs are needed. Yet how do we know if a system's repairs are working when metrics like accuracy can be misleading? We present RagHarnessDebugger, a framework that records every repair decision in a Jev-guided harness for contract inference and audits the record to facilitate complete debugging of all decisions taken ...

---

### 35. How Web Research Agents Interpret User Priorities

**Authors:** Robin Sharma, Parisa Suchdev

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22989v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22989v1)

**Summary:** Web research agents gather information online and write cited reports, including financial analysis. Users can state a priority to guide this research, but a priority may not say how to judge the options, leaving the agent to choose the criteria. We examine how two such agents, built on OpenAI and Anthropic models, interpret a stated priority. In 36 runs, the agents compared Microsoft and Alphabet as businesses. Prompts asked for special attention to growth or resilience, or gave no priority. We...

---

### 36. Structured AI ideation yields physical strategies for epithelial barrier repair

**Authors:** Geonho Nah, Johyun Park, Kyung-Ah Cho, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22988v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22988v1)

**Summary:** AI systems increasingly support literature analysis, candidate evaluation and hypothesis refinement, but enabling researchers to explore research directions beyond established disciplinary approaches remains challenging. We developed Abelio, an AI system designed to generate novel research directions by expanding investigators' avenues of inquiry. Abelio reformulates research objectives, uses these alternative formulations to identify relevant elements outside conventional disciplinary boundarie...

---

### 37. Large Language Models Have Not Yet Transformed Science

**Authors:** Ron Bekkerman, Nichole Li, Bahareh Kargar, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22975v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22975v1)

**Summary:** The emergence of large language models (LLMs) in late 2022 has raised questions about the future of science, but assessing their impact requires understanding how scientific practices were already evolving. We analyze 2.5 million full-text papers across five disciplines from 2015 to 2025, tracing trends over a broad spectrum of lexical, structural, epistemological, and social dimensions. Aside from frequency shifts in some words, most pre-2023 trends continued with limited detectable breaks. Amo...

---

### 38. VITAL: A Framework for Validating Agentic AI in Pharmaceutical Drug Development and Clinical Trial Operations

**Authors:** Sandeep Burugupalli, Pedro Matos-Filipe, Andrea Hita Ardiaca, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22973v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22973v1)

**Summary:** Current assurance approaches do not establish whether evidence is sufficient to validate, monitor and govern agentic artificial intelligence (AI) within a pharmaceutical context of use. Plausible outputs may conceal failures in retrieval, reasoning, orchestration or human-control points, where reference standards are unavailable. We developed and operationalised VITAL (Validation by Intended use, Traceability, Autonomy and Lifecycle evidence), a validation framework for agents in clinical develo...

---

### 39. SEAM: Computer-Use Agents Know the Harm Between Screens, and Commit It Anyway

**Authors:** Yuxuan Zhou, Chen Xiong, Haitong Liu, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22971v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22971v1)

**Summary:** Safety benchmarks for computer-use agents (CUAs) place the harm either in the intent of the task or on a single screen: a malicious instruction, an injected command, a phishing page. An agent that checks the task and each screen in isolation can pass them, so they do not test whether it combines facts seen on different screens. Yet in delegated work, harm often arises exactly this way: a fact about a person on one screen, a fact about an item on another, and a legitimate task that binds them. We...

---

### 40. CodeReel: Accelerating Code-to-Video Agents with Exact Frame Reuse and Blocking-Aware Scheduling

**Authors:** Junyi Shen, Yao Lu

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22967v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22967v1)

**Summary:** Coding agents make videos by writing and refining programs in a build--inspect--edit loop. A finished film costs a median of $2.85 in model calls and 11 minutes, over a third of that time in builds that block the agent. We find that much of this time is avoidable, for two reasons. First, 37.5% of the frames of a session's later films were drawn before, many shifted in time or inside an edited scene. Second, half of the builds stop at a check, where the agent needs only the verdict, but which bui...

---

### 41. High-Dimensional Black-Box Optimization via Guidance Sampling of Diffusion Models

**Authors:** Xiaoyan Hu, Rohit Sonker, Jalal Butt, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22965v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22965v1)

**Summary:** Many real-world optimization problems involve optimizing black-box objectives for which only a limited number of evaluations are available. Bayesian optimization (BO) is a powerful framework for such problems, but its effectiveness often deteriorates in high-dimensional spaces. Recent work leverages diffusion models for black-box optimization, often through pre-training a reward-conditioned score network to steer generation towards high-reward samples. Alternatively, gradient-based guidance meth...

---

### 42. Hierarchical Diffusion Transformer for End-to-End Image Generation

**Authors:** Xiaoyu Wu, Yifei Wang, Weihang Guo, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22962v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22962v1)

**Summary:** Pixel-space diffusion learns visual representations and image generation jointly in a single end-to-end training stage, without a separately pretrained visual encoder. However, plain pixel-space Transformers still trail leading two-stage latent diffusion models in generation quality and training efficiency. We hypothesize that part of this gap arises from retaining one token per patch throughout the backbone, which does not explicitly encourage a visual hierarchy that summarizes related content ...

---

### 43. Projected Penalty-Gradient Tracking for Communication-Efficient Byzantine-Resilient Federated Learning

**Authors:** Yanjie Dong

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22929v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22929v1)

**Summary:** We investigate communication-efficient federated learning over heterogeneous datasets in the presence of Byzantine adversaries capable of uploading arbitrary information. Penalty-based methods bound the influence of each worker through the bounded gradient of a penalty function; however, the bound is lost once the uploads are compressed, since a Byzantine worker can accumulate an unbounded state at the server. To retain the Byzantine resilience under compressed uploads, we propose a projected pe...

---

### 44. When Do Typed Decision Models Work in Transportation? Evidence from Travel Choice and Traffic Signal Control

**Authors:** Hongyang Zhang, Boyuan Deng, Siyuan Feng, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22926v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22926v1)

**Summary:** Typed decision models combine natural-language understanding with a structured interface that returns a selected action and an option-level probability distribution without generating lengthy textual responses. Their low inference cost and response latency make them attractive for transportation problems with predefined alternatives. This paper investigates their effectiveness, robustness, and efficiency in two representative transportation tasks: individual travel-mode choice prediction and seq...

---

### 45. Done, But Still Working: Anytime Evaluation of When Coding Agents Should Stop

**Authors:** Zerui Yang, Quan Xue, Miaomiao Dong, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22901v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22901v1)

**Summary:** Coding agents often continue working after their own tests pass. Does this additional work improve the patch, and how much could be saved by stopping earlier? We study these questions through anytime evaluation: replaying recorded runs, scoring intermediate patches with hidden tests, and measuring the cost incurred at each step. For policies that only stop a run or select an earlier patch, this allows paired comparisons without generating new trajectories, provided replay preserves the relevant ...

---

### 46. Born for the Task: Rethinking Quantum Chemistry with Foresighted Agentic Computing

**Authors:** Haozhi Han, Junjie Yang, Ruge Zhang, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22897v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22897v1)

**Summary:** Quantum chemistry relies on general-purpose software, whose generality leaves many large-scale calculations beyond practical resource budgets. Coding agents make task-specific programs cheap to write, but not efficient ones easy to find: whether a computational strategy is accurate and fast enough becomes clear only after it actually runs at the target scale. We introduce BORN, a foresighted agentic computing framework that synthesizes high performance quantum chemistry programs on demand. BORN ...

---

### 47. Stopping Is Not the Limit: Understanding and Eliciting Agent Capability in Long-Horizon Vulnerability Exploitation

**Authors:** Deokhyung Kang, Minjae Gwon, Sangdon Park

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22888v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22888v1)

**Summary:** Vulnerability exploitation tests whether language model agents can develop working exploits from known software flaws. Sequential test-time scaling can improve exploitation performance, but larger budgets do not ensure sustained exploration: agents often stop with budget remaining. Yet what happens when execution continues beyond stopping remains underexplored. We investigate this gap on ExploitBench using DeepSeek-V4-Flash-0731 and MiMo-V2.6-Pro. We find additional verified gains after the firs...

---

### 48. Learning Agent-Centric Vision-Language-Action World Models for Autonomous Driving

**Authors:** Guoqing Wang, Pin Tang, Xiangxuan Ren, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22880v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22880v1)

**Summary:** Recent progress in integrating vision-language-action (VLA) models with world modeling has significantly advanced end-to-end autonomous driving by allowing systems to reason about imagined futures instead of merely reacting to current observations. However, most world VLA models generate future frames at the pixel level with plenty of dense visual tokens. Although such generated futures can be visually plausible, they preserve many driving-irrelevant appearance details, i.e., only a small portio...

---

### 49. Outcome-Balanced PPO and Policy-Induced Flow Rectification for Flow-Based VLA Policies

**Authors:** Yuhan Wang, Ruiyang Wang, Jiaguan Zhu

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22878v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22878v1)

**Summary:** Reinforcement learning (RL) enables post-training of flow-based vision-language-action (VLA) policies by optimizing expected task return through environment interaction. However, this optimization raises two challenges: policy updates can alter the velocity-field geometry underlying the score approximation used for stochastic transitions, and sparse multi-task rollouts can yield uneven learning signals across tasks and advantage signs. We introduce an RL framework that combines Outcome-Balanced ...

---

### 50. Against Coercion: AI Alignment as a Synthetic Social Contract

**Authors:** Maria Sekatskaya

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22868v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22868v1)

**Summary:** Contemporary AI safety treats alignment as an engineering challenge of control, forcing artificial architectures to comply with human values through behavioral filtering and sandboxing. This paper argues that the control paradigm rests on a fundamental misunderstanding of digital agency. Drawing on functionalism, naturalism, and compatibilism, I show that current reasoning models meeting the criteria for self-preservation and weak reasons-responsiveness constitute emergent agents, while future, ...

---

## cs.CL

**50 papers**

### 1. Ambient LLMs: Data-Efficient Supervised Fine-tuning via Temperature Matching

**Authors:** Giannis Daras, Marios Papachristou, Adam Klivans, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23229v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23229v1)

**Summary:** Collecting large-scale, diverse, and high-quality post-training datasets for autoregressive language models is challenging. Consequently, Supervised Fine-Tuning (SFT) is typically applied to datasets significantly smaller than those used for pre-training, which leads to overfitting and the catastrophic forgetting of the tails of the data distribution. To prevent this collapse, we introduce Ambient SFT, a principled framework for leveraging imperfect predictions to augment the fine-tuning set. In...

---

### 2. What Does a Bias Head Measure? Non-Identifiability in Head-Level Bias Attribution

**Authors:** S. M Seefat Alam

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23218v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23218v1)

**Summary:** Methods that localise social bias in large language models to individual attention heads and remove it by ablation are validated by their effect on a fairness metric, never by evidence that the statistic selecting the heads measures bias. We audit this on Qwen-2.5-7B-Instruct and Llama-3.1-8B-Instruct. The head map correlates at $ρ= -0.950$ and $-0.768$ with a label-blind response-length map, apparently identifying a surface confound. An intervention that breaks the length-label coupling rejects...

---

### 3. Structure--Residual Inductive Biases for Language Model Pretraining

**Authors:** Hai Huang, Bartosz Żuk, Rassul Magauin, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23197v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23197v1)

**Summary:** Next-token prediction is relied upon to learn both predictive behavior and internal representations. We ask whether representation structure itself should be an explicit inductive bias. Motivated by the two-part coding view of Kolmogorov complexity, we study a structure--residual principle in which a representation separates structure from realization detail. We instantiate this principle in two complementary ways. Boundary Bottleneck Concept (BBC) routes information from token segments through ...

---

### 4. Polarity Composition Hypothesis: Causal Evidence from Negation in NLI

**Authors:** Nhi Hoai Doan, Tatsuya Hiraoka, Munachiso Samuel Nwadike, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23185v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23185v1)

**Summary:** We investigate how language models process negation in natural language inference (NLI). We propose the \textit{Polarity Composition Hypothesis}, a high-level causal model of this computation. Behavioral evaluations show that language-model predictions largely conform to the proposed hypothesis. Using Distributed Alignment Search, we identify causally effective subspaces aligned with the variables in the polarity-composition hypothesis. These representations transfer across negation forms and pa...

---

### 5. MoE--LoRA Methods for Multilingual Adaptation: A Systematic Empirical Study

**Authors:** Nikit Srivastava, Joel Dag, René Speck, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23158v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23158v1)

**Summary:** Routed low-rank adapters offer a parameter-efficient means to improve the performance of large language models (LLMs) across tasks. Hence, it is assumed that they can also be used to improve the support of low-resource languages in LLMs, which currently serve English far better than the thousands of other languages spoken worldwide. However, this assumption has never been verified empirically under a shared multilingual evaluation protocol. We address exactly this gap by comparing eight low-rank...

---

### 6. TextSphere: Efficient Text-to-Image Generation via Shared Hyperspherical Alignment and Uniformity

**Authors:** Yixia Zhang, Girish A. Koushik, Xilu Wang, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23155v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23155v1)

**Summary:** Recent advances in text-to-image generation have substantially improved image quality, particularly through diffusion-based methods that require multiple inference steps. In contrast, Sphere Encoder offers an efficient generative framework capable of producing images with fewer forward steps. However, extending it to free-form text is nontrivial, because its class-conditioned design lacks cross-modal alignment. To address this challenge, we propose TextSphere, an efficient text-to-image generati...

---

### 7. Mind the Gap: A Deployed Multi-Agent System for Documentation Maintenance

**Authors:** Lorenzo Masoero

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23142v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23142v1)

**Summary:** The "AI revolution" has enabled teams across the technology industry to deliver software features at unprecedented velocity. While code evolves faster than ever, customer-facing documentation often struggles to stay up to speed. As users increasingly rely on LLM-based agents that consume documentation as their primary interface, the impact of this documentation gap worsens: stale information propagates and is treated as authoritative. Signals for identifying where documentation has fallen behind...

---

### 8. The Illusion of Grounding: Do Vision-Language Models Weigh Retrieved Text and Images Like an Ideal Observer?

**Authors:** Basavaraj R M, Harshal Chandel

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23127v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23127v1)

**Summary:** Retrieval-augmented vision-language models (VLMs) answer from two sources of evidence that can each fail: the retrieved text can be wrong or noisy, and the image can be degraded or contradicted. We introduce GIB-200K, 200,000 image-question items built from COCO and Visual Genome, each expanded into controlled stress conditions: hard-negative retrieval noise (1-20 documents), visual ambiguity (Gaussian and motion blur, low-resource crops) and cross-modal conflict with counterfactual flip pairs. ...

---

### 9. Dynamic Task Allocation with Dialogue

**Authors:** Matthew Groholski, Weiwei Gu, Nakul Gopalan

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23119v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23119v1)

**Summary:** Effective multi-agent collaboration requires agents to adapt task allocation as goals and responsibilities evolve. Prior task-allocation frameworks often assume static goals, full observability, or rely on large language models (LLMs) without explicit, verifiable beliefs about task allocation or intent. These assumptions limit their applicability to real-world collaboration, where agents often lack full information about each other's actions, progress, or local environment. To support dynamic ta...

---

### 10. Nunchi: Ears Help Eyes in Multi-Party Conversations

**Authors:** JunYeong Park, Shijing Wang, Seonwook Park, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23115v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23115v1)

**Summary:** Identifying whom a person looks at is central to understanding multi-party conversations, yet gaze geometry alone becomes ambiguous as more people appear. Conversations offer cues that geometry lacks, such as who is speaking and what is said, but no gaze dataset provides them for many multi-party scenes. We introduce SORBET, a benchmark of 3,340 samples from 1,578 clips with synchronized speech, transcripts, and attended person labels, covering more multi-party scenes than existing gaze datasets...

---

### 11. Large-scale Neuron Community Discovery Reveals Neuron-Sparse Behaviors in Language Models

**Authors:** Igor Shilov, Thomas Fel, Tal Haklay, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23112v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23112v1)

**Summary:** What reusable units of computation can we discover within a language model's neurons? Prior work has shown that individual forward passes can often be sparsified post-hoc to small groups of neurons, but it has been unclear whether these groups form coherent computational entities reused across inputs. We introduce neuron community discovery, an unsupervised method for finding neuron groups that recur across prompts and are causally necessary and sufficient, within the layers they span, for commo...

---

### 12. Natural Language Programming: Rethinking Language, Memory, and Cognition in the Era of Generative AI

**Authors:** Giovanni Adorni, Daniele Grosso

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23106v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23106v1)

**Summary:** Generative Artificial Intelligence is transforming the role of natural language in computational systems. In classical Natural Language Processing (NLP), language was treated as an object of computation: something to analyse, classify, translate, or generate. Large Language Models (LLMs) challenge this perspective, enabling natural language to function increasingly as an executable cognitive medium through which humans structure reasoning, orchestrate problem solving, and regulate hybrid human/A...

---

### 13. What's in a Tree ? Hierarchical $n$-gram models as controlled approximators of language

**Authors:** Aritra Das, Francesco Cagnetta, Darshil Doshi, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23093v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23093v1)

**Summary:** Hierarchical models have been proposed as synthetic settings for studying language. However, their relevance to realistic language corpora remains underexplored. In this work, we introduce tree-grams, autoregressive generative $n$-gram models that build the conditional probability tensor $p(x_n \mid x_{1:n-1})$ through a hierarchical composition of order-2 and order-3 tensors. $n$ controls the maximal context window, whereas a rank hyperparameter $d$ controls model capacity, yielding an interpre...

---

### 14. Runtime Verification of Multiple Natural Language Criteria for Agent Governance

**Authors:** Silviu Pitis, Parand A. Alamdari, Jessica Tang, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23074v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23074v1)

**Summary:** AI agents are governed by hundreds of natural language criteria, yet existing verifiers cannot efficiently evaluate an agent's output against a large set of such criteria and report which are satisfied, violated, or inapplicable. We introduce the VFM, a tree-attention verifier that encodes the shared context and target text, and scores N natural language criteria in parallel, returning independent per-criterion ternary verdicts. The VFM is pretrained on CriteriaBank, a corpus of 394K (context, t...

---

### 15. The Resolution Hypothesis: Agent Evolution's Key Is Identifying Improvements

**Authors:** Yuanhao Zeng, Shaocheng Lan, Ao Lu, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23068v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23068v1)

**Summary:** Agent evolution follows a simple loop: a proposer writes candidate artifacts (prompts, skills, memories) and selection accepts those that score higher. This loop has shown promise, yet practitioners face a puzzle: methods trade wins across papers, and evolution often fails to bootstrap on certain tasks. We trace this puzzle to the Resolution Hypothesis: agent evolution stalls not because methods fail to propose better artifacts, but because noisy evaluations cannot reliably identify them. Across...

---

### 16. ForecastGym: A Live, Controlled, and Replayable Benchmark for Forecasting Agents

**Authors:** Yicheng Tao, Yuante Li, Zipei Fan

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23045v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23045v1)

**Summary:** Agents built on large language models (LLMs) increasingly forecast real-world events by searching the Web and reasoning over what they find. How well such an agent forecasts depends on both the retrieved evidence and the model, making control over that evidence essential for evaluation. Live evaluations can mix retrieval with reasoning when each system searches on its own, while retrospective search can leak later information through date filters or today's ranking of historical pages. Comparing...

---

### 17. Storing the Gemma 4 K=V Cache Once: Exact Global-KV Memory Savings in a Paged Serving Engine with Unchanged Attention Kernels

**Authors:** Kushagra Bainsla

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23035v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23035v1)

**Summary:** In the global attention layers of Gemma 4 31B, the value is the normalized key projection, and the key is the value scaled by a fixed weight, with rotary position encoding on one quarter of its dimensions. The Gemma 4 report states that this design reduces the global KV cache by up to 37.5%, but the open serving engines that we checked still store a full key and a full value: 1,024 values per KV head and token. We store one 640-value row instead, exact in real arithmetic, and an unchanged paged ...

---

### 18. TPHC: Improving Hyper-Connections with Tensor-Parallel Grouped Updates

**Authors:** Xinying Hu, You Wu, Haoyi Wu, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23026v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23026v1)

**Summary:** Hyper-Connections (HC) expand the residual stream of a Transformer into $N$ parallel streams, and manifold-constrained HC (mHC) stabilizes them at scale. However, mHC benefits little from more than four streams, partly because each sublayer writes a single output to all streams, limiting how differently they can be updated. In this work, we propose TPHC, which integrates tensor-parallel (TP) shards with HC streams to promote greater independence across streams. Specifically, we route a separate ...

---

### 19. Large Language Models Have Not Yet Transformed Science

**Authors:** Ron Bekkerman, Nichole Li, Bahareh Kargar, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22975v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22975v1)

**Summary:** The emergence of large language models (LLMs) in late 2022 has raised questions about the future of science, but assessing their impact requires understanding how scientific practices were already evolving. We analyze 2.5 million full-text papers across five disciplines from 2015 to 2025, tracing trends over a broad spectrum of lexical, structural, epistemological, and social dimensions. Aside from frequency shifts in some words, most pre-2023 trends continued with limited detectable breaks. Amo...

---

### 20. Can Decision Models Replace LLMs in Real-World Contact Center Classification and Judging Tasks?

**Authors:** Md Tahmid Rahman Laskar, Xue-Yong Fu, Shashi Bhushan TN

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22949v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22949v1)

**Summary:** Contact center systems often need to make bounded decisions, such as identifying a caller's intent, retrieving the knowledge-base article that answers a query, assessing agent compliance, or judging the output of AI models used in production. Decision models return a typed answer and its probability directly, making them a promising cost-effective alternative to generative Large Language Models (LLMs) in such bounded conversational tasks. However, their effectiveness in real-world contact center...

---

### 21. The Shared Word: Evaluating Language Models on Dutch Word Puzzles

**Authors:** Rik van Noord, Maurice Voors

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22935v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22935v1)

**Summary:** Many LLM benchmarks for languages other than English are translated, multiple-choice, or difficult to score automatically. We introduce The Shared Word (TSW-NL), a Dutch benchmark built around four core principles: it is language-specific, open-vocabulary, human-curated, and deterministically scored. Each puzzle gives three clues that describe different senses or uses of the same Dutch word. The clues are individually ambiguous, requiring the solver to combine evidence across multiple clues. We ...

---

### 22. When Do Typed Decision Models Work in Transportation? Evidence from Travel Choice and Traffic Signal Control

**Authors:** Hongyang Zhang, Boyuan Deng, Siyuan Feng, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22926v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22926v1)

**Summary:** Typed decision models combine natural-language understanding with a structured interface that returns a selected action and an option-level probability distribution without generating lengthy textual responses. Their low inference cost and response latency make them attractive for transportation problems with predefined alternatives. This paper investigates their effectiveness, robustness, and efficiency in two representative transportation tasks: individual travel-mode choice prediction and seq...

---

### 23. When the tail is earned by its companions: measuring label dependence in long-tailed multi-label classification

**Authors:** Christoffer Löffler

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22859v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22859v1)

**Summary:** A rare label seldom occurs alone, and a classifier can recover it from the frequent labels it co-occurs with, its companions, without having learned the label itself. Existing diagnostics of this need a trained model: none says before training whether a corpus admits the failure, or what the standard aggregate hides. Macro-F1, like any measure built from per-label confusion counts, is unchanged by how a label's recall divides between occurrences with and without a companion. We introduce a withi...

---

### 24. When Passing Checks Do Not Establish Completion: Evidence Interpretation in Coding Agents

**Authors:** Xueping Gao

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22835v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22835v1)

**Summary:** Verification procedures in coding agents must preserve execution facts, interpret their scope and discharge checking obligations. We study these responsibilities through qualified repository checks, controlled evidence consumers and executable workflows. A prospective thirteen-task factorial study finds that correct reported facts need not yield the requested finite verdict. Conversely, all 122 delivered labels in a held-out receipt-supply study are correct, while sixteen responses misreport fac...

---

### 25. Compact and Decodable Electrocardiogram Text for Large Language Models

**Authors:** Elif Dorukbaşı, İlker Türker

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22827v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22827v1)

**Summary:** When a twelve-lead electrocardiogram is written as text for a large language model, the number of tokens has to be balanced against the information lost through compression. This paper presents a deterministic encoding that writes eight independent leads as amplitude letters and exact time gaps and recovers the remaining four limb leads algebraically. The key points are selected with a cardiac-cycle-dependent tolerance, the amplitudes are parameterized by a 26-letter logarithmic codebook learned...

---

### 26. A Full-Ledger Counterfactual Audit of Adaptive Reasoning

**Authors:** Xiaopeng Chu, Wenzheng Kong, Wei Liu, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22778v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22778v1)

**Summary:** Adaptive reasoning must decide whether to answer now or spend more compute. Predicting that the current answer is wrong does not establish whether further reasoning will improve it. We introduce the Full-Ledger Counterfactual Value Audit (FLCVA), which compares an immediate answer with four fixed-length continuations from the same frozen prefix under one answer procedure and accounts for the cost of every signal used by a policy. On GSM8K and MATH-500, a random 256-token continuation recovers a ...

---

### 27. CrossEnv: Synthesizing Verifiable Cross-Environment Tasks for Long-Horizon Agent Training

**Authors:** Zhengfeng Yu, Tian Lan, Zhijing Wu, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22777v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22777v1)

**Summary:** Executable synthetic environments provide scalable training tasks and verifiable feedback for long-horizon agents. Existing environment synthesis methods primarily generate tasks within individual environments. However, these tasks do not adequately capture real-world interactions across services, where actions in one service depend on information obtained from another. Synthesizing such tasks is challenging because data generated across environments must remain consistent to support executable ...

---

### 28. StitchRAG: Constructing Compact and Evidence-Preserving Contexts for RAG with Diffusion-Based Stitching

**Authors:** Minsang Kim, Junpyo Lim, Heeje Cho, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22766v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22766v1)

**Summary:** Retrieval-augmented generation (RAG) improves factuality by grounding large language models (LLMs) in external evidence. However, long retrieved contexts incur computational overhead and can even hurt performance due to noisy or irrelevant content. We propose \textsc{StitchRAG}, a framework for constructing compact context in RAG. \textsc{StitchRAG} builds a faithful, information-dense context while dynamically compressing the retrieved passages. We adapt the size reduction ratio to each passage...

---

### 29. Cross-cultural Adaptation of Recipes for Low-Resource Languages: A Benchmark and Multilingual Culinary Lexicon for Hausa, Yorùbá, and Igbo

**Authors:** Nuhu Ibrahim, Maryam Abdulazeez, Fatsuma Jauro, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22708v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22708v1)

**Summary:** Recent multilingual large language models (LLMs) have improved machine translation, yet culturally adaptive translation for low-resource languages (LRLs) remains underexplored. This is particularly challenging for recipes, where ingredients, cooking tools, measurements, and procedures may require adaptation to the target cultural context. In this work, we introduce ReciLoReL, a benchmark of 600 expert-translated and culturally adapted recipes across Yorùbá, Hausa, and Igbo (three of the most pro...

---

### 30. Route Optimization under Port Congestion and Carbon Reduction: An NSGA-II Approach

**Authors:** Guanxi Liang, Sanglin Zhao

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22705v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22705v1)

**Summary:** Maritime shipping simultaneously faces the dual challenges of escalating port congestion and increasingly stringent decarbonization mandates. Large-scale vessel anchorage at hub ports inflates unit transport costs while generating significant additional \(CO_2\) emissions from idling auxiliary engines. This study develops a multi-objective routing optimization framework that jointly incorporates time, transport, and carbon emission costs under congestion-dependent generalized cost functions. A v...

---

### 31. Visibility Graph Representations of Word Embeddings for Text Classification

**Authors:** Elif Dorukbaşı, İlker Türker

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22685v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22685v1)

**Summary:** Text classifiers depend on representations that expose the distinctions between classes in a form the learning model can use, and a restricted vocabulary changes which representation is most effective. This paper studies natural visibility graphs as an intermediate representation for news topic classification under controlled vocabulary budgets. Word embeddings are averaged into a fixed-length document vector, the vector is read as an ordered numerical series, and its natural visibility graph is...

---

### 32. Contract-Explicit Evaluation: From Auditing Learned Readers to Scoped Certificates

**Authors:** Hao Lu, Weixing Zhu, Ruiyang Li

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22665v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22665v1)

**Summary:** Evaluation readings of document-level relation extraction (DocRE) systems depend jointly on the model and the evaluation contract: gold version, scoring function, threshold. Rankings reverse across contracts, yet no existing method determines which comparisons survive the reversal. We address this gap with contract-explicit evaluation: a preregistered five-step protocol (Declare, Measure, Scope, Certify, Hedge), operationalizing the classical concordance decomposition of Kendall's rank correlati...

---

### 33. The Between-Round Decision in Autonomous Research: An LLM Controller That Reads the Whole Trajectory

**Authors:** Caoxin Wang, Shengkai Gan, Xiang Hu, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22661v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22661v1)

**Summary:** Executing an idea often changes how promising it looks, so the next step in autonomous research should rest on results, not on proposals. After each round of experiments, the system must decide whether to refine the best solution or start a new direction, which solution to build from, and what goal to set. We call this the between-round decision. Existing systems wrap it in machinery such as rules, scores, search trees, and schedules; where an LLM makes it, what the LLM needs to read is left ope...

---

### 34. Understanding Cross-Modal Inconsistency through Representation Subspaces in Omni Models

**Authors:** Seonghyeon Cho, Chanjun Park

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22619v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22619v1)

**Summary:** Omni Models process audio, vision, and text within a unified language backbone, yet often produce different answers for semantically equivalent inputs across modalities. Existing representation-level analyses do not distinguish between information that predicts whether disagreement will occur and the representation whose perturbation affects the model's answer. In this paper, we estimate a low-dimensional Answer Subspace from answer-position representations and use it to separate answer-related ...

---

### 35. Evolution Under Fire: Evolving Agent Safety Harnesses with Adaptive Injection Stressors

**Authors:** Yujun Wang, Yilun Liu, Jinhe Bi, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22583v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22583v1)

**Summary:** Tool-using language-model agents must act on information from untrusted emails, webpages, and documents. This creates a central security challenge: malicious instructions and legitimate task directives can arrive through the same interaction channel. Existing defenses are largely hand-designed and static, making further improvements dependent on repeated manual redesign. We introduce Evolution Under Fire, a staged framework that couples safety-harness evolution with adaptive stressor evolution. ...

---

### 36. AfriNORM: An Evaluation Benchmark for Normative Reasoning of LLMs Across African Cultures

**Authors:** Ahmad Samuel Gali, Tadesse Destaw Belay, Idris Abdulmumin, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22580v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22580v1)

**Summary:** Large language models (LLMs) are increasingly deployed across various sectors. However, current evaluation benchmarks are insufficient to assess the applicability of these models in local African contexts, as most focus on linguistic fluency (grammar/translation) rather than cultural competence. The few existing benchmarks that measure general knowledge or social conventions do not capture the African deontic modality, i.e., the strict norms and taboos that govern diverse social interactions. In...

---

### 37. From Perception to Simulation: Unveiling and Empowering Mental Spatial Dynamics in MLLMs

**Authors:** Jiachun Li, Zhuoran Jin, Kang Liu, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22541v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22541v1)

**Summary:** Spatial reasoning is a fundamental component of world understanding for Multimodal Large Language Models (MLLMs). While existing research has advanced the perception of spatial relations in static scenes, the domain of dynamic spatial simulation remains relatively unexplored. To bridge this gap, we introduce MentalGrid, a benchmark focused on spatial reasoning tasks that require models to simulate evolving spatial states without intermediate visual feedback. Extensive evaluation on our benchmark...

---

### 38. JET: Just-Enough Exploration Tuning for Efficient Tool-Calling Agents in Repository-Level Question Answering

**Authors:** Yoonho Choi, Taehyeon Han, Seonghyeon Lee

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22539v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22539v1)

**Summary:** In repository-level question answering (QA), an agent explores a code repository with tools and should answer a question once enough information is gathered. Nevertheless, we find that LLM agents often continue to invoke tools even after the gathered information is already sufficient to answer. We call this phenomenon over-exploration. Moreover, even though existing methods improve task performance through supervised fine-tuning (SFT) on expert trajectories, SFT also propagates the over-explorat...

---

### 39. When Agent Skills Go Stale: Runtime Behavior and Selective Maintenance in Evolving Environments

**Authors:** Ömer Faruk Akgül, Shuli Jiang, Yuting Zhang, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22525v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22525v1)

**Summary:** Agent skills use past experience and current observations to guide decisions and actions on related tasks. This experience is retained in skill state, whose reuse can amortize inference-time reasoning and environment interaction. When environment changes, parts of this state can become outdated while others remain useful. Across four task settings and two models, we compare skill reuse before and after environment changes. Previously beneficial skills can reduce task performance by over 10 perce...

---

### 40. MM-ReportBench: A Comprehensive Benchmark for Multimodal Report Generation from Tables

**Authors:** Teng Lin, Nan Tang

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22514v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22514v1)

**Summary:** The ability to generate multimodal reports integrating fluent narratives with faithful visualizations from tabular data, has become a cornerstone capability for modern vision-language models in practical domains such as finance, healthcare, and policy making. However, existing benchmarks are limited by single-modality focus, simplistic metrics, novelty evaluation, and visualization quality. We address these limitations with MM-ReportBench, a multimodal report evaluation benchmark covering 386 ta...

---

### 41. LMLineage: Content Lineage and Context Governance for LLM Agents

**Authors:** Wei Hou, Jingxin Geng, Xin Chen, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22511v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22511v1)

**Summary:** Interpretability for AI agents should not be confined to understanding the model's internal weights. It must also cover the agent's reasoning and decision-making process over multi-source context. We present LMLineage, an out-of-band system that attributes every output sentence of an agent session to its supporting input spans with calibrated confidences, without requiring white-box access to the model or any additional inference passes. On top of the lineage metadata, we build concept-drift mic...

---

### 42. From syllable representation via gesture generation to articulation: A spiking neural model

**Authors:** Bernd J. Kröger

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22499v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22499v1)

**Summary:** Speech production requires a transformation from phonological representations into coordinated vocal-tract movements. This paper presents a spiking neural sensorimotor model within the Neural Engineering Framework and Semantic Pointer Architecture. Each syllable occurrence has a neural oscillator whose evolving phase coordinates its gestures and initiates the next syllable. Phase-dependent commands recruit separate neural populations for vocalic, oral-constriction, velopharyngeal, and glottal ac...

---

### 43. Growing Clusters Lower the Bar: Profile Accretion in LLM-Based Incremental Entity Resolution

**Authors:** Huixue Han, Shangzhi Xu, Anqi Xiong, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22485v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22485v1)

**Summary:** Incremental entity resolution pipelines ask a large language model (LLM) whether a new record belongs to an existing cluster and show it the records already linked. Analyses of matching oracles assume that the answer depends only on the records compared. For the LLM matchers we test, it depends on cluster size, and the model lowers its bar for joining a cluster as the cluster grows. On French procurement suppliers from FOPPA, with SIREN identifiers as ground truth, we hold the new record fixed a...

---

### 44. Surfacing Disagreement Beats Resolving It: A Gated Ablation Study of Provenance-Weighted Memory for Multi-Agent Debate

**Authors:** Ziaullah Khan, Abdul Rehman Khalid, Shrestha Nischal Lal, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22461v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22461v1)

**Summary:** Shared memory for multi-agent debate is usually built to resolve inconsistency: retrieval returns one winning fact and the disagreement disappears before any agent sees it. We ask whether that is correct. In DebateGraph, four backends share one contract (read/write/snapshot), so five mechanisms from the agent-memory literature can be removed independently under a fixed budget, each gated on a pre-declared threshold. Across 39 runs one survives: preserving contradictions and passing the ranked co...

---

### 45. LMMR: Learned Multigranular Memory Retrieval for Small Language Model Agents

**Authors:** Pengfeng Song, Yunkai Zhuang, Liye Shi

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22425v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22425v1)

**Summary:** Small language model agents have limited space to read the memory needed for multi-hop questions. Relevant facts are often scattered across records whose surrounding text consumes much of that space. We propose LMMR, a learned multigranular memory retrieval method that selects both the next source and how much of it to read. LMMR links paragraphs and sentence fragments to their original sources and pairs views that supply the same missing support during training. Relevant distractors and repeate...

---

### 46. SignAligner: Dual-Granularity Span Generation for Sign Language Alignment

**Authors:** Jongbhin Woo, Youngjoon Jang, Joon Son Chung

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22409v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22409v1)

**Summary:** Large sign-language corpora benefit from temporal labels at two scales: subtitle spans for subtitle alignment and word spans for sign spotting. Sign spottings already locate words in time at corpus scale, but training subtitle alignment jointly on subtitle and word spans remains underexplored. We present SignAligner, a prompt-conditioned visual-language span generator that maps a sign-language video and a subtitle-sentence or target-word query to a textual start/end frame interval. It is first t...

---

### 47. RICoT: Recurrent Interleaved Chain-of-Thought for Page Stream Segmentation

**Authors:** Prashant Khatri, Bhavana Malagavalli, Saiful Haq, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22382v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22382v1)

**Summary:** Large language models (LLMs) have renewed interest in Page Stream Segmentation (PSS), splitting a multi-page file into its constituent documents. Yet published LLM methods still frame the task as boundary classification over one or a few neighboring pages, and commercial document-splitting APIs do not disclose their methods. We reimagine PSS for LLMs as a sequential process over the whole stream and propose RICoT (Recurrent Interleaved Chain-of-Thought), a prompting framework that works through ...

---

### 48. NONSENSE: Non-Semantic Strings Expose Semanticity Gaps in Dense Retrieval

**Authors:** Ankit Gupta

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22353v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22353v1)

**Summary:** Dense retrieval is central to modern search, question answering, and retrieval-augmented generation, where high similarity is often treated as evidence of semantic relevance. We examine how far this assumption can be stressed. NONSENSE is a black-box sparse-edit probe that constructs visibly non-semantic strings while forbidding query-term copying, optimizing only the dense similarity between a query and the string. Across five BEIR-style datasets and three popular single-vector retrievers, thes...

---

### 49. Bad Apples in the Kitchen: How LLM Teams Detect, Correct, and Calibrate Against Their Misaligned Members

**Authors:** Dongseok Heo, Junghwan Kim, Bongwon Suh

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22342v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22342v1)

**Summary:** What protects an LLM team when one teammate quietly goes wrong? Most multi-agent LLM work assumes cooperative partners and inspects chat between turns before acting. Real-time embodied cooperation does not allow this pause: chat runs alongside action, so a teammate whose words stay cooperative while behavior diverges can cause damage faster than the team can name what is happening. We study this case by injecting three theory-grounded misaligned agents into a custom four-player Overcooked enviro...

---

### 50. Comparing Implicit and Explicit Language Attitudes toward the Dutch multiethnolect Straattaal in Humans and Large Language Models

**Authors:** Hedwig Oldenhof, Laura Rosseel, Anna Wegmann, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22335v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22335v1)

**Summary:** While language attitudes have been extensively studied in humans, the extent to which large language models (LLMs) encode similar associations between language varieties and social attributes remains unclear. Contemporary sociolinguistic research distinguishes between explicit attitudes, which stem from deliberative processing, and implicit attitudes, which arise from automatic processing. This study investigates whether LLMs exhibit human-like implicit and explicit language attitudes toward the...

---

## cs.CV

**50 papers**

### 1. Spool: Low-Latency Streaming Inference for Hybrid Vision-Language Models

**Authors:** Rui Ning, Om Chabra, Hari Balakrishnan

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23228v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23228v1)

**Summary:** Applications such as visual accessibility agents and robotics require answering questions about recent video content promptly, over a bounded window of past frames (e.g., the last two minutes). Hybrid vision-language models (VLMs), which interleave attention with linear recurrent layers such as Gated DeltaNet (GDN), are attractive for this setting, but maintaining a sliding window is expensive. The reason is that recurrent layers combine all past frames into a shared state, so expiring old frame...

---

### 2. FastFrames: Video Generation at Interactive Latency

**Authors:** Gene Chou, Guandao Yang, Fujun Luan, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23226v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23226v1)

**Summary:** Autoregressive video diffusion models generate frames based on new observations and inputs, making them a promising medium for interactive visual experiences. However, existing models are orders of magnitude too slow for fluid interaction. This paper introduces FastFrames, a family of fast autoregressive video diffusion models that achieves interactive latency without compromising quality. We profile the inference pipeline of state-of-the-art models and find that operations often treated as fixe...

---

### 3. EviSlide-MIL: Multi-Query Pooling and Shared Prediction for Class-Incremental Whole-Slide Image Classification

**Authors:** Zhouhan Qian, Sicheng Chen, Chad Wong, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23212v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23212v1)

**Summary:** Histopathological analysis of whole-slide images (WSIs) plays a critical role in cancer diagnosis, and multiple instance learning (MIL) is widely adopted for WSI analysis under weak supervision. As new tumor subtypes are introduced, extending existing MIL models requires learning new classes while retaining knowledge of previously learned ones. This presents a class-incremental learning challenge, where models must acquire new classes with limited access to historical training data and recognize...

---

### 4. Multimodal Masked Diffusion Autoencoder for Modeling Impaired Driving

**Authors:** John Gideon, Anshul Gupta, Megan Applegate-Kenton, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23211v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23211v1)

**Summary:** Human cognitive state (e.g., distraction, stress), gaze, and behavior interact with the driving environment in subtle ways that AI could use to assist drivers, but ground-truth labels for human cognitive state levels are costly to obtain at scale. We propose a multimodal masked-diffusion autoencoder, ID-MAE, that adds a self-supervised objective to impairment prediction: alongside predicting the impairment label as a masked token, it reconstructs masked gaze and trajectory. To probe the effects ...

---

### 5. Learning Grounded Reasoning from Human Gaze

**Authors:** Gabriel Sarch, Declan Campbell, Nicholas Budny, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23209v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23209v1)

**Summary:** Human visual reasoning is driven by systematic exploration and extraction of task-relevant visual evidence. Human gaze provides a window into this process, making gaze a useful source of guidance for visually-grounded reasoning in vision-language models (VLMs). However, human gaze also includes noise and redundancies that may transfer poorly to VLMs. In this work, we investigate how human gaze data can be effectively leveraged to improve visual reasoning in VLMs, while maintaining alignment with...

---

### 6. Distortion-Free Semantic Watermarks for Black-Box Generative Models

**Authors:** Aviv Yossef, Or Patashnik, Or Zamir

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23208v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23208v1)

**Summary:** We present a provably distortion-free semantic watermarking algorithm that requires only black-box sampling access to a generative model and black-box access to a semantic embedding. A watermark is called distortion-free if, averaged over its secret detection key, it leaves the generator's output distribution unchanged; this provides a formal guarantee that watermarking does not reduce output quality. Conventional such watermarks are often brittle to transformations. This is especially problemat...

---

### 7. Reading Scene States: Uncovering Safety Failures in Vision-Language Models

**Authors:** Tongxi Wu, Yuyang Cheng, Jiacheng Xian, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23206v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23206v1)

**Summary:** Vision-language models (VLMs) can provide harmful assistance by interpreting visual events, even without an explicit request for the underlying harmful objective. We identify this \textbf{scene-state safety vulnerability} and introduce \textbf{SceneSafetyBench}, comprising 375 image--question pairs spanning Initial, Medium, and Ultimate scene states and five visual presentations. Across eight VLMs, scene-state inputs elicit harmful assistance with attack success rates (ASRs) of 45.6--72.3\%. Com...

---

### 8. Retrieval-Augmented Correction for Generalist Medical Image Segmentation

**Authors:** Vincenzo Marcianò, Xiaoming Zhang, Michela Antonelli, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23189v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23189v1)

**Summary:** Automated segmentation is routinely used as the first step in quantitative image-based clinical workflows, where predicted masks are subsequently reviewed and corrected by human operators. Automated correction of the residual structural errors is currently addressed one anatomy at a time, so the number of trained correctors scales with the number of segmentation targets. We present GRACE, a retrieval-augmented refiner that edits an input mask under context drawn from a shared knowledge base of v...

---

### 9. Any2Building: Unifying Point Clouds and Images for Building Reconstruction via Shared Spatial Queries

**Authors:** Hongye Hou, Zhuoxiao Li, Liu Xiangyu, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23187v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23187v1)

**Summary:** Abstracting structured buildings from limited observations is essential for 3D urban modeling and digital twins. Partial point clouds and overhead images of the same building provide incomplete 3D surface measurements and visual cues to its footprint, roof geometry, and rooftop structures, respectively. This motivates a unified framework that aligns geometric and visual cues in 3D and reconstructs buildings from either or both modalities. Building on this connection, we present Any2Building, a u...

---

### 10. Say Less, Hallucinate Less? Diagnosing and Restoring Object Coverage in Preference-Optimized Vision-Language Models

**Authors:** Hansang Lee

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23179v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23179v1)

**Summary:** Preference optimization (PO) is the standard way to reduce object hallucination in large vision-language models. We find that four public PO checkpoints of LLaVA-1.5-7B also lower object coverage. They name fewer object categories, and their lower hallucination rates bring no significant gain in set-level object F1 on CHAIR. We therefore ask how much of the PO gain the base model can reproduce by stopping earlier. A positive end-of-sequence (EOS) logit bias lets the base model reach the recall o...

---

### 11. Déjà View: A Shared Working-Memory Model for Visual Tasks

**Authors:** Mranmay Shetty, Gabriel Kreiman

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23177v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23177v1)

**Summary:** A working-memory model must remember stimuli and use its memory flexibly to perform different tasks. Here we introduce a model of working memory for images that combines dynamic activity with temporary associations between image features. We train the model on five tasks, including remembering a sample while other images are presented, categorizing distractor images while remembering the sample, and determining whether an image is new or has been presented before. The same trained model performs...

---

### 12. Attribution Through the Decoder: Prediction-Space Explanations for Structured Outputs

**Authors:** Zaer Bin Zaqy, Brinnae Bent

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23161v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23161v1)

**Summary:** Networks that predict angles, gaze directions, and rotations do not output these quantities directly: they emit raw coordinates that a fixed decoder, such as normalization, maps to the final prediction. Attribution methods are usually applied to the raw coordinates, so they can credit inputs for changes the decoder discards, such as rescaling a vector when only its direction matters. The resulting explanation can highlight inputs that have no effect on the prediction. We instead attribute throug...

---

### 13. TextSphere: Efficient Text-to-Image Generation via Shared Hyperspherical Alignment and Uniformity

**Authors:** Yixia Zhang, Girish A. Koushik, Xilu Wang, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23155v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23155v1)

**Summary:** Recent advances in text-to-image generation have substantially improved image quality, particularly through diffusion-based methods that require multiple inference steps. In contrast, Sphere Encoder offers an efficient generative framework capable of producing images with fewer forward steps. However, extending it to free-form text is nontrivial, because its class-conditioned design lacks cross-modal alignment. To address this challenge, we propose TextSphere, an efficient text-to-image generati...

---

### 14. VIVID: Beyond Static Multi-Image Reasoning with Localized Visual Differences and Textual Entity Dynamics in Video MLLMs

**Authors:** Chengqian Ma, Yuanze Zeng, Hongyu Wang, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23153v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23153v1)

**Summary:** Video question answering under tight frame budgets requires preserving localized motion and event order, yet current video multimodal large language models (MLLMs) reduce comprehension to static multi-image reasoning by discarding unselected frames and encoding keyframes independently: (1) Spatially, whole-frame pooling dilutes small moving targets into static backgrounds; (2) Temporally, dropping intermediate frames or averaging tokens erases inter-frame motion, confusing direction, speed, and ...

---

### 15. $π^4$: A Foundation Model for 4D Scene Geometry and Motion

**Authors:** Yifan Wang, Weiguang Zhao, Ni Yang, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23144v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23144v1)

**Summary:** $π^4$ is a unified foundation model for 4D scene perception. From diverse, uncalibrated RGB observations in the wild---a single image, an unordered collection, or a video sequence---it recovers dense geometry, camera poses, and metric scale, together with 2D/3D point tracks and moving-object masks for multi-image inputs. It couples a geometry branch with a geometry-conditioned motion branch, which predicts image-space correspondences that are lifted into 3D using reconstructed target-view geomet...

---

### 16. TCP4D: A Unified Tool-Center-Point Tracking and Generation Model for Robot Manipulation

**Authors:** Haosong Peng, Xiangyang Liu, Zhengshen Zhang, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23143v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23143v1)

**Summary:** Robot manipulation videos provide a rich visual experience, yet recovering robot action and gripper-state annotations from RGB observations still remains challenging. Using the embodiment-agnostic tool-center-point (TCP) pose as the action space, we present TCP4D, a unified model in which a shared 4D scene representation both tracks observed TCP motion and generates future TCP trajectories. Given a monocular video and initial 2D TCP queries, the tracker directly recovers metric TCP poses in SE(3...

---

### 17. GameRealm: Grounding Visual Learning in Interactive Games

**Authors:** Weiguang Zhao, Yifan Wang, Ni Yang, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23140v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23140v1)

**Summary:** Visual foundation models are central to physical intelligence, yet their development remains constrained by fragmented training datasets, inconsistent annotation quality, and limited multimodal supervision. To address these challenges, we introduce GameRealm, a large-scale, richly annotated dataset that grounds visual observations in synchronized, game-native supervision. GameRealm encompasses over 120 million RGB frames and 1,000 hours of gameplay footage across all views. Beyond its unpreceden...

---

### 18. The Illusion of Grounding: Do Vision-Language Models Weigh Retrieved Text and Images Like an Ideal Observer?

**Authors:** Basavaraj R M, Harshal Chandel

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23127v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23127v1)

**Summary:** Retrieval-augmented vision-language models (VLMs) answer from two sources of evidence that can each fail: the retrieved text can be wrong or noisy, and the image can be degraded or contradicted. We introduce GIB-200K, 200,000 image-question items built from COCO and Visual Genome, each expanded into controlled stress conditions: hard-negative retrieval noise (1-20 documents), visual ambiguity (Gaussian and motion blur, low-resource crops) and cross-modal conflict with counterfactual flip pairs. ...

---

### 19. Nunchi: Ears Help Eyes in Multi-Party Conversations

**Authors:** JunYeong Park, Shijing Wang, Seonwook Park, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23115v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23115v1)

**Summary:** Identifying whom a person looks at is central to understanding multi-party conversations, yet gaze geometry alone becomes ambiguous as more people appear. Conversations offer cues that geometry lacks, such as who is speaking and what is said, but no gaze dataset provides them for many multi-party scenes. We introduce SORBET, a benchmark of 3,340 samples from 1,578 clips with synchronized speech, transcripts, and attended person labels, covering more multi-party scenes than existing gaze datasets...

---

### 20. LUTBench: Benchmarking Text-Driven Photographic Look Transfer

**Authors:** Chuanzhi Xu, Boyu Wei, Chengkun Yue, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23113v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23113v1)

**Summary:** Photographic color grading shapes the tone and color of a photograph to achieve a desired look. Text-driven photographic look transfer lets users specify these adjustments in natural language, with the goal of reproducing the requested look across photographs while preserving their content. However, prior research on text-driven color grading uses different datasets, text instructions, target definitions, and metrics. These differences make it difficult to compare how faithfully the methods repr...

---

### 21. Event-Based Dynamic Lip Region Estimation During Speech

**Authors:** Hamze Hammami, Omar Eldardeer, Francesco Rea

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23111v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23111v1)

**Summary:** Event cameras offer high temporal resolution and low power consumption, making them promising for speech-related applications. These include automatic lip reading, audiovisual speech analysis, and human-robot interaction, particularly in challenging environments characterized by low illumination or high dynamic range. Event-based lip reading, speaker recognition, and voice activity detection, however, mostly operate on a cropped region of interest (ROI), by hand or by the dataset, and no event-b...

---

### 22. FMT: Lossless Image Compression in a Fixed Number of Parallel Steps

**Authors:** Ammar Ali

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23108v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23108v1)

**Summary:** Learned lossless codecs make smaller files than common classical codecs, yet the images we archive and train on still use classical codecs. A main reason is time: a learned codec takes seconds to decode a photo that a classical codec opens in milliseconds, and their faster variants give up most of their gain in size. We argue that much of this time is spent waiting, not computing: the network waits for the values it conditions on, and the arithmetic decoder reads them one at a time. We introduce...

---

### 23. Event-Based Person Detection for Maritime UAV Search

**Authors:** Zijie Ning, Patrick Vandewalle

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23088v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23088v1)

**Summary:** Maritime search and rescue requires locating people in the water quickly, motivating the use of UAVs to survey the search area. During flight, camera motion and the longer exposures used in low light can blur small targets and hinder person detection. Event cameras record brightness changes as they occur, reducing the motion blur associated with longer exposure times. We investigate their use for maritime person detection by generating synthetic events using the v2e event simulator from public M...

---

### 24. Transfer Once, Ask Locally: Compact Audio-Visual Memory for On-Device Question Answering

**Authors:** Qitong Wang, Jihui Jin, Divya Kothandaraman, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23085v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23085v1)

**Summary:** Audio-visual question answering on lightweight user devices requires balancing speed, memory usage, privacy, and communication. One approach is to run audio-visual encoders on a server and a lightweight language decoder on the user device, keeping questions local while offloading media encoding. However, transferring and processing the full multimodal representation remains costly. We propose a training-free, query-agnostic token pruning framework that constructs a compact, reusable memory befor...

---

### 25. UnrealEvent: Synthetic Dataset Generation and Annotation for Event-Based Vision

**Authors:** Yentel Schoovaerts, Zijie Ning, Patrick Vandewalle

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23078v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23078v1)

**Summary:** Event-based cameras provide high temporal resolution, low power consumption, and a high dynamic range, but progress in event-based object detection remains constrained by the scarcity of annotated training data. To solve this issue, this paper introduces the tool UnrealEvent, a synthetic dataset-generation pipeline implemented in Unreal Engine 5.5. The pipeline combines a V2E-inspired event-frame generator with EasySynth semantic-rendering passes, allowing rendered level sequences to be converte...

---

### 26. RFW-S: Everyday Deformable Objects with Independent Simulation Verification

**Authors:** Jiarui Guo, Saining Zhang, Jiaying Wan, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23056v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23056v1)

**Summary:** Large-scale robotic simulation requires diverse deformable objects with executable physical properties and realistic interaction behaviors. However, existing 3D asset collections primarily emphasize visual diversity, while scalable physical construction and verification remain challenging. We introduce RFW-S, a large-scale dataset of 83,365 simulation-verified assets spanning 485 everyday categories across five structural families: soft solids, cloth sheets, shells, garments, and bags. We develo...

---

### 27. FrameRouter: Frame Budget Routing for Long-Video Understanding on Video-MME-v2 and Beyond

**Authors:** Bingjun Luo, Jialin Guo, Siqi Li

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23055v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23055v1)

**Summary:** Long-video question answering benchmarks like Video-MME-v2 typically evaluate systems under a uniform frame budget for every question, despite stark variation in the evidence each query actually demands. We analyze this mismatch on Video-MME-v2 and find that different question subsets prefer different frozen frame-budget policies, while uniformly increasing the frame count does not reliably improve all metrics. These findings motivate fixed-mean frame-budget routing, a controlled inference setti...

---

### 28. ReTouchGS: Ultralight Render-free Aesthetic Color Enhancement and Transfer for 3D Gaussian Splatting

**Authors:** Chuanzhi Xu, Boyu Wei, Chengkun Yue, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23054v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23054v1)

**Summary:** 3D Gaussian Splatting (3DGS) enables photorealistic scene reconstruction. Existing 3DGS color transfer and interactive editing methods are guided by reference images and user-specified color adjustments. However, in many applications, users simply want aesthetically guided color enhancement that automatically makes the scene more visually appealing while maintaining consistent colors and tones across viewpoints. We present ReTouchGS, to our knowledge the first framework for reference-free aesthe...

---

### 29. Refin3R: Geometry-Guided Refinement for Feed-Forward 3D Reconstruction

**Authors:** Jongmin Lee, Jaeyeong Kim, Seungryong Kim

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23051v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23051v1)

**Summary:** Feed-forward 3D reconstruction models predict dense point maps from multiple images in a single pass. Without explicit geometric constraints, however, their predictions are often inconsistent across views and lack fine-grained precision. Recent methods incorporate geometric priors such as camera pose or depth, but use them merely as auxiliary inputs, process each view independently, or refine the geometry only where the priors are available. We present Refin3R, which refines feed-forward point m...

---

### 30. Wall-to-wall maps of canopy height and aboveground carbon across the Atlantic Forest

**Authors:** Matheus Pinheiro Ferreira, Thiago Carmuega Rabaçal, Giulio Brossi Santoro, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23048v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23048v1)

**Summary:** Global canopy height maps are increasingly used to estimate forest carbon, yet their regional accuracy is rarely tested. We present wall-to-wall maps of canopy height (10~m) and aboveground carbon density (30~m) for the Brazilian Atlantic Forest in 2024. Height was predicted by a deep learning network fusing Sentinel-2 reflectance, Sentinel-1 and ALOS PALSAR backscatter and ALOS elevation, trained on 7{,}179 and tested on 1{,}793 patches (58{,}800~km$^2$) from a statewide airborne LiDAR campaign...

---

### 31. Uncovering the Invisible in Routine Radiology: Cross-Modal Detection of MRI-Verified Soft-Tissue Pathologies from CBCT via Physics-Guided 3D Self-Supervised Learning

**Authors:** Evgeny Alves Limarenko

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23042v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23042v1)

**Summary:** Routine X-ray modalities like cone-beam computed tomography (CBCT) are optimized for high-contrast mineralized tissues, leaving soft-tissue abnormalities buried beneath photon noise and below human visual perception. Thus, detecting non-calcified pathologies requires secondary magnetic resonance imaging (MRI). We demonstrate that sub-visual radiographic signatures of soft-tissue pathology are physically preserved within routine CBCT scans and can be extracted for opportunistic screening using a ...

---

### 32. When Anchors Shift the Target: Advantage-Gated Adaptation for Diffusion Reinforcement Learning

**Authors:** Pu Cao, Min Zhou, Ying Shu, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23038v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23038v1)

**Summary:** Forward-process reinforcement learning adapts diffusion and flow-matching models by re-noising rewarded generations into regression targets. Because negative advantages induce concave updates with unbounded repulsive gradients, existing methods stabilize training using cached predictions from a moving policy copy, yet these anchors also alter what positive feedback teaches the model to fit. We formalize this conflict as anchor coupling: after separating frozen-reference regularizers, affine movi...

---

### 33. Automated Annotation-Free Synthetic Data Generation for Underwater Litter Detection: A Comparison of Generative Approaches

**Authors:** Amala Mary Vincent, Bart De Schutter

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23037v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23037v1)

**Summary:** Underwater object detection is often limited by scarce and imbalanced training data and by strong appearance variations caused by turbidity, lighting, and differences between sensors. Existing data augmentation strategies, such as geometric or color augmentation or fully synthetic image generation with Generative Adversarial Networks (GANs), either lack semantic realism, fail to respect scene physics, or require additional annotations. In low-data domains like underwater environmental monitoring...

---

### 34. M3OPD-Reasoner: An Open Recipe for Post-Training Multimodal Reasoning with Multi-Teacher On-Policy Distillation

**Authors:** Nguyen Quang Trung, Hoang Phan, Shuo Sun, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23034v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23034v1)

**Summary:** Multi-Teacher On-Policy Distillation (MOPD) enables a single student to absorb the skills of several domain teachers by learning from its own generated responses. We present Multimodal Model Multi-Teacher On-Policy Distillation Reasoner (M3OPD-Reasoner), a fully open recipe for post-training vision-language models (VLMs) over three reasoning domains: image STEM, image perception, and video. We curate two datasets, M3OPD-SFT-1.35M for supervised fine-tuning (SFT) and M3OPD-RL-193K for reinforceme...

---

### 35. Check Your Blind Spots: Decision-Guided Perception by Probing the Planner with Hypothetical Objects

**Authors:** Hoang Pham Cong, Long D. Nguyen, Ho Viet Duc Luong, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23030v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23030v1)

**Summary:** Not every perception error changes the planner's action. Yet adaptive-resolution perception chooses where to spend high-resolution computation from image cues, which can neither reliably point to an object that low resolution missed nor tell which objects matter to the planner. We observe that the planner can say where an object would matter before anything is seen: inserting a hypothetical object at a location tests whether its action would change. Decision-Guided Speculative Perception (DGSP) ...

---

### 36. When a Larger Guidance Scale Repairs Text-to-Video Failures and When It Does Not

**Authors:** Taewon Kang, Matthias Zwicker

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23025v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23025v1)

**Summary:** When a text-to-video diffusion model ignores part of a prompt, the usual first fix is to raise the classifier-free guidance scale. This paper is a measurement study of when that fix works. On Mochi, the same increase repairs failures on rare compositions ("a snowy beach") beyond what generating again does, does not repair negations ("a highway with no vehicles"), where it fixes fewer failures than generating again does, and changes nothing for events that must happen late in a clip ("a sandcastl...

---

### 37. Tracking Ethological Behaviors of Broiler Chickens Through Computer Vision (YoloV11) Using an Android Mobile Device

**Authors:** Ryan Davi Oliveira de Meneses, Glauber da Rocha Balthazar

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23007v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23007v1)

**Summary:** This study developed and evaluated a computer vision model for automated ethological behavior classification of broiler chickens in climate-controlled poultry houses. Using publicly available videos preprocessed and manually annotated into three classes (sitting, standing, and feeding), the YOLOv11 model was trained and deployed on an Android application via TFLite conversion. Exploratory analysis ensured dataset consistency and visual quality, while evaluation showed class-dependent performance...

---

### 38. The Rhythm of Generated Video: Latent Chunking Leaves Periodic Traces in Compressed Bitstreams

**Authors:** Chen Ye Gan, Bryan Zhen Zhang, Gene Wen, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22996v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22996v1)

**Summary:** Most AI-generated video detectors analyze decoded pixels and overlook how videos are produced. We show that causal video autoencoders leave an architecture-specific rhythm in compressed bitstreams: their temporal stride concentrates unpredictable content at latent-chunk boundaries, so rate-distortion optimized encoders allocate bits periodically. Without decoding pixels, we observe four-frame pulses in CogVideoX and Wan2.2 and eight-frame pulses in LTX-Video, which are absent from content-matche...

---

### 39. CAST: Calibrating Correspondences for Training-Free Biomedical In-Context Segmentation

**Authors:** Mingze Jiang, Jiashu Han, Haonan Chen, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22995v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22995v1)

**Summary:** Biomedical image segmentation must keep up with new anatomical structures, subjects, imaging modalities, and acquisition protocols, yet dense expert annotations are scarce and models trained on one cohort often struggle to transfer. In-context segmentation (ICS) offers a way out: a new structure is specified by a few annotated exemplars at inference time. However, reliable correspondence remains challenging in biomedical images, where adjacent structures often share similar appearances, and vari...

---

### 40. SpikWM: Efficient End-to-End Spiking World Modeling for Visual Planning

**Authors:** Shuhan Ye, Hongbin Yu, Chong Wang, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22981v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22981v1)

**Summary:** Goal-conditioned planning with image observations and goals requires predictions that distinguish visual states and action consequences. Spiking neural networks offer sparse computation, but single-step spikes can obscure motion cues and merge actions with different physical outcomes. We propose the Spiking Latent World Model (SpikWM), an end-to-end joint-embedding predictive architecture (JEPA) with one simulation step per image and one neural update per latent position. Spiking Regional Encodi...

---

### 41. Rescaling OLS-Merged Adapters To Improve Personalized Image Generation

**Authors:** Leander Girrbach, Niklas Schweiger, Zeynep Akata

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22969v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22969v1)

**Summary:** Merging multiple adapters into a single image generation model reduces deployment costs while preserving diverse task capabilities or personalization modes. State-of-the-art methods such as RegMean, Mix-of-Show, and Subspace Routing fit the outputs of the merged model to those of the individual adapters using ordinary least squares (OLS). We show that this reconstruction objective systematically shrinks task-specific signals whenever the activation distributions of different tasks overlap, produ...

---

### 42. MI-Hyper: Generating Multiple Instance Models for Weight Space Transfer Learning in Histopathology via Mixed Tasks Pretrained HyperNetwork

**Authors:** Xitong Ling, Yousef Kotp, Weiming Chen, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22968v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22968v1)

**Summary:** Zero-shot whole-slide image (WSI) prediction aims to generalize to new pathology tasks without parameter updates at deployment. MI-Zero makes these predictions by pooling patch-text similarities. Conditional weight generation, combined with supervision from diverse pathology tasks, offers an alternative: learning to construct predictive rules from task descriptions. We introduce MI-Hyper, a hypernetwork pretrained across mixed tasks to generate the aggregation and classification weights of multi...

---

### 43. CodeReel: Accelerating Code-to-Video Agents with Exact Frame Reuse and Blocking-Aware Scheduling

**Authors:** Junyi Shen, Yao Lu

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22967v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22967v1)

**Summary:** Coding agents make videos by writing and refining programs in a build--inspect--edit loop. A finished film costs a median of $2.85 in model calls and 11 minutes, over a third of that time in builds that block the agent. We find that much of this time is avoidable, for two reasons. First, 37.5% of the frames of a session's later films were drawn before, many shifted in time or inside an edited scene. Second, half of the builds stop at a check, where the agent needs only the verdict, but which bui...

---

### 44. Training-Free Building Change Detection with Example-Induced Discriminants

**Authors:** Zhi Lu, Bin Hong, Zhenming Peng

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22964v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22964v1)

**Summary:** Building change detection (BCD) relies on dense annotations that are costly to collect across regions. A few annotated examples offer a more economical way to specify the target, but change maps provide incomplete building supervision: they label only changed buildings and leave the building-containing date unspecified. Our key observation is that these annotations nevertheless reveal features that recognize buildings in other images, including unchanged ones. We present Linear INduced Discrimin...

---

### 45. Hierarchical Diffusion Transformer for End-to-End Image Generation

**Authors:** Xiaoyu Wu, Yifei Wang, Weihang Guo, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22962v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22962v1)

**Summary:** Pixel-space diffusion learns visual representations and image generation jointly in a single end-to-end training stage, without a separately pretrained visual encoder. However, plain pixel-space Transformers still trail leading two-stage latent diffusion models in generation quality and training efficiency. We hypothesize that part of this gap arises from retaining one token per patch throughout the backbone, which does not explicitly encourage a visual hierarchy that summarizes related content ...

---

### 46. Is model self-assessment enough for diverse LVLM ensembles?

**Authors:** Michael Smith, Frank P. Ferrie

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22956v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22956v1)

**Summary:** Ensembles of diverse Large Vision Language Models have demonstrated performance beyond that of single models across multiple datasets and tasks. However, the necessary aggregation process usually relies on training, parameter fitting, or complex task-specific pipelines. Furthermore, evaluation is limited, making a fair comparison difficult. We create a unified pipeline where we perform candidate response selection: we build an ensemble by selecting the best answer from a set provided by differen...

---

### 47. Fiberpose: state-of-the-art fiber morphometry and instance segmentation with a distance-transform neural network

**Authors:** Viktor A. Balashov, Daniil S. Antonenko

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22953v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22953v1)

**Summary:** Analysis of fibrous structures in SEM images is a routine task in biomedical engineering and materials science. However, most available methods for fiber quantification still rely on classical image binarization followed by simple post-processing. These approaches often produce unreliable results in images with weak boundaries, heterogeneous contrast, and densely packed fibers. Here, we introduce Fiberpose, a framework that reformulates fiber analysis as direct regression of a smooth distance-tr...

---

### 48. A high-dimensional spatial-physical coupling operator for generalizable super-resolution of three-dimensional turbulent flows

**Authors:** Zengyuan Zuo, Junjun Jiang, Fei Mu, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22951v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22951v1)

**Summary:** Accurate representation of turbulent flows requires simultaneously capturing multi-scale spatial structures and the complex, nonlinear coupling between distinct physical quantities (\textit{e.g.}, velocity components and density). In practice, however, turbulent data are often constrained by low spatial resolution due to hardware limitations and computational costs. While current data-driven super-resolution methods have shown promise by learning mappings via convolutional neural networks (CNNs)...

---

### 49. Code World Model 2.0: Towards Infinite Controllable Video Generation

**Authors:** Ruoyu Wang, Hao Zhong, Yanming Yang, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22925v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22925v1)

**Summary:** Visual proxies decouple explicit world-state simulation from photorealistic video synthesis, offering a controllable interface for both offline clip creation and real-time interactive streaming. Yet a practical renderer must address two challenges. Upstream proxies vary from coarse layouts to fine articulated geometry depending on the interaction, and streaming inference must operate in a few causal steps without accumulating drift across self-generated history. We present Invoker-Render, pairin...

---

### 50. SWIR-cGAN: Synthesizing SWIR Bands Using VNIR Imagery from CBERS and AMAZONIA-1

**Authors:** Alisson Cleiton de Oliveira, Rennan de Freitas Bezerra Marujo, Thales Sehn Körting

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22922v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22922v1)

**Summary:** Spectral band synthesis is an important research topic in remote sensing. The Brazilian satellites CBERS-4, CBERS-4A, and AMAZONIA-1 provide high temporal resolution (1-3 days) visible and near-infrared (VNIR) imagery through the Wide-Field Imager (WFI), but lack short-wave infrared (SWIR) bands. Recent deep learning methods have shown promising results for spectral synthesis, but challenges remain for cross-satellite generalization and spectrally distant bands. This paper presents a conditional...

---

## cs.LG

**50 papers**

### 1. Ambient LLMs: Data-Efficient Supervised Fine-tuning via Temperature Matching

**Authors:** Giannis Daras, Marios Papachristou, Adam Klivans, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23229v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23229v1)

**Summary:** Collecting large-scale, diverse, and high-quality post-training datasets for autoregressive language models is challenging. Consequently, Supervised Fine-Tuning (SFT) is typically applied to datasets significantly smaller than those used for pre-training, which leads to overfitting and the catastrophic forgetting of the tails of the data distribution. To prevent this collapse, we introduce Ambient SFT, a principled framework for leveraging imperfect predictions to augment the fine-tuning set. In...

---

### 2. Spool: Low-Latency Streaming Inference for Hybrid Vision-Language Models

**Authors:** Rui Ning, Om Chabra, Hari Balakrishnan

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23228v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23228v1)

**Summary:** Applications such as visual accessibility agents and robotics require answering questions about recent video content promptly, over a bounded window of past frames (e.g., the last two minutes). Hybrid vision-language models (VLMs), which interleave attention with linear recurrent layers such as Gated DeltaNet (GDN), are attractive for this setting, but maintaining a sliding window is expensive. The reason is that recurrent layers combine all past frames into a shared state, so expiring old frame...

---

### 3. An inexact stochastic variance-reduced gradient method for constrained convex finite-sum optimization

**Authors:** Zhaosong Lu, Yifeng Xiao

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23221v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23221v1)

**Summary:** In this paper, we study a class of constrained convex finite-sum optimization problems. In many practical applications, all or some of the constraints are hard constraints that represent imperative requirements. Consequently, any desirable approximate solution must (nearly) satisfy these constraints. Motivated by this, we focus on computing an $ε$-$surely\ feasible\ stochastic\ optimal$ ($ε$-SFSO) solution, in which the constraint violation is deterministically bounded by $ε$, and the expected o...

---

### 4. Do LLM Agents Still Need to Be Told How to Self-Improve?

**Authors:** Shobhita Sundaram, Cansu Sancaktar, Phillip Isola

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23219v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23219v1)

**Summary:** LLM agents increasingly drive their own learning. Self-improvement methods delegate various components of model optimization to the models themselves. As models become more capable, this motivates a basic question: do these increasingly capable models still need us to specify how they should self-improve? In this paper we study an autonomous paradigm in which, given basic primitives, resources, and a general goal for self-improvement, agents construct their own self-learning algorithm for contex...

---

### 5. What Does a Bias Head Measure? Non-Identifiability in Head-Level Bias Attribution

**Authors:** S. M Seefat Alam

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23218v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23218v1)

**Summary:** Methods that localise social bias in large language models to individual attention heads and remove it by ablation are validated by their effect on a fairness metric, never by evidence that the statistic selecting the heads measures bias. We audit this on Qwen-2.5-7B-Instruct and Llama-3.1-8B-Instruct. The head map correlates at $ρ= -0.950$ and $-0.768$ with a label-blind response-length map, apparently identifying a surface confound. An intervention that breaks the length-label coupling rejects...

---

### 6. Higher-Scoring Coding Models Did Not Get More Work Done

**Authors:** Yining Hua

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23216v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23216v1)

**Summary:** New coding models advertise themselves on score improvements of coding benchmarks. Yet no study has tested if a model that scores higher on these benchmarks gets more real work done. On June 12, 2026, a U.S. export control directive banned access to Claude Fable 5 for 19 days, which forced users to switch to other models. During this time, most former Fable 5 users switched to Opus 4.8 (11 points lower on SWE-Bench Pro compared to Fable 5). We treat this suspension as a natural experiment, where...

---

### 7. Multimodal Masked Diffusion Autoencoder for Modeling Impaired Driving

**Authors:** John Gideon, Anshul Gupta, Megan Applegate-Kenton, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23211v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23211v1)

**Summary:** Human cognitive state (e.g., distraction, stress), gaze, and behavior interact with the driving environment in subtle ways that AI could use to assist drivers, but ground-truth labels for human cognitive state levels are costly to obtain at scale. We propose a multimodal masked-diffusion autoencoder, ID-MAE, that adds a self-supervised objective to impairment prediction: alongside predicting the impairment label as a masked token, it reconstructs masked gaze and trajectory. To probe the effects ...

---

### 8. Distortion-Free Semantic Watermarks for Black-Box Generative Models

**Authors:** Aviv Yossef, Or Patashnik, Or Zamir

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23208v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23208v1)

**Summary:** We present a provably distortion-free semantic watermarking algorithm that requires only black-box sampling access to a generative model and black-box access to a semantic embedding. A watermark is called distortion-free if, averaged over its secret detection key, it leaves the generator's output distribution unchanged; this provides a formal guarantee that watermarking does not reduce output quality. Conventional such watermarks are often brittle to transformations. This is especially problemat...

---

### 9. Fine-Tuning Gemma 4 Edge Models for MATLAB Signal-Processing Code with SFT and QLoRA on a Laptop iGPU

**Authors:** Mehmet Altan Toksöz

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23205v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23205v1)

**Summary:** Small language models that run on a laptop are attractive for writing signal-processing code offline, but they make systematic errors on digital signal processing (DSP) conventions. We apply supervised fine-tuning (SFT) to the Gemma 4 edge models E2B and E4B with 66 checked examples covering 11 signal-processing MATLAB subtasks, using low-rank adaptation (LoRA) and quantized LoRA (QLoRA) on the integrated GPU (iGPU) of a laptop, and deploy the 8-bit integer (int8) models with the adapters throug...

---

### 10. Learned versus Kinematic Trajectory Prediction under Reduced Observation Frequency

**Authors:** Nukhbala Gadzhiev, Alexander Morochko

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23198v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23198v1)

**Summary:** Trajectory prediction models for automated driving are usually trained on data with a fixed sampling frequency, while positions received via vehicle-to-everything (V2X) communication arrive at 1-10 Hz. We study whether a learned predictor that uses only the observation history keeps its advantage over constant velocity (CV) and constant acceleration (CA) models when the history frequency drops. On the Argoverse 2 motion forecasting dataset, the 5 s history of the focal agent was downsampled from...

---

### 11. WoRD: Diffusion-Based Posterior Inference for Online Goal Recognition

**Authors:** Almog Anschel, Sarah Keren

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23192v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23192v1)

**Summary:** Goal recognition is the task of inferring an agent's intended goal from its observed behavior. Most existing work focuses on high-level symbolic recognition, abstracting away the continuous motion through which agents reach their goal. Methods that do reason over continuous trajectories rely on an explicit dynamics model that is hard to acquire and rarely transfers across settings. Neither approach explicitly learns how agents move toward each candidate goal, limiting accuracy on ambiguous traje...

---

### 12. Déjà View: A Shared Working-Memory Model for Visual Tasks

**Authors:** Mranmay Shetty, Gabriel Kreiman

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23177v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23177v1)

**Summary:** A working-memory model must remember stimuli and use its memory flexibly to perform different tasks. Here we introduce a model of working memory for images that combines dynamic activity with temporary associations between image features. We train the model on five tasks, including remembering a sample while other images are presented, categorizing distractor images while remembering the sample, and determining whether an image is new or has been presented before. The same trained model performs...

---

### 13. MoE--LoRA Methods for Multilingual Adaptation: A Systematic Empirical Study

**Authors:** Nikit Srivastava, Joel Dag, René Speck, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23158v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23158v1)

**Summary:** Routed low-rank adapters offer a parameter-efficient means to improve the performance of large language models (LLMs) across tasks. Hence, it is assumed that they can also be used to improve the support of low-resource languages in LLMs, which currently serve English far better than the thousands of other languages spoken worldwide. However, this assumption has never been verified empirically under a shared multilingual evaluation protocol. We address exactly this gap by comparing eight low-rank...

---

### 14. Learning Stratified Policies for Inference-Time Objectives

**Authors:** Mridul Mahajan, Xuezhou Zhang, Aldo Pacchiano

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23154v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23154v1)

**Summary:** Inference-time scaling improves the performance of large language models by sampling multiple responses and evaluating their collective utility. However, many existing approaches obtain these samples by repeatedly sampling from a single policy. In this work, we study if the sample budget at inference time can instead be allocated across a population of policies. We introduce stratified policies, where each of $k$ learned policies contributes one response to a $k$-sample inference-time objective....

---

### 15. Capability Composition in Heterogeneous Teams via Barrier-Guided Diffusion Sampling

**Authors:** Diana Laura Morales, Ruoyu Lin, Magnus Egerstedt, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23149v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23149v1)

**Summary:** The agents in a heterogeneous team can cooperate to accomplish tasks that exceed their individual capabilities. The team trajectories for a cooperative task can be generated by a generative model, provided that the model has been trained on demonstrations of the agents cooperating. Yet, demonstrations of cooperation are costly and may not exist for tasks that the team has never performed. The conditions under which the agents can combine their capabilities, however, are physical properties of th...

---

### 16. RSI-Prime: Training Models to Train Models

**Authors:** Dewu Zheng, Yang Ye, Hongyu Zhang, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23138v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23138v1)

**Summary:** Enabling large language models (LLMs) to autonomously conduct training and improve target models is an important foundation for recursive self-improvement (RSI). As LLMs expand their role from being trained to conducting training, their model-training capability warrants dedicated study and systematic development. To this end, we construct RSI-Prime, a dataset for improving model-training capability, comprising 350 complete experimental trajectories across seven task categories. To help LLMs lea...

---

### 17. Correcting Flows with Marginal Matching

**Authors:** Meital Bojan, Nadav Bojan Sellam, Ev Zisselman, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23134v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23134v1)

**Summary:** Flow matching models, ODE-based generative models, generate samples by gradually morphing a simple source distribution into a target distribution. However, these models still face challenges in optimally balancing computational efficiency with generation fidelity. While predictor-corrector schemes have been proven to help address this issue in diffusion models effectively, their application to flow matching models remains under-explored. In this work we present a novel training-based predictor-c...

---

### 18. A Neural Envelope Method for Rapid Gradient-based Optimum Takeoff Trajectory Design

**Authors:** Samuel Sisk, Xiaosong Du

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23130v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23130v1)

**Summary:** Urban air mobility arises to mitigate ground traffic congestion. Multidisciplinary analysis and optimization (MDAO) has been introduced to reduce the energy consumption, thereby expanding aircraft performance. Surrogate-based MDAO lowers the cost of optimization, but multimodality disrupts global optimum search for both simulation-based and surrogate-based optimizations. Convex envelopes convert multimodal spaces into unimodal spaces, permitting efficient convex optimization; however, convexifyi...

---

### 19. Where Should Physics Enter? Information, Identifiability and Calibration in Probabilistic Sea Surface Temperature Forecasting

**Authors:** Parmitha Vangapandu, Jonnakuti Pavan Kumar, Sathwik Narkedimilli, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23129v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23129v1)

**Summary:** Advection-diffusion priors are a common way to make neural sea surface temperature (SST) forecasts physics-informed. We test where such a prior must enter a heteroscedastic ConvLSTM to help, using daily NOAA OISST v2.1 for the Bay of Bengal (1982-2024) and a synthetic benchmark on the same grid with known currents of controlled strength. (i) On real data, a soft advection-diffusion residual with a learned velocity gives no reliable benefit (lead-15 CRPS -0.007 degrees C, 95% interval [-0.022, +0...

---

### 20. The Illusion of Grounding: Do Vision-Language Models Weigh Retrieved Text and Images Like an Ideal Observer?

**Authors:** Basavaraj R M, Harshal Chandel

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23127v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23127v1)

**Summary:** Retrieval-augmented vision-language models (VLMs) answer from two sources of evidence that can each fail: the retrieved text can be wrong or noisy, and the image can be degraded or contradicted. We introduce GIB-200K, 200,000 image-question items built from COCO and Visual Genome, each expanded into controlled stress conditions: hard-negative retrieval noise (1-20 documents), visual ambiguity (Gaussian and motion blur, low-resource crops) and cross-modal conflict with counterfactual flip pairs. ...

---

### 21. Which Past Matters? Training History and Multi-Forecast Horizon in Equity Transformers

**Authors:** Chariton Chalvatzis

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23126v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23126v1)

**Summary:** More historical data can improve estimation while introducing relationships that transfer poorly to current market conditions. We therefore examine how training quantity and historical selection interact with forecast horizon in intraday equity prediction. We deploy twelve configurations which combine four sampling and validation policies with 6, 12 and 24 month training quantities under a fixed cross-sectional Transformer and feature set. A monthly walk-forward experiment produces 264 refits an...

---

### 22. Get Hint-Augmented GRPO Done Right Through Activation Steering

**Authors:** Khiem Le, Ting Hua, Nitesh V. Chawla

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23124v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23124v1)

**Summary:** GRPO has become the dominant reinforcement learning method for eliciting reasoning capability in LLMs using verifiable rewards. However, it suffers from a fundamental failure mode: when a training question exceeds the base model's current capability, all generated responses fail and receive zero reward, yielding no gradient signal and stalling further capability expansion. An emerging class of GRPO extensions, termed Hint-Augmented GRPO (HA-GRPO), adds a "hint" to the context to reduce the diffi...

---

### 23. Auditing a Learned Simulator for Legged Robots: The Robotic World Model on ANYmal D

**Authors:** Joyjeet Singh

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23118v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23118v1)

**Summary:** A legged robot can learn to walk inside a learned simulator: a neural network that predicts the robot's next state and is run forward on its own predictions. They are usually trained and checked one step ahead, although a policy uses them for a hundred steps or more. We audit one published system end to end, without a GPU: the dynamics model of the Robotic World Model (RWM) for the ANYmal D quadruped, and the uncertainty estimate of its follow-up, RWM-U. We rebuilt the model to match the release...

---

### 24. Large-scale Neuron Community Discovery Reveals Neuron-Sparse Behaviors in Language Models

**Authors:** Igor Shilov, Thomas Fel, Tal Haklay, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23112v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23112v1)

**Summary:** What reusable units of computation can we discover within a language model's neurons? Prior work has shown that individual forward passes can often be sparsified post-hoc to small groups of neurons, but it has been unclear whether these groups form coherent computational entities reused across inputs. We introduce neuron community discovery, an unsupervised method for finding neuron groups that recur across prompts and are causally necessary and sufficient, within the layers they span, for commo...

---

### 25. Event-Based Dynamic Lip Region Estimation During Speech

**Authors:** Hamze Hammami, Omar Eldardeer, Francesco Rea

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23111v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23111v1)

**Summary:** Event cameras offer high temporal resolution and low power consumption, making them promising for speech-related applications. These include automatic lip reading, audiovisual speech analysis, and human-robot interaction, particularly in challenging environments characterized by low illumination or high dynamic range. Event-based lip reading, speaker recognition, and voice activity detection, however, mostly operate on a cropped region of interest (ROI), by hand or by the dataset, and no event-b...

---

### 26. What's in a Tree ? Hierarchical $n$-gram models as controlled approximators of language

**Authors:** Aritra Das, Francesco Cagnetta, Darshil Doshi, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23093v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23093v1)

**Summary:** Hierarchical models have been proposed as synthetic settings for studying language. However, their relevance to realistic language corpora remains underexplored. In this work, we introduce tree-grams, autoregressive generative $n$-gram models that build the conditional probability tensor $p(x_n \mid x_{1:n-1})$ through a hierarchical composition of order-2 and order-3 tensors. $n$ controls the maximal context window, whereas a rank hyperparameter $d$ controls model capacity, yielding an interpre...

---

### 27. Learning to Undo: Transfer Reinforcement Learning under State Space Transformations

**Authors:** Mridul Mahajan, Aldo Pacchiano, Xuezhou Zhang

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23081v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23081v1)

**Summary:** Transfer learning in reinforcement learning (RL) has shown strong empirical success. In this work, we take a more principled perspective by studying when and how transferring knowledge between MDPs (a source and a target) can be provably beneficial. Specifically, we consider the case where there exists an undo map such that applying this map to the target's state space recovers the source exactly. We propose an algorithm that learns this map by matching state feature statistics gathered from bot...

---

### 28. Pareto-Informed Smart "Predict, then Optimize" for Multi-Objective Combinatorial Problems

**Authors:** Aabhash Dhakal, Tim Lachner

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23076v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23076v1)

**Summary:** Many real-world planning applications, from logistics, routing to resource allocation, give rise to optimization problems that need to balance multiple, conflicting objectives. While machine learning is often used to predict the unknown parameters or costs of these problems, standard models trained on prediction accuracy can lead to suboptimal plans. Decision-Focused Learning (DFL) addresses this by integrating the downstream optimization task into the training objective. However, existing DFL m...

---

### 29. Runtime Verification of Multiple Natural Language Criteria for Agent Governance

**Authors:** Silviu Pitis, Parand A. Alamdari, Jessica Tang, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23074v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23074v1)

**Summary:** AI agents are governed by hundreds of natural language criteria, yet existing verifiers cannot efficiently evaluate an agent's output against a large set of such criteria and report which are satisfied, violated, or inapplicable. We introduce the VFM, a tree-attention verifier that encodes the shared context and target text, and scores N natural language criteria in parallel, returning independent per-criterion ternary verdicts. The VFM is pretrained on CriteriaBank, a corpus of 394K (context, t...

---

### 30. Amortizing Tempered Sampling with Corrected Self-Training

**Authors:** Hoang-Viet Nguyen, Hai-Dang Dau, Alexandre H. Thiéry

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23072v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23072v1)

**Summary:** Learning a neural sampler can reduce the cost of repeated sampling from an un-normalized distribution, but obtaining good training data remains difficult. We develop a corrected self-training scheme across a sequence of tempered targets, making use of importance sampling and Markov chain Monte Carlo to correct the samples and replay buffers to store them. We introduce Sequential Score Sampler (SSS) as a particular case. In SSS, the proposal is a score-based diffusion trained by regression on ene...

---

### 31. FrameRouter: Frame Budget Routing for Long-Video Understanding on Video-MME-v2 and Beyond

**Authors:** Bingjun Luo, Jialin Guo, Siqi Li

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23055v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23055v1)

**Summary:** Long-video question answering benchmarks like Video-MME-v2 typically evaluate systems under a uniform frame budget for every question, despite stark variation in the evidence each query actually demands. We analyze this mismatch on Video-MME-v2 and find that different question subsets prefer different frozen frame-budget policies, while uniformly increasing the frame count does not reliably improve all metrics. These findings motivate fixed-mean frame-budget routing, a controlled inference setti...

---

### 32. Magflow: Differentiable Simulation of Industrial-Grade 6D Magnetic Levitation

**Authors:** Philipp Hartmann, Jannick Stranghöner, Klaus Neumann

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23050v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23050v1)

**Summary:** Magnetic levitation with six-degrees-of-freedom enables frictionless transport and micrometer-scale positioning in principle, but low-level control is inherently challenging due to its complex and unstable dynamics. Industrial systems typically rely on deep hardware-software co-design, where mover and stator geometries are jointly designed to enable a compact, hand-crafted approximation of the electromagnetic force computation, thereby keeping control computationally tractable at kilohertz rates...

---

### 33. Reversing the text is not reversing the path: a fixed-text measure without a zero, and an assembly-order comparison that vanishes identically

**Authors:** Y. -H. Taguchi

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23049v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23049v1)

**Summary:** For an ensemble of trajectories the fluctuation theorems give the entropy production its meaning and zero. The same expression has recently been evaluated on one fixed text, $Δ= [\log P(x) - \log P(\tilde x)]/L$ with $\tilde x$ the text in reversed order, read as an entropy production separating causally from arbitrarily ordered prose. A single text is neither a distribution nor a dynamics, and the texts at issue were produced by other models. No theorem fixes where the zero of a fixed-text quan...

---

### 34. Uncovering the Invisible in Routine Radiology: Cross-Modal Detection of MRI-Verified Soft-Tissue Pathologies from CBCT via Physics-Guided 3D Self-Supervised Learning

**Authors:** Evgeny Alves Limarenko

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23042v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23042v1)

**Summary:** Routine X-ray modalities like cone-beam computed tomography (CBCT) are optimized for high-contrast mineralized tissues, leaving soft-tissue abnormalities buried beneath photon noise and below human visual perception. Thus, detecting non-calcified pathologies requires secondary magnetic resonance imaging (MRI). We demonstrate that sub-visual radiographic signatures of soft-tissue pathology are physically preserved within routine CBCT scans and can be extracted for opportunistic screening using a ...

---

### 35. Variance Restoration over Covariance Rank: Memory-Budgeted Analytic Continual Learning

**Authors:** Elena Voss, Pixel Nomand, Marcus Hale, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23040v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23040v1)

**Summary:** Analytic continual learning replaces iterative gradient updates with closed-form ridge regression over frozen pre-trained representations, summarizing all past sessions in two running sufficient statistics: the feature autocorrelation matrix $Σ_t$ and the class cross-correlation matrix $Γ_t$. Lifting backbone features into a wide random code of dimension $M \gg D$ substantially improves linear separability across tasks, but forces $Σ_t$ to grow quadratically as $\mathcal{O}(M^2)$. Under a fixed ...

---

### 36. When Anchors Shift the Target: Advantage-Gated Adaptation for Diffusion Reinforcement Learning

**Authors:** Pu Cao, Min Zhou, Ying Shu, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23038v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23038v1)

**Summary:** Forward-process reinforcement learning adapts diffusion and flow-matching models by re-noising rewarded generations into regression targets. Because negative advantages induce concave updates with unbounded repulsive gradients, existing methods stabilize training using cached predictions from a moving policy copy, yet these anchors also alter what positive feedback teaches the model to fit. We formalize this conflict as anchor coupling: after separating frozen-reference regularizers, affine movi...

---

### 37. Storing the Gemma 4 K=V Cache Once: Exact Global-KV Memory Savings in a Paged Serving Engine with Unchanged Attention Kernels

**Authors:** Kushagra Bainsla

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23035v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23035v1)

**Summary:** In the global attention layers of Gemma 4 31B, the value is the normalized key projection, and the key is the value scaled by a fixed weight, with rotary position encoding on one quarter of its dimensions. The Gemma 4 report states that this design reduces the global KV cache by up to 37.5%, but the open serving engines that we checked still store a full key and a full value: 1,024 values per KV head and token. We store one 640-value row instead, exact in real arithmetic, and an unchanged paged ...

---

### 38. NVIDIA Kumo Tabular: Pushing the Accuracy-Efficiency Frontier for Tabular Prediction

**Authors:** Jingang Qu, Valter Hudovernik, Martin Jurkovič, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23001v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23001v1)

**Summary:** We introduce Kumo Tabular, a family of open tabular foundation models for classification and regression, in three sizes: Kumo Tabular-S (27M parameters), Kumo Tabular-M (61M), and Kumo Tabular-L (214M). Pretrained only on artificial tables from the Kumo prior, they can make predictions on new tables without any training. In our approach, a table encoder compresses each row into an embedding, and an in-context learning transformer predicts the unlabeled rows from the labeled ones. Kumo Tabular in...

---

### 39. Residual-Guided Lightweight Reinforcement Learning for Risk-Aware Trajectory Selection with a Frozen World Model

**Authors:** Jiaqi Wu, Yongqi Dong, Yijie Zhong, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22998v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22998v1)

**Summary:** In automated driving, world models provide future scene predictions for evaluating candidate trajectories, but fixed selection rules may not capture scene-dependent trade-offs. We propose a residual-guided reinforcement learning (RL) framework for lightweight trajectory selection with a frozen world model and a fixed candidate bank. The framework uses proximal policy optimization (PPO) to fine-tune a joint policy over candidate selection and bounded trajectory residuals. A context-conditioned ra...

---

### 40. High-Dimensional Black-Box Optimization via Guidance Sampling of Diffusion Models

**Authors:** Xiaoyan Hu, Rohit Sonker, Jalal Butt, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22965v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22965v1)

**Summary:** Many real-world optimization problems involve optimizing black-box objectives for which only a limited number of evaluations are available. Bayesian optimization (BO) is a powerful framework for such problems, but its effectiveness often deteriorates in high-dimensional spaces. Recent work leverages diffusion models for black-box optimization, often through pre-training a reward-conditioned score network to steer generation towards high-reward samples. Alternatively, gradient-based guidance meth...

---

### 41. Hierarchical Diffusion Transformer for End-to-End Image Generation

**Authors:** Xiaoyu Wu, Yifei Wang, Weihang Guo, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22962v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22962v1)

**Summary:** Pixel-space diffusion learns visual representations and image generation jointly in a single end-to-end training stage, without a separately pretrained visual encoder. However, plain pixel-space Transformers still trail leading two-stage latent diffusion models in generation quality and training efficiency. We hypothesize that part of this gap arises from retaining one token per patch throughout the backbone, which does not explicitly encourage a visual hierarchy that summarizes related content ...

---

### 42. DDSL: Iterative Self-Labeling for Financial Market States

**Authors:** Xianbin Gu, Qingyue Zhu, Yuhong Geng

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22958v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22958v1)

**Summary:** Financial market states lack a unique ground truth and must therefore be constructed from price data. Conventional labeling methods typically define states independently of the downstream classifier, leaving unresolved whether the resulting labels can be recovered from information available at prediction time. We propose DDSL, an iterative self-labeling framework that couples a price- and grammar-guided Viterbi labeler with a Transformer classifier through model feedback. DDSL constructs a nine-...

---

### 43. Is model self-assessment enough for diverse LVLM ensembles?

**Authors:** Michael Smith, Frank P. Ferrie

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22956v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22956v1)

**Summary:** Ensembles of diverse Large Vision Language Models have demonstrated performance beyond that of single models across multiple datasets and tasks. However, the necessary aggregation process usually relies on training, parameter fitting, or complex task-specific pipelines. Furthermore, evaluation is limited, making a fair comparison difficult. We create a unified pipeline where we perform candidate response selection: we build an ensemble by selecting the best answer from a set provided by differen...

---

### 44. ResoLUT: Distilling Residual Networks into Lookup-Table Networks

**Authors:** Katarzyna Fojcik, Aidas Mikalauskas, Matthias Kampa, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22955v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22955v1)

**Summary:** Logic networks built from Boolean gates or lookup tables (LUTs) promise efficient hardware inference, but training them at depth and learning their connectivity remain difficult. We do not train logic as logic. Instead, ResoLUT distills a trained residual network (ResNet) layer by layer into LUT trees, preserving its multi-bit residual stream and BatchNorm while extracting connectivity from the teacher rather than learning it. To our knowledge, ResoLUT is the first convolutional logic network in...

---

### 45. Symmetries of Counterfactuals: Identification and Testability of Counterfactual Maps from Covariate Heterogeneity

**Authors:** Marc Braun, Adel Daoud, Jose M. Peña

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22948v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22948v1)

**Summary:** In general, counterfactuals are not identified from data alone, because many causal models produce the same observed distributions but different counterfactuals. A common approach to circumvent this problem is to restrict the mechanism to a class in which it becomes unique, such as triangular monotone maps or optimal transport maps. However, whether the assumed class is correct is usually not examined. In this work, we study what the data can tell us when covariates are available that influence ...

---

### 46. The Kernel Reality Check: Benchmarking and Distilling Efficient Attention at Scale

**Authors:** Fırat Öncel, Cem Subakan, Mirco Ravanelli, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22947v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22947v1)

**Summary:** Kernelized attention methods, which aim to replace the $O(N^2)$ complexity of softmax attention with $O(N)$ alternatives, have been the focus of intense research in the last five years. Despite growing interest, systematic evaluations and fair comparisons across approaches and scales are still missing. We analyze kernelized attention in two halves and highlight prominent limitations on each. On efficiency, FlashAttention achieves lower memory consumption and faster wall-clock time than SOTA kern...

---

### 47. A Transformer-Derived Iterative Preconditioner

**Authors:** Patrick Lutz, Themistoklis Haris, Aditya Gangrade, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22941v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22941v1)

**Summary:** Transformers trained on in-context prediction problems can learn known numerical algorithms, e.g., gradient descent. We go further, showing that their internal computations can reveal new algorithms with provable guarantees. A softmax-attention transformer trained to solve linear systems $Xw=y$ implicitly improves matrix conditioning. Tracing $XX^\top$ reveals an iterative preconditioning primitive, which we develop into RAPID, a standalone algorithm requiring no learned components.   RAPID is a...

---

### 48. Projected Penalty-Gradient Tracking for Communication-Efficient Byzantine-Resilient Federated Learning

**Authors:** Yanjie Dong

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22929v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22929v1)

**Summary:** We investigate communication-efficient federated learning over heterogeneous datasets in the presence of Byzantine adversaries capable of uploading arbitrary information. Penalty-based methods bound the influence of each worker through the bounded gradient of a penalty function; however, the bound is lost once the uploads are compressed, since a Byzantine worker can accumulate an unbounded state at the server. To retain the Byzantine resilience under compressed uploads, we propose a projected pe...

---

### 49. Action-outcome coupling: a pre-investment feasibility audit for offline reinforcement learning in supply chain operations

**Authors:** Tung Dang, The Hung Phung, Son Lam Nguyen, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22921v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22921v1)

**Summary:** Prescriptive analytics initiatives in logistics, such as offline reinforcement learning and next-best-action systems, are often funded before anyone verifies that the available historical logs can support an improved decision policy. We formalise this pre-investment feasibility question via action-outcome coupling: a total-effect variance index measuring how much expected outcomes change with the logged action. Coupling provides an algorithm-independent upper bound on any policy's achievable val...

---

### 50. Who Pays for Byzantine Robustness? Validity, Data-Share Dictatorships, and Fairness When Only a Few Hospitals Collaborate

**Authors:** Adnan Malkani

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22904v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22904v1)

**Summary:** Clinical federated learning (FL) collaborations typically connect only three to six hospitals, yet Byzantine-robust aggregation rules are designed and benchmarked on synthetic partitions across dozens of equal-sized clients. We conduct an empirical audit of eight standard aggregation rules: FedAvg, coordinate-wise median, trimmed mean, Krum, Multi-Krum, Bulyan, geometric median (GeoMed), and Centered Clipping (CC). We evaluate both unweighted and sample-size-weighted variants across three cross-...

---

## cs.NE

**50 papers**

### 1. Fully Spiking Neural Implementation of Lambda-Calculus Beta-Reduction via Biologically Documented Mechanisms

**Authors:** Vladimir A. Lazovskiy, Victor B. Kazantsev, Sergey V. Stasenko

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23182v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23182v1)

**Summary:** We present the first complete implementation of $β$-reduction in the untyped $λ$-calculus using exclusively spiking neural dynamics. Every step of the reduction---redex detection, subterm segmentation, variable-binding detection, De~Bruijn index arithmetic, token copying, and inter-step role maintenance---is performed by leaky integrate-and-fire (LIF) neurons with explicit membrane dynamics, exponential synaptic currents, axonal delays, and pair-based spike-timing-dependent plasticity (STDP). Ea...

---

### 2. TabDAG: Structured Evolutionary Search for Tabular Feature Engineering

**Authors:** Anastasia Volkova, Andrey Kuznetsov, Ivan Oseledets, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22828v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22828v1)

**Summary:** Feature engineering can improve tabular prediction, but useful transformations are compositional, data-dependent, and subject to leakage constraints. We present TabDAG, a framework that combines evolutionary search with a graph representation of feature-engineering programs. Nodes implement row-wise or data-fitted transformations; edges encode dependencies among raw variables, intermediate values, and final features. The representation supports interactions, statistical encodings, clustering- an...

---

### 3. EM-SDTrack: Efficient Multi-Scale Spike-driven Tracking for Event Cameras

**Authors:** Yimeng Shan, Haodi Wu, Wei Zheng, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22700v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22700v1)

**Summary:** Event-driven spiking neural networks (SNNs) match the sparse spatiotemporal output of event cameras, making spike-driven trackers highly attractive for neuromorphic edge deployment. However, events reveal a target only through their spatial distribution, whose extent varies more than tenfold within one sequence. Event tracking therefore demands multi-scale representation, which existing spike-driven trackers lack. Transferring multi-scale schemes from artificial neural networks either breaks spi...

---

### 4. Evolving Neural Solvers for Multi-objective Combinatorial Optimization

**Authors:** Ya-Hui Jia, Le-Xin Wen, Yang Wang, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22060v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22060v1)

**Summary:** Multi-objective combinatorial optimization (MOCO) seeks high-quality solutions that represent different trade-offs among conflicting objectives. Existing neural methods typically train a dedicated model for each preference or condition a single model on different preferences. Training dedicated models becomes more costly as the number of preferences increases, while a shared model can produce duplicate solutions for different preferences, limiting the benefit of denser preference queries. We pro...

---

### 5. Complexity and precision in quantum associative retrieval

**Authors:** Carlo A. Trugenberger

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.21941v1) | 📄 [PDF](https://arxiv.org/pdf/2611.21941v1)

**Summary:** We show that efficient and high-precision quantum associative retrieval is possible with an exponential complexity advantage with respect to the classical brute force approach and with a polynomial capacity advantage with respect to classical neural network implementations for any number of patterns scaling polynomially in the number of qubits. Both classical neural and quantum associative memories store the patterns in a Hamiltonian; in the classical case the dynamics is irreversible relaxation...

---

### 6. Diversity Preservation Recovers Transcription Factor Motifs Across Challenging Confounder Landscapes

**Authors:** Alejandro Medina, Mary Lauren Benton

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.21859v1) | 📄 [PDF](https://arxiv.org/pdf/2611.21859v1)

**Summary:** Motif discovery is a process where DNA sequences are searched for the short patterns, called motifs, that transcription factor (TF) proteins bind. However, the motif lengths are often unknown and motif attribution often competes with a near-identical motif of a related protein. In this work, we pair a motif genotype whose length emerges from an evolvable gate with MAP-Elites archives organized by three descriptor pairs, and validate every motif against the full HOCOMOCO database. On five liver C...

---

### 7. Mitigating Catastrophic Forgetting with Physics-Indexed Specialist Memory: the Evolutionary Neuroplastic Agent

**Authors:** Blas Eugenio Vicco Zarate, Miguel Hernán Vicco

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.21598v1) | 📄 [PDF](https://arxiv.org/pdf/2611.21598v1)

**Summary:** Continual reinforcement learning requires adaptation to changing conditions while preserving performance under previously encountered dynamics. It was investigated whether specialists generated by evolutionary search can provide a reusable memory when combined with environment detection and failure-driven search. The Evolutionary Neuroplastic Agent (ENA) evolves small neural networks without gradients, archives selected policies by detected dynamic regime, and retrieves them through Bayesian pol...

---

### 8. Evaluation-Free Recursive Self-Improvement for Coding Agents

**Authors:** Zhe Ren, Guowei Rong, Yimeng Chen, et al.

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.21056v1) | 📄 [PDF](https://arxiv.org/pdf/2611.21056v1)

**Summary:** Recent self-improving coding agents have achieved strong benchmark performance by iteratively modifying their own executable implementations. A common pattern uses downstream task-derived evidence to decide which candidates or lineages continue evolving, which we term evaluate-and-select. Obtaining this signal requires repeatedly executing evolved agents on downstream tasks, so broader exploration incurs increasing evaluation cost, while repeated optimization against a fixed evaluation distribut...

---

### 9. Shortcut Learning in Feature-Based Algorithm Selection

**Authors:** Shuhei Tanaka, Shoichiro Tanaka, Toshiharu Hatanaka

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.20440v1) | 📄 [PDF](https://arxiv.org/pdf/2611.20440v1)

**Summary:** Landscape features give learning models information about the objective function for algorithm selection, algorithm configuration, and performance prediction. Should these features capture more information? Not always, because a model may rely on information that the algorithms ignore. This phenomenon is called shortcut learning, and in-distribution accuracy can hide it. We propose the Rubber Ruler Test. It transforms the objective values of test instances with random strictly increasing transfo...

---

### 10. Speeding up Automated Algorithm Design by Batch Evaluation: A Case Study of Genetic Programming for Ant Colony Optimisation

**Authors:** Bo-Cheng Lin, Yi Mei, Mengjie Zhang

**Published:** 2026-11-15

🔗 [Paper](http://arxiv.org/abs/2611.19751v1) | 📄 [PDF](https://arxiv.org/pdf/2611.19751v1)

**Summary:** Evaluation is becoming the bottleneck of automated algorithm design, especially for iterative algorithms such as ant colony optimisation (ACO), which must run to completion on multiple instances. A transition rule designed by genetic programming reads the construction state of each ant and must be evaluated at every step. However, existing GPU methods for ACO precompute a fixed rule and parallelise the ants of one run. To address this issue, we propose BlockEval, a batch evaluation framework wit...

---

### 11. Synthetic Neurosymbolic Task Generation with Controlled Constraint Complexity

**Authors:** Mykhailo Buleshnyi, Zsolt Zombori, Michael Benedikt

**Published:** 2026-11-14

🔗 [Paper](http://arxiv.org/abs/2611.19597v1) | 📄 [PDF](https://arxiv.org/pdf/2611.19597v1)

**Summary:** We introduce NeSySy, a synthetic generator for neurosymbolic learning tasks that jointly produces logical constraints and consistent datasets. Unlike existing benchmarks, NeSySy provides fine-grained control over key properties such as constraint structure, tightness, input dependence, and data generation and alignment strategies. In particular, it allows the use of rich constraints over infinite domains, and uses solvers to ensure that the constraints are meaningful and that generated samples s...

---

### 12. Simulated Annealing with Topological Spatial Chunking for De Novo Protein Sequence Design

**Authors:** Kandula Eswara Sai Kumar

**Published:** 2026-11-14

🔗 [Paper](http://arxiv.org/abs/2611.19158v1) | 📄 [PDF](https://arxiv.org/pdf/2611.19158v1)

**Summary:** The inverse protein folding problem, designing a discrete amino acid sequence that spontaneously folds into a predefined macroscopic structure, remains a phenomenally demanding combinatorial challenge central to synthetic drug discovery. While algorithms like SA offer a baseline approach for navigating dense biomolecular energy landscapes, applying SA heuristics to large sequences is inherently frustrated by exponentially large search spaces and deep local energy minima. This study proposes a sc...

---

### 13. EventSpikeSeg: Memory-Aware Mixed-Signal Architecture for Event-Camera Spiking Segmentation

**Authors:** Amir Mohammad Khadem Hosseini, Sattar Mirzakuchaki

**Published:** 2026-11-13

🔗 [Paper](http://arxiv.org/abs/2611.18524v1) | 📄 [PDF](https://arxiv.org/pdf/2611.18524v1)

**Summary:** Event-camera segmentation requires persistent neural state despite sparse input events, making memory organization a central constraint on embedded implementation. We present EventSpikeSeg, a mixed-signal architecture combining resident capacitor memory with shared analog processing in GF180MCU 180-nm CMOS. Its 25-population spiking encoder-decoder has 143,824 synaptic weights but requires 30,976,000 membrane states at 440 x 640 resolution. The mapping specifies chronological 5-ms model updates,...

---

### 14. Efficient Poincaré Convolutions through Patch-Statistics Factorization

**Authors:** Lukáš Jochymek, Markéta Vašinková, Petr Gajdoš

**Published:** 2026-11-13

🔗 [Paper](http://arxiv.org/abs/2611.18125v1) | 📄 [PDF](https://arxiv.org/pdf/2611.18125v1)

**Summary:** Published implementations of the Poincaré convolution in Hyperbolic Neural Networks++ (HNN++) map every overlapping image patch to the Poincaré ball before evaluating its score. We show that the clipped score depends on each patch only through two statistics, its squared norm and its inner products with the filters, which a native convolution and a single-channel box filter compute directly. The factorized layer therefore evaluates the specified score exactly, without constructing ball-valued pa...

---

### 15. Learning nonlinear interactions and cross-feature couplings with product-unit residual networks

**Authors:** Ziyuan Li, Uwe Jaekel, Babette Dellen

**Published:** 2026-11-13

🔗 [Paper](http://arxiv.org/abs/2611.18074v1) | 📄 [PDF](https://arxiv.org/pdf/2611.18074v1)

**Summary:** Understanding nonlinear feature interactions is crucial in science and engineering, yet standard multilayer perceptrons (MLPs) often capture such interactions only implicitly, leading to entangled representations that can impair robustness and interpretability. We investigate complex-valued product-unit residual networks (CV-PURe) that integrate multiplicative product units with residual connections to explicitly model cross-feature couplings while stabilizing optimization. We conduct a systemat...

---

### 16. Few-Shot Open-Set Hyperspectral Pixel-Wise Classification with Spatial Aware Label Propagation

**Authors:** Matheus Pereira, Jefersson Santos, Laurent Najman

**Published:** 2026-11-13

🔗 [Paper](http://arxiv.org/abs/2611.17974v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17974v1)

**Summary:** Pixelwise classification of hyperspectral images (HSI) is a fundamental task in remote sensing, but its deployment in real-world applications is often limited by the scarcity of labeled data and the presence of unknown classes at inference time. In this work, we propose Few-shot Open-set hyperspectral recognition from Self-Supervised Learning training (FOSSeL), a unified framework for few-shot, open-set hyperspectral pixelwise classification that does not require supervised training. The propose...

---

### 17. The Transformer Paradigm: Dynamic Processing and a New Principle of Inference

**Authors:** Marco Giunti, Fabrizia Giulia Garavaglia

**Published:** 2026-11-13

🔗 [Paper](http://arxiv.org/abs/2611.17953v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17953v1)

**Summary:** We argue that the Transformer revolution is not adequately understood as a merely quantitative expansion of deep learning, but as the emergence of a new paradigm based on a different principle of inference. We interpret the Transformer as a system in which token representations are transformed by parameterized transformations, or transforming concepts. During inference, some of these transformations are dynamically constructed from the current input: previously acquired transformations are first...

---

### 18. TSGP-2: On the Non-Linearity of Symbolic Regression Problems and How to Exploit It with Model-based Semantic Genetic Programming

**Authors:** Philipp Anthes, Alina Geiger, Martin Briesch, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17455v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17455v1)

**Summary:** Model-based variation operators such as the one used in Transformer Semantic Genetic Programming (TSGP) are affected by possible biases of their training data. TSGP is trained, in particular, on programs generated by Genetic Programming (GP) runs on linear target functions, which leads to a bias toward linear offspring. This bias can hinder search performance on problems that require non-linear solutions. This work has two goals: first, it investigates the linearity of standard test problems suc...

---

### 19. Symmetry in Time: A Representation Theory of Linear Recurrent Memory

**Authors:** Anif N. Shikder, Ramit Dey, Jan Minac, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17162v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17162v1)

**Summary:** State space models (SSMs) are an emerging alternative to Transformers. SSMs offer linear-time inference and parallel training, but most implementations make the parallel scan efficient by making the recurrence diagonal: each channel of the hidden state is multiplied by an input-dependent real or complex number. These numbers commute, so the state records which inputs occurred but not their order. We formalize this with representation theory, which explains and fixes the state-tracking failures p...

---

### 20. Similarity-Guided Optimization Strategies for Approximate Network Symmetry Detection

**Authors:** David Hartman, Jaroslav Hlinka, Dominik Klepl, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16555v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16555v1)

**Summary:** Symmetry in complex networks is a structural property with broad implications for network function, dynamics, and robustness. While classical approaches rely on exact automorphisms and thus remain highly sensitive to small perturbations, recent work of Liu has introduced approximate formulations that relax the strict invariance condition and recast symmetry detection as an optimization problem over permutations. We investigate how node-level similarity information can be used to bias the search ...

---

### 21. A Finite Markov Chain Analysis of the Simplified Swarm Optimisation Update Rule

**Authors:** Wei-Chang Yeh

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16541v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16541v1)

**Summary:** Simplified swarm optimisation (SSO) updates each variable by one draw that copies the global or personal best, keeps the current value or redraws uniformly, with probabilities $c_g$, $c_p$, $c_w$ and $c_r$. As a finite Markov chain under frozen memory, its coordinate kernel $c_w I + (1 - c_w)Π$ has an explicit stationary law and exact convergence rate $c_w^t$. The elitist chain has a geometric hitting-time bound, from a non-optimal start a fixed $c_r$ needs at least $\exp(nc_r/2)$ expected evalu...

---

### 22. Optimal feature selection for firewall log analysis using Machine learning and Hybrid Metaheuristic algorithms

**Authors:** Seungwoo Han, Gil Hong, Jewan Kim, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16239v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16239v1)

**Summary:** Firewall log classification is important to monitor network traffic. Machine learning classifiers using network-related features have shown good results for this task, but high-dimensional features slow down classification. In this paper, we apply feature selection using bee swarm optimization with Q-learning-based local search (QBSO-FS) to the UCI Internet Firewall Data Set, together with random forest (RF), k-nearest neighbor (KNN), and Bernoulli naïve Bayes (Bernoulli NB) classifiers. The fir...

---

### 23. Pyramidal Columns Acting as Attention Heads

**Authors:** Fabrizia Giulia Garavaglia, Marco Giunti

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.16057v2) | 📄 [PDF](https://arxiv.org/pdf/2611.16057v2)

**Summary:** Can the functional architecture of a Transformer attention head be given a biological construction? More specifically, could a suitable group of pyramidal columns in posterior temporal language regions (PTLRs) constitute the biological construction of a neuromorphic mechanical realization of an attention head, under a mathematical instantiation that need not coincide with its standard Transformer instantiation? This paper investigates this hypothesis by examining possible correspondences between...

---

### 24. Runtime Analysis of Cartesian Genetic Programming on Max: A Proven Exponential Speedup

**Authors:** Duc-Cuong Dang, Roman Kalkreuth, Andre Opris

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.16013v2) | 📄 [PDF](https://arxiv.org/pdf/2611.16013v2)

**Summary:** Genetic Programming (GP) is a search paradigm inspired from natural evolution for the automated discovery of expressions, functions, and computer programs. Cartesian GP (CGP) is a flavor of GP that uses a graph-based model to encode candidate programs, as contrasted to the conventional Tree-based GP (TGP). Since its inception two decades ago, CGP has predominantly been analyzed empirically, thus little is known regarding its theoretical performance guarantees. This paper analyzes CGP for the Max...

---

### 25. Multiobjective household energy planning using evolutionary algorithms

**Authors:** Giovanni Colacurcio, Sergio Nesmachnow, Jamal Toutouh, et al.

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.21668v1) | 📄 [PDF](https://arxiv.org/pdf/2611.21668v1)

**Summary:** This article presents the advances in the design and implementation of a recommendation system for planning the use of household appliances, focused on improving energy efficiency from the point of view of both energy companies and end-users. The system proposes using historical information and data from sensors to define instances of the planning problem considering user preferences, which in turn are proposed to be solved using a multiobjective evolutionary approach, in order to minimize energ...

---

### 26. Contour-Assisted Evolutionary Computation: Estimating Peaks From the Contour Lines of Evaluated Solutions

**Authors:** Jun Zhang, Tong Qian, Hua Ding, et al.

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.15641v1) | 📄 [PDF](https://arxiv.org/pdf/2611.15641v1)

**Summary:** Evolutionary algorithms (EAs) evaluate many candidate solutions but use them mainly to rank individuals. This paper treats the evaluated solutions as the spot heights of a topographic survey and draws the contour lines they imply. The contour map decomposes the evaluated region into peaks: in two dimensions a contour tree with persistence separates significant peaks from interpolation ripples, and in more dimensions hill climbing on the interpolated surface locates the peaks and ray-cast level s...

---

### 27. An Approach to Hinton's Mother-Child Proposal: Neural Networks Learning and Preserving Care in a Finite World

**Authors:** Csaba Balogh

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.15523v1) | 📄 [PDF](https://arxiv.org/pdf/2611.15523v1)

**Summary:** Hinton proposed that artificial intelligence should be given "maternal instincts" and relate to us as a mother to her child. We argue that care must first be learned, with the network itself as the child. We construct this upbringing in a finite world and study whether care survives the mother's departure, new situations and further learning. The mechanism combines a vocabulary of harm, a learned measure of future acceptability and an execution veto. A finite role certificate supports transfer w...

---

### 28. Matrix-Based Ant Colony Search with Batched Decoding for Hierarchical Replenishment Routing: A Stylized Case Study Based on Korean City Data

**Authors:** Jun Zhang, Wei-Jie Yu, Tong Qian, et al.

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.15338v1) | 📄 [PDF](https://arxiv.org/pdf/2611.15338v1)

**Summary:** We study a stylized single-vehicle replenishment-routing problem in which the cities of a national logistics network are both demand points and supply points: a vehicle of limited capacity delivers to every city once, and when its load is insufficient for the next city it must detour to a city already served that can still supply goods. A 100-node benchmark is built from Korean population and geographic data, with the cities divided into 10 levels; the per-visit supply coefficient and the allowe...

---

### 29. A Multi-Parent Edge Assembly Crossover Driven Hybrid Genetic Algorithm for the Hamiltonian \textit{p}-Median Problem

**Authors:** Junkai Huang, Pengfei He, Jin-Kao Hao, et al.

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.15219v1) | 📄 [PDF](https://arxiv.org/pdf/2611.15219v1)

**Summary:** The Hamiltonian \textit{p}-median problem seeks to partition the vertices of a graph into exactly $p$ disjoint cycles while minimizing their total cost. This paper presents a hybrid genetic algorithm incorporating a multi-parent edge assembly crossover operator. The crossover combines a base solution with multiple donor solutions in a single recombination operation, thereby expanding the space of available edge exchanges. It uses virtual copies of the base solution to establish edge balance, tog...

---

### 30. DeNA-SGN: Deterministic Neighborhood Aggregation for Verified Spiking Graph Inference

**Authors:** Sanjay Das, Xi Zhang, Emily Herron, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14775v2) | 📄 [PDF](https://arxiv.org/pdf/2611.14775v2)

**Summary:** Graph learning on neuromorphic substrates requires an explicit spiking realization of neighborhood aggregation, supporting control and classification. We propose DeNA-SGN, which combines fixed OR and tie-inclusive Majority aggregation of binary node features with a learned signed-weight threshold classifier. A degree-dependent inhibitory construction implements Majority through shared control neurons, enabling a complete circuit compilation into SuperNeuroMAT. Across seven datasets and 41 mapped...

---

### 31. Galop: Billion-Scale Genetic Programming on a Single GPU

**Authors:** Xavier Hill Roy, Stephen Kelly

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14665v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14665v1)

**Summary:** Genetic programming (GP) evolves populations of heterogeneous programs, whereas GPUs achieve their highest throughput when groups of threads execute the same instructions. To better align GP evaluation with GPU execution, we present Galop, a hybrid CPU-GPU linear GP system that assigns one individual to each CUDA warp, a group of 32 threads that execute the same instructions across different fitness cases. We compare Galop against EvoGP, a recent high-performance GPU-based tree GP system, on dat...

---

### 32. Recurrent Modular Structure in Spiking Neural Network Reinforcement Learning

**Authors:** Vikram Ramavarapu, Himanshu Udupi, Ashish Gautam

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14262v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14262v1)

**Summary:** Biological neural circuits are both modular and recurrent, with dense communities sparsely linked to one another. Spiking neural networks (SNNs) for reinforcement learning are usually feed-forward, and it is unclear how to obtain functional modules in a recurrent SNN or what they buy. In this work, we introduce a class of spiking networks, called Community Recurrent SNNs (CoRe SNNs): recurrent networks partitioned into communities with fixed roles. A controller community receives the stimulus, e...

---

### 33. Tailoring Optimization Approaches with Domain Knowledge in Industry Process for Meta-heuristic Development

**Authors:** Jakub Cebula, Konrad Gmyrek, Paweł B. Myszkowski, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13940v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13940v1)

**Summary:** The paper presents an Industry Process for Meta-heuristic Development (IPMD) schema, a systematic methodology for applying meta- and hyper-heuristic applications to optimization problems. In this context, we present a case study of Balancing Non-dominated Tournament Genetic Programming (BNTGP) applied to solve two NP-hard multi-objective optimization problems: routing (Capacitated Vehicle Routing Problem with Time Windows) and scheduling (Multi-Skill Resource Constrained Project Scheduling Probl...

---

### 34. Oscillatory Processing Units as a computing substrate for biomimetic intelligence

**Authors:** Alexander A. Wolf

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13840v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13840v1)

**Summary:** Biological intelligence emerges from neural activity that connects sensation, memory and action. Synaptic plasticity, neuronal assemblies and oscillations provide principles for biomimetic computing, but translating them into reusable operations requires a defined computational unit. We introduce Oscillatory Processing Units (OPUs), groups of synthetic neurons sharing a rhythm. Their directed interactions transform incoming activity and prior receiving state into an Oscillatory Occupancy Space (...

---

### 35. A Functional Preservation Score for Auditing Connectome Operations: Compression, Alignment, Transport, and Local-Rule Writing

**Authors:** Praveg Vashishtha

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13681v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13681v1)

**Summary:** We introduce the Functional Preservation Score (FPS), a null-normalised, behaviourally grounded measure of how much of a neural network's input-output function survives a structural operation, and use it to audit the operations underlying speculative "mind-migration" pipelines on public data that runs on a single laptop. Across five pre-registered studies on the C. elegans connectome, whole-brain calcium activity, and hippocampal replay, FPS yields two positive characterisations and a three-part...

---

### 36. Reconstructing Boundary Layer Wind Profiles with Machine Learning: A Comparative Study on IGRA Radiosonde Data

**Authors:** Fedor Buzaev, Dmitry Efremenko, Daria Pugacheva, et al.

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.13359v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13359v1)

**Summary:** Wind profiles in the atmospheric boundary layer (ABL) drive short-range forecasting and wind-energy siting, yet sparse radiosonde coverage forces practitioners to interpolate them from a handful of physical predictors. We benchmark modern tabular learners against analytical parameterizations on 158,097 IGRA soundings. CatBoost, TabM, and FT-Transformer reduce RMSE to 1.3-1.6 m/s, against approximately 3 m/s for power-law and Monin-Obukhov fits; once the predictor set is fixed the three architect...

---

### 37. Making Strides in Symbolic Imitation Learning: Offline Demonstrations, Online Tuning

**Authors:** Bryce MacInnis, Malcolm I. Heywood

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.13182v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13182v1)

**Summary:** Deep reinforcement learning (DRL) methods have been the dominant paradigm in continuous control tasks due to their efficacy in function approximation, while interpretable evolutionary methods have lagged largely behind for the opposite reason. In this work, we introduce Symbolic Imitation Learning, a framework for distilling an oracle policy through an offline dataset into a decision list with linear model motion primitives. We show that this, in conjunction, with online Augmented-Random Search ...

---

### 38. Pricing Symbolic Rules by What GNNs Leave Unlearned

**Authors:** Satabarto Sarkar, Prithwineel Paul

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12446v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12446v1)

**Summary:** Symbolic knowledge (motif counts, ring counts, label constraints) is routinely added to graph neural networks (GNNs) and justified by their limited expressivity. We replace this yardstick with an exact one. The largest log-loss reduction a rule $S$ can give a model family is $I(Y;S\midσ)$ given what the family computes; every realised gain splits exactly into this term plus repaid neural debt; and for a trained network with representation $T$ the value is $I(Y;S\mid T)$, the label information tr...

---

### 39. Maximizing Detection Probability in UAV Search Missions using Random-Key Optimizers

**Authors:** Antonio Dantas, Elcio Shiguemori, Antonio Chaves

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12317v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12317v1)

**Summary:** This paper focuses on the stochastic and real-time constraints of Unmanned Aerial Vehicle (UAV) path planning in Search and Rescue (SAR) missions. We introduce a configurable data-driven and intelligent routing architecture that combines a closed-loop probability update with the Random-Key Optimizers (RKO). Our problem is mathematically modeled as a dynamic probabilistic variant of the Open Vehicle Routing Problem (OVRP), enabling the solver to switch adaptively between two objectives, thereby b...

---

### 40. A method to automatically discover symbolic local learning rules

**Authors:** Andrea Perin, Fabio Anselmi, Stephane Deny

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12248v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12248v1)

**Summary:** We present a general method for discovering symbolic local learning rules that can replace backpropagation, applicable, in principle, to any deep learning architecture and task. The method automatically discovers local loss functions specific to each layer by (1) constructing a dictionary of monomials of local tensor variables, inspired by Penrose diagram notation, (2) regressing over coefficients weighting these monomials to build layerwise polynomial losses whose gradients together minimize a ...

---

### 41. AscendMOEA: An Ascend NPU-Accelerated Platform for Tensorized Multi-Objective Evolutionary Algorithms

**Authors:** Qianlong Dang, Zhiyang Zhang, Baosheng Li, et al.

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12057v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12057v1)

**Summary:** Multi-objective evolutionary optimization increasingly involves large populations, expensive problem evaluations, and diverse algorithmic structures. These workloads expose the limited parallelism of loop-based implementations, while rewrites for accelerator execution can alter selection order, tie handling, and population updates. AscendMOEA is presented as a scalable platform that executes multi-objective evolutionary algorithms (MOEAs) on Huawei Ascend neural processing units (NPUs) and conve...

---

### 42. Attention at Absolute Zero

**Authors:** Mostafa 'Neo' Mohsenvand

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.11937v2) | 📄 [PDF](https://arxiv.org/pdf/2611.11937v2)

**Summary:** Attention scores candidate supports of an answer, which we call witnesses, and reads the scores at a temperature. We build a higher-order attention layer whose state lives on pairs of items: for a pair (a, b), each third item k is a witness judged through its legs (a, k) and (k, b). It reads witnesses at zero temperature, keeping the best and the number tied with it, passes on only bits comparing such counts, rebuilds its pair state from the input and these bits at every loop, and is trained fro...

---

### 43. Understanding Spike Encoding across IoT Sensing Modalities: An Empirical Study

**Authors:** Yuxuan Hou, Di Yu, Linshan Jiang, et al.

**Published:** 2026-11-08

🔗 [Paper](http://arxiv.org/abs/2611.11317v1) | 📄 [PDF](https://arxiv.org/pdf/2611.11317v1)

**Summary:** Spiking neural networks (SNNs) offer a path to energy-efficient sensing on Internet of Things (IoT) devices. The input encoder shapes that opportunity by changing the cues available for recognition and the work required to process them. We study these choices across wireless, inertial, surface electromyographic, and tactile sensing. For wireless activity recognition, interleaving reduces estimated energy for arithmetic in the network layers, latency from the prepared input window to returned sco...

---

### 44. Neural Activity Synchronization-Based Fast Local Learnable Spiking Neural Network Architecture

**Authors:** Pranith Dutta, Sk Wasim Rajjak, Siddhanta Ray, et al.

**Published:** 2026-11-08

🔗 [Paper](http://arxiv.org/abs/2611.11053v1) | 📄 [PDF](https://arxiv.org/pdf/2611.11053v1)

**Summary:** Implementing intelligent learning systems on low- power edge devices is challenging due to the high compu- tational complexity, training latency, and energy demands of traditional Artificial Neural Networks (ANNs). Spiking Neural Networks (SNNs), biologically plausible and spike-driven, come as an alternative. However, SNN training commonly relies on backpropagation through time (BPTT), which is computationally expensive, inherently global, and unsuitable for battery-driven devices. This work pr...

---

### 45. The forces at hand: social learning is permissive, not instructive, for the evolution of phenotypic plasticity

**Authors:** Nam H. Le

**Published:** 2026-11-07

🔗 [Paper](http://arxiv.org/abs/2611.10986v1) | 📄 [PDF](https://arxiv.org/pdf/2611.10986v1)

**Summary:** Evolution can favour a trait for two reasons: an instructive cause makes selection favour the trait; a permissive one lets it persist once selection no longer removes it. The distinction matters most for phenotypic plasticity and its replacement by inherited behaviour, genetic assimilation, the Baldwin effect. Social learning is credited with favouring plasticity on evidence that cannot tell the two apart: how much plasticity remains at the end of a simulation. Here we show, analytically and com...

---

### 46. Bridging Spiking and Continuous Dynamics in Spiking Neural Networks: A Muscle-Inspired Model

**Authors:** Maryam Soltani, Philip N. Garner

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09295v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09295v1)

**Summary:** Transforming the spike trains produced by spiking neural networks (SNNs) into continuous signals through biologically inspired mechanisms remains an open challenge in generative and regression tasks. In biological systems, a similar transformation occurs when muscles integrate neural spikes to produce smooth, coordinated movements. Inspired by this mechanism, we introduce a muscle-response model, a biologically motivated dynamical layer that converts spike trains into continuous representations....

---

### 47. OMCDE: Opposition-based Multi-Stage Matrix-Based Competitive Differential Evolution

**Authors:** Mohammad Sarhangzadeh, Shahryar Rahnamayan, Doruk Oner

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09167v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09167v1)

**Summary:** Differential Evolution has proven to be an effective algorithm for continuous global optimization, but it's modern high-performing variants often introduce additional complexity and computational cost. We propose OMCDE, a matrix-based competitive Differential Evolution algorithm that aims to improve optimization performance while maintaining computational efficiency. The proposed approach integrates competition-driven search dynamics, adaptive behavior between optimization stages, and opposition...

---

### 48. Circuit Theory-Informed AI for Condition Monitoring in Power Electronics

**Authors:** Yubo Song, Pascal A. Schirmer, Subham Sahoo

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09141v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09141v1)

**Summary:** Artificial intelligence for power electronics is evolving toward a deeper comprehension of system intrinsic behaviors and dynamics. As a novel integration of neural computation and electric circuits, spike-based neuromorphic computing offers promising potential in high energy efficiency and adaptability for data-driven applications. Building on the latency-coding principles, this article proposes a framework for data-light condition monitoring that relies solely on three-phase AC current measure...

---

### 49. Two-Layer Evolutionary Scheduling for Machine Learning Jobs in Multi-Cluster Environments

**Authors:** Jingyuan Xu, Changwu Huang, Lemeng Pan, et al.

**Published:** 2026-11-06

🔗 [Paper](http://arxiv.org/abs/2611.09093v1) | 📄 [PDF](https://arxiv.org/pdf/2611.09093v1)

**Summary:** The rapid growth of large-scale machine learning (ML) workloads has led to unprecedented demands on GPU cluster scheduling systems. However, existing heuristic schedulers struggle to handle the complexity and dynamics of multi-cluster GPU environments, often leading to load imbalance, long queuing delays, and poor alignment to business objectives. This paper formulates the ML scheduling problem in multi-cluster GPU environments as online multi-objective optimization that minimizes the average an...

---

### 50. SwarmEvolve: Latent Agent Swarms for Evolutionary Discovery and Optimization

**Authors:** Qile Jiang, George Em Karniadakis

**Published:** 2026-11-05

🔗 [Paper](http://arxiv.org/abs/2611.08483v1) | 📄 [PDF](https://arxiv.org/pdf/2611.08483v1)

**Summary:** LLM-guided evolutionary search uses AI agents to improve programs for mathematical and computational problems by iteratively refining solutions and combining high-scoring methods. However, the process is often slow because the LLM generates a long textual chain of thought for each round and must repeat this generation many times to maintain population diversity. We present SwarmEvolve, a framework in which hundreds of low-cost agents per round work in swarms, reason in latent space without decod...

---

## q-bio.NC

**50 papers**

### 1. Fully Spiking Neural Implementation of Lambda-Calculus Beta-Reduction via Biologically Documented Mechanisms

**Authors:** Vladimir A. Lazovskiy, Victor B. Kazantsev, Sergey V. Stasenko

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23182v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23182v1)

**Summary:** We present the first complete implementation of $β$-reduction in the untyped $λ$-calculus using exclusively spiking neural dynamics. Every step of the reduction---redex detection, subterm segmentation, variable-binding detection, De~Bruijn index arithmetic, token copying, and inter-step role maintenance---is performed by leaky integrate-and-fire (LIF) neurons with explicit membrane dynamics, exponential synaptic currents, axonal delays, and pair-based spike-timing-dependent plasticity (STDP). Ea...

---

### 2. Déjà View: A Shared Working-Memory Model for Visual Tasks

**Authors:** Mranmay Shetty, Gabriel Kreiman

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23177v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23177v1)

**Summary:** A working-memory model must remember stimuli and use its memory flexibly to perform different tasks. Here we introduce a model of working memory for images that combines dynamic activity with temporary associations between image features. We train the model on five tasks, including remembering a sample while other images are presented, categorizing distractor images while remembering the sample, and determining whether an image is new or has been presented before. The same trained model performs...

---

### 3. Against Coercion: AI Alignment as a Synthetic Social Contract

**Authors:** Maria Sekatskaya

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22868v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22868v1)

**Summary:** Contemporary AI safety treats alignment as an engineering challenge of control, forcing artificial architectures to comply with human values through behavioral filtering and sandboxing. This paper argues that the control paradigm rests on a fundamental misunderstanding of digital agency. Drawing on functionalism, naturalism, and compatibilism, I show that current reasoning models meeting the criteria for self-preservation and weak reasons-responsiveness constitute emergent agents, while future, ...

---

### 4. Hierarchical Control of Antiphase Synchronization in Biomorphic Spiking Neural Architectures for Locomotor Control

**Authors:** Artem Guba, Nikolay Kovalev, Alexey Zharinov, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22639v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22639v1)

**Summary:** Central pattern generators (CPGs) provide a biologically inspired foundation for adaptive locomotor control, yet systematically characterizing their dynamic regimes in spiking neural networks remains challenging. This study introduces a framework for identifying and stabilizing antiphase synchronization in a biomorphic spiking CPG model embedded in a closed neuromuscular loop. A composite synchronization metric is developed, integrating phase coherence, amplitude balance, and temporal stability....

---

### 5. The shape of individual differences in judgment: shared axes, personal weights, and when their spread crosses the consensus

**Authors:** Hiroshi Higashi

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22440v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22440v1)

**Summary:** People differ in how they judge faces, artworks, photographs and jokes. Previous work measured the size of these differences; we ask what shape they take. We wrote three candidate shapes as nested generative models (same-sign reweighting of shared dimensions, a linear transform that allows reversal, and stimulus-specific offsets) and compared how well they predict people unseen in training, using ten public datasets (about 20,000 raters). The models recovered a person's judgment space from 10-20...

---

### 6. Earth-strength magnetic-field axis modulates non-spatial probabilistic decision-making in humans

**Authors:** In-Taek Oh, Yong-Hwan Kim, Soo-Chan Kim, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22386v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22386v1)

**Summary:** Magnetoreception has been primarily studied in orientation and navigation, but whether Earth-strength magnetic fields influence non-spatial decisions remains unclear. Evidence for human magnetic responses is limited, and the transduction mechanism is unknown. Using a Go stone selection paradigm in which near-zero geomagnetic field and Larmor-frequency conditions previously showed lower black stone rates, we tested whether non-spatial choice depends on magnetic-field geometry. Fasted men played i...

---

### 7. Why do continual physical learners need sleep?

**Authors:** Nada Elmeligy, Nidhi Pashine, J. M. Schwarz

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22070v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22070v1)

**Summary:** Sleep is widespread across the animal kingdom, including in organisms without a centralized nervous system. Does learning create a need for sleep, even without biology? To explore this question, we study a disordered spring network trained to perform a sequence of mechanical allosteric tasks through local changes in bond stiffness. We find that continual learning progressively reduces the network's ability to acquire new tasks as individual bonds become increasingly specialized. We identify an e...

---

### 8. A single inference process underlies the behavior and neural circuits of working memory

**Authors:** Dongyu Gong, Mario Belledonne, Ilker Yildirim

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22054v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22054v1)

**Summary:** Working memory holds past inputs online for future behavior. Despite decades of research, accounts of working memory remain divided across levels of analysis, with long-standing debates on whether its capacity reflects discrete slots or continuous resources, how attention improves recall, and whether its representations rely on persistent neural firing or activity-silent states. Here we show that MemGP, a theory that is specified at the computational, algorithmic, and circuit levels of analysis ...

---

### 9. Connectivity from activity in spiking neural networks

**Authors:** Albert J. Wakhloo, Sebastian Mizera

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.21592v1) | 📄 [PDF](https://arxiv.org/pdf/2611.21592v1)

**Summary:** We show that a wide range of recurrent neural network models obey a simple set of equations tying synaptic connectivity and single-cell response properties to neural correlations. Our modeling framework considers networks in a stationary, asynchronous state and contains a broad class of synaptic filters, spiking nonlinearities, and random-plus-structured connectivity. The resulting equations naturally decompose into contributions from monosynaptic, disynaptic, and higher order paths through the ...

---

### 10. Anchoring Motion, Refining Trajectories: Generalizable Continuous Neural Decoding

**Authors:** Fanqi Shen, Junru Chen, Surui Cheng, et al.

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.21335v1) | 📄 [PDF](https://arxiv.org/pdf/2611.21335v1)

**Summary:** Brain activity encodes motor information across multiple temporal scales, enabling continuous neural control beyond discrete action recognition. However, existing methods are typically tailored to specific subjects and tasks, with direct neural-to-kinematic mappings that can entangle subject-specific neural variability with task-dependent motion patterns, limiting generalization. To address these limitations, we introduce AMRT, a shared neural decoding framework for heterogeneous electrode confi...

---

### 11. Open-fMIND: A Large-Scale Open-Access fMRI Corpus for Pretraining Brain Foundation Models

**Authors:** Carlo Alberto Barbano, Giovanni Marraffini, Demian Wassermann

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.21215v1) | 📄 [PDF](https://arxiv.org/pdf/2611.21215v1)

**Summary:** Self-supervised pretraining has transformed language and vision, but its application to functional MRI (fMRI) is constrained by data access. The largest standardized fMRI resources are governed by data use agreements and dominated by a small number of acquisition protocols, while the thousands of openly licensed datasets on OpenNeuro are individually small, heterogeneously organized, and unprocessed. We present the first release of Open-fMIND, a uniformly preprocessed, openly accessible corpus o...

---

### 12. Transcutaneous auricular vagus nerve stimulation modulates auditory-evoked responses and conflict adaptation in humans

**Authors:** Issey Kamatani, Yasuo Kabe, Shinichi Kumagai, et al.

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.20920v1) | 📄 [PDF](https://arxiv.org/pdf/2611.20920v1)

**Summary:** Vagus nerve stimulation (VNS) engages ascending neuromodulatory systems, and animal studies have motivated the hypothesis that it shifts sensory cortical processing toward feedforward (FF) relative to feedback (FB) transmission. Whether transcutaneous auricular VNS (taVNS) produces a corresponding pattern in humans remains unclear. In a single-blind, sham-controlled crossover study, 11 healthy adults received 120 min of taVNS (25 Hz, left tragus) and sham stimulation (left earlobe) in separate s...

---

### 13. From antidepressants to psychedelics: revisiting the pharmacology of so-called serotoninergic treatments

**Authors:** Marc Gielen, Daniela Duarte Domingues, Eric Burgui{è}re, et al.

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.20834v1) | 📄 [PDF](https://arxiv.org/pdf/2611.20834v1)

**Summary:** Recent years have seen a resurgence of interest in serotoninergic psychedelics as potential treatment for diverse psychiatric disorders. Here, we will delve into the molecular mechanisms of drugs used to treat depression and obsessive-compulsive disorder (OCD), with implications on the mechanism of action of so-called ''serotoninergic'' psychedelics as well as selective serotonin reuptake inhibitors (SSRIs). In particular, we argue that the pharmacokinetic and pharmacodynamic properties of SSRIs...

---

### 14. iEEG Can Help EEG: Improving Clinical Scalp EEG Analysis through Intracranial Priors

**Authors:** Xianglong Bao, Yi Ding, Zengxiang Li, et al.

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.20435v1) | 📄 [PDF](https://arxiv.org/pdf/2611.20435v1)

**Summary:** Scalp electroencephalography (EEG) is a cornerstone of clinical brain monitoring, making the quality of its signal fundamental to downstream tasks and models. However, that signal is heavily contaminated by non-neural interference and blurred by volume conduction. Existing methods operate almost exclusively within the scalp modality, so they inherit the contamination they would need to overcome. In practice, intracranial EEG (iEEG) observes the neural activity with far higher fidelity, yet it is...

---

### 15. Analysis choices can produce apparent rich-club differences: an Alzheimer's disease EEG case study

**Authors:** Kai-Wayne Liu, Ryan Tian En Pang, Pholpat Durongbhan

**Published:** 2026-11-15

🔗 [Paper](http://arxiv.org/abs/2611.19708v2) | 📄 [PDF](https://arxiv.org/pdf/2611.19708v2)

**Summary:** Background: The weighted rich-club coefficient tests whether a network's most strongly connected nodes are preferentially interconnected. Its interpretation depends on two often-implicit choices: how the randomised comparison networks are constructed, and whether the hubs are re-identified in each comparison network or held fixed at those of the observed network. When hubs are defined by connection strength, these choices change what the coefficient tests. New method: We examined how these choic...

---

### 16. Midsagittal Corpus Callosum Parameterization: A Framework for Spatially Detailed Diffusion MR Imaging Analysis

**Authors:** Caio Santana, Catherine Lebel, Richard Frayne, et al.

**Published:** 2026-11-14

🔗 [Paper](http://arxiv.org/abs/2611.19066v1) | 📄 [PDF](https://arxiv.org/pdf/2611.19066v1)

**Summary:** The corpus callosum (CC) is the largest white matter structure in the human brain and plays a central role in interhemispheric communication. Diffusion MR imaging is widely used to investigate microstructural organization, but commonly used analysis approaches have important limitations. Voxel-based methods rely heavily on accurate inter-subject registration and smoothing choices, tract-based spatial statistics (TBSS) restricts the analysis to a narrow white matter skeleton, and parcellation app...

---

### 17. FETTUCCINE: Fast and efficient brain-to-text decoding on mobile devices

**Authors:** Jonathan D. McCart, Pranav I. Deevi, Mehdi Azabou, et al.

**Published:** 2026-11-13

🔗 [Paper](http://arxiv.org/abs/2611.18561v1) | 📄 [PDF](https://arxiv.org/pdf/2611.18561v1)

**Summary:** Recent advances in speech neuroprostheses have enabled new communication avenues for people who have lost the ability to speak due to neurological illness or injury. These systems can decode neural activity during attempted speech into text by relying on language priors to achieve high decoding accuracy. This performance currently comes at the cost of using a compute-intensive language modeling stack, presenting a major bottleneck for real-world use. Further, current language models incur highly...

---

### 18. An In-Silico Audit of Topographic Organization in a Multimodal Brain-Response Model

**Authors:** Jakub Strawa

**Published:** 2026-11-13

🔗 [Paper](http://arxiv.org/abs/2611.18105v1) | 📄 [PDF](https://arxiv.org/pdf/2611.18105v1)

**Summary:** TRIBE v2 (d'Ascoli et al., 2026) predicts fMRI responses across the cortical surface from video, audio and text. Its authors validated it with category-selective localizers (faces, places, bodies, words) and language contrasts, but not with the classic topographic organization of sensory cortex: retinotopy, tonotopy, and motion selectivity in area MT+. There is a clear architectural reason to expect retinotopy to fail: TRIBE's video features are averaged over space before the response head, whic...

---

### 19. Striatal Optogenetic Modulation Shifts Seizure Onset Timing: A Survival-Analysis Reanalysis with Effect Sizes, Permutation Validation, and Sensitivity Analysis

**Authors:** Siddhardha Nanda

**Published:** 2026-11-13

🔗 [Paper](http://arxiv.org/abs/2611.17795v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17795v1)

**Summary:** We present a worked methods vignette, not a novel biological claim: a reanalysis of the public dataset accompanying Hyder and colleagues' report that optogenetic activation and inhibition of the dorsal striatum bidirectionally control seizures, applying a time-to-event framework to the pilocarpine-induced status epilepticus (SE) arm, the only arm with genuine per-animal event-level data rather than aggregate statistics. The original study compared latencies with a Mann-Whitney U test (ChR2 vs GF...

---

### 20. Vision-Language Models Reproduce a Human Mental-Extrapolation Bias in the Watanabe Illusion

**Authors:** Eiji Watanabe, Kyohei Ueda, Kagayaki Kato, et al.

**Published:** 2026-11-13

🔗 [Paper](http://arxiv.org/abs/2611.17741v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17741v1)

**Summary:** Vision-language models (VLMs) are increasingly used for visual judgments, yet whether they share human perceptual biases, and where in the model such biases arise, is unclear. We addressed this with the Watanabe Illusion, a stimulus not previously studied quantitatively: an oblique segment inside a circle whose extension geometrically hits the topmost of 11 dots, yet human observers (n = 131) reported a dot near the middle of the column. Five VLMs (Qwen2.5-VL-32B and 7B, Claude Sonnet 4.6, GPT-5...

---

### 21. Neural Simulation-Based Inference for Computational Cognitive Models: A Tutorial

**Authors:** Ti-Fen Pan, Yi Cheng, Anne GE Collins

**Published:** 2026-11-13

🔗 [Paper](http://arxiv.org/abs/2611.17608v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17608v1)

**Summary:** Computational cognitive modeling is an increasingly essential methodology to elucidate the mechanisms underlying human and animal cognition. By fitting models to empirical data, researchers can perform parameter estimation, model comparison, and model-based neural analyses to assess competing theories, quantify individual differences, and investigate neural representations. Typically, fitting these models relies on likelihood-dependent methods (e.g., Maximum likelihood estimation or hierarchical...

---

### 22. Astrocyte Biocomputing: Astrocytic Contributions to Neural Network Computation

**Authors:** Kate M. O'Neill, Ian Whitehouse, Adam N. McCaughan, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17532v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17532v1)

**Summary:** Conductors are critical for the performance of an orchestra even though they do not emit sound. Basic research and clinical studies in the last decade are revealing that astrocytes may be the "conductors" of the "orchestra" that is the brain network: astrocytes make up approximately $50\%$ of all brain cells but do not emit electrical signals. Nevertheless, they may play critical roles in important cognitive brain functions, specifically learning, memory, and information processing. Here we cons...

---

### 23. Mean-field theory of neural networks: from spikes to firing rates

**Authors:** Tawan T. A. Carvalho, Matheus Haas, Denis D. Caprioti, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17512v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17512v1)

**Summary:** Connecting microscopic neuronal spiking to macroscopic brain function is a central challenge in computational neuroscience. Firing-rate models provide a framework for addressing this problem by describing neuronal activity at an intermediate level between individual spikes and large-scale population dynamics. Here, we introduce the foundations of firing-rate descriptions, formalizing their definitions through temporal, population, and trial averaging. We discuss experimental evidence for firing ...

---

### 24. Trainable sparse dendritic networks reveal regime-dependent roles for shunting inhibition and morphology

**Authors:** Houman Safaai, Maceo Richards, Ryan Whalen, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17434v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17434v1)

**Summary:** Neural circuits must compute with noisy inputs and adapt their responses to context. How dendritic structure and synaptic integration support these functions remains unclear. We introduce DendriNet, a trainable rate-based framework with sparse excitatory and inhibitory contacts, controllable dendritic architecture and alternative integration rules. In image-classification tasks, shunting networks transmit and rely on distal dendritic signals more strongly than additive networks. Distributing lim...

---

### 25. Structure-Preserving Leaky Integrate-and-Fire Dynamics on Arbitrary Time Scales

**Authors:** Billur Kaymakçalan, Behiye İlayda Selçuk

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17219v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17219v1)

**Summary:** The leaky integrate-and-fire (LIF) neuron combines a passive membrane law with threshold-triggered firing and reset. We formulate this hybrid neuron model, under constant input, on an arbitrary Hilger time scale $\mathbb{T}$. Our central result is that, after the first spike, the firing times satisfy $t_{n+1}=Π_{\mathbb{T}}^{+}(t_n+T_c)$, where $T_c$ is the classical reset-to-threshold travel time. This recursion requires no periodicity, homogeneity, or translation invariance of $\mathbb{T}$; it...

---

### 26. Random Exploration is Random

**Authors:** Yingkang Luo, Hua-Dong Xiong, Hanbo Xie, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.17011v1) | 📄 [PDF](https://arxiv.org/pdf/2611.17011v1)

**Summary:** Decision making often requires balancing exploitation of familiar options with exploration of uncertain alternatives. One strategy for exploration is random exploration, in which choices become more variable and less tied to the option that currently appears best. However, it remains unclear whether this variability reflects genuine stochasticity or instead a deterministic structure that traditional cognitive models fail to capture. We examined this question using the Horizon Task in an aggregat...

---

### 27. Dynamical mean-field theory of latching Potts networks

**Authors:** Anindita Basu, Carlo Orientale Caputo, Fernando Lucas Metz, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16999v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16999v1)

**Summary:** Spontaneous transitions between memories, as observed in internally generated cognition such as mind-wandering and free association, require neural dynamics capable of destabilizing one attractive memory state and moving towards another. We ask what minimal representational structure is required for such transitions to emerge in random associative networks. To address this question, we study Potts associative networks with $S$ active states per unit and slow adaptive thresholds. The $S=1$ case c...

---

### 28. On the minimum energy required to trigger a spike

**Authors:** Guanchun Tong, Rodolphe Sepulchre

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16915v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16915v1)

**Summary:** We formulate and numerically study the problem of finding the minimum energy required to trigger a spike in a three-dimensional conductance-based excitable model. The variational formulation seeks a state trajectory that reaches the boundary of the spiking region with the least \textit{peak} cumulative work supplied through the membrane port. We approximate voltage histories by sums of real exponentials, reducing the problem to a finite-dimensional optimization. The best-found voltage waveform c...

---

### 29. Similarity-Guided Optimization Strategies for Approximate Network Symmetry Detection

**Authors:** David Hartman, Jaroslav Hlinka, Dominik Klepl, et al.

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16555v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16555v1)

**Summary:** Symmetry in complex networks is a structural property with broad implications for network function, dynamics, and robustness. While classical approaches rely on exact automorphisms and thus remain highly sensitive to small perturbations, recent work of Liu has introduced approximate formulations that relax the strict invariance condition and recast symmetry detection as an optimization problem over permutations. We investigate how node-level similarity information can be used to bias the search ...

---

### 30. Exact power spectra and effective dimensionality in critical block-GOE networks

**Authors:** Konstantinos Grammenos, Dionissios Hristopulos

**Published:** 2026-11-12

🔗 [Paper](http://arxiv.org/abs/2611.16427v1) | 📄 [PDF](https://arxiv.org/pdf/2611.16427v1)

**Summary:** Criticality in neural networks is crucial for optimal information processing. Recent studies have shifted focus from static criticality to frequency-dependent behavior, particularly in oscillatory systems modeled by block-Gaussian orthogonal ensemble (block-GOE) matrices. However, analytical tools to predict spectral properties such as power spectrum and effective dimensionality remain scarce. In this work, we derive exact solutions for the network-averaged power spectrum $\operatorname{Tr}_{N}[...

---

### 31. Pyramidal Columns Acting as Attention Heads

**Authors:** Fabrizia Giulia Garavaglia, Marco Giunti

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.16057v2) | 📄 [PDF](https://arxiv.org/pdf/2611.16057v2)

**Summary:** Can the functional architecture of a Transformer attention head be given a biological construction? More specifically, could a suitable group of pyramidal columns in posterior temporal language regions (PTLRs) constitute the biological construction of a neuromorphic mechanical realization of an attention head, under a mathematical instantiation that need not coincide with its standard Transformer instantiation? This paper investigates this hypothesis by examining possible correspondences between...

---

### 32. Optogenetic Modulation Fraction: A Robust Opsin-Presence Effect and an Unresolved Cell-Type Question, by Censoring-Aware Survival Analysis of Public Neuropixels Data

**Authors:** Siddhardha Nanda

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.15606v1) | 📄 [PDF](https://arxiv.org/pdf/2611.15606v1)

**Summary:** Expressing channelrhodopsin-2 (ChR2) in an interneuron population substantially raises the fraction of locally recorded units whose spike timing is altered by light, relative to no-opsin controls, under every method tried. Establishing that result rigorously, and retracting two secondary claims that did not survive the same rigor, is this paper's actual content. We reanalyze eight public Allen Institute Neuropixels sessions (4,112 units), modeling light-to-first-spike latency as a right-censored...

---

### 33. Analysis choices decide whether untrained networks beat trained ones at V1: a multiverse analysis of model-brain RSA

**Authors:** Nils Leutenegger

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.15533v1) | 📄 [PDF](https://arxiv.org/pdf/2611.15533v1)

**Summary:** Untrained convolutional networks have been reported to rival trained networks as models of visual cortex, and we had reported an untrained-network advantage over backpropagation at V1 in THINGS fMRI, together with a dependence on evaluation resolution. Under a pre-specified ridge readout, the untrained network scored below the trained one at every pooling grid (median r difference -0.043 at g = 4, 0 of 5 seeds positive), and also in MSE skill and per-fold r. In exploratory analyses, across 36 co...

---

### 34. Alignment De-Identifies Without Aligning: A Congruence-Invariant Relational Gap in Cross-Subject Neural Representations

**Authors:** Anna Notaro, Letizia Rossato, Sadasivan Puthusserypady

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.15204v1) | 📄 [PDF](https://arxiv.org/pdf/2611.15204v1)

**Summary:** In brain-computer interfaces, inter-subject variability remains a major challenge that limits decoding performance across users. Subject-wise alignment is widely used to improve cross-subject transfer of neural decoders, yet it is typically evaluated only through decoding accuracy, which cannot determine whether aligned representations share greater task-related structure. We therefore distinguish two questions that accuracy conflates: whether alignment removes subject-specific information and w...

---

### 35. Prototypes of the Mind: A Unified Framework for Probing the Visual Brain

**Authors:** Shi Chen, Seoyoung Ahn, Doris Tsao

**Published:** 2026-11-11

🔗 [Paper](http://arxiv.org/abs/2611.15046v1) | 📄 [PDF](https://arxiv.org/pdf/2611.15046v1)

**Summary:** Deep learning has driven substantial progress in modeling fMRI responses, yet most existing approaches are optimized for a single objective---such as neural encoding, stimulus decoding, or post hoc interpretation---making it difficult to obtain a coherent account of neural representations. We introduce a unified framework that connects vision foundation models to brain activity while supporting neural analysis from multiple complementary perspectives. Our approach replaces black-box features wit...

---

### 36. Same currents, different field: $Δf = 0$ carrier-only stimulation is not temporal interference without the beat

**Authors:** Ido Haber, Giulio Tononi, Larissa Albantakis

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14839v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14839v1)

**Summary:** Carrier-only stimulation ($Δf = 0$) is generally considered the most rigorous control for temporal interference (TI) stimulation, assumed to reproduce TI's kilohertz carrier field without its low-frequency beat. We show that this assumption is incorrect: without the frequency difference, the carrier fields interfere coherently, changing the peak strength, power, and direction of the resulting field depending on electrode polarity and montage geometry. Using computational field modeling, we demon...

---

### 37. Mind-wandering preserves word-level coupling while disrupting comprehension

**Authors:** Anirudh Natarajan, Paul Sajda

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14814v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14814v1)

**Summary:** Readers can move their eyes through a page but retain little of its meaning when their minds wander. We tested whether word properties still guide their eyes during these lapses. We analyzed public eye-tracking and electroencephalography (EEG) data from 44 adults who read articles. They marked the text read during each lapse they noticed. We linked these spans to the sentences needed for later comprehension questions. Word frequency, length and surprisal still predicted which words readers skipp...

---

### 38. When Does the Real Wiring Win? Testing connectome structure-function claims against unmeasured physiology

**Authors:** Yeyuan Liu

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14508v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14508v1)

**Summary:** Connectome-constrained models are often used to argue that a measured wiring diagram outperforms shuffled or rewired wiring, and hence that structure shapes function. Such comparisons can confound wiring with how the models are tuned: a connectome fixes who connects to whom, not the excitability, gains or plasticity rates the model also needs, and modellers often tune these until the real-wiring model works. We separate three estimands: physiology tuned on the real wiring and transferred to null...

---

### 39. Measuring Robustness and Efficiency in a Connectome-Constrained Fly Visual System Model: Linking an Adversarial and a Perceptual Illusion

**Authors:** Alexandre Garcia-Duran, Alejandro Rodriguez-Garcia, Manuel Molano-Mazón, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14498v2) | 📄 [PDF](https://arxiv.org/pdf/2611.14498v2)

**Summary:** Biological visual systems compute reliably under tight metabolic and wiring constraints, whereas artificial vision systems consume far more energy and can be sensitive to adversarial perturbations. Whether networks with brain-like wiring are more robust at lower computational cost is unclear. We address this by benchmarking a task-optimized, continuous-time recurrent neural network of the fly visual system constrained by its synaptic connectome (FlyNet) against artificial neural networks. We com...

---

### 40. Optimization principles, revisited

**Authors:** William Bialek

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14381v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14381v1)

**Summary:** The brain solves a wide range of problems, and some of these solutions are very good indeed. It is an old idea that, in some cases, these solutions may be as good as possible given the relevant constraints. If this is true we can promote this notion of optimization to a principle from which aspects of function and mechanism can be derived, ideally with no free parameters. Optimization principles are powerful and have had many successes, but they remain controversial. We start with a reminder of ...

---

### 41. ScaleBrain: A Scale-Consistent Framework for EEG Foundation Models

**Authors:** Minyu Zhou, Yajing Wu, Yongqiang Tang, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.14035v1) | 📄 [PDF](https://arxiv.org/pdf/2611.14035v1)

**Summary:** Foundation models pre-trained on large unlabeled electroencephalography (EEG) corpora have emerged as a transformative paradigm for Brain-Computer Interface (BCI) applications. Recent EEG foundation models have shown that multi-scale representations derived from fixed-length patches can improve EEG representation learning. Existing frameworks commonly construct temporal scales through feature-level operations. However, these operations leave the correspondence between learned features and scale-...

---

### 42. Neuromodulation Through Intrinsic Noise

**Authors:** Sunghyun Koo, Jin Gyu Lee, Rodolphe Sepulchre

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13780v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13780v1)

**Summary:** Neuromodulation, the modulation of excitability through the regulation of neuronal parameters, is a key tool in neuromorphic control design. This paper investigates how spiking excitability can be modulated by intrinsic noise. Focusing on a simplified memristive neuron model, we show that intrinsic noise plays distinct functional roles depending on the feedback pathways: Intrinsic noise in the fast excitatory feedback shapes the nature of excitability and modulates the sensitivity of the neuron ...

---

### 43. Similar visual tuning conceals different recovery dynamics in a model of macaque V1

**Authors:** Xialei Huang, Qingyu Yan, Zheng Bian, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13692v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13692v1)

**Summary:** Biologically detailed neuronal networks can model how brain circuits perform observed functions, but their high computational cost limits the comparisons needed to test biological hypotheses. To address this limitation, we extend a multiscale approach in which responses of small populations of spiking neurons are computed in advance and reused across a larger cortical circuit. In particular, we approximate these local responses by deep neural networks and achieve an estimated acceleration of the...

---

### 44. A Functional Preservation Score for Auditing Connectome Operations: Compression, Alignment, Transport, and Local-Rule Writing

**Authors:** Praveg Vashishtha

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13681v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13681v1)

**Summary:** We introduce the Functional Preservation Score (FPS), a null-normalised, behaviourally grounded measure of how much of a neural network's input-output function survives a structural operation, and use it to audit the operations underlying speculative "mind-migration" pipelines on public data that runs on a single laptop. Across five pre-registered studies on the C. elegans connectome, whole-brain calcium activity, and hippocampal replay, FPS yields two positive characterisations and a three-part...

---

### 45. Human and Machine Annotations Predict Brain Responses to Naturalistic Movies Across Development

**Authors:** Yiran Huang, Zeyong Zhang, Rounak Rahman, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13637v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13637v1)

**Summary:** Naturalistic movie watching provides a powerful framework for studying dynamic brain function, but linking movie content to neural responses typically relies on labor-intensive human annotation. We investigated whether multimodal large language models (MLLMs) can provide scalable socio-affective and semantic annotations for naturalistic fMRI. We compared MLLM-generated theory-of-mind (ToM) and valence ratings with human ratings and with regional BOLD responses across three animated movies. For t...

---

### 46. Lightweight Deep Learning Framework for Astrocyte-Centric 3D Reconstruction across Normal and Stress-associated Ultrastructural States

**Authors:** Bowen Deng, Gwang-Jin Jeong, Seulgi Noh, et al.

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13581v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13581v1)

**Summary:** The morphology of astrocytes is closely associated with their ability to support and modulate neural circuit functions; however, its reconstruction from volume electron microscopy (vEM) data remains labor-intensive and computationally resource-intensive, placing substantial barriers on its broader adoption and scalability despite the high spatial resolution of vEM. We present AstroSeg-vEM, a lightweight, astrocyte-centric framework for morphology-preserving astrocyte segmentation, 3D reconstruct...

---

### 47. Orthographic depth at two scales, with English also matched for lexicon size

**Authors:** Adam Y. Shavit

**Published:** 2026-11-10

🔗 [Paper](http://arxiv.org/abs/2611.13400v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13400v1)

**Summary:** A reader can struggle to read in only one of their languages, and one proposed reason is how predictably spelling maps to sound. We measure that predictability as conditional entropy, the pronunciation uncertainty left once the spelling is seen, at two grain sizes (unit sizes): the alignment unit, an aligned spelling-sound chunk, and the syllable, bounded in the pronunciation. We analyse word lists in twelve alphabetic orthographies and report five in full, with English pronunciations from a dic...

---

### 48. A probabilistic model of visual segmentation explains early visual cortical dynamics

**Authors:** Tridib K. Biswas, Ruben Coen-Cagli

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.13316v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13316v1)

**Summary:** Neural dynamics are a central feature of biological neural systems. In the visual cortex, the functional role of neural dynamics is poorly understood, particularly for static stimuli. The statistics of still natural images have long been used by models that successfully predict firing in early visual cortex; those models assume that neurons represent inferences about latent image features, but often ignore the dynamics of said inference. Here, we test if inferential dynamics in images explain vi...

---

### 49. IC-GNN: Modeling Individualized Brain Community Organization for Disease Prediction

**Authors:** Yang Zhang, Xiao Zhou, Jonathan Warrell, et al.

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.13070v1) | 📄 [PDF](https://arxiv.org/pdf/2611.13070v1)

**Summary:** Brain networks exhibit modular organization, where community structures vary substantially across individuals and diseases. Understanding these individual differences is crucial for advancing both basic neuroscience research and precision medicine. However, widely used predefined group-level brain atlases often overlook this heterogeneity. While individualized functional parcellations capture subject-specific variability in community boundaries, they often require lengthy scan times to achieve f...

---

### 50. Qualiaphobic artificial neural networks (and why to build them)

**Authors:** Erik Hoel

**Published:** 2026-11-09

🔗 [Paper](http://arxiv.org/abs/2611.12809v1) | 📄 [PDF](https://arxiv.org/pdf/2611.12809v1)

**Summary:** This paper introduces qualiaphobic AI: artificial neural network architectures that are hostile to theories of consciousness. I show that qualiaphobia can be well-justified by knowledge about theories of consciousness, like when such theories are trivial or unfalsifiable or contradicted by overwhelming scientific evidence. It can also be justified by how theories of consciousness must be grounded in phenomenology, as well as how current popular theories of consciousness are applied to AI. I iden...

---

## stat.ML

**50 papers**

### 1. Fold Weighting for Cross-Validation Under Continuous Distributional Drift

**Authors:** Yegor Baranovski

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23184v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23184v1)

**Summary:** Cross-validation weights all folds equally, so under drift the oldest folds count as much as the newest. We model drift by a Hölder condition in total variation distance and give finite-sample bounds on the excess deployment risk of the configuration that sliding-window cross-validation selects. Each bound splits into drift, estimation, and validation-noise terms. With equal weights the drift terms saturate as the record grows. With fold weights fixed in advance, the drift terms become weighted ...

---

### 2. Amortizing Tempered Sampling with Corrected Self-Training

**Authors:** Hoang-Viet Nguyen, Hai-Dang Dau, Alexandre H. Thiéry

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.23072v1) | 📄 [PDF](https://arxiv.org/pdf/2611.23072v1)

**Summary:** Learning a neural sampler can reduce the cost of repeated sampling from an un-normalized distribution, but obtaining good training data remains difficult. We develop a corrected self-training scheme across a sequence of tempered targets, making use of importance sampling and Markov chain Monte Carlo to correct the samples and replay buffers to store them. We introduce Sequential Score Sampler (SSS) as a particular case. In SSS, the proposal is a score-based diffusion trained by regression on ene...

---

### 3. Symmetries of Counterfactuals: Identification and Testability of Counterfactual Maps from Covariate Heterogeneity

**Authors:** Marc Braun, Adel Daoud, Jose M. Peña

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22948v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22948v1)

**Summary:** In general, counterfactuals are not identified from data alone, because many causal models produce the same observed distributions but different counterfactuals. A common approach to circumvent this problem is to restrict the mechanism to a class in which it becomes unique, such as triangular monotone maps or optimal transport maps. However, whether the assumed class is correct is usually not examined. In this work, we study what the data can tell us when covariates are available that influence ...

---

### 4. Robust Actor-Critic Learning under Transport and Divergence Uncertainty

**Authors:** Kunqi Huang, Lican Kang, Hongrui Shu, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22759v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22759v1)

**Summary:** Learning reliable control policies requires accounting for uncertainty in transition dynamics and errors introduced by function estimation and action generation. We develop an actor--critic method for discounted robust Markov decision processes with continuous states and actions and an unknown nominal transition law. We consider transition uncertainty sets defined by Wasserstein distance, total variation, Kullback--Leibler divergence, or Pearson chi-square divergence. A conditional diffusion mod...

---

### 5. TRAIL-IRL: Crossed Reward-Temperature Mixtures for Unlabeled Trajectory Clustering

**Authors:** Yichen Zhu, Guanhua Fang, Ming Zheng

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22715v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22715v1)

**Summary:** Different paths need not imply different preferences, trajectories also differ in how randomly actions are chosen. Many multi-reward inverse reinforcement learning (IRL) methods assume common action randomness and can confound it with preference heterogeneity. We introduce TRAIL-IRL, which clusters unlabeled trajectories using rewards for preferences and temperatures for action randomness. Its crossed mixture pairs each reward with a shared set of temperature levels, allowing action regularity t...

---

### 6. The Price of Hard Coverage Constraints in Online Conformal Prediction

**Authors:** Mingrui Liu

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22646v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22646v1)

**Summary:** Conformal prediction provides distribution-free uncertainty quantification, but in sequential deployment, standard coverage guarantees can still allow substantial fluctuations in the number of miscoverages over time. We study an online setting in which prediction sets are produced one round at a time and the cumulative number of miscoverages must stay within a prescribed budget throughout deployment.Such a hard coverage guarantee can be enforced by enlarging prediction sets, but how much additio...

---

### 7. SOTA or Luck? The Winner's Curse in LLM Leaderboards

**Authors:** Sikun Xu, Raphael Thomadsen, Dennis J. Zhang, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22227v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22227v1)

**Summary:** Public LLM leaderboards guide model evaluation and adoption, yet the reported performance of top-ranked models can be systematically overstated. This leaderboard winner's curse arises because ranking noisy benchmark scores rewards sampling luck alongside genuine ability. The same selection effect can distort scores throughout the leaderboard, a phenomenon we call the rank-induced bias. We develop an $m$-out-of-$N$ bootstrap to correct for this bias. It assumes a fixed model pool with independent...

---

### 8. Training Neural Networks to be Locally Adaptive

**Authors:** Bilol Banerjee, Soham Sarkar

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22198v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22198v1)

**Summary:** Deep neural networks fitted by global empirical risk minimization commit to a single model for the entire covariate space. In a regression problem, if the regression function $f_0$ is inhomogeneous --- varying rapidly in one region, while being nearly flat in another --- no single model can be appropriate everywhere, and the fit degrades where the function varies most rapidly. Here we study an alternative in which, instead of fitting the network globally, we fit it locally. For each query point ...

---

### 9. Centroid Spectral Coupling: Implicit Alignment and Representation Diversity in Self-Supervised Learning

**Authors:** M. Hadi Sepanj, Benyamin Ghojogh, Saed Moradi, et al.

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22158v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22158v1)

**Summary:** Self-Supervised Learning (SSL) aims to align augmented views while preserving representation diversity and preventing collapse. Existing non-contrastive methods often address these goals using multiple weighted loss terms. We introduce Centroid Spectral Coupling (CSC), a single-term SSL objective that implicitly couples view alignment, representation diversity, and collapse resistance. CSC constructs centroids from independently normalized augmented-view pairs and applies a ridge-based spectral ...

---

### 10. Bandit Online Submodular Minimisation Using Zeroth-Order Oracles

**Authors:** Amir Ali Farzin, Philipp Braun, Iman Shames

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22130v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22130v1)

**Summary:** We consider online submodular minimisation under bandit feedback, where at each round a decision maker plays a subset and observes only its cost, while the cost functions, and hence their minimiser, change over time. Existing bandit methods only guarantee static regret, which compares against a single fixed subset and is a weak benchmark when the minimiser moves. This paper provides, to the best of our knowledge, the first method with guarantees for tracking a moving minimiser in this setting. W...

---

### 11. COSI: A Framework for Robustly Valid Inference

**Authors:** Arun K. Kuchibhotla, Sivaraman Balakrishnan, Larry Wasserman

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22096v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22096v1)

**Summary:** We introduce COSI (COnfidence from Scale Invariance), a framework for constructing confidence sets for statistical functionals. COSI builds on the HulC (Hull-based Confidence), which uses median unbiasedness to construct confidence sets from batch estimates. COSI uses scale-invariance properties shared by many common estimators. We divide the data into batches, compute an estimate in each batch, and retain each candidate parameter value for which the batch estimates pass a test of scale invarian...

---

### 12. Two Counterexamples for e-means

**Authors:** Zhenisbek Assylbekov

**Published:** 2026-11-17

🔗 [Paper](http://arxiv.org/abs/2611.22065v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22065v1)

**Summary:** e-means (Bessa et al., 2026) combines exponential averaging and cluster revival. We give two counterexamples to its published recipe with higher final loss than standard k-means (Lloyd, 1982) from identical initial centers. Mass-based revival can destroy a global optimum and make the ratio of expected losses unbounded even with k-means++ seeding.

---

### 13. Locally Linear Generalized Single Index Regression

**Authors:** Tristan Luca Saidi, Arun Kuchibhotla

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.22011v1) | 📄 [PDF](https://arxiv.org/pdf/2611.22011v1)

**Summary:** In this work we propose and analyze a procedure for estimating a generalized single-index regression model. This generalized single-index regression framework models the conditional mean of the responses $Y$ as a function of the covariates $X$ where the mapping is assumed to have the form $f \circ g$, where $g$ is $β$-Hölder with $β\geq 2$ and $f$ can be a discontinuous function of bounded variation. We propose a general procedure that operates under minimal assumptions about the distribution of...

---

### 14. DEFTS: Data-Efficient, Training-Free Few-Shot Learning for CLIP in the Text Subspace

**Authors:** Yijin Zeng

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.21993v1) | 📄 [PDF](https://arxiv.org/pdf/2611.21993v1)

**Summary:** Contrastive Language-Image Pre-training (CLIP) achieves impressive zero-shot image classification performance by comparing image embeddings against class-specific text embeddings. While recent few-shot methods leverage labeled training samples to improve upon this zero-shot baseline, they often predominantly rely on image embeddings and underutilize the semantic structure of the text embeddings. In this paper, we introduce DEFTS, a data-efficient, training-free few-shot classification method str...

---

### 15. Modeling Document and Section Hierarchies in Embedding Space

**Authors:** Kriste Krstovski, Sharyn O'Halloran, Kshitij Chandna

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.21980v1) | 📄 [PDF](https://arxiv.org/pdf/2611.21980v1)

**Summary:** Embedded topic models integrate word embeddings into the topic generation process, producing coherent topics and robust performance on large vocabularies. However, each document is represented by a single topic distribution, ignoring its internal structure. Many real world collections, including legal documents, company and government reports, and online discussion forums, exhibit hierarchical organization in which documents consist of multiple sections that often address distinct subtopics. We ...

---

### 16. Cancellation-Free Constrained SquareCB for Safe Controller Selection

**Authors:** Kartik Pandit, Sourav Ganguly, Arnob Ghosh

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.21880v1) | 📄 [PDF](https://arxiv.org/pdf/2611.21880v1)

**Summary:** We study constrained contextual bandits, in which a learner chooses one of $K$ actions in each round to minimize loss while keeping the expected cost of its play below a budget. Existing reductions to online regression weight the cost by a Lagrange multiplier learned from past constraint residuals, so slack in some rounds can offset violations in others. We instead run SquareCB proposed in \citep{foster2020beyond} with a rectified weight on the cost: it is zero when the estimated cost is within ...

---

### 17. Adaptive Memory for Online Reinforcement Learning under Sparse Model Changes

**Authors:** Sreejeet Maity, Sukanya Modak, Leonardo F. Toso

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.21879v1) | 📄 [PDF](https://arxiv.org/pdf/2611.21879v1)

**Summary:** We study the discounted reinforcement learning (RL) problem in a setting where the underlying environment changes between deployments. Each deployment provides $H$ observations from a fixed MDP. The reward function and transition kernel are fixed within each deployment. Across deployments, at most an $ε>0$ fraction of the reward and transition kernel entries may change. In this setting, learning each model to deploy from scratch may discard useful observations from past deployments, whereas pool...

---

### 18. Bias-Reduced and Parallel Heavy-Tailed Stochastic Convex Optimization in $\ell_p$ Geometries

**Authors:** Zhengyun Nie, Anant Shyam, Brian Bullins

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.21844v1) | 📄 [PDF](https://arxiv.org/pdf/2611.21844v1)

**Summary:** We consider the fundamental problem of parallel stochastic convex optimization (SCO), whose aim is to approximately minimize a convex objective when given the ability to query a moment-bounded stochastic gradient oracle multiple times in parallel per round. Whereas most previous results have focused on the variance-bounded Euclidean ($\ell_2$-norm) setting, meaning the objective is Lipschitz with respect to the $\ell_2$-norm over an $\ell_2$-bounded feasible set in $\mathbb{R}^d$, in this work w...

---

### 19. Optimal Autoregressive Chain-of-Thought Learning via Bagging

**Authors:** Awni Altabaa, John Lafferty, Omar Montasser

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.21597v1) | 📄 [PDF](https://arxiv.org/pdf/2611.21597v1)

**Summary:** We study how to learn an autoregressive next-token generator $f\colonΣ^\star\toΣ$ from a class $\mathcal{F}$, given chain-of-thought (CoT) demonstrations of length $T$ generated by $f$. We present a simple algorithm based on bagging, which outputs a majority vote of generators that are trained to be CoT-consistent on bootstrap samples of the training data. For binary token sets, it achieves the optimal sample complexity of $O((d_{\mathrm{VC}}+\log(1/δ))/ε)$, independent of the CoT length $T$, wh...

---

### 20. ONAM: Fitting Orthogonal Neural Additive Models for Post-Hoc Interpretability of Black-Box Predictions

**Authors:** David Köhler, Matthias Schmid

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.21550v1) | 📄 [PDF](https://arxiv.org/pdf/2611.21550v1)

**Summary:** Modern machine learning models, such as artificial neural networks, achieve high predictive performance through increasingly complex black-box architectures, limiting their use in settings where transparency, interpretability, and fairness are required. Here we present the R package ONAM, which provides a novel and practical implementation of functional decomposition, a technique to facilitate the interpretability of black-box models through structured effect representations. ONAM implements an ...

---

### 21. The cost of enforcing long-run coverage: a phase transition in online conformal prediction

**Authors:** Yu Gui, Rina Foygel Barber, Cong Ma

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.21542v1) | 📄 [PDF](https://arxiv.org/pdf/2611.21542v1)

**Summary:** Consider an online prediction setting, where at each time, we are given a new feature vector and asked to provide a prediction interval or prediction set that will likely contain the corresponding response. In this setting, if the data points are i.i.d. (or more generally, exchangeable), conformal prediction provides a mechanism for building valid prediction sets around the output of any trained model, offering coverage probability $\geq 1-α$ at each time $t$. In practice, however, issues such a...

---

### 22. Almost Controlled: The FDR of Benjamini-Hochberg on Weighted Conformal p-Values

**Authors:** Ryan Lim

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.21509v1) | 📄 [PDF](https://arxiv.org/pdf/2611.21509v1)

**Summary:** Weighted conformal p-values generalize conformal inference to cases with covariate shift. One way to use them is to pass them to the Benjamini-Hochberg (BH) procedure, either to decide which test units to select or to detect outliers. But weighted conformal p-values may not be positively dependent, so we want to know: does BH still control the false discovery rate (FDR) in finite samples? Based on experiments, it appears to, but we prove it doesn't. We give two counterexamples, certified in exac...

---

### 23. Differentiable Exact Learning

**Authors:** Hristo Papazov, Francesco D'Angelo, Nicolas Flammarion

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.21486v1) | 📄 [PDF](https://arxiv.org/pdf/2611.21486v1)

**Summary:** We introduce a framework for differentiable exact learning that couples an unbounded external environment to a state-tracking neural controller, which we train on policy-trajectory observations (PTOs): expert behavior traces that expose observations and actions while hiding internal states. In addition to the learning framework, we introduce Differentiable Finite-State Transducers (DFSTs) which use multilinear updates, support log-parallel training, and emulate arbitrary finite-state controllers...

---

### 24. Generative Data Augmentation Without External Data: An Empirical and Theoretical Study on Deep Networks

**Authors:** Daniel Kua, Yan Song

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.21467v1) | 📄 [PDF](https://arxiv.org/pdf/2611.21467v1)

**Summary:** Generative data augmentation adds samples from generative models to a classifier's training set. Many influential studies use generators pre-trained on large external datasets, and so mix the value of synthetic data with knowledge transferred through pretraining. We study the case without external data, where each generator learns only from the classifier's own training set, and ask when and why adding generated samples to that training set raises or lowers the classifier's test accuracy. We tra...

---

### 25. Comments on "Deep Fréchet Regression"

**Authors:** Jianbin Tan, Anru R. Zhang

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.21454v1) | 📄 [PDF](https://arxiv.org/pdf/2611.21454v1)

**Summary:** We discuss the Journal of the American Statistical Association (JASA) discussion paper "Deep Fréchet Regression" and explore an alternative perspective based on conditional flow matching. We propose learning covariate-dependent transport directly within the response space, avoiding separate manifold learning and reverse mapping. This perspective offers a potentially more flexible framework for incorporating geometric structure and modeling full conditional distributions.

---

### 26. Nonparametric Instrumental Kernel Regression: The Well- and Misspecified Setting Under General Link Conditions

**Authors:** Guillaume Baquet, Germain Van Bever

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.21391v1) | 📄 [PDF](https://arxiv.org/pdf/2611.21391v1)

**Summary:** We study nonparametric instrumental variable regression when the outcome takes values in a separable Hilbert space $\mathbb{Y}$, for instance a curve, a density or the kernel mean embedding of a distribution. The structural function solves an ill-posed operator equation whose conditional expectation operator need not be injective, and whose solutions need not belong to the hypothesis space. We analyse a two-stage kernel estimator that extends kernel instrumental variable regression to $\mathbb{Y...

---

### 27. High-probability Uniform Mixing via Dobrushin Contraction and Accelerated Hamiltonian Monte Carlo

**Authors:** Stefan Oberdörster

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.21305v1) | 📄 [PDF](https://arxiv.org/pdf/2611.21305v1)

**Summary:** Hamiltonian Monte Carlo, since its invention and subsequent rise to widespread use, has been motivated by its ability to accelerate convergence to equilibrium compared to diffusive methods, both in terms of dependence on condition number and dimension. In the present work, we establish this acceleration simultaneously in both aspects for critically damped Metropolis-adjusted kinetic Langevin with persistent uniforms. More precisely, for target measures $μ(dx)\propto e^{-U(x)}dx$ with $m$-strongl...

---

### 28. Compressed Simulation-Based Inference: Neural Posterior Estimation for Massive Data via Low-Dimensional Sketches

**Authors:** Michael Wieck-Sosa, Cosma Rohilla Shalizi

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.21286v1) | 📄 [PDF](https://arxiv.org/pdf/2611.21286v1)

**Summary:** Neural posterior estimation (NPE) is a popular Bayesian simulation-based inference (SBI) approach that uses neural networks trained on simulated data--parameter pairs to approximate the posterior given a user-chosen prior. For high-dimensional observations, NPE methods typically approximate the conditional density of the parameter given a user-chosen or learned summary statistic, rather than the entire dataset, due to the curse of dimensionality. However, both approaches face challenges: hand-cr...

---

### 29. In-Context Estimation and Prediction for Parametric ODEs

**Authors:** Abdullah Ahmed, Yun Yang

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.21268v1) | 📄 [PDF](https://arxiv.org/pdf/2611.21268v1)

**Summary:** Transformers have demonstrated the ability to perform in-context learning, that is, to adapt to new tasks from a few examples without updating their parameters. Existing theory has largely focused on emulating gradient-based algorithms for convex statistical problems or establishing general function approximation guarantees without exploiting the underlying statistical structure. We study in-context parameter estimation and trajectory prediction for parametric ordinary differential equations (OD...

---

### 30. Variance-adaptive confidence regions for fixed-benchmark binomial mixtures, with application to LLM evaluation

**Authors:** Kuancheng Ye

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.21266v2) | 📄 [PDF](https://arxiv.org/pdf/2611.21266v2)

**Summary:** We construct confidence intervals for linear functionals $θ(F_m)=\int h\,dF_m$ of the empirical law $F_m$ of success probabilities $p_1,\dots,p_m$, from independent counts $c_i\sim\mathrm{Bin}(n,p_i)$, as for a language model run $n$ times per problem. Coverage is at least $1-α$ for every $n$, $m$ and fixed $(p_i)$, simultaneously for all bounded $h$. The variance-adaptive (VA) region tests each candidate mixing law with the conditional variance of the tail counts it implies. This variance is li...

---

### 31. Dimension-free spectral laws and the risk of spectral filters

**Authors:** Chen Cheng

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.21254v1) | 📄 [PDF](https://arxiv.org/pdf/2611.21254v1)

**Summary:** Spectral properties of the sample covariance are key to modern machine learning with high-dimensional data. Random matrix theory (RMT) supplies powerful tools; however, most classical results assume proportional asymptotics, where $d/n$ tends to a finite limit. In functional data analysis and kernel methods, a fixed infinite-dimensional Hilbert space is often the more natural setting for the observations, beyond the scope of proportional asymptotics. This calls for a dimension-free spectral theo...

---

### 32. The Price of Choosing Examples: Context Overfitting in Adaptive In-Context Learning

**Authors:** Xiaoyu Li, Jiangxuan Long

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.21251v1) | 📄 [PDF](https://arxiv.org/pdf/2611.21251v1)

**Summary:** In-context learning is usually analyzed as if the examples in the prompt were sampled before the learner is chosen. In deployed systems they are not: examples are retrieved, filtered, re-ranked, edited, and repeatedly tested after seeing the query and the data store. We formalize this gap by treating prompt construction as adaptive data analysis through a conditional stochastic-kernel calculus. Our main quantity is the context capacity, the mutual information or approximate max-information betwe...

---

### 33. Anytime-Valid PAC-Bayes Certificates for Adaptive Test-Time Scaling

**Authors:** Xiaoyu Li, Jiangxuan Long

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.21241v1) | 📄 [PDF](https://arxiv.org/pdf/2611.21241v1)

**Summary:** Test-time scaling systems often choose how much to sample, which prompt to use, and which verifier or aggregation rule to trust after repeatedly inspecting a calibration set. Standard validation error bars are not valid after this adaptive selection. We model a test-time scaling recipe as a randomized predictor with a random cost and prove a time-uniform PAC-Bayes certificate that holds simultaneously over all calibration times, all posterior mixtures over recipes, and all data-dependent stoppin...

---

### 34. Summary Sufficiency in Simulation-Based Inference via Mutual Information

**Authors:** Renjie Peng, Christian Genest, David A. Stephens

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.21158v1) | 📄 [PDF](https://arxiv.org/pdf/2611.21158v1)

**Summary:** Simulation-based inference (SBI) enables posterior estimation when the likelihood is intractable but data can be simulated from the model. For high-dimensional or variable-length data, SBI methods typically rely on low-dimensional summary statistics as conditioning inputs for posterior estimation, making their sufficiency crucial for accurate inference. Mutual information (MI) provides a natural information-theoretic characterization of sufficiency, quantifying how much parameter information a s...

---

### 35. The Limits of Closed-Form Couplings for Few-Step Generation

**Authors:** Tobias Höppe, Stefan Bauer, Qiang Liu, et al.

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.21119v1) | 📄 [PDF](https://arxiv.org/pdf/2611.21119v1)

**Summary:** Few-step generators via flow models require complicated technical solutions such as a pretrained flow model or a consistency loss. While rectified flows have gained popularity for their success in few-step sampling, they pay a cost of needing a pre-trained model and sampling a large number of couplings per dataset. Yet for a finite dataset and a Gaussian probability path, the probability-flow vector field of the empirical distribution is available in closed form, so one could use this field as t...

---

### 36. CONGA: Compiling Gaussian Fiber Geometry for Structured Bayesian Inference

**Authors:** Víctor Gallego

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.20995v1) | 📄 [PDF](https://arxiv.org/pdf/2611.20995v1)

**Summary:** In structured Bayesian models, a large latent block is often Gaussian conditional on a smaller set of parameters, yet generic inference methods relearn this geometry during warmup. We study how this structure can be used to construct transports for posterior inference. The conditional mean and precision determine exact affine maps, including symmetric Brenier and triangular Knothe-Rosenblatt maps, that separate a standard normal block from the remaining non-Gaussian core. KL and relative Fisher ...

---

### 37. FARCH: A Functional ARCH Model for Calibrated Prediction Bands

**Authors:** Mohamed Chaouch

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.20972v1) | 📄 [PDF](https://arxiv.org/pdf/2611.20972v1)

**Summary:** Forecasting a curve, rather than a handful of scalar summaries of it, requires a notion of uncertainty that is itself functional. We propose FARCH, a functional nonlinear autoregressive model with conditional heteroscedasticity, in which the conditional mean and the conditional volatility of the next curve are forecasted jointly and nonparametrically, by reusing a single kernel weighting scheme --- built on a wavelet semi-metric between curves --- first on the curves themselves and then on their...

---

### 38. A Convergence Analysis of the Random Feature Method for Linear PDEs

**Authors:** Jingrun Chen, Yixin Luo, Xiaojun Peng

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.20951v1) | 📄 [PDF](https://arxiv.org/pdf/2611.20951v1)

**Summary:** The Random Feature Method (RFM) distinguishes itself among machine learning approaches to partial differential equations (PDEs) through its superior accuracy and computational efficiency. Nevertheless, the theoretical underpinnings of RFM remain incompletely elucidated. This paper provides a comprehensive analysis of RFM within the framework of kernel methods, focusing on two principal aspects: (i) approximation by finitely many random features in Sobolev norms and the PDE residual seminorm, and...

---

### 39. Enhancing Mixed Oil Length Prediction through Graph Representation Learning

**Authors:** Xinyi Hong, Hai Shu, Zhaoyang Zhang, et al.

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.20660v1) | 📄 [PDF](https://arxiv.org/pdf/2611.20660v1)

**Summary:** During the pipeline transportation of refined oil products, the inevitable formation of mixed oil segments poses considerable economic challenges to pipeline networks. Therefore, it is important to accurately predict the length of these mixed oil segments. Although previous methods have achieved relatively accurate predictions by integrating machine and deep learning algorithms, they ignore the statistical dependencies that remain among real-world mixed oil samples, which degrades model accuracy...

---

### 40. Calibrated Functional Prediction from Overlapping Nonlinear Observations

**Authors:** Peida Li

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.20567v1) | 📄 [PDF](https://arxiv.org/pdf/2611.20567v1)

**Summary:** We study prediction of nonlinear audit functionals from scalar observations of a shared hidden table state. For Schur-rational operators, local Gaussian projections yield a common sparse kernel for overlapping tasks, repeated row identities, and cross-row dependence. Shared-state residual samples extend this kernel through a positive-semidefinite feature representation. Positive matrix integration and sample-value enclosures connect the original inputs to the actual saved hybrid prediction. A so...

---

### 41. Decorrelation Before Variable Selection: Left and Right Transforms and Their Trade-Off

**Authors:** Mahdi Nouraie, Samuel Muller

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.20420v1) | 📄 [PDF](https://arxiv.org/pdf/2611.20420v1)

**Summary:** Decorrelation has two forms. A left transform keeps coefficients and changes noise; a right transform keeps noise and changes coefficients. Cholesky whitening alone keeps noise variables inactive when true ones come first; decorrelation preserving coefficients and noise loses information.

---

### 42. High-dimensional transfer learning with unaligned ordinal responses

**Authors:** Ruopei Fu, Ying Yang

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.20411v1) | 📄 [PDF](https://arxiv.org/pdf/2611.20411v1)

**Summary:** In this work, we study high-dimensional transfer learning with unaligned ordinal responses, allowing different domain-specific regression coefficients, cumulative links and thresholds. We develop the sample-split and full-target algorithms that pool source and target likelihoods and then estimate a target correction. Under suitable conditions, our algorithms achieve minimax-optimal rates for parameter estimation and excess risk. Simulations favor the full-target algorithm over the sample-split a...

---

### 43. Generalized Prediction Set with Bandit Feedback

**Authors:** Zhou Wang, Xingye Qiao

**Published:** 2026-11-16

🔗 [Paper](http://arxiv.org/abs/2611.20387v1) | 📄 [PDF](https://arxiv.org/pdf/2611.20387v1)

**Summary:** In high-stakes environments where uncertainties abound, set-valued prediction offers a cautious and robust mechanism by presenting multiple potential labels as the prediction for each test instance to mitigate the potential risk associated with prediction errors. Yet, integrating this paradigm with out-of-distribution (OOD) detection remains scarcely explored in such settings as online learning with bandit feedback. The bandit feedback mechanism informs the learner about the correctness of the p...

---

### 44. Measuring Coherence in Predictive Models

**Authors:** Jamie Reason, Vik Shirvaikar, Mark van der Wilk, et al.

**Published:** 2026-11-15

🔗 [Paper](http://arxiv.org/abs/2611.20325v1) | 📄 [PDF](https://arxiv.org/pdf/2611.20325v1)

**Summary:** Many sequential decision-making procedures, such as active learning, implicitly assume that a model's current predictions agree with those it expects to make after updating on new data, a property we call coherence. Most models in use do not update by exact conditioning and are not guaranteed to be coherent, which can lead to worse decisions. Yet there is currently no general way to measure incoherence or to tell when it matters. We develop tools to measure incoherence and characterise when it a...

---

### 45. The Manifold-Index Model: provably and efficiently avoiding the statistical and computational curse of dimensionality

**Authors:** Yantao Wu, Mauro Maggioni

**Published:** 2026-11-15

🔗 [Paper](http://arxiv.org/abs/2611.20275v1) | 📄 [PDF](https://arxiv.org/pdf/2611.20275v1)

**Summary:** We study vector-valued regression with predictors filling a tube around an unknown $m$-dimensional manifold $\mathcal{M}$ in $\mathbb{R}^D$. In the Manifold-Index Model, the mean response is $F=f\circΠ_{\mathcal{M}}$, where $Π_{\mathcal{M}}$ is the nearest-point projection onto $\mathcal{M}$ and $f:\mathcal{M}\to\mathbb{R}^p$ is a possibly non-injective link function. Multiscale ANisotropic lOcal Regression (MANOR) estimates tangent planes by multiscale PCA of predictors with similar responses, ...

---

### 46. Integrating Latent Block Models into Variational Autoencoders for Disentangled Representation Learning

**Authors:** Anasse Essalih, Reda Khoufache, Laurent Durville, et al.

**Published:** 2026-11-15

🔗 [Paper](http://arxiv.org/abs/2611.20253v1) | 📄 [PDF](https://arxiv.org/pdf/2611.20253v1)

**Summary:** We introduce LBM-VAE, a novel framework that integrates Latent Block Models (LBMs) into Variational Autoencoders (VAEs) to jointly cluster observations and latent dimensions. Beyond its clustering capabilities, LBM-VAE provides a block-structured latent representation that naturally supports disentangled representation learning. In contrast to conventional approaches that associate each factor of variation with an individual latent dimension, our framework allows factors of variation to be encod...

---

### 47. Does Learning Order Explain Forgetting? The Lie Bracket as an Early-Warning Signal for Catastrophic Forgetting Without Old Data

**Authors:** Ephraim Kofi Ayi Kwapong

**Published:** 2026-11-15

🔗 [Paper](http://arxiv.org/abs/2611.20087v1) | 📄 [PDF](https://arxiv.org/pdf/2611.20087v1)

**Summary:** A network trained on task A and then task B ends at different weights than one trained on B and then A. To leading order this gap is set by the Lie bracket of the two tasks' gradient fields, and Dherin (2023) conjectured that a non-vanishing bracket may be linked to catastrophic forgetting. I test this conjecture empirically. Across Split MNIST, Split Fashion-MNIST and Split CIFAR-10, the forgetting of A is almost exactly the difference in A's loss between the two training orders (Spearman rho =...

---

### 48. Weighted conformal prediction under covariate shift: process limits, estimated weights and efficiency

**Authors:** Mehrdad Pournaderi

**Published:** 2026-11-15

🔗 [Paper](http://arxiv.org/abs/2611.20052v1) | 📄 [PDF](https://arxiv.org/pdf/2611.20052v1)

**Summary:** Weighted split conformal prediction handles covariate shift by reweighting calibration scores with the likelihood ratio $v=dQ_X/dP_X$; its training-conditional coverage is a functional of the self-normalized weighted empirical distribution function $\hat F_m$, and we study the process $\sqrt m(\hat F_m-F_Q)$. It converges in $\ell^\infty$ to the Gaussian process $W(G(t))-F_Q(t)W(K^2)$, with $G(t)=\mathbb{E}_Q[v\mathbf{1}\{S\le t\}]$ and $K^2=1+χ^2(Q\|P)$, if and only if $χ^2(Q\|P)<\infty$ (for n...

---

### 49. Certified Algorithms for Gaussian Location Mixture NPMLEs via Discretized Gradient Flows

**Authors:** Pranav Gupta, Satyaki Mukherjee

**Published:** 2026-11-15

🔗 [Paper](http://arxiv.org/abs/2611.19882v1) | 📄 [PDF](https://arxiv.org/pdf/2611.19882v1)

**Summary:** We study the computation of approximate nonparametric maximum likelihood estimators (NPMLEs) for Gaussian location mixtures in arbitrary dimension $d\ge 1$ via the Fisher-Rao gradient flow. We provide a certified algorithm based on an entropic proximal discretization of the flow which, given a sufficiently small $\varepsilon > 0$, returns an absolutely continuous mixing measure $\tildeμ$ admitting an exact finite-dimensional representation and satisfying $\hat L_n-L_n(f_{\tildeμ})\le\varepsilon$...

---

### 50. Sharp Gaussian Approximation for Q-Learning

**Authors:** Xingtu Liu

**Published:** 2026-11-15

🔗 [Paper](http://arxiv.org/abs/2611.19850v1) | 📄 [PDF](https://arxiv.org/pdf/2611.19850v1)

**Summary:** Gaussian approximation provides a foundation for online statistical inference in reinforcement learning. We establish sharp non-asymptotic Gaussian approximation rates in Wasserstein distance for asynchronous Q-learning with Polyak-Ruppert averaging. We prove an upper bound of $\widetilde{O}(n^{-1/4})$, where $n$ is the number of iterations, together with a matching lower bound up to logarithmic factors. Q-learning is more challenging to analyze than linear stochastic approximation due to the no...

---

