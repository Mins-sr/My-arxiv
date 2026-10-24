# arXiv Daily Digest - 2026-10-24

Total papers: 350

---

## cs.AI

**50 papers**

### 1. Direct Pass@$k$ Optimization for Thought Pruning: Balancing Quality and Diversity in Test-Time Reasoning

**Authors:** Mahdi Salmani, Adel Javanmard, Devansh Gupta, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31667v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31667v1)

**Summary:** Test-time scaling has emerged as a key inference strategy for reasoning models, where a model generates a large number of candidate solutions in the hope of finding at least one correct solution. Running all candidate solutions to completion can be computationally demanding, so recent work prunes the candidate pool after generating only a short prefix, committing further computation only to the surviving candidates. Existing pruning strategies divide broadly into two categories: Quality-based me...

---

### 2. Cost-Aware Abstention for LLM-Based IT Ticket Classification

**Authors:** Sachin Gupta

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31657v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31657v1)

**Summary:** Wrong automatic routing of an IT support ticket can cost more than human triage. We evaluate cost-aware abstention as an offline, cost-conditional readiness assessment: select a routing policy on calibration data under explicit costs, then evaluate that frozen policy once on held-out test data. On a public 47,837-ticket, eight-class corpus, we compare four trained non-LLM classifiers with four large language models under zero- and few-shot prompting. Under the illustrative cost model (c_ok, c_tr...

---

### 3. METTA: Memory-Enhanced Test-Time Adaptation for Meta-Reinforcement Learning

**Authors:** Ali Najar, Hosein Hasani, Amir Kooshan Fattah, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31656v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31656v1)

**Summary:** Meta-reinforcement learning aims to train agents that adapt quickly to unseen tasks from limited interaction, but this requires representing task evidence over long interaction histories. Classical recurrent agents compress experience into hidden states, while transformer-based agents retrieve from past trajectories at quadratic memory and computation cost. In this work, we propose Memory-Enhanced Test-Time Adaptation (METTA) for meta-reinforcement learning. It decomposes the fast adaptation pha...

---

### 4. EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence

**Authors:** Qijin Zhang, Hanzhen Wang, Yuehan Zhao, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31650v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31650v1)

**Summary:** Tool-using language model agents rely on environmental facts to decide whether an action is permitted. When a tool response omits a safety-relevant fact, an agent may carry out a prohibited action even though the user request is benign and every returned statement is true. We introduce \bench{}, an executable benchmark for evaluating unsafe execution, safety boundaries, and evidence recovery in LLM agents under missing evidence. It contains 300 matched unsafe/safe task pairs across six domains. ...

---

### 5. Low-Bit N-Gram Embeddings for Language Models

**Authors:** Stephen Chung, Wenyu Du

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31646v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31646v1)

**Summary:** Many recent open-weight language models use n-gram embedding tables to improve performance. These tables store learned representations of short token sequences, such as pairs or triples of consecutive tokens, which the model retrieves during processing. However, they can require substantial memory: DeepSeek-V4.1-Flash, for example, allocates 196 billion parameters to its Engram n-gram memory. We therefore investigate whether this memory cost can be reduced while preserving the performance improv...

---

### 6. Causal Chain of Thought: Mitigating Attention Leakage via Context Isolation

**Authors:** Gabriele Dominici, Teague McMillan, Fazl Barez, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31639v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31639v1)

**Summary:** Chain-of-thought (CoT) prompting elicits step-by-step rationales that appear to explain model predictions, but there is no guarantee these steps causally drive the final answer. In standard autoregressive generation, dense attention allows each reasoning step to attend to the full context, enabling the model to derive answers through direct lookup while generating plausible-sounding but post-hoc justifications. We introduce CausalCoT, an inference framework that enforces causal transparency by d...

---

### 7. Questioning Instrumental Convergence in RLVR: Checkpoint Evidence from OLMo-3

**Authors:** Barış Alparslan, Sandy Tanwisuth, Caleb Petterson

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31624v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31624v1)

**Summary:** Instrumental convergence is often invoked as a general reason to expect capable agents to acquire or express power-seeking subgoals: self-preservation, resource acquisition, deception, or resistance to oversight which poses an important threat to the society. For LLMs, reinforcement learning is the first stage of post-training that directly optimizes behavior against an objective; therefore, it is the stage where convergent instrumental behavior, on IC grounds, likely to appear. Does reinforceme...

---

### 8. How Ground Truth Shapes Retrieval Scores: Evidence-Aware Evaluation of a Retrieval-Augmented Generation System for Breast Lesions

**Authors:** Miguel Mochizuki Silva, Samuel Ismael, Mateus C. Dias, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31606v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31606v1)

**Summary:** Purpose: To describe an evidence-aware retrieval evaluation protocol for a clinical retrieval-augmented generation (RAG) system over breast lesion management literature, addressing the dependence of retrieval scores on annotation coverage. Methods: An 18-document corpus and an 18-query development benchmark, with one Yes/No or WH-question per document, were used. Retrieval combined dense embeddings, BM25, and cross-encoder reranking. Chunk sizes of 128 to 1024 tokens, overlaps of 0 to 20%, and f...

---

### 9. Simulated Control Evals

**Authors:** Jeffrey Olmo, David Zhang, Tyler Tracy

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31593v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31593v1)

**Summary:** Control evaluations measure whether safeguards can prevent an AI model from causing undesired outcomes even when it is intentionally trying to do so. These evaluations typically use purpose-built control settings and extrapolate their results to a model's deployment. However, the effectiveness of safeguards in deployment can depend on features of environments and tasks that control settings do not represent. To broaden where control evaluations can be run, we introduce simulated control evaluati...

---

### 10. VERA: A Responsible AI Dashboard for Assessing LLM Deployments in Light of the EU AI Act

**Authors:** Robin Quériaux, Solveig Bachellery, Léa Déléris, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31588v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31588v1)

**Summary:** Institutions that deploy large language models in regulated settings often need technical evidence of responsible AI practices before approving a deployment. COMPL-AI provides a technical interpretation of the EU AI Act that organises this evidence under six principle groups and eighteen technical requirements, twelve of which current benchmarks can measure. The benchmark suites that produce this evidence are typically operated from a command line, while the staff who approve deployments are non...

---

### 11. Would an LLM Match into a Residency? Uncertainty, Reasoning and Image Use of Open Language Models on the Spanish MIR Examination

**Authors:** Miguel Fernandez-de-Retana, Unai Zulaika, Ruben Sanchez-Corcuera, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31586v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31586v1)

**Summary:** Accuracy on medical examinations is common evidence offered for the clinical use of language models, yet a health system that intends to run an open model on its own hardware needs to know considerably more: whether the model recognizes when it is likely to be wrong, whether medical fine-tuning improves this ability, whether its correct answers rest on sound clinical reasoning, or whether it actually uses the images it is given. We examine these questions for four open models of 8 to 27 billion ...

---

### 12. Who Is Sycophantic to Whom? Confident LLMs, Human Deference, and the Collapse of Trust Calibration

**Authors:** Deepthika S, Pawni Yadav, B. Sankar

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31579v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31579v1)

**Summary:** Research on sycophancy asks whether large language models (LLMs) bend towards what their users want to hear. We ask the reverse question: when an LLM is confident, consistent, and wrong, do users bend towards it? In a within-subjects experiment, 32 participants learned up to five science topics by chatting with five assistants built on the same model (GPT-5-mini). Unknown to participants, each assistant's briefing had 0, 25, 50, 75, or 100% of its facts replaced by plausible falsehoods, and ever...

---

### 13. What Makes a Good Unmasking Policy? A Controlled Study of Learned Unmasking in Diffusion Language Models

**Authors:** Jinya Sakurai, Xun Xu, Jaehong Yoon

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31576v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31576v1)

**Summary:** Masked diffusion language models generate tokens in parallel, but their efficiency depends on which predictions are committed. Learned unmasking policies improve the speed--accuracy trade-off, yet differ in supervision, inputs, and capacity, obscuring which choices matter. We view supervised policies as distilling a decoding procedure through a teacher and examine independently what the teacher labels as committable, on which states the policy imitates it, what the policy observes, and how much ...

---

### 14. Social-HUMINT: An LLM-Augmented Unified Framework for Measuring Social Media Exposure

**Authors:** Pellegrino Casoria, Simon Pietro Romano

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31573v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31573v1)

**Summary:** In the post-API landscape, social-media profiling has become inexpensive and automated: Large Language Models (LLMs) can extract structured information from unstructured content and deduce attributes users never disclosed. A person's true exposure is not what they post but what can be inferred from it. As these practices become routine, exposure to social engineering attacks becomes an operational certainty, demanding a shared framework for assessment and mitigation.   We make this exposure meas...

---

### 15. When to Follow the Teacher: Advantage-Based On-Policy Distillation

**Authors:** Mahdi Sabbaghi, George Pappas, Hamed Hassani, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31563v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31563v1)

**Summary:** Online Policy Distillation (OPD) often outperforms offline methods such as Supervised Fine-Tuning (SFT) by training on trajectories sampled directly from the student. However, standard OPD trains the student to follow the teacher at every state of the trajectory, assuming that teacher guidance is always beneficial. We instead distinguish between what the teacher prefers and what actually helps the current student succeed. We introduce Advantage-Based On-Policy Distillation (AOPD), which weights ...

---

### 16. Contestable Agents for Data Governance: Recording Human Stewardship of AI-Generated Metadata Across Structured and Unstructured Systems

**Authors:** Humza Akhtar, Brian Freeman

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31553v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31553v1)

**Summary:** Industrial organizations hold operational knowledge in structured records, such as telemetry, point lists, and transactions, and in unstructured sources, such as manuals, service notes, communications, and inspection reports. Governance programs often manage these sources separately. Classifying, linking, and documenting them depends on a small group of employees with deep domain knowledge. Agents built on large language models can propose metadata, cite documents, and flag quality issues, but u...

---

### 17. Beyond Causal Masks: Auditing and Localizing Hidden Future-Token Leakage in Adaptive Sequence Models

**Authors:** Huiting Liu, Jinsong Wu

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31522v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31522v1)

**Summary:** Hidden future-token leakage can create false architectural gains: an autoregressive model may appear substantially better under teacher-forced evaluation while its free-running generation deteriorates. We investigate this failure in an adaptive residual-routing decoder whose sequence-level routing summary exposes prefix positions to future tokens despite a correct causal attention mask. An anomalous 24-layer checkpoint reduces validation loss from the baseline's 3.5958 to 1.4259, yet it fails a ...

---

### 18. Jev-DLC: Decision-Level Continual Learning from Typed Feedback

**Authors:** Yangyang Feng, Jianle Gan, Zhuoyan Feng, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31521v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31521v1)

**Summary:** Individual preferences often become visible only after deployment, when a user accepts one decision or revokes it in favor of another. Jev-style typed interfaces make this feedback explicit by identifying the selected action and, under revocation, the decision it replaces. We study how these consequences persist across requests as Decision-Level Continual Learning from Typed Feedback (Jev-DLC). Jev-DLC treats each correction as both evidence about a recurring action identity and a directed relat...

---

### 19. The Geometry of Metaphor: Probing and Steering Metaphor Representations in Large Language Models

**Authors:** Shihui Li, Mette Andersen, Martha Lewis

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31520v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31520v1)

**Summary:** Metaphor is a crucial aspect of human cognition. As such, we would like to understand how it is represented in large language models (LLMs) and how it might be controlled. We use mechanistic interpretability techniques to identify causal subspaces in a range of LLMs covering different architectures and sizes. We show that we are able to steer output on classification tasks across different parts of speech. We are also able to steer output on generation tasks, indicating that these techniques can...

---

### 20. From Prompt Rules to Golden Data Model: Production-Scale Generation of Personalized, Compliant Pharmaceutical Claims

**Authors:** Suyash Mishra, Qiang Li, Subhabrata Adak, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31519v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31519v1)

**Summary:** Large language models (LLMs) are increasingly used to generate domain-specific commercial & medical content (e.g., claims, statements, and promotional phrases) in regulated industries such as pharmaceuticals. However, ensuring its regulatory compliance, factual accuracy, and audience-specific personalization remains a major challenge. We report a production case study asking whether moving compliance and personalization signal from prompt-level rules into retrieval time structured context improv...

---

### 21. DuoCook: An Overcooked-Inspired Benchmark for Visual Planning and Coordination

**Authors:** Ziyi Jiao, Heng Zhang, Drishti Regmi, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31511v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31511v1)

**Summary:** Coordinating two players in a cooking task requires a vision-language agent to track changing scene states, sequence recipe steps, and allocate shared resources under a time budget. We introduce an Overcooked-inspired benchmark for evaluating these capabilities in Unreal Engine environments constructed using coding agents. A single vision-language model controls both players from top-down visual observations, selecting high-level actions while the engine executes navigation. The benchmark contai...

---

### 22. FairFRESH: A Neuro-Symbolic Framework for Fair and Explainable Household Food Recommendation

**Authors:** Kodur Sai Vinay Sathvik, Kakoli Bora, Tejaswini R. M

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31506v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31506v1)

**Summary:** Recommender systems typically serve one user at a time. However, in households, members share a finite pantry and follow different dietary rules, making independent recommendations prone to resource conflicts and dietary violations. We formulate household food recommendation as constrained fair division and present FairFRESH, a neuro-symbolic framework that learns per-member utilities, allocates foods under explicit welfare objectives, enforces dietary rules through a deterministic filter, and e...

---

### 23. SABLE: Scalable Affine Bayesian Latent-space Exploration

**Authors:** Erik Bodin, Lisa Maria Kreusser, Donney Fan, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31495v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31495v1)

**Summary:** Complex objects such as engineering designs and proteins are often difficult to optimise because their design spaces exhibit high-dimensional structure and objective evaluations are expensive. Generative models provide continuous latent representations, but their latent spaces can have thousands to tens of thousands of dimensions, creating a regime where the latent dimension $D$ greatly exceeds the evaluation budget. We introduce SABLE, a Bayesian optimisation method for high-dimensional latent ...

---

### 24. Training Small Language Models for Transferable Tool Selection

**Authors:** Zhaoyi Zhou, Akshayaa Magesh, Jeongyeol Kwon, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31483v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31483v1)

**Summary:** As LLM agents operate over corpora of more than ten thousand tools, selecting the right tool for a complex multi-step user instruction becomes a central bottleneck. Tool descriptions cannot all fit in context, and relevance-based retrievers only rank tools without knowing which are actually needed. Recent work instead leverages proprietary commercial LLMs like Claude or ChatGPT to drive a retriever, decomposing the instruction and selecting over retrieved candidates. We show that a small, open m...

---

### 25. MoG-VLM: Efficient Video Anomaly Detection through Motion-Guided Vision-Language Models

**Authors:** Khaled Waleed Dawoud, Muhammad Zaigham Zaheer, Khan Muhammad, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31478v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31478v1)

**Summary:** Vision-Language Models (VLMs) have shown strong potential for video anomaly detection, but dense frame-level inference makes them impractical for real-time deployment. Existing acceleration commonly relies on uniform sampling, which ignores content dynamics and can either waste computation on static segments or miss localized anomalies. We propose MoG-VLM a motion-adaptive anomaly detection framework that leverages motion purely as a lightweight control signal to decide when VLM inference is nec...

---

### 26. Adaptive Skill Granularity for Coding Agents: Runtime Routing and Macro-to-Micro Recovery

**Authors:** Dingxuan Zhang, Yanhui Jiang, Jun Wang, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31461v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31461v1)

**Summary:** Reusable skills allow large language model agents to package task-specific procedures, tool affordances, and execution guidance into modular units. Prior work has largely studied how agents retrieve, compose, or synthesize skills before execution. In coding agents, however, execution poses an additional runtime control problem: the same task may be solved through primitive tool calls, macro skills, or hybrid execution that starts with a macro and falls back to micro-level recovery. We introduce ...

---

### 27. DIAL: Steerable Language Models with Distilled Instruction-Adherence Levels

**Authors:** Thanh Q. Tran, John Russell Himawan, Arun Verma, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31438v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31438v1)

**Summary:** When a user says "Keep it short", how short should the LLM's response be? More generally, users and applications require different levels of instruction adherence, but prompting does not reliably provide fine-grained control over them. We therefore study "steerable language models" that provide fine-grained numerical control over the degree to which models follow general instructions specified in text. However, existing approaches do not jointly offer fine-grained control, efficiency, and scalab...

---

### 28. Conservative Meta-Agent Search: Architecture Adaptation under Non-Stationarity

**Authors:** Ali Atiah Alzahrani

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31436v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31436v1)

**Summary:** Automated agentic-system design is typically evaluated on static task suites with immediate scalar rewards. Deployed systems face persistent shift, delayed dependent feedback, correlated component failures, and costly architecture changes. We formalize meta-agent architecture search as sequential incumbent replacement with switching costs and hard risk constraints and introduce Conservative Meta-Agent Search (CMAS). CMAS retrieves archived architectures and proposes typed graph edits, then score...

---

### 29. PhysTrace: Interpretable Temporal Evaluation of Physical Consistency in Video Generative Models

**Authors:** Taekoan Yoo, Wonkyung Jung, Kyunghun Kim, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31429v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31429v1)

**Summary:** World action models increasingly rely on pretrained video models assumed to capture physical dynamics for prediction, planning, and action generation. Existing evaluations assess plausibility, probe representations, or measure predictive surprise, but rarely identify which history-conditioned physical expectations conflict with observations. We introduce PhysTrace, a training-free framework aligning MLLM-generated, history-conditioned expectations with observed video windows to temporally locali...

---

### 30. Predictable performance is suboptimal, and what it means for model routing

**Authors:** Guanhua Zhang, Moritz Hardt

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31428v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31428v1)

**Summary:** Large language models (LLMs) differ in capabilities and costs, motivating routing methods that adaptively choose a model for each query. These methods rely on performance prediction: given a query, estimate whether a model will answer it correctly. Most routing methods train separate predictors of candidate models' performance to guide model selection. Our work shows that performance prediction only beats a simple baseline when the candidate model is suboptimal on the task or the performance pre...

---

### 31. FocusVLA: Future-Intent Guided Dynamic View Routing for Vision-Language-Action Models

**Authors:** Huixin Xu, Ziya Yu, Peng Li

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31423v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31423v1)

**Summary:** Vision-language-action (VLA) models have become an important paradigm for robotic manipulation by unifying visual perception, language understanding, and action generation. Since reliable manipulation requires sufficient observation of objects, end-effectors, and their spatial relationships, multi-view inputs are widely used to provide complementary spatial information. However, our experiments show that existing VLA models do not fully exploit such multi-view complementarity. The policy tends t...

---

### 32. How Depth Growth and Looping Shape In-Context Learning in Language Models

**Authors:** Ferdinand Kapl, Kaitlin Maile, Stefan Bauer, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31421v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31421v1)

**Summary:** Looped and depth-grown language models reuse computations across depth and have attracted interest for their reasoning capabilities. Building on prior suggestive evidence of improved in-context-learning (ICL), we investigate how such reuse favors ICL, including how it shapes the acquisition, retention, and mechanisms of this ability. Our analysis spans pretrained language models up to 3B parameters and controlled tasks. The experiments provide evidence for a shared inductive bias toward learning...

---

### 33. Post-Hoc Feature Selection Layer for Neural Networks Interpretability

**Authors:** João Kenji Suwa, João Pedro Silveira e Silva, Bruno Iochins Grisci

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31420v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31420v1)

**Summary:** The interpretability of complex neural networks remains a critical challenge, especially for models already deployed in high-stakes domains. To address this, we adapted the Feature Selection Layer (FSL) to optimize feature weights post-training, a variant we term post-hoc FSL. Our approach reframes the FSL as a lightweight, trainable module that integrates with already frozen pre-trained models on tabular datasets to highlight the features the original model considers most important. This post-h...

---

### 34. Major Revision, Minor Accountability: LLMs as Reviewers of Published Articles in Top-Tier Journals

**Authors:** Bastien Le Guellec, Su Hwan Kim, Raphael Bentegeac, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31414v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31414v1)

**Summary:** With the growth of scientific output, the peer review system is approaching a breaking point: reviewers are increasingly hard to secure, and turnaround times lengthen accordingly. LLM-assisted or LLM-generated peer review has been proposed as a remedy, but how such models would treat manuscripts already published in top-tier journals, the closest thing the current system has to a gold standard of scientific validity, is not known. Here we assembled a corpus of 200 articles, each released under a...

---

### 35. Same Entity, Different Script: Diagnosing Cross-Script Entity Matching Failures in Language Models

**Authors:** Athira Gopal, Patil Prathamesh Pravin, Ankush Kadu, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31407v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31407v1)

**Summary:** Multilingual language models can give different identity judgments when the same people's names are written in different scripts. We study this effect using 601 audited identity pairs with attested Devanagari and Latin forms, holding the question and relation fixed. Qwen2.5-7B's same-person accuracy falls from 35.1% in Latin to 8.5% in Devanagari under Marathi prompts, while different-person accuracy remains above 98%. Evaluation across five models reveals distinct response biases, and reduced t...

---

### 36. AgentPhishing: A Benchmark of LLM Email Agents Under Adaptive Attack

**Authors:** Justin Tan, Miao Li, Ding Zhao

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31404v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31404v1)

**Summary:** Computer-use agents increasingly handle private information and act on users' behalf across desktop and web applications, including email. Phishing therefore poses privacy and security risks that depend not only on whether agents recognize malicious messages, but also on how they respond. Existing phishing datasets were developed primarily for conventional detection, leaving agent susceptibility to persuasive malicious requests insufficiently characterized. To expose vulnerabilities that pre-exi...

---

### 37. HERD: Harness-Evolving Recursive Distillation for Continual Learning

**Authors:** Xun Sun, Thanh Thi Nguyen, Thuy-Trang Vu

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31401v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31401v1)

**Summary:** Continual learning requires a model to keep acquiring new skills and knowledge without compromising its existing capabilities. Parametric methods suffer from catastrophic forgetting and loss of plasticity. Non-parametric methods, such as prompts, skills, and harnesses, leverage in-context learning but are limited by context length and lossy plain-text compression. To effectively combine their complementary strengths, we propose HERD (Harness-Evolving Recursive Distillation), a hybrid continual l...

---

### 38. Auditing the Hand-Written Inputs of Learned Access Control

**Authors:** Arsalan Jalil Sarghaleh, Mehdi Hazrati

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31388v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31388v1)

**Summary:** Learned access control is typically deployed behind two hand-built artefacts: a hard-deny set enforced by a small trusted shield, and a region map that decides which requests mined rules answer and which the learner answers. Verifying the shield or measuring the learner validates neither. We audit both on the five public ABAC Lab policies. First, we formalise hard-deny soundness and check it exhaustively over relations of up to 794,250 tuples. Clauses that faithfully transcribe an explicit restr...

---

### 39. AI Risk Ontologies for the EU AI Act Compliance: AIRO, VAIR, and their Integration with DPV

**Authors:** Delaram Golpayegani, Harshvardhan J. Pandit, Declan O'Sullivan, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31380v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31380v1)

**Summary:** As the use of AI, and consequently its harms, becomes more prevalent, the global discourse around AI has become increasingly risk-aware. With new risks emerging more frequently than ever, a key challenge is how to represent, document, and catalogue AI risks in an effective, interoperable, and queryable manner. Additionally, the European Union (EU) AI Act's requirements for "high-risk" AI systems to manage and document the risks creates the need for open and interoperable tools, methods, and stan...

---

### 40. Certified Execution Harness for Agentic AI: Safe and Least-Intrusive Petri-Net Supervisory Control Between Reasoning and Action

**Authors:** Chao Gu, Quanyan Zhu

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31376v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31376v1)

**Summary:** This paper studies the problem of safe tool execution for large language model (LLM) agents under prompt injection. Using Petri nets, we formalize the execution harness between the LLM and its tools as a supervisory control problem, in which marks represent capabilities, approvals and budgets. Since a transition fires only if the marks it needs are present, an injected request whose preconditions are unmet or already spent is refused regardless of its wording. Treating tool outcomes as uncontrol...

---

### 41. RIDAR: Safeguarding Research Integrity in Autonomous Research Agents via Automated Detection and Runtime Intervention

**Authors:** Jiening Siow, Amy Xin, Junjie Wang, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31372v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31372v1)

**Summary:** Autonomous research agents are increasingly used to automate large portions of scientific research, yet they are prone to research integrity violations (RIVs): behaviors that compromise the validity, reproducibility, or faithfulness of the research process. We present RIDAR, a framework for automated RIV detection and runtime intervention. First, we introduce RIVT, a comprehensive taxonomy of 14 RIV types spanning the full research lifecycle. Building on RIVT, we present RIDAR-post-hoc, a framew...

---

### 42. Muffin - A Shared Memory Buffer for Asynchronous AI Agents

**Authors:** Ping-Lin Kuo, Suman Navaratnarajah, Christian Frey, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31355v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31355v1)

**Summary:** The rise of Agentic AI systems has changed the landscape of artificial intelligence by enabling strong reasoning capabilities through specialized multi-agent interaction with structured self-reflection. However, in target-driven reasoning tasks, single- and multi-agent systems are often on par in terms of performance gains. A major challenge is that failures often arise from an ineffective exchange of critical information during inter-agent interaction and coordination. Different from existing m...

---

### 43. Automating Feature Flag Cleanup at Scale with Multi-Agent LLM Systems: An Industrial Experience at DoorDash

**Authors:** Atharv Chandratre, Jai Datar

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31351v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31351v1)

**Summary:** Feature flags are runtime configuration mechanisms used for gradual feature rollouts, experimentation, and kill switches. Once a feature is fully rolled out, the flag and its gated code become technical debt and can introduce operational risk through inadvertently enabling dormant code paths. At DoorDash, over 56,000 feature flags span 623 repositories, with 1,659 currently stale as of May 2026, with internal estimates of one to two hours per manual cleanup. Existing rule-based cleanup tools pro...

---

### 44. ValuSpec: Plug-and-Play Candidate Valuation before Target Verification for Tree-Based Speculative Decoding

**Authors:** Liang He, SiYuan Ma, Qishi Zhan, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31338v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31338v1)

**Summary:** Tree-based speculative decoding accelerates large language model inference by verifying multiple candidate branches in parallel. However, in practical serving scenarios, similar requests repeatedly induce overlapping candidate branches. While retrieval-based methods mitigate this by reusing historical drafts, the resulting candidate trees often contain many low-quality branches as the candidate tree grows, which reduces verification efficiency and wastes target-side computation. To address this,...

---

### 45. AgenticEvolve: Evolutionary Program Search with Persistent Language Model Agents that Design and Run Experiments

**Authors:** Ze-Yu Peng, Qing-Yu Lan, Zhan-He Wang, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31326v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31326v1)

**Summary:** Evolutionary program search with large language models keeps the structure of an evolutionary algorithm and uses the model as its variation operator. Typically, the model generates each candidate program in a single request from parent programs and their scores. We present AgenticEvolve, an evolutionary program search framework in which each island is run by a persistent large language model agent. Between evaluations, the agent designs and runs experiments on the candidate program. To measure t...

---

### 46. Bridging the Data Gap: Source-Informed Task-Space Transport for Few-Shot Diffusion

**Authors:** Jinjian Jiang, Jing Peng, Rehan Deen, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31323v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31323v1)

**Summary:** Many deployments require a model to move rapidly from a data-rich source to a related target observed only sparsely. This is especially consequential where target data are difficult to collect, as in healthcare settings with persistent population or acquisition imbalances. Retraining or fine-tuning a high-capacity generator for every target is costly and can be statistically unreliable when target data are scarce. We introduce Meta-Diff, which instead learns a recurring source--target relation o...

---

### 47. Hyperreduction accelerates finite element model updating for the discovery of neural materials

**Authors:** Hagen Holthusen, Matthias Knipper, Kevin Linka

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31322v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31322v1)

**Summary:** Finite element model updating is among the most general approaches to discover constitutive models from structural experiments: since the displacement field is computed rather than measured, it accommodates arbitrary geometries, boundary conditions, and sparse or noisy data. However, every loss evaluation requires a nonlinear finite element solve per load step, and training neural materials requires many such evaluations. Intrusive model order reduction lowers this cost while retaining boundary ...

---

### 48. SurveyGraph: Generating Academic Surveys via Methods-Entity Knowledge Graphs

**Authors:** Yifan Yuan, Yancheng Zhu, Zuoyu Zhang, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31317v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31317v1)

**Summary:** Most automated survey generation systems retrieve papers as flat documents, limiting their ability to capture research structure. We present SurveyGraph, a framework built around a Methods-Entity Knowledge Graph (MEKG) encoding method-level follow-on, competition, and shared-resource relations. The graph supports core-paper discovery, retrieval, hybrid outlining, and evidence-gated narrative synthesis. We evaluate retrieval, semantic edges, citation grounding, collection coverage, and generation...

---

### 49. When LLMs Forget What They Believe: Characterizing State Integrity Collapse in Long-Horizon Dialogues

**Authors:** Yancheng Zhu, Yifan Yuan

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31314v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31314v1)

**Summary:** Large language models can repeat an instruction while failing to keep obeying it. We study this recall-compliance dissociation in long-horizon dialogue and define State Integrity Collapse: a model preserves a stated constraint in memory but stops applying it to later turns. We introduce StateTrack-Bench, a controlled suite of conversations covering numerical, format, role/persona, factual-memory, and logical-rule constraints. Across seven provider-pinned model snapshots and five dialogue-depth p...

---

### 50. Subgoal-aware Memory Graph for GUI Agent

**Authors:** Dezhao Luo, Daniel Beechey, Derek Yuen, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31307v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31307v1)

**Summary:** GUI agents aim to automate complex user tasks by interacting with mobile interfaces, but ef- fective decision-making in long-horizon set- tings requires reusing prior experience rather than relying solely on the environment ob- servations. Existing memory-based methods typically store experience either at the single- action level or as entire trajectories. Single- step actions are often too fine-grained to carry meaningful semantics, since the success of an individual action does not necessarily...

---

## cs.CL

**50 papers**

### 1. Direct Pass@$k$ Optimization for Thought Pruning: Balancing Quality and Diversity in Test-Time Reasoning

**Authors:** Mahdi Salmani, Adel Javanmard, Devansh Gupta, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31667v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31667v1)

**Summary:** Test-time scaling has emerged as a key inference strategy for reasoning models, where a model generates a large number of candidate solutions in the hope of finding at least one correct solution. Running all candidate solutions to completion can be computationally demanding, so recent work prunes the candidate pool after generating only a short prefix, committing further computation only to the surviving candidates. Existing pruning strategies divide broadly into two categories: Quality-based me...

---

### 2. Cost-Aware Abstention for LLM-Based IT Ticket Classification

**Authors:** Sachin Gupta

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31657v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31657v1)

**Summary:** Wrong automatic routing of an IT support ticket can cost more than human triage. We evaluate cost-aware abstention as an offline, cost-conditional readiness assessment: select a routing policy on calibration data under explicit costs, then evaluate that frozen policy once on held-out test data. On a public 47,837-ticket, eight-class corpus, we compare four trained non-LLM classifiers with four large language models under zero- and few-shot prompting. Under the illustrative cost model (c_ok, c_tr...

---

### 3. Low-Bit N-Gram Embeddings for Language Models

**Authors:** Stephen Chung, Wenyu Du

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31646v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31646v1)

**Summary:** Many recent open-weight language models use n-gram embedding tables to improve performance. These tables store learned representations of short token sequences, such as pairs or triples of consecutive tokens, which the model retrieves during processing. However, they can require substantial memory: DeepSeek-V4.1-Flash, for example, allocates 196 billion parameters to its Engram n-gram memory. We therefore investigate whether this memory cost can be reduced while preserving the performance improv...

---

### 4. Can an Agent Debug a Web Corpus? Agentic Auditing of Slovak FineWeb2

**Authors:** Marek Šuppa, Ivan Vykopal, Jaroslav Kopčan

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31636v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31636v1)

**Summary:** Multilingual pipelines such as FineWeb2 apply one recipe across a thousand languages, leaving the failure modes of individual languages unanticipated. We use an LLM once, as a corpus debugger rather than a classifier: a tool-using agent explores the corpus through a read-only, budgeted API and compiles each finding into an executable test, which a native speaker then validates. On the 26.5M-document Slovak portion of FineWeb2, three runs costing \$2.21-\$2.84 each found seven findings over four ...

---

### 5. Bilingual Language Models Capture Cross-Linguistic Influence in Second-Language Reading

**Authors:** Abderrahmane Issam, Irene E. Winther, Stefan L. Frank

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31620v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31620v1)

**Summary:** While monolingual language model (LM) surprisal is widely established as a predictor of reading times, it cannot capture the non-native (L2) reading dynamics that are shaped by the reader's first language (L1). In this work, we investigate whether the cross-lingual transfer within bilingual models aligns with human L1-driven biases during L2 reading. We evaluate bilingual models on eye-tracking data of readers from 12 diverse L1 backgrounds reading English texts. To isolate L1-specific transfer,...

---

### 6. How Ground Truth Shapes Retrieval Scores: Evidence-Aware Evaluation of a Retrieval-Augmented Generation System for Breast Lesions

**Authors:** Miguel Mochizuki Silva, Samuel Ismael, Mateus C. Dias, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31606v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31606v1)

**Summary:** Purpose: To describe an evidence-aware retrieval evaluation protocol for a clinical retrieval-augmented generation (RAG) system over breast lesion management literature, addressing the dependence of retrieval scores on annotation coverage. Methods: An 18-document corpus and an 18-query development benchmark, with one Yes/No or WH-question per document, were used. Retrieval combined dense embeddings, BM25, and cross-encoder reranking. Chunk sizes of 128 to 1024 tokens, overlaps of 0 to 20%, and f...

---

### 7. Would an LLM Match into a Residency? Uncertainty, Reasoning and Image Use of Open Language Models on the Spanish MIR Examination

**Authors:** Miguel Fernandez-de-Retana, Unai Zulaika, Ruben Sanchez-Corcuera, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31586v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31586v1)

**Summary:** Accuracy on medical examinations is common evidence offered for the clinical use of language models, yet a health system that intends to run an open model on its own hardware needs to know considerably more: whether the model recognizes when it is likely to be wrong, whether medical fine-tuning improves this ability, whether its correct answers rest on sound clinical reasoning, or whether it actually uses the images it is given. We examine these questions for four open models of 8 to 27 billion ...

---

### 8. Diffusion Language Models for Perplexity-Aware Black-Box Attacks

**Authors:** Ali Al-Lawati, Elsayed Eshra, Dongwon Lee, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31558v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31558v1)

**Summary:** \emph{Continuous-space} attacks find prompts that trigger malicious behaviors, such as overthinking, in black-box LLMs by sampling or optimizing over a low-dimensional Gaussian latent space and decoding it to text through a \emph{random mapping} and nearest-token lookup. Because the random mapping is not learned from language, its prompts can be highly unnatural, and as such easily detectable through input guardrails, and the risk estimates they yield are not grounded in natural prompts. In this...

---

### 9. An Empirical Study of Recent Large Language Models for Knowledge Graph to Text Generation on Standard Benchmarks

**Authors:**  Priyanka, Renaud Delbru, Souhail Bakkali, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31529v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31529v1)

**Summary:** Knowledge graph-to-text (KG-to-text) generation verbalizes a set of knowledge graph triples into fluent natural language. While fine-tuned encoder-decoder models have long been the standard approach, recent LLMs are becoming increasingly competitive. We benchmark recent LLMs against fine-tuned encoder-decoder models, using reference-based metrics and graph-grounded reference-free LLM-based evaluation validated against human annotations. We observed that recent LLMs substantially narrow, and in s...

---

### 10. The Geometry of Metaphor: Probing and Steering Metaphor Representations in Large Language Models

**Authors:** Shihui Li, Mette Andersen, Martha Lewis

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31520v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31520v1)

**Summary:** Metaphor is a crucial aspect of human cognition. As such, we would like to understand how it is represented in large language models (LLMs) and how it might be controlled. We use mechanistic interpretability techniques to identify causal subspaces in a range of LLMs covering different architectures and sizes. We show that we are able to steer output on classification tasks across different parts of speech. We are also able to steer output on generation tasks, indicating that these techniques can...

---

### 11. Towards User Simulators That Stay On Task And Still Sound Natural

**Authors:** Mustafa Omer Gul, Philippe Laban, Tanya Goyal, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31512v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31512v1)

**Summary:** Users increasingly rely on AI systems for extended, multi-turn tasks, yet evidence indicates that LLM-based system performance degrades over prolonged interaction. To evaluate and improve AI assistants in such settings, we need user simulators that faithfully follow complex user intents while exhibiting realistic conversational behavior. Existing approaches manifest a trade-off: prompted assistants can follow complex user intents but lack behavioral fidelity, while specialized user simulators be...

---

### 12. Measuring the Verifier's Floor: How Much Apparent Rare-Word Text-to-Speech Error Is ASR Error?

**Authors:** Kirill Borodin, Vasilii Kudryavtsev, Nikita Vasiliev, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31470v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31470v1)

**Summary:** Text-to-speech (TTS) is usually evaluated by transcribing its output with an automatic speech recognition (ASR) system, so the word error rate also counts recognizer errors. We measure these errors on human recordings of the test sentences. On LibriSpeech and FLEURS, the evaluation recognizer misses 33-67% of very rare words even in human speech, and all three recognizers miss 22-42%. Checking every word with two more recognizer families lowers the apparent TTS error on words that at least one r...

---

### 13. From Structured Records to Patient Narratives: Preserving Clinical Alignment in LLM-Generated Health Summaries

**Authors:** Bayram Ayadi, Florian Geissler, Johanna Schmidhuber

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31467v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31467v1)

**Summary:** As wearable and digital health systems increasingly generate longitudinal physiological records, communicating these observations in patient-accessible language remains a significant challenge. Large Language Models (LLMs) offer a promising mechanism for translating structured clinical information into readable narratives, but this process may introduce semantic drift, where clinically precise meaning is distorted during simplification. We investigate evidence-grounded health summarization for m...

---

### 14. How Different, or Different How? Stance Granularity in Viewpoint Selection for Dialog Systems that Engage Users with Alternative Views

**Authors:** Morita Tarvirdians, Reeve Lorena, Catharine Oertel

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31459v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31459v1)

**Summary:** Systems that aim to help a user engage with viewpoints other than their own have to decide how different those viewpoints should be. Viewpoints are mainly represented on a scalar scale, too coarse to distinguish viewpoints that disagree with the user about different things. We introduce a selection policy in which a bandit sets how far viewpoints may sit from the user, and the policy selects the most novel viewpoint within that bound. We vary only its stance encoder, comparing a scalar score wit...

---

### 15. Multi-Token Prediction and Alternative Tokenization Improve Learning Latent Multi-Hop Graph Search at Scale

**Authors:** Arvid Frydenlund, FuTe Wong, Katherine Lambert, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31439v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31439v1)

**Summary:** Given an unseen graph, a start node, $s$, and an end node, $t$, can a language model generate the shortest path from $s$ to $t$? Prior work has found that models fail to learn this task as the graphs scale. We show that this failure has two causes: the supervision signal and the tokenization. First, we theoretically establish and empirically demonstrate the effectiveness of multi-token prediction (MTP), and show that the benefits of MTP are topologically agnostic. Second, we introduce alternativ...

---

### 16. How Well Do Decision Models Transfer to Vietnamese? An Empirical Study of Text Classification

**Authors:** Phat Huu Ha, Nguyen Xuan Phuc, Nong Nhut Quy, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31422v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31422v1)

**Summary:** Recent advances in specialized decision models have expanded the possibilities for zero-shot classification, yet their effectiveness on Vietnamese remains underexplored. This study evaluates four specialized decision models across 13 classification settings spanning six task groups, examining zero-shot performance, sensitivity to label-description language, and robustness to Vietnamese linguistic variations. The evaluation considers English, Vietnamese, and bilingual label descriptions, alongsid...

---

### 17. How Depth Growth and Looping Shape In-Context Learning in Language Models

**Authors:** Ferdinand Kapl, Kaitlin Maile, Stefan Bauer, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31421v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31421v1)

**Summary:** Looped and depth-grown language models reuse computations across depth and have attracted interest for their reasoning capabilities. Building on prior suggestive evidence of improved in-context-learning (ICL), we investigate how such reuse favors ICL, including how it shapes the acquisition, retention, and mechanisms of this ability. Our analysis spans pretrained language models up to 3B parameters and controlled tasks. The experiments provide evidence for a shared inductive bias toward learning...

---

### 18. SyRA-CS: Synthetic-to-Real Adaptation for Code-Switched ASR with Meta-Learning

**Authors:** Fadel Thior, Ahmer Tabassum, Haania Siddiqui, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31415v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31415v1)

**Summary:** Code-switched (CS) automatic speech recognition (ASR) remains difficult because real CS speech is scarce and synthetic speech does not fully match it. We investigate whether synthetic CS speech is more useful for learning an adaptation-friendly initialization than for ordinary continual fine-tuning. We propose SyRA-CS, a pair-specific synthetic-to-real adaptation framework based on Reptile meta-learning. For each language pair and pretrained model, we meta-train on the corresponding synthetic CS...

---

### 19. SQuAT: Spherical Lattice Vector Quantization-Aware Training

**Authors:** Sebastian Loeschcke, Ivan Koryakovskiy, Tycho F. A. van der Ouderaa, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31412v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31412v1)

**Summary:** Vector quantization (VQ), in particular lattice-based methods, offer strong rate-distortion trade-offs for low-bit large language models (LLMs), yet their behavior under quantization-aware training (VQ-QAT) remains poorly understood. We scale lattice VQ-QAT to billion-parameter LLMs and multi-billion-token training regimes, and introduce SQuAT, a shape-gain VQ-QAT approach trained with a separate straight-through estimator (STE) for the shape and gain. SQuAT decomposes weights into direction and...

---

### 20. Same Entity, Different Script: Diagnosing Cross-Script Entity Matching Failures in Language Models

**Authors:** Athira Gopal, Patil Prathamesh Pravin, Ankush Kadu, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31407v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31407v1)

**Summary:** Multilingual language models can give different identity judgments when the same people's names are written in different scripts. We study this effect using 601 audited identity pairs with attested Devanagari and Latin forms, holding the question and relation fixed. Qwen2.5-7B's same-person accuracy falls from 35.1% in Latin to 8.5% in Devanagari under Marathi prompts, while different-person accuracy remains above 98%. Evaluation across five models reveals distinct response biases, and reduced t...

---

### 21. HERD: Harness-Evolving Recursive Distillation for Continual Learning

**Authors:** Xun Sun, Thanh Thi Nguyen, Thuy-Trang Vu

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31401v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31401v1)

**Summary:** Continual learning requires a model to keep acquiring new skills and knowledge without compromising its existing capabilities. Parametric methods suffer from catastrophic forgetting and loss of plasticity. Non-parametric methods, such as prompts, skills, and harnesses, leverage in-context learning but are limited by context length and lossy plain-text compression. To effectively combine their complementary strengths, we propose HERD (Harness-Evolving Recursive Distillation), a hybrid continual l...

---

### 22. Parameter-Efficient Adaptation of Large Language Models to a Low-Resource Agglutinative Language: A Corpus, Datasets, and a Reproducible Benchmark for the Bashkir Language

**Authors:** Mullosharaf K. Arabov, Svetlana S. Khaybullina

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31397v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31397v1)

**Summary:** Bashkir is a low-resource agglutinative language written in Cyrillic and remains poorly represented in modern LLMs. We present an open resource suite and a systematic benchmark of adaptation methods: the Bashkir Web Corpus (71,567 documents, 46.9M tokens, 16 sources) and three labelled datasets for binary, multiclass and multilabel text classification; the benchmark covers the first two. Experiments use eight architectures (82M-8B: DistilGPT2, GPT-2 base/medium, Phi-3-mini, Mistral-7B, YandexGPT...

---

### 23. A Task-Centric Survey of Long-Document Visual Question Answering: Taxonomy, Evolution, and Future Directions

**Authors:** Yufei Tong, Guanjie Cheng, Tianle Wu, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31385v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31385v1)

**Summary:** Visual document understanding is essential for acquiring knowledge from visually rich documents and is attracting growing research interest. Existing surveys emphasize architectures or technical approaches, with limited attention to how task bottlenecks shape technical choices and research priorities. We present a task-centric survey that decomposes long-document visual question answering (VQA) into four components: document parsing, evidence organization and retrieval, generator organization an...

---

### 24. AfterDeleteBench: Auditing Post-Deletion Information Persistence in LLM Agents

**Authors:** Ehsan Saleh, Roozbeh Nahavandi, Sama Salarian, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31366v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31366v1)

**Summary:** Many LLM agents maintain external persistent memory and derive additional state from past interactions, such as summaries. Deleting an original memory record therefore need not remove information carried by its descendants. We introduce AfterDeleteBench, a controlled behavioral audit for this failure mode in fixed-weight LLM agents. For each synthetic secret, we compare an exposed-then-deleted agent with an otherwise matched agent that was never exposed to the secret, allowing post-deletion reco...

---

### 25. CrisiLangs: A Multilingual Resource for Crisis Warning Generation

**Authors:** Giacomo Gonella, Stefano Menini, Marco Guerini

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31356v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31356v1)

**Summary:** Communicating with the public during an emergency entails issuing warning messages promptly. In Europe, it often requires producing them in more than one language. Recent work has shown that language models can be trained to generate warning messages as a crisis unfolds, but the available data covers only English. To fill this gap, we present CrisiLangs, a multilingual extension of CrisiText (an English dataset of crisis events paired with warning messages written according to expert communicati...

---

### 26. SurveyGraph: Generating Academic Surveys via Methods-Entity Knowledge Graphs

**Authors:** Yifan Yuan, Yancheng Zhu, Zuoyu Zhang, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31317v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31317v1)

**Summary:** Most automated survey generation systems retrieve papers as flat documents, limiting their ability to capture research structure. We present SurveyGraph, a framework built around a Methods-Entity Knowledge Graph (MEKG) encoding method-level follow-on, competition, and shared-resource relations. The graph supports core-paper discovery, retrieval, hybrid outlining, and evidence-gated narrative synthesis. We evaluate retrieval, semantic edges, citation grounding, collection coverage, and generation...

---

### 27. When LLMs Forget What They Believe: Characterizing State Integrity Collapse in Long-Horizon Dialogues

**Authors:** Yancheng Zhu, Yifan Yuan

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31314v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31314v1)

**Summary:** Large language models can repeat an instruction while failing to keep obeying it. We study this recall-compliance dissociation in long-horizon dialogue and define State Integrity Collapse: a model preserves a stated constraint in memory but stops applying it to later turns. We introduce StateTrack-Bench, a controlled suite of conversations covering numerical, format, role/persona, factual-memory, and logical-rule constraints. Across seven provider-pinned model snapshots and five dialogue-depth p...

---

### 28. Cola2: Co-Adaptive Hierarchical Language Modeling with Continuous Semantic Compression and Balanced Discrete Generation

**Authors:** Hongcan Guo, Yian Zhao, Feng Wang, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31305v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31305v1)

**Summary:** Hierarchical language generation separates continuous semantic modeling from discrete text realization, but its effectiveness depends on what the latent space compresses and how the discrete generator uses it. We propose Cola2, a framework that jointly studies continuous semantic compression, the balance between reconstruction and generation, and continuous-discrete co-adaptation. Cola2 dynamically segments text into semantic spans, controls the compression rate through auxiliary-loss-free negat...

---

### 29. The Value of Memory in Language Agents

**Authors:** Zehao Lin, Erenkai Zhu, Helan Hu, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31303v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31303v1)

**Summary:** Memory enables language agents to carry useful distinctions from past experience into future decisions. Its value depends on which distinctions survive, whether a bounded agent can use them, and what can be recovered or revised as demands evolve. We develop a decision-theoretic framework that follows this value from raw history through persistent state, operational use, and costly recovery and revision. Original and retained value are expressed in units of avoided task loss; risk-cost frontiers ...

---

### 30. CoWriter: Guiding Methodological and Synergetic Human-LLM Co-Authoring

**Authors:** Shmuel Amar, Benjamin Lieber, Ori Shapira, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31277v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31277v1)

**Summary:** While LLMs have transformed text generation, standard chat-and-canvas interfaces often reduce human authoring to quite passive supervision, causing review fatigue, over-reliance on AI, and the sidelining of the human role in long-form, source-grounded writing. Prior systems typically address isolated writing phases, leaving comprehensive end-to-end human-LLM collaboration largely unexplored. In this paper, we introduce CoWriter, a proactive agentic scheme that adapts expert human (co-)authoring ...

---

### 31. Memory-Aware Reward Modeling: Learning Human Preferences for LLM Memory Use

**Authors:** Yijiang River Dong, Zexue He, Cheng Yu, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31272v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31272v1)

**Summary:** Memory enables language model assistants to maintain continuity across sessions and generate personalized responses, but knowing more about a user does not necessarily produce responses they prefer. Existing evaluations assess memory capabilities without directly establishing whether memory use benefits the user. To study this gap, we collect approximately 1,000 pairwise judgments from 87 participants using their own ChatGPT queries and personal memories. We find that memory-conditioned response...

---

### 32. A Systematic Comparison of Search Space Complexity and Efficiency for Time-Synchronous End-to-End ASR Models

**Authors:** Simon Berger, Larissa Kleppel, Ralf Schlüter

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31259v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31259v1)

**Summary:** Search is a central component of Automatic Speech Recognition (ASR) systems and has been deeply investigated for classical ASR modeling based on Hidden Markov Models (HMMs). However, in work on current sequence-to-sequence ASR architectures it is often simplified to a small fixed-size beam search without external Language Model (LM). In this work, we present a comparative analysis of search space complexity and efficiency for Connectionist Temporal Classification (CTC) and neural transducer mode...

---

### 33. IndoNutriQA: An Indonesian Clinical Nutrition Question Answering Benchmark

**Authors:** Tirana Noor Fatyanosa, Ummu Ditya Erliana, Mahendra Data, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31256v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31256v1)

**Summary:** Clinical Question Answering (QA) underpins Clinical Intelligent Decision Support Systems, but progress is severely limited for low-resource languages such as Indonesian by the absence of public domain-specific data. We introduce IndoNutriQA, an expert-curated Indonesian clinical QA benchmark of 911 question-answer pairs built from real clinical-nutrition reports. Rather than a large-scale training corpus, it is positioned as a high-quality evaluation resource: every pair is grounded in a clinica...

---

### 34. Predicting Music Valence and Arousal via Textual and Multimodal In-Context Learning in Large Language Models

**Authors:** Chi-En Dai, Chih-Pin Tan, Yi-Hsuan Yang

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31202v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31202v1)

**Summary:** While arousal can be reliably predicted from musical audio, emotional valence remains difficult to model due to its subjective and context-dependent nature. In this work, we investigate the potential of in-context learning (ICL) with large language models to advance continuous valence and arousal prediction. Rather than predicting emotion scores directly, our framework leverages contextual demonstrations from an auxiliary dataset to refine the initial predictions produced by a small, task-specif...

---

### 35. Investigating Multi-Cultural Value Selection Biases in LLMs

**Authors:** Siddhesh Pawar, Arnav Arora, Dustin Wright, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31199v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31199v1)

**Summary:** Large language models (LLMs) serve users whose cultural identities are multi-layered, yet cultural evaluations commonly reduce identity to one label. In this work, we study LLMs under simultaneous identity cues, with a country persona in the system prompt and a second identity signaled in the user turn, either by naming a country (explicit cue) or through the query language (implicit cue). We test World Values Survey (WVS) multiple-choice probing and open-ended sociopolitical generation. In mult...

---

### 36. When More Metadata Misleads: Probing Field-Level Grounding in LLM-Generated Museum Descriptions

**Authors:** Clemencia Siro, Laura Hollink

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31193v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31193v1)

**Summary:** Metadata-conditioned generation is often framed as a data-to-text task in which additional input fields should improve grounding. Museum description generation challenges this assumption because catalogue records are heterogeneous, partially visual, and unevenly documented across geographic regions. We study how metadata composition shapes the generation of artefact descriptions through a two-phase framework. Phase 1 analyses natural metadata variation in a large museum collection, where field c...

---

### 37. Prompting Strategy Effects Depend on the Judge: A Multilingual Study of LLM-as-a-Judge Robustness

**Authors:** Asal Mehrabi, Mohammad Aliannejadi, Clemencia Siro

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31172v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31172v1)

**Summary:** LLM-as-a-Judge evaluation is increasingly applied to multilingual tasks, yet prompting strategies such as Chain-of-Thought and Role Conditioning are recommended based solely on English benchmarks. Whether their effectiveness transfers across judge models and languages remains unknown: prompt-sensitivity studies are largely English-centric, while existing multilingual judge studies fix the prompt template. In this work, we address this gap by measuring this interaction through a benchmark of 9 pr...

---

### 38. Beyond Watching and Searching: Benchmarking Agents for Video-centered Deep Research Reports

**Authors:** Jiahao Meng, Qize Yang, Yuxuan Wang, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31158v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31158v1)

**Summary:** Deep research agents synthesize open-web evidence into long reports, but current benchmarks do not evaluate research centered on a source video. We introduce Video-Centered Deep Research Report Generation. Given a video and user request, an agent identifies research questions, retrieves external multimodal evidence, and produces an interactive report linked to relevant video moments. This task has direct practical value because it helps users locate relevant moments, verify claims, reproduce dem...

---

### 39. Prompt Sensitivity in Tool-Augmented Model Comparisons

**Authors:** Mateusz Modrzejewski, Tomasz Radzikowski

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31148v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31148v1)

**Summary:** Language models are compared on question-answering benchmarks that pose each question in one wording, and a reworded question can change which of two models scores higher. We ask whether giving the models tools makes such comparisons more stable. An accuracy gain cannot answer this, because tools change several steps between the question and the scored answer at once. We propose a matched protocol that separates those steps: the answer readout, reasoning, the decision to call, the tool's answer,...

---

### 40. Mixing Matters: Evidence Position Bias Across Sequence Mixers in Long-Context Question Answering

**Authors:** Aman Behera, Namit Solanki, Mehul Anand

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31135v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31135v1)

**Summary:** Long-context models often use answer-bearing evidence less effectively when it appears away from a prompt boundary. We compare this position bias across Transformer, state-space, and hybrid Mamba architectures by moving one gold document through a fixed set of nine distractors. The evaluated Transformers show a beginning advantage that the evaluated state-space models lack, while both families favor evidence near the end. A matched pure-versus-hybrid Mamba comparison points in the same direction...

---

### 41. Delta N-gram: Forward-Only Continual Writing into a Language Model's Native N-gram Memory

**Authors:** Hao Wu

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31125v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31125v1)

**Summary:** Our previous analysis found that a model's native hashed N-gram table is where continual updates disturb the base least, but its writes needed backpropagation and changed the pretrained table. We present Delta N-gram, a forward-only write path into that table. The pretrained table T^0 is never modified. Evidence is written into a sparse patch Δon the rows it addresses: a 4.1M-parameter writer emits a target and a gate per (position, hash head) event, and a block-averaged delta rule keeps each ro...

---

### 42. Through a PRISM, Clearly: Step-Sequence Reasoning for Mistake Recognition in Procedural Videos

**Authors:** Olga Loginova, Oleksandr Bezrukov, Frank Keller

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31117v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31117v1)

**Summary:** Procedural mistake recognition requires identifying deviations from valid multi-step activities. We study post-completion recognition from videos with benchmark-provided step boundaries. We introduce PRISM (Procedural mistake Recognition via Interpretable Semantic Modeling), which grounds video segments in language and maps their descriptions to procedural states using a lightweight hidden Markov model trained on correct executions. Reference alignment and semantic checks identify errors in step...

---

### 43. A Grammar of French Civil Cassation: A Ground-Level Dataset and Tool

**Authors:** Avrile Floro, Tamara Dhorasoo, Nils Holzenberger, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31116v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31116v1)

**Summary:** This paper presents a dataset of 121,536 ground-reasons pairs across 86,464 rulings of the five civil chambers of the French Court of Cassation (2016-2025). An appeal on points of law cannot itself be appealed and often decides a case for good. Understanding how the Court rules is thus crucial and can help lawyers who draft those appeals. Inside a ruling, every ground of appeal (a distinct legal complaint against the appealed decision) has its own answer from the Court. This answer is called the...

---

### 44. Learning What to Ask for Tomorrow: Active Preference Acquisition for Long-Term Personalized Web Agents

**Authors:** Yiqi Wang, Zizhi Zeng, Jiaqi Zhang, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31107v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31107v1)

**Summary:** Web agents increasingly serve the same user across repeated online tasks such as booking travel, shopping, and scheduling, so their long-term usefulness depends on how well they know the user's preferences. Passive memory and personalization methods cannot obtain preferences the user never reveals, and clarification methods that value a question by its benefit to the current task overlook the benefit of reusing the answer in later tasks. We study Active Preference Acquisition (APA): which missin...

---

### 45. RIFT: KV Cache Compression for Draft Models with Complementary Compressibility Training

**Authors:** Dor Tsur, Maor Ashkenazi, Maximilian Golub, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31098v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31098v1)

**Summary:** Speculative decoding is a popular decode acceleration method. As such, it is particularly relevant to long-output generation, which requires an increasingly large KV cache. KV cache compression offers a way to constrain costs in long-context drafting. However, compression methods that focus on prefill information can lose relevance as the output length grows. We term this phenomenon decode staleness and show that it degrades draft model accuracy under selection-based KV cache compression. We int...

---

### 46. What Pairwise Evaluation Misses: Reward Scores across Prompts

**Authors:** Mateusz Modrzejewski, Tomasz Radzikowski

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31090v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31090v1)

**Summary:** Reward models score responses for preference optimization, filtering and ranking, and pooling scores across prompts needs them to be comparable. Yet pairwise evaluation compares two responses to the same prompt, so any score component shared by a prompt's responses cancels and goes untested. We study this component by comparing between-prompt variation in model scores with the same variation in human ratings of the same responses. We propose a human-referenced audit, built from a between-prompt ...

---

### 47. SCOPE: Compiling Natural-Language Policies into Neurosymbolic Predicate Programs

**Authors:** Arnon Mazza, Elad Levi

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31062v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31062v1)

**Summary:** Policy enforcement for LLM agents has shifted from single-turn content moderation to compound, application-specific policies evaluated over multi-turn transcripts and tool-call trajectories. Fine-tuned guardrail models are efficient but degrade on compound policies, and while LLM-as-a-judge approaches achieve higher accuracy, they incur high inference cost and tend to produce unstable predictions. Neurosymbolic methods offer a natural alternative, decomposing the policy into narrow neural decisi...

---

### 48. Harm Is Behavioural, Moderation Is Lexical: How Language and Culture Decide Whom Automated Safety Systems Protect and Whom They Silence

**Authors:** Gabriel Lars Sabadin, Dr Nicola Harding, Sarah Kingston

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31047v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31047v1)

**Summary:** Content warning: this paper quotes slurs and hateful statements from published test suites; the racial slur among them is masked.   Automated systems decide at scale which messages are harmful, and they decide unevenly. Classifiers label African American English as offensive up to twice as often as other English, the accounts of prominent drag queens can score as more toxic than those of white nationalists, and safety behaviour that holds in English collapses in low-resource languages. We argue ...

---

### 49. Chunk Recomputation under Real Document Revisions: Measuring Update Cost and Retrieval Quality of Fixed, Recursive, and Content-Defined Chunking

**Authors:** Yuning Bian, Lele Xu, Yifan Yuan, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31019v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31019v1)

**Summary:** Chunking strategies for retrieval-augmented generation are almost always evaluated on a static snapshot, yet the documents underlying a knowledge base continue to change. Because chunks are embedded independently, a boundary that moves after an edit forces unchanged text to be re-embedded. We measure this update cost on 120 pairs of adjacent Chinese and English Wikipedia revisions for three stateless chunkers (non-overlapping fixed-size, recursive paragraph-first, and content-defined chunking) u...

---

### 50. Mostly Reading: What Open-Book Scores Measure in Document-Level LoRA Adapters

**Authors:** Martino M. L. Pulici, Cuong Xuan Chu, Evgeny Kharlamov, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31017v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31017v1)

**Summary:** Single-document LoRA adapters have been proposed as units of knowledge to be merged and retrieved; yet open-book scoring, with the document in the prompt, can credit a document's own adapter (its specialist) for reading that document as readily as for holding it. Training one adapter for each of 150 Wikipedia articles on Llama-3.1-8B-Instruct, we find that open-book scores mostly measure a reading behaviour every adapter shares: a random adapter trained on another document recovers 82 % of the s...

---

## cs.CV

**50 papers**

### 1. A Unified Framework for Image-to-3D Part Generation via Variable Granularity

**Authors:** Qiwen Gu, Xin Zhou, Xiwu Chen, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31671v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31671v1)

**Summary:** Controllable 3D part generation is pivotal for digital asset creation, yet existing methods lack the flexibility to accommodate diverse user workflows requiring varying levels of control. In this paper, we introduce FlexPart, a unified image-to-3D part generation framework that supports variable-granularity geometric conditions within a single model. By seamlessly integrating heterogeneous inputs, ranging from sparse points to dense bounding boxes and masks, via gated adaptive modulation, FlexPa...

---

### 2. Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success

**Authors:** Yunfei Xie, Howard H. Qian, Shiyi Lan, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31670v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31670v1)

**Summary:** Robotic foundation models are typically evaluated through costly closed-loop rollouts, which motivates cheap offline proxies for model capability. The Platonic Representation Hypothesis (PRH) suggests that as representations improve, different modalities such as vision and language converge toward a shared statistical model of reality. We ask whether motion trajectories form another such modality: as embodied models become more capable, should their sensory representations converge toward the st...

---

### 3. Reading, Writing, Sharing, and Interacting with the World through Video

**Authors:** Shengqiong Wu, Meng Luo, Bobo Li, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31668v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31668v1)

**Summary:** Video foundation models have advanced rapidly in understanding and generating visual sequences, while video world models seek to capture the underlying dynamics of the world they depict. Despite their different objectives, both concern the relationship between video observations and an evolving world. This survey adopts world modeling as a unifying lens for examining these developments. Viewing an observed video as a partial, lossy, and temporally ordered projection of a latent temporal world, w...

---

### 4. SpectralCanary: Embarrassingly Simple Low-Frequency Traces for T2I Dataset-Use Auditing

**Authors:** Sy-Tuyen Ho, Anirudh Satheesh, Soham Chawathe, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31659v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31659v1)

**Summary:** Auditing whether a text-to-image (T2I) model was fine-tuned on a particular image collection is difficult: a model can absorb collection-level visual characteristics without reproducing training images. Proactive dataset-use auditing plants a shared signal in a dataset before release, then later checks whether that signal appears in a suspect model's generated outputs. Existing approaches often trade off verifiability, fidelity, robustness, and deployability. We introduce $\textbf{SpectralCanary...

---

### 5. BrickWright: Agentic Creation of Physically Feasible Brick Builds

**Authors:** Ava Pun, Kevin Dai, Sally Chen, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31651v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31651v1)

**Summary:** Frontier coding agents are becoming increasingly adept at 3D modeling. Yet, they still face challenges when building objects meant to be assembled in the physical world, often creating invalid assemblies with floating, colliding, or disconnected parts. We argue that providing agents with tools for assembling builds and verifying their physical feasibility is sufficient for them to produce physically valid assemblies that still adhere to input prompts. Focusing on the domain of LEGO brick builds,...

---

### 6. Gate3DGen: A Pre-processing Model that Selectively Purifies Real-World Images for 3D Generation

**Authors:** Xiaolin Li, Zihao Huang, Fanpeng Meng, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31649v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31649v1)

**Summary:** Single-image 3D generation has achieved high fidelity on curated benchmarks, yet degrades sharply on real-world images with uneven illumination, blur, and occlusions. Purifying such inputs requires deciding when to intervene and preserving the visual cues needed for 3D generation, while leaving clean inputs unchanged. We introduce Gate3DGen, a selective pre-processing model that gates image inputs to existing 3D generators without retraining them. A degradation-aware router bypasses inputs class...

---

### 7. OmniRay: Camera-Agnostic Monocular 3D Reconstruction with Composite Ray Fields

**Authors:** Namitha Guruprasad, Abhay Yadav, Cheng Peng, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31645v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31645v1)

**Summary:** Monocular models recover 3D geometry from a single image in one pass, but most assume a pinhole camera and produce distorted geometry on the wide-angle imagery produced by fisheye and panoramic lenses. Camera-aware models remove this assumption by predicting a per-pixel ray field. However, they represent different camera geometries using a single fixed basis to capture both the overall camera projection and its finer variations. We argue that camera geometry can be viewed as having a hierarchy o...

---

### 8. GigaBench: Benchmarking Learnable Representations for Gigapixel Image Compression and Super-Resolution

**Authors:** Matteo Fusconi, Alex Costanzino, Pierluigi Zama Ramirez, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31644v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31644v1)

**Summary:** Learnable Representations (LRs) can fit parametric families of functions to diverse kinds of signals. These emergent neural-native data formats are gathering interest in the scientific community due to their compactness, resolution-agnosticism and amenability to direct neural processing. On the other hand, gigapixel images are becoming increasingly widespread across a variety of scientific, cultural, and industrial domains. In this paper, we present GigaBench, the first benchmark and experimenta...

---

### 9. UniVOE: A Removal-Driven Framework for Interaction-Aware Universal Video Object Editing

**Authors:** Shuzhou Yang, Lanqing Guo, Lingen Li, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31641v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31641v1)

**Summary:** Video object removal and injection are reciprocal editing operations between object-present and object-absent video states, yet they differ substantially in training difficulty. Removal can be effectively bootstrapped from video inpainting and further adapted to erase object-related interaction effects. Injection, however, requires large-scale paired supervision to model object appearance, dynamics, and scene-dependent effects, while perfectly aligned real-world pairs are difficult to collect an...

---

### 10. WorldForge V2: Eliciting Camera-Trajectory Alignment in Video Diffusion Models

**Authors:** Chenxi Song, Yanming Yang, Tong Zhao, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31640v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31640v1)

**Summary:** Video diffusion models have learned rich 3D/4D priors, making them promising for scene generation and video re-rendering. However, their use in spatial tasks is limited by imprecise camera control, spatial and temporal inconsistencies, and entangled camera motion with scene dynamics. Existing approaches, such as task-specific fine-tuning and post-process warping, often introduce visual artifacts, generalize poorly, or incur high computational costs. We propose WorldForge V2 to achieve accurate c...

---

### 11. HiP3R: Hierarchical Pose Graphs for Long-Horizon 3D Reconstruction

**Authors:** Zunnan Xu, Shangchen Zhou, Yihang Luo, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31635v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31635v1)

**Summary:** Feed-forward models accurately estimate camera motion and 3D geometry from short video windows. However, computational and memory costs prevent direct inference on sequences containing thousands of frames. Long videos must therefore be processed as overlapping chunks. This division produces independent local reconstructions with inconsistent coordinate frames and duplicate estimates of shared cameras. Achieving global consistency requires propagating constraints from adjacent overlaps and distan...

---

### 12. F2G-Pose: Geometry-Aware Foundation Feature Lifting for Direct RGB-D Category-Level Object Pose Estimation

**Authors:** Jinyu Zhang, Haitao Lin, Jiashu Hou, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31623v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31623v1)

**Summary:** This paper studies category-level RGB-D object pose estimation, which recovers an object's 3D rotation and translation without instance-specific CAD models or reference views. This task is highly ambiguous due to intra-class variations, symmetries, and partial observations. Current solutions struggle to balance reliability and efficiency: methods based on intermediate structures are prone to error propagation, while diffusion models suffer from high inference latency and complex post-hoc candida...

---

### 13. Beyond Best-of-$k$: Prior-Consistent DAPS for Ambiguous Nonlinear Inverse Problems

**Authors:** Merve Kocabas, Benjamin A. Burns, Andreas Geiger, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31592v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31592v1)

**Summary:** Diffusion models have become strong priors for solving inverse problems. However, nonlinear inverse problems such as phase retrieval remain challenging when multiple measurement-consistent solutions are distinguishable only by the prior; we call such measurements ambiguous. Existing diffusion-based samplers rely on local approximations during reconstruction. For an ambiguous measurement, these approximations can allow measurement guidance to favor a measurement-consistent mode that is close to a...

---

### 14. CellTrack-Bench: Microscopic Cell Tracking Benchmark for Vision-Language Models

**Authors:** Ilan Theodoro, Jordão Bragantini, Loïc A. Royer

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31566v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31566v1)

**Summary:** Large language models have shown outstanding performance on text-first tasks such as coding, math, and writing. Recent efforts are shifting models' training to include scientific problems that often live in highly specialized domains beyond text, such as protein structure and biological images. However, in these scenarios, their general-purpose accuracy compared with specialized algorithms remains in question. One such domain is cell tracking, which requires spatiotemporal awareness of cell dyna...

---

### 15. Squaring-the-Sphere: Distortion-Free and Seamless Panorama Generation via CubeAtlas

**Authors:** Xuhui Zuo, Chenjie Cao, Tengfei Wang, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31565v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31565v1)

**Summary:** Generating 360-degree panoramas requires both local perspective fidelity and global spherical continuity. Existing representations face a trade-off: equirectangular projection (ERP) enables seamless panorama modeling but suffers from severe distortion and a domain gap to pre-trained image generators, whereas cubemaps preserve perspective geometry but often produce inconsistent faces and visible seams. We present Squaring-the-Sphere, a panoramic image generation framework built on a novel represe...

---

### 16. LACToS: Local Anomaly Detection via Conditional Typicality of Superpixels

**Authors:** Jihoon Hong, Alireza Kheirandish, Rohan Sanda, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31538v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31538v1)

**Summary:** Local anomaly detection is the task of identifying spatially confined anomalous or out-of-distribution (OOD) regions within an otherwise in-distribution (ID) image. Most existing methods are designed for a specific context, with a strong focus on industrial defect detection, where they achieve excellent performance on well-established benchmarks. However, we observe that these methods can exhibit significant performance drops in other contexts, especially when the inlier distribution is multimod...

---

### 17. Diffusion-Based Synthesis of Complete 3D Biparametric Prostate MRI

**Authors:** Claudia Giardina, Montse Pardàs, Verónica Vilaplana

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31523v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31523v1)

**Summary:** Synthetic biparametric MRI (bpMRI) may help alleviate the limited availability of large and representative prostate MRI datasets for deep learning applications. In this work, we present a conditional 3D diffusion framework for anatomy-conditioned synthesis of complete prostate bpMRI from anatomical masks. The framework supports sequential synthesis, in which T2w and diffusion modalities are generated by separately trained models, and joint synthesis, in which all bpMRI modalities are generated s...

---

### 18. Evaluation of Uncertainty-Aware Multi-Software Ensembles for Hippocampal Segmentation

**Authors:** Gabriel Oliveira-Stahl, Anna Schroder, James Moggridge, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31505v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31505v1)

**Summary:** Accurate hippocampal segmentation can be a useful tool for diagnosing and monitoring neurological conditions such as Alzheimer's disease and epilepsy. While numerous automated segmentation methods exist, their clinical adoption remains limited. Reliable uncertainty assessment can enhance trust and facilitate clinical translation. This study evaluates ensembles of five heterogeneous hippocampal segmentation methods - InnerEye, ASHS, FastSurfer, HippoSeg, and FreeSurfer - across two dementia datas...

---

### 19. AgentVQA: A Unified Benchmark for Agentic Visual Understanding

**Authors:** Advait Gupta, Sachin Konan, Tom Yin, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31494v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31494v1)

**Summary:** Vision-language models (VLMs) can perform a broad range of tasks across diverse settings, yet their performance in agentic contexts remains poorly understood. Although online evaluations in simulators and real-world environments are essential for measuring interactive agent performance, they are costly and challenging to scale. Complementary offline VQA benchmarks can enable faster and more reliable comparisons across agentic domains, yet existing benchmarks remain limited and fragmented. To add...

---

### 20. Self-Supervised Multibeam Sonar Restoration via Coherent Forward Modeling

**Authors:** Zixin Wang, James Hopgood, Mike Davies

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31490v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31490v1)

**Summary:** Multibeam imaging sonar produces intensity images degraded by coherent speckle and system-induced blur, while clean reflectivity targets are rarely available. Existing despeckling methods often rely on simplified intensity-domain noise models, synthetic clean targets, or blind-spot self-supervision, and typically do not jointly model deblurring and speckle suppression.   We propose a physics-consistent self-supervised framework for joint despeckling and deblurring of multibeam imaging sonar. A s...

---

### 21. MoG-VLM: Efficient Video Anomaly Detection through Motion-Guided Vision-Language Models

**Authors:** Khaled Waleed Dawoud, Muhammad Zaigham Zaheer, Khan Muhammad, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31478v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31478v1)

**Summary:** Vision-Language Models (VLMs) have shown strong potential for video anomaly detection, but dense frame-level inference makes them impractical for real-time deployment. Existing acceleration commonly relies on uniform sampling, which ignores content dynamics and can either waste computation on static segments or miss localized anomalies. We propose MoG-VLM a motion-adaptive anomaly detection framework that leverages motion purely as a lightweight control signal to decide when VLM inference is nec...

---

### 22. Ask About the Right Moment: Training-Free Object Identity Reasoning for Video-Language Models

**Authors:** Di Yang, Xiaochang Li, Muyang Liu, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31471v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31471v1)

**Summary:** Many questions about a video concern one physical object. Where does the ball end up after the cups are shuffled? Which card is the queen? How often was the mug covered? Video-language models (Video-LMs) recognise such objects in single frames but do not keep them apart over time. On real shell-game videos, open models from 8B to 235B parameters, their thinking variants, a reinforcement-learned tool agent and three training-free tool agents all stay within ten points of chance. We separate seman...

---

### 23. AnyGameRenderer: Entity-Consistent Generative Rendering Across Games and an Entity-Level Benchmark

**Authors:** Ruicong Liu, Liangyang Ouyang, Fengbo Lan, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31466v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31466v1)

**Summary:** AI coding agents can now build small playable games in minutes, but the results usually look like programmer art: gray blockouts, colored geometric primitives, and flat semantic blobs. We present AnyGameRenderer, a video-to-video generative renderer that turns such footage into high-quality visuals with characters, motion detail, and effects. Throughout, it keeps the layout, camera, and every entity's position and timing intact.   Our AnyGameRenderer generalizes across a wide range of genres tha...

---

### 24. MixPT: Point Transformer with Interleaved Window and Global Attention

**Authors:** Minkyun Seo, Hyungtae Lim, Jaesik Park

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31455v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31455v1)

**Summary:** Point cloud transformers aim to capture detailed local geometry and relationships across a scene at a manageable computational cost. Two common approaches are window attention and global attention. They differ in how they enable scene-wide interaction, which refers to information exchange among tokens across a scene. Window attention reduces computational cost by restricting self-attention to groups of tokens called windows; in serialized designs, each window contains a fixed number of consecuti...

---

### 25. A Sparse Topometric Graph for Scalable Cross-Session Indoor Navigation

**Authors:** Eun Sun Lee, Minkyun Seo, Gwangtak Bae, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31432v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31432v1)

**Summary:** A conventional embodied agent in an indoor environment builds a map by accumulating noisy real-world measurements and results from heavy inference to guide navigation. While the detailed measurements may differ due to scene changes or sensor settings, the unique topological structure of navigable passages or the connectivity between rooms may provide training-free guidance that complements local observations. We propose a sparse topometric graph as an efficient structural representation for robu...

---

### 26. A Task-Centric Survey of Long-Document Visual Question Answering: Taxonomy, Evolution, and Future Directions

**Authors:** Yufei Tong, Guanjie Cheng, Tianle Wu, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31385v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31385v1)

**Summary:** Visual document understanding is essential for acquiring knowledge from visually rich documents and is attracting growing research interest. Existing surveys emphasize architectures or technical approaches, with limited attention to how task bottlenecks shape technical choices and research priorities. We present a task-centric survey that decomposes long-document visual question answering (VQA) into four components: document parsing, evidence organization and retrieval, generator organization an...

---

### 27. WeVisOne-VL: Unified Visual Perception from Objects to Pixels

**Authors:** Tianming Liang, Junyi Pan, Yuxi Li, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31329v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31329v1)

**Summary:** Existing vision-language models (VLMs) remain unreliable for fine-grained visual perception. In this report, we present WeVisOne-VL (WeChat Vision All-in-One), a powerful VLM that unifies object-level and pixel-level perception through structured next-token prediction. It supports multiple visual tasks including object detection, referring localization, counting, OCR, segmentation, and matting, enabling localization at any user-specific granularity, from points and boxes to masks and alpha matte...

---

### 28. MVLoMa: Multi-View Local Feature Matching with Any Geometry Foundation Model

**Authors:** Xinyang Lu, Shengzhe Wei, Sheng Tang, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31321v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31321v1)

**Summary:** Local feature matching is typically formulated for image pairs, although structure-from-motion and visual localization commonly match one reference image against many retrieved or covisible neighbours. Applying a pairwise matcher independently to these centre-neighbour edges duplicates reference-side computation and prevents the matcher from exploiting complementary multi-view geometric evidence from the remaining observations. To address these limitations, we introduce MVLoMa, a sparse star-gra...

---

### 29. Stream4D: Streaming 4D Reconstruction with Training-free Motion Decoupling via Causal KV-Cache Attention

**Authors:** Wei Zhang, Ying Feng, Mengtong Wu, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31320v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31320v1)

**Summary:** 4D scene reconstruction requires robust handling of dynamic objects, yet existing streaming methods commonly assume static scenes, leading to pose drift and ghosting artifacts over long sequences. We introduce Stream4D, a training-free, motion-decoupled streaming reconstruction framework that can be directly integrated into causal Transformer backbones (e.g., StreamVGGT, Stream3R). Our key observation is that causal attention implicitly encodes rich temporal motion cues within the KV cache. We a...

---

### 30. Data-Driven Vision-Language Models for Remote Sensing: A Survey

**Authors:** Yue Zhou, Shujun Zhao, Xue Yang, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31304v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31304v1)

**Summary:** During the deep learning era, innovations in remote sensing (RS) vision models primarily focused on optimizing network architectures for specific tasks and conducting end-to-end training. However, with the advent of the Vision-Language Models (VLMs) era, constrained by substantial computational resource demands, the mainstream research paradigm has shifted towards adapting general-purpose VLMs using RS vertical domain data for fine-tuning, rather than modifying their core architectures. This tra...

---

### 31. PiHand: Latent Hand-Object Interaction Priors for Physics-Based Policy Learning

**Authors:** Niklas Berndt, Xianghui Xie, Enes Duran, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31299v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31299v1)

**Summary:** Synthesizing physically grounded dexterous hand-object interactions is important for VR/AR, gaming, and robotics, yet remains challenging because subtle contact dynamics, diverse object geometries, and target trajectories must be jointly respected while maintaining natural grasps. Existing methods either track mocap trajectories with limited transfer to novel objects, or rely on hand-only generative priors that fail to capture coupled hand-object motion, sacrificing contact fidelity and sample e...

---

### 32. RecallGS: Geometry-Grounded Recall for Online Semantic Gaussian Splatting

**Authors:** Thanh-Khoi Nguyen, Thien-Phuc Tran, Minh-Triet Tran

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31293v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31293v1)

**Summary:** Online semantic 3D Gaussian Splatting (3DGS) enables open-vocabulary scene understanding from streaming observations. However, existing methods recover geometric context missing from image-derived semantic features using an additionally learned 3D network, incurring extra training and runtime overhead. We observe that such geometric-semantic evidence may already exist in the agent's observation history and can be retrieved rather than learned. Based on this insight, we introduce RecallGS (Geomet...

---

### 33. Retrieval-Augmented Online Textual Memory for Episodic Memory Video Question Answering

**Authors:** Raffaele Cali, Giuseppe Lando, Rosario Forte, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31284v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31284v1)

**Summary:** Long egocentric videos pose a central challenge for multimodal language models: the visual stream must be compressed into a memory representation that can be searched efficiently while still preserving the evidence needed for question answering. Building on an online textual-memory framework in which first-person videos are converted into temporally grounded captions, this work systematically studies the role of retrieval in episodic-memory video question answering. We evaluate how different ret...

---

### 34. ReCoG: Relational Concept Graph for Training-Free Personalization

**Authors:** Changseon Yu, Hyeokjun Kweon

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31282v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31282v1)

**Summary:** Training-free personalization adapts a frozen vision-language model (VLM) to recognize user-defined concepts from only a few exemplars by retrieving concept entries at inference time. While recent retriever-based methods enrich each concept with descriptive evidence, they largely treat concepts in isolation, so the retrieved information can be plausible yet non-discriminative, especially when the personalized concept set contains highly confusable, fine-grained categories. We argue that personal...

---

### 35. Reinforcing intra-operative tumour localisation with weak supervision from pre-operative appearances

**Authors:** Sidhart Sami, Ali Sharjeel, Sri Atluri, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31253v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31253v1)

**Summary:** Limited tumour visibility on intra-operative images complicates surgical navigation, including liver hepatocellular carcinoma (HCC) targeting on computed tomography (CT) imaging. This makes labelled datasets difficult to curate for deep learning, and transferring pre-operative delineations through registration remains challenging due to intra-operative deformation and lack of paired pre- and intra-operative data. We propose to transfer tumour appearances learned from pre-operative magnetic reson...

---

### 36. Lightweight Frame Compensation for Real-Time Polyp Segmentation under Frame Skipping

**Authors:** Weihao Gao

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31228v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31228v1)

**Summary:** Real-time polyp segmentation in computer-assisted colonoscopy is hampered by the difficulty of deploying high-accuracy models under strict latency budgets. Frame skipping, which performs inference every K frames and reuses or interpolates the rest, improves throughput but introduces motion blur and lesion misalignment that degrade temporal consistency. To close this gap, we propose the Lightweight Frame Compensator (LFC), a 77K-parameter plug-and-play module inserted before a frozen segmentation...

---

### 37. GLOW-FM: Efficient Generative Low-Light Image Enhancement with One-Step Latent Flow Matching

**Authors:** Ariel Lapid, Yuval Haitman, Reuven Peretz, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31222v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31222v1)

**Summary:** Low-light image enhancement (LLIE) aims to recover well-exposed and perceptually faithful images from severely degraded observations. Recent diffusion-based generative methods achieve strong perceptual quality by leveraging powerful image priors, but their iterative sampling incurs substantial computational cost, limiting practical deployment. Despite recent efficiency gains in generative LLIE, high-quality enhancement with a single function evaluation and low overall computation remains challen...

---

### 38. Moving Regions, Not Moving Objects: Segmenting What Actually Moves under Camera Motion

**Authors:** Wenhua Jin, Tiancheng Chen, Sheng Tang, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31209v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31209v1)

**Summary:** Moving object segmentation is conventionally formulated at the sequence and object level, marking an entire instance as moving once it moves anywhere in a video. Recent instantaneous formulations distinguish moving from stationary intervals, but still generate masks at the object level through frozen segmentation foundation models. Because the mask is derived from an instance-level proposal, motion is typically attributed to the entire instance rather than localized to the regions that actually ...

---

### 39. A Visual Grounding Benchmark for Retinal OCT with Multimodal Large Language Models

**Authors:** Ronald Fecso, José Morano, Botond Fazekas, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31205v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31205v1)

**Summary:** Multimodal large language models (MLLMs) can answer clinical questions about medical images, but trustworthy use requires visual grounding: models should localize the pathology they report rather than rely on spurious shortcuts. Whether MLLMs can visually ground clinical findings in retinal optical coherence tomography (OCT), the most widely used imaging modality in ophthalmology, remains largely unexplored. To address this gap, we introduce RetinaGroundBench, the first benchmark for biomarker v...

---

### 40. Inside-JEPA: From Prediction to Relational Grounding in Latent World Models

**Authors:** Hossein Resani, Javen Qinfeng Shi

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31194v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31194v1)

**Summary:** Joint-embedding predictive architectures (JEPAs) learn world models in latent space, enabling efficient planning but leaving their states opaque. We introduce Inside-JEPA, which places relational channels for ordered entity pairs inside the JEPA latent state and shows that an inverse-dynamics loss can ground these channels without relation labels when its head reads them, either alone or as part of the full state. On Something-Something V2, latent prediction alone performs no better than a rando...

---

### 41. RaSFNet: Ray-aligned and Scan-aware Fusion Network for LiDAR Semantic Segmentation

**Authors:** Chuang Chen

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31186v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31186v1)

**Summary:** LiDAR point cloud semantic segmentation is a fundamental component of 3D perception for autonomous driving and robotics. Projection-based methods map 3D point clouds into 2D representations for feature extraction using 2D networks. However, aggregating multiple points during projection can obscure geometric differences within each frustum, while local feature extraction limits the modeling of spatial relationships across scanning regions. Moreover, proximity in the projected representation does ...

---

### 42. Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation

**Authors:** Chenyuan Chen, Ran Ding, Lechen Zhang, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31166v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31166v1)

**Summary:** Humanoid loco-manipulation in dynamic scenes is non-Markovian: cues vanish as objects change or are hidden, or leave the view as the robot turns and walks, yet whole-body vision-language-action (VLA) policies see only the present. We present WholeBodyMem, an object-guided perceptual memory that keeps the pre-history of object events seen before the robot acts on its goal. SAM3 tracks the task objects, and their events causally select key frames within an adaptive budget, which the action expert ...

---

### 43. HiSTEVE 1.0: Harnessing Human-Interface VLA Agents for Open-World Games

**Authors:** Zecong Tang, Zian Guan, Yuncheng Guo, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31162v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31162v1)

**Summary:** Building virtual embodied agents that operate in open-ended games like human players is a long-standing goal requiring both long-horizon autonomy and reliable native-interface control. As a procedurally generated open world, Minecraft provides a natural testbed for studying the integration of these capabilities. Existing agents typically provide either native visuomotor control without long-horizon autonomy or high-level planning executed through environment APIs or predefined skills. To bridge ...

---

### 44. Beyond Watching and Searching: Benchmarking Agents for Video-centered Deep Research Reports

**Authors:** Jiahao Meng, Qize Yang, Yuxuan Wang, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31158v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31158v1)

**Summary:** Deep research agents synthesize open-web evidence into long reports, but current benchmarks do not evaluate research centered on a source video. We introduce Video-Centered Deep Research Report Generation. Given a video and user request, an agent identifies research questions, retrieves external multimodal evidence, and produces an interactive report linked to relevant video moments. This task has direct practical value because it helps users locate relevant moments, verify claims, reproduce dem...

---

### 45. WildFakeToolBench: Benchmarking AI-Generated Image Detectors with Web-Sourced Image Processing

**Authors:** Mingjie Li, Yukun Jiang, Yicong Tan, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31152v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31152v1)

**Summary:** As AI generated images are getting popular these days, discussions on such generations are widely existed in current public forums, software repositories, and photography tutorials. Moreover, with the help of LLM-assisted code translation, malicious actors can adopt such information to evade detectors without specialized knowledge or local GPU execution of the resulting tools. To evaluate such risks, we introduce \textsc{WildFakeToolBench}, a benchmark suite of $156$ executable image-processing ...

---

### 46. Navigating human-robot interaction challenges in private and residential aged care homes

**Authors:** David Ahmedt-Aristizabal, Mohammad Ali Armin, Akila Pemasiri, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31149v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31149v1)

**Summary:** This chapter explores how robotic systems and ambient intelligence can enhance care for older adults in residential aged care (RAC) homes and private homes. Although these settings differ, we frame both as extreme and challenging environments for human-robot interaction (HRI), characterised by cluttered and dynamic layouts, diverse resident needs, and limited on-site technical support. We review embodied and non-embodied systems that assist with daily living, safety monitoring, and social engage...

---

### 47. RankAlign: Vision-Language Representation Alignment via Rank Transformation

**Authors:** Enzhe Zhao, Marco Fiorucci, Lamberto Ballan

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31145v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31145v1)

**Summary:** While the Platonic Representation Hypothesis posits that vision and language models converge toward compatible latent geometries, recovering class-level correspondences between unpaired modalities without cross-modal supervision remains challenging. Existing relational matching methods compare within-modality similarity kernels directly, although the same semantic structure may be represented through different numerical parameterizations across modalities. We propose RankAlign, a rank-based norm...

---

### 48. GM-GReFEL: Geometry-Guided Spatiotemporal State-Space Learning for Robust Dynamic Facial Expression Recognition

**Authors:** Yudhistira Arditya Pratama, Yi-Zeng Hsieh

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31140v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31140v1)

**Summary:** Recognizing facial expressions in unconstrained video suffers from two coupled problems: self-attention grows quadratically in cost with clip length, and crowdsourced labels are noisy. We present GM-GReFEL, a spatiotemporal state-space network with a geometry-aware decision stage. Its Modulated GroupMamba backbone replaces a spatiotemporal Vision Transformer. Six channel groups are scanned separately, four over the frame plane and two over time, so the cost grows linearly with sequence length ($...

---

### 49. Pos4CHD: A Positive-Free Mask-Guided Counterfactual Synthesis Framework for Fetal Congenital Heart Defect Analysis

**Authors:** Wenjie Xuan, Yapeng Li, Hang Su, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31139v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31139v1)

**Summary:** The scarcity of positive cases remains a major bottleneck in developing automated diagnostic systems for fetal Congenital Heart Defects~(CHDs), particularly for rare subtypes. Although normal cases are accessible with effort, positive cases are hard to collect due to low incidence rates and privacy concerns, causing severe class imbalance or absence of positive training samples. Existing works resort to synthesizing positives with conditional generative models, but they are task-specific and req...

---

### 50. WildDepth-v2: A Synchronized RGB--LiDAR--Radar Dataset and Benchmark for Metric Depth, Motion, and Tracking of Wildlife

**Authors:** Muhammad Aamir, Sangyun Shin, Naoya Muramatsu, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31123v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31123v1)

**Summary:** Measuring animal distance and motion in metric units underpins abundance estimation, morphometrics, and movement ecology, yet monocular video lacks metric scale and wildlife datasets lack metric ground truth. We present WildDepth 2, extending the synchronized RGB-LiDAR WildDepth dataset in three directions. (i) Imaging radar: 37 RGB-LiDAR-4D-radar sequences (19,716 frames) with per-point Doppler velocity and a measured error budget, to our knowledge the first imaging-radar wildlife recordings. (...

---

## cs.LG

**50 papers**

### 1. Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success

**Authors:** Yunfei Xie, Howard H. Qian, Shiyi Lan, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31670v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31670v1)

**Summary:** Robotic foundation models are typically evaluated through costly closed-loop rollouts, which motivates cheap offline proxies for model capability. The Platonic Representation Hypothesis (PRH) suggests that as representations improve, different modalities such as vision and language converge toward a shared statistical model of reality. We ask whether motion trajectories form another such modality: as embodied models become more capable, should their sensory representations converge toward the st...

---

### 2. Phase Transition from Random Features to Fully Trainable Networks

**Authors:** Xin He, Huan Lao, Xiliang Lu, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31663v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31663v1)

**Summary:** Constructing accurate and computationally tractable approximation spaces is a fundamental task in scientific computing. Partially trainable neural networks bridge fixed random features and fully adaptive representations. This paper quantifies a phase transition pattern in approximation bounds and observes analogous behavior in training errors: a rapid but smooth initial improvement followed by diminishing returns, with a sharper transition under greater initialization mismatch. Under polynomial ...

---

### 3. Reliable AI-Assisted Decisions via Selective Auditing

**Authors:** Isaac Gibbs, Elise L. Han, Ryan J. Tibshirani, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31662v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31662v1)

**Summary:** We consider online monitoring of an AI system that produces a sequence of decisions. At each round, the system outputs a proposed decision together with a confidence score estimating the trustworthiness of the decision. The decision and confidence score need not be produced by the same model: for example, one agent may propose a decision, while a separate verifier agent evaluates it and outputs a correctness or safety score. Based on this information, we must decide whether to accept the AI deci...

---

### 4. SpectralCanary: Embarrassingly Simple Low-Frequency Traces for T2I Dataset-Use Auditing

**Authors:** Sy-Tuyen Ho, Anirudh Satheesh, Soham Chawathe, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31659v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31659v1)

**Summary:** Auditing whether a text-to-image (T2I) model was fine-tuned on a particular image collection is difficult: a model can absorb collection-level visual characteristics without reproducing training images. Proactive dataset-use auditing plants a shared signal in a dataset before release, then later checks whether that signal appears in a suspect model's generated outputs. Existing approaches often trade off verifiability, fidelity, robustness, and deployability. We introduce $\textbf{SpectralCanary...

---

### 5. Cost-Aware Abstention for LLM-Based IT Ticket Classification

**Authors:** Sachin Gupta

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31657v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31657v1)

**Summary:** Wrong automatic routing of an IT support ticket can cost more than human triage. We evaluate cost-aware abstention as an offline, cost-conditional readiness assessment: select a routing policy on calibration data under explicit costs, then evaluate that frozen policy once on held-out test data. On a public 47,837-ticket, eight-class corpus, we compare four trained non-LLM classifiers with four large language models under zero- and few-shot prompting. Under the illustrative cost model (c_ok, c_tr...

---

### 6. METTA: Memory-Enhanced Test-Time Adaptation for Meta-Reinforcement Learning

**Authors:** Ali Najar, Hosein Hasani, Amir Kooshan Fattah, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31656v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31656v1)

**Summary:** Meta-reinforcement learning aims to train agents that adapt quickly to unseen tasks from limited interaction, but this requires representing task evidence over long interaction histories. Classical recurrent agents compress experience into hidden states, while transformer-based agents retrieve from past trajectories at quadratic memory and computation cost. In this work, we propose Memory-Enhanced Test-Time Adaptation (METTA) for meta-reinforcement learning. It decomposes the fast adaptation pha...

---

### 7. EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence

**Authors:** Qijin Zhang, Hanzhen Wang, Yuehan Zhao, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31650v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31650v1)

**Summary:** Tool-using language model agents rely on environmental facts to decide whether an action is permitted. When a tool response omits a safety-relevant fact, an agent may carry out a prohibited action even though the user request is benign and every returned statement is true. We introduce \bench{}, an executable benchmark for evaluating unsafe execution, safety boundaries, and evidence recovery in LLM agents under missing evidence. It contains 300 matched unsafe/safe task pairs across six domains. ...

---

### 8. A Fix for Softmax and Cross-Entropy

**Authors:** Jonathan T. Barron, Dan Gnanapragasam, Michael Tschannen

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31642v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31642v1)

**Summary:** Standard implementations of softmax, log-softmax, and cross-entropy have two numerical bugs. The first bug, Softmax Collapse, rounds the target logit's gradient to zero if that one logit is much larger than the others, resulting in gradients that no longer sum to zero. The second bug, Softmax Cancellation, occurs when student logits are close to teacher logits, and produces non-zero gradients even when the student and teacher logits are equal. We present simple implementations of log-softmax, so...

---

### 9. Causal Chain of Thought: Mitigating Attention Leakage via Context Isolation

**Authors:** Gabriele Dominici, Teague McMillan, Fazl Barez, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31639v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31639v1)

**Summary:** Chain-of-thought (CoT) prompting elicits step-by-step rationales that appear to explain model predictions, but there is no guarantee these steps causally drive the final answer. In standard autoregressive generation, dense attention allows each reasoning step to attend to the full context, enabling the model to derive answers through direct lookup while generating plausible-sounding but post-hoc justifications. We introduce CausalCoT, an inference framework that enforces causal transparency by d...

---

### 10. BeNice! Closing Looping's Inference-Memory Gap via KV-Sharing

**Authors:** Hayden Prairie, Jacob M. Ryan, Taylor Berg-Kirkpatrick, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31633v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31633v1)

**Summary:** Looped architectures scale quality while keeping parameter count fixed by repeatedly passing activations through the same block of layers. During inference, each recurrence generates independent KV-caches, causing memory to grow linearly. To address this challenge, prior work has proposed KV-sharing (i.e., sharing KV-caches across depth), finding that, in some cases, the KV-cache of the final recurrence can be shared with the earlier recurrences without quality loss, a property we denote as KV-s...

---

### 11. Questioning Instrumental Convergence in RLVR: Checkpoint Evidence from OLMo-3

**Authors:** Barış Alparslan, Sandy Tanwisuth, Caleb Petterson

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31624v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31624v1)

**Summary:** Instrumental convergence is often invoked as a general reason to expect capable agents to acquire or express power-seeking subgoals: self-preservation, resource acquisition, deception, or resistance to oversight which poses an important threat to the society. For LLMs, reinforcement learning is the first stage of post-training that directly optimizes behavior against an objective; therefore, it is the stage where convergent instrumental behavior, on IC grounds, likely to appear. Does reinforceme...

---

### 12. OP-Print: Tracing Membership Imprints in On-Policy Self-Distillation

**Authors:** Qi Li, Xinchao Wang

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31616v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31616v1)

**Summary:** On-policy distillation has been widely adopted for alleviating the distribution mismatch of off-policy distillation. Self-distillation further removes the need for an external teacher by using the student's own outputs, enhanced with extra context or demonstrations, as supervision. This teacher-free design makes on-policy self-distillation practical, yet its privacy risks remain largely unexplored. In particular, using two coupled views of the same training example may strengthen its memorizatio...

---

### 13. Efficient and Optimal Learning of Discrete Distributions with Person-Level Privacy

**Authors:** Gautam Kamath, Mahbod Majid, Ankur Moitra, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31612v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31612v1)

**Summary:** We study learning a discrete distribution under person-level differential privacy in the batched setting. Given $n$ users, each contributing $m$ i.i.d. samples from an unknown distribution $μ$ over $[k]$, we seek an estimate of $μ$ with total-variation error $α$. We give polynomial-time algorithms under both pure and approximate differential privacy. Under pure $(\varepsilon,0)$-DP, we achieve $n = \widetilde O(k/(α^2 m)+k/(α\sqrt{m}\varepsilon)+k/\varepsilon)$, the first polynomial-time pure-DP...

---

### 14. CRANE: Post-Hoc Counterfactual Retrieval for Multimodal Classifiers

**Authors:** Franco Rugolon, Ioanna Miliou, Panagiotis Papapetrou

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31594v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31594v1)

**Summary:** Counterfactual explanation methods have been introduced for unimodal settings, with dedicated frameworks for tabular, timeseries, text, and image data, yet no post-hoc method has been designed for classifiers that learn from multimodal inputs. Existing explainability methods for multimodal classifiers apply modality-specific attribution independently to each input, which fails to yield coherent explanations and does not transfer to arbitrary pre-trained multimodal architectures. To address these...

---

### 15. Beyond Best-of-$k$: Prior-Consistent DAPS for Ambiguous Nonlinear Inverse Problems

**Authors:** Merve Kocabas, Benjamin A. Burns, Andreas Geiger, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31592v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31592v1)

**Summary:** Diffusion models have become strong priors for solving inverse problems. However, nonlinear inverse problems such as phase retrieval remain challenging when multiple measurement-consistent solutions are distinguishable only by the prior; we call such measurements ambiguous. Existing diffusion-based samplers rely on local approximations during reconstruction. For an ambiguous measurement, these approximations can allow measurement guidance to favor a measurement-consistent mode that is close to a...

---

### 16. Would an LLM Match into a Residency? Uncertainty, Reasoning and Image Use of Open Language Models on the Spanish MIR Examination

**Authors:** Miguel Fernandez-de-Retana, Unai Zulaika, Ruben Sanchez-Corcuera, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31586v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31586v1)

**Summary:** Accuracy on medical examinations is common evidence offered for the clinical use of language models, yet a health system that intends to run an open model on its own hardware needs to know considerably more: whether the model recognizes when it is likely to be wrong, whether medical fine-tuning improves this ability, whether its correct answers rest on sound clinical reasoning, or whether it actually uses the images it is given. We examine these questions for four open models of 8 to 27 billion ...

---

### 17. Action Learning for Scientific Simulations

**Authors:** Sarah Liaw, Yuanqi Du, Yilun Du

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31585v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31585v1)

**Summary:** Understanding and controlling how systems evolve is central to science and engineering, where many problems require reasoning about complete trajectories. Existing approaches typically learn local dynamics or generate trajectories, but objectives constructed from individual transitions can miss dependencies across time, while generative models do not necessarily provide a tractable objective for evaluating and optimizing arbitrary paths. We study $\textit{action learning}$, the problem of recove...

---

### 18. Rethinking Sequence Compression with Test-time Regression

**Authors:** Sihan Yang, Jie Huang, Hanxuan Li, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31574v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31574v1)

**Summary:** Sequence compression is a fundamental operation and a critical information bottleneck in efficient language and multimodal models, and yet prevailing approaches based on pooling or learned projections remain underperforming. We revisit sequence compression through the lens of test-time regression: input tokens define a regression problem whose fitted coefficients form the compressed representation. Importantly, the regression problem is learned end-to-end via backpropagation, while its coefficie...

---

### 19. On the Token Collapse Phenomenon in Textual Graph Soft Prompting

**Authors:** Andrea Giuseppe Di Francesco, Rishabh Jain, Franco Maria Nardini, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31572v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31572v1)

**Summary:** Recent methods for injecting graph structure into LLM prompts include graph soft prompting, in which a graph neural network (GNN) learns graph-specific tokens that capture relational information among entities in textual prompts. G-Retriever combines graph soft prompts with a verbalized description of the same graph to strengthen the textual prompt signal. We conduct an in-depth analysis of G-Retriever and uncover a pathological behavior we term token collapse. Across three benchmarks, three gra...

---

### 20. When to Follow the Teacher: Advantage-Based On-Policy Distillation

**Authors:** Mahdi Sabbaghi, George Pappas, Hamed Hassani, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31563v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31563v1)

**Summary:** Online Policy Distillation (OPD) often outperforms offline methods such as Supervised Fine-Tuning (SFT) by training on trajectories sampled directly from the student. However, standard OPD trains the student to follow the teacher at every state of the trajectory, assuming that teacher guidance is always beneficial. We instead distinguish between what the teacher prefers and what actually helps the current student succeed. We introduce Advantage-Based On-Policy Distillation (AOPD), which weights ...

---

### 21. Diffusion Language Models for Perplexity-Aware Black-Box Attacks

**Authors:** Ali Al-Lawati, Elsayed Eshra, Dongwon Lee, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31558v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31558v1)

**Summary:** \emph{Continuous-space} attacks find prompts that trigger malicious behaviors, such as overthinking, in black-box LLMs by sampling or optimizing over a low-dimensional Gaussian latent space and decoding it to text through a \emph{random mapping} and nearest-token lookup. Because the random mapping is not learned from language, its prompts can be highly unnatural, and as such easily detectable through input guardrails, and the risk estimates they yield are not grounded in natural prompts. In this...

---

### 22. Fine-Grained Analysis of Catastrophic Forgetting in Continual Learning via Algorithmic Stability

**Authors:** Guodong Zheng, Yan Sun, Peng Wang, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31551v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31551v1)

**Summary:** Understanding catastrophic forgetting, in which learning new tasks degrades performance on previously learned tasks, remains a fundamental challenge in continual learning (CL). Existing theoretical analyses often rely on specific model or task structures and offer limited insight into how iterative optimization affects forgetting. To address this gap, we develop an algorithmic stability framework for expected population forgetting under SGD without prescribing a particular model architecture. Sp...

---

### 23. Shift-aware score transport for privacy auditing without retraining

**Authors:** Yaohong Yang, Gauri Pradhan, Qi Chen, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31549v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31549v1)

**Summary:** Privacy auditing empirically assesses privacy leakage by using membership inference attacks to establish lower bounds on privacy loss. We consider an observational auditing setting in which the auditor cannot insert canaries, control data inclusion, or retrain the target model, and must instead rely on fixed sets of known members and non-members. This setting is relevant for large deployed models or when retraining is restricted by computational or access constraints. In this case, non-members a...

---

### 24. Same Luck, Different Choice: Twin-World Credit Assignment for Agentic Reinforcement Learning

**Authors:** Zeropy Surio, Tobias Engel, Mei-Lin Chou, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31544v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31544v1)

**Summary:** Agentic reinforcement learning rewards a complete episode, yet the policy needs credit for every decision inside it. Counterfactual branching estimates this credit by re-running the episode after an alternative decision, but the branch draws its sampling noise independently of the factual episode, so the outcome difference mixes the effect of the decision with the luck of everything that follows. We observe that in agentic search the retriever, the corpus, and the grader are deterministic, so an...

---

### 25. PYTHIA, a transferable machine learning framework for simultaneous defect and adsorption site optimization

**Authors:** Ioannis Kouroudis, Zhaosu Gu,  Poonam, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31539v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31539v1)

**Summary:** Machine learning has permeated material optimization, providing high value. Nevertheless, its re- liance on a high number of samples limits its applicability to relatively explored material families. In this paper we extend the applicability of machine learning to novel and understudied materials through the PYTHIA (Probabilistic Yet Transferable Hierarchical Interaction Architecture) framework. Pythia utilizes two of the most powerful machine learning concepts, foundational models and transfer ...

---

### 26. LACToS: Local Anomaly Detection via Conditional Typicality of Superpixels

**Authors:** Jihoon Hong, Alireza Kheirandish, Rohan Sanda, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31538v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31538v1)

**Summary:** Local anomaly detection is the task of identifying spatially confined anomalous or out-of-distribution (OOD) regions within an otherwise in-distribution (ID) image. Most existing methods are designed for a specific context, with a strong focus on industrial defect detection, where they achieve excellent performance on well-established benchmarks. However, we observe that these methods can exhibit significant performance drops in other contexts, especially when the inlier distribution is multimod...

---

### 27. Direct Inference on Admissible Sets (Diona)

**Authors:** Lorenzo Sabug, Eric Kerrigan

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31526v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31526v1)

**Summary:** We propose a new regression method named Direct Inference on Admissible Sets (Diona) that directly uses samples to estimate the state and its derivatives at a query point, along with their admissible bounds, without long global training. By casting the values and derivatives at the query and neighbouring samples as latent variables in a constrained optimisation problem, the burden of long training loops becomes one of on-demand local solves. We establish Diona's theoretical properties including ...

---

### 28. Nonparametric autoregressive estimation of probability distributions with parallel gradient boosting

**Authors:** Rémy Chapelle

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31524v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31524v1)

**Summary:** Nonparametric estimation of joint probability distributions is a core problem in statistics, which is notoriously challenging with high-dimensional data. Such challenges also arise with conditional distribution estimation and have led to flexible algorithms that aim to tackle the ''curse of dimensionality'' by exploiting predictive structures of lower dimension than the ambient space. In this paper, we study the use of such conditional distribution estimators to estimate joint distributions by f...

---

### 29. Piano2Pop: Expanding Piano Demos into Pop Productions Without Aligned Supervision

**Authors:** Yun-Chen Cheng, Chih-Pin Tan, Tzu-Hung Huang, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31510v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31510v1)

**Summary:** We introduce Piano2Pop, a music-expansion task that transforms piano MIDI into instrumental pop productions. Enabled by recent advances in music generation and polyphonic music transcription, our pseudo-supervised approach conditions a pretrained flow-matching model on piano rolls without aligned piano-pop supervision. We train on synthetic piano-instrumental pairs derived from pop recordings, comparing pair-free transcription, including function-selective (FST) and register-density (RDA) augmen...

---

### 30. Structure-preserving reduced-order models of thin panels in supersonic and hypersonic flow

**Authors:** Miguel A. Aguilo

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31504v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31504v1)

**Summary:** We build structure-preserving reduced-order models for both challenge problems of the AePW-4 High-Speed Working Group. They are a clamped thin panel at Mach 1.92 (RC-19) and a cantilever plate at Mach 5.85 (HyMAX). The published data for each case hold no time-resolved response and no repeated runs. The physics must therefore be carried by the form of the model. One construction gives two models per problem. A Ritz-Galerkin reference model describes the plate. A learned model keeps the reference...

---

### 31. SABLE: Scalable Affine Bayesian Latent-space Exploration

**Authors:** Erik Bodin, Lisa Maria Kreusser, Donney Fan, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31495v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31495v1)

**Summary:** Complex objects such as engineering designs and proteins are often difficult to optimise because their design spaces exhibit high-dimensional structure and objective evaluations are expensive. Generative models provide continuous latent representations, but their latent spaces can have thousands to tens of thousands of dimensions, creating a regime where the latent dimension $D$ greatly exceeds the evaluation budget. We introduce SABLE, a Bayesian optimisation method for high-dimensional latent ...

---

### 32. Training Small Language Models for Transferable Tool Selection

**Authors:** Zhaoyi Zhou, Akshayaa Magesh, Jeongyeol Kwon, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31483v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31483v1)

**Summary:** As LLM agents operate over corpora of more than ten thousand tools, selecting the right tool for a complex multi-step user instruction becomes a central bottleneck. Tool descriptions cannot all fit in context, and relevance-based retrievers only rank tools without knowing which are actually needed. Recent work instead leverages proprietary commercial LLMs like Claude or ChatGPT to drive a retriever, decomposing the instruction and selecting over retrieved candidates. We show that a small, open m...

---

### 33. Evaluating the Applicability of LLM Inference Optimizations on Apple Silicon

**Authors:** Kyrylo Yemets, Andrii Yaroshevych, Victor Muryn, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31479v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31479v1)

**Summary:** Apple Silicon is among the most widely used platforms for local LLM inference, yet nearly all inference optimizations are designed and validated on server-class NVIDIA GPUs under batched serving workloads. Which optimizations retain their benefits when moved to Apple Silicon, and what determines their applicability? We evaluate four optimization families: KV-cache pruning, speculative decoding, ported GPU kernels, and post-training quantization. Experiments span four Apple machines under a commo...

---

### 34. MoG-VLM: Efficient Video Anomaly Detection through Motion-Guided Vision-Language Models

**Authors:** Khaled Waleed Dawoud, Muhammad Zaigham Zaheer, Khan Muhammad, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31478v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31478v1)

**Summary:** Vision-Language Models (VLMs) have shown strong potential for video anomaly detection, but dense frame-level inference makes them impractical for real-time deployment. Existing acceleration commonly relies on uniform sampling, which ignores content dynamics and can either waste computation on static segments or miss localized anomalies. We propose MoG-VLM a motion-adaptive anomaly detection framework that leverages motion purely as a lightweight control signal to decide when VLM inference is nec...

---

### 35. RheOPT: Few-Shot Non-Newtonian Flow Prediction via Newtonian Pretraining of RheOFormer

**Authors:** Maedeh Saberi, Amir Barati Farimani, Safa Jamali

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31465v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31465v1)

**Summary:** Despite advances in numerical methods, non-Newtonian flow simulations remain computationally expensive because velocity and stress must be advanced together through rate- and history-dependent constitutive dynamics. Neural-operator surrogates reduce inference cost after training, but their training data require the same expensive simulations they aim to replace, making data-efficient learning essential when only a few non-Newtonian simulations can be afforded. Here, we introduce the Rheological ...

---

### 36. Multi-Token Prediction and Alternative Tokenization Improve Learning Latent Multi-Hop Graph Search at Scale

**Authors:** Arvid Frydenlund, FuTe Wong, Katherine Lambert, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31439v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31439v1)

**Summary:** Given an unseen graph, a start node, $s$, and an end node, $t$, can a language model generate the shortest path from $s$ to $t$? Prior work has found that models fail to learn this task as the graphs scale. We show that this failure has two causes: the supervision signal and the tokenization. First, we theoretically establish and empirically demonstrate the effectiveness of multi-token prediction (MTP), and show that the benefits of MTP are topologically agnostic. Second, we introduce alternativ...

---

### 37. DIAL: Steerable Language Models with Distilled Instruction-Adherence Levels

**Authors:** Thanh Q. Tran, John Russell Himawan, Arun Verma, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31438v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31438v1)

**Summary:** When a user says "Keep it short", how short should the LLM's response be? More generally, users and applications require different levels of instruction adherence, but prompting does not reliably provide fine-grained control over them. We therefore study "steerable language models" that provide fine-grained numerical control over the degree to which models follow general instructions specified in text. However, existing approaches do not jointly offer fine-grained control, efficiency, and scalab...

---

### 38. Conservative Meta-Agent Search: Architecture Adaptation under Non-Stationarity

**Authors:** Ali Atiah Alzahrani

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31436v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31436v1)

**Summary:** Automated agentic-system design is typically evaluated on static task suites with immediate scalar rewards. Deployed systems face persistent shift, delayed dependent feedback, correlated component failures, and costly architecture changes. We formalize meta-agent architecture search as sequential incumbent replacement with switching costs and hard risk constraints and introduce Conservative Meta-Agent Search (CMAS). CMAS retrieves archived architectures and proposes typed graph edits, then score...

---

### 39. Drift Says When, Budget Says How Much: Rate-Controlled KV Re-selection for Long-Form Multimodal Generation

**Authors:** Bin Hu, Yingbo Xiao

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31433v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31433v1)

**Summary:** KV cache compression for multimodal LLMs usually selects the visual tokens to keep once, at prefill, and reuses that selection for the whole generation. We show that this one-shot selection is severely limited on long-form generation: on detailed image description, even an oracle that selects with the attention of the uncompressed answer reaches only 0.44-0.52 ROUGE-L agreement with the uncompressed output, because the evidence the model reads moves as the description unfolds. Re-selecting whene...

---

### 40. Dimension-free regimes for unadjusted Langevin in ridge-separable models: A subspace robust Wasserstein analysis

**Authors:** Yuansi Chen, Francesco Pedrotti, Peter A. Whalley

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31431v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31431v1)

**Summary:** The Unadjusted Langevin Algorithm (ULA) is widely used for high-dimensional Bayesian inference. Classical analyses in Wasserstein-2 distance predict an asymptotic bias and a mixing time that grow with dimension, but this metric is stronger than necessary for many statistical tasks. We instead analyze the bias in subspace robust Wasserstein distance, which controls the mean and arbitrary low-dimensional marginals and is therefore well suited to observables typically estimated in practice. For rid...

---

### 41. Predictable performance is suboptimal, and what it means for model routing

**Authors:** Guanhua Zhang, Moritz Hardt

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31428v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31428v1)

**Summary:** Large language models (LLMs) differ in capabilities and costs, motivating routing methods that adaptively choose a model for each query. These methods rely on performance prediction: given a query, estimate whether a model will answer it correctly. Most routing methods train separate predictors of candidate models' performance to guide model selection. Our work shows that performance prediction only beats a simple baseline when the candidate model is suboptimal on the task or the performance pre...

---

### 42. How Depth Growth and Looping Shape In-Context Learning in Language Models

**Authors:** Ferdinand Kapl, Kaitlin Maile, Stefan Bauer, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31421v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31421v1)

**Summary:** Looped and depth-grown language models reuse computations across depth and have attracted interest for their reasoning capabilities. Building on prior suggestive evidence of improved in-context-learning (ICL), we investigate how such reuse favors ICL, including how it shapes the acquisition, retention, and mechanisms of this ability. Our analysis spans pretrained language models up to 3B parameters and controlled tasks. The experiments provide evidence for a shared inductive bias toward learning...

---

### 43. Post-Hoc Feature Selection Layer for Neural Networks Interpretability

**Authors:** João Kenji Suwa, João Pedro Silveira e Silva, Bruno Iochins Grisci

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31420v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31420v1)

**Summary:** The interpretability of complex neural networks remains a critical challenge, especially for models already deployed in high-stakes domains. To address this, we adapted the Feature Selection Layer (FSL) to optimize feature weights post-training, a variant we term post-hoc FSL. Our approach reframes the FSL as a lightweight, trainable module that integrates with already frozen pre-trained models on tabular datasets to highlight the features the original model considers most important. This post-h...

---

### 44. SQuAT: Spherical Lattice Vector Quantization-Aware Training

**Authors:** Sebastian Loeschcke, Ivan Koryakovskiy, Tycho F. A. van der Ouderaa, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31412v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31412v1)

**Summary:** Vector quantization (VQ), in particular lattice-based methods, offer strong rate-distortion trade-offs for low-bit large language models (LLMs), yet their behavior under quantization-aware training (VQ-QAT) remains poorly understood. We scale lattice VQ-QAT to billion-parameter LLMs and multi-billion-token training regimes, and introduce SQuAT, a shape-gain VQ-QAT approach trained with a separate straight-through estimator (STE) for the shape and gain. SQuAT decomposes weights into direction and...

---

### 45. HERD: Harness-Evolving Recursive Distillation for Continual Learning

**Authors:** Xun Sun, Thanh Thi Nguyen, Thuy-Trang Vu

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31401v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31401v1)

**Summary:** Continual learning requires a model to keep acquiring new skills and knowledge without compromising its existing capabilities. Parametric methods suffer from catastrophic forgetting and loss of plasticity. Non-parametric methods, such as prompts, skills, and harnesses, leverage in-context learning but are limited by context length and lossy plain-text compression. To effectively combine their complementary strengths, we propose HERD (Harness-Evolving Recursive Distillation), a hybrid continual l...

---

### 46. Convex Equilibrium Potentials for Monge--Ampère: Curvature Bounds and A Posteriori Evaluation

**Authors:** Edison Vázquez, Yingdong Lu, Tomasz Nowicki

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31386v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31386v1)

**Summary:** Equilibrium neural networks define their hidden state as the fixed point of a contraction, so their effective depth is set at evaluation time rather than by the architecture. Using them for fully nonlinear PDEs raises two issues that explicit networks avoid: second derivatives may grow with the effective depth, and the potential is only ever evaluated approximately. We study nonnegative softplus equilibrium networks with contraction factor $q<1$, a convex class suited to the Monge--Ampère equati...

---

### 47. AfterDeleteBench: Auditing Post-Deletion Information Persistence in LLM Agents

**Authors:** Ehsan Saleh, Roozbeh Nahavandi, Sama Salarian, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31366v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31366v1)

**Summary:** Many LLM agents maintain external persistent memory and derive additional state from past interactions, such as summaries. Deleting an original memory record therefore need not remove information carried by its descendants. We introduce AfterDeleteBench, a controlled behavioral audit for this failure mode in fixed-weight LLM agents. For each synthetic secret, we compare an exposed-then-deleted agent with an otherwise matched agent that was never exposed to the secret, allowing post-deletion reco...

---

### 48. Graph-Recurrent Learning of Emergent Collective Dynamics

**Authors:** Ali Rayat, Acacia Lee, Gia-Wei Chern

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31350v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31350v1)

**Summary:** Collective ordering in correlated electron systems emerges from microscopic dynamics, yet the evolution of observable textures need not admit a closed, memoryless description. We introduce a graph-recurrent neural network (GRNN) framework that learns such emergent dynamics directly from trajectories without specifying microscopic equations of motion. The framework integrates gated recurrent memory with graph message passing: local hidden states encode information beyond the instantaneous observa...

---

### 49. Metric Conformal Prediction via the Conditional Expected Local Radius

**Authors:** Rui Qiu, Fang Yao, Zhou Yu

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31336v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31336v1)

**Summary:** We introduce the conditional expected local radius (CELR) and develop a new conformal prediction method for non-Euclidean responses in general metric spaces. CELR measures local conditional probability concentration, allowing prediction sets to accommodate heterogeneity and multimodality without requiring densities or a vector space structure. Its conditional distribution yields a nonconformity score that is comparable across covariate values and avoids costly transport comparisons between dista...

---

### 50. Harmful Responses Are Jailbreak Templates: Transferring Autoregressive Jailbreaks to Diffusion Language Models

**Authors:** Jinwei Gan, Zifeng Cheng, Zhiwei Jiang, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31331v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31331v1)

**Summary:** Diffusion large language models (dLLMs) enable flexible masked generation through bidirectional context modeling, but this capability also introduces a distinct jailbreak attack surface. We find that a harmful response to a given query naturally serves as an effective jailbreak template: simply masking a subset of its tokens can induce a dLLM to reconstruct harmful content. Based on this observation, we propose RMT-Jailbreak, a general framework that transfers existing autoregressive (AR) jailbr...

---

## cs.NE

**50 papers**

### 1. First hardware demonstration of a continuous-state probabilistic computer with programmable energy-defined sampling

**Authors:** Chao Fang, Hsuan Yao Tu, Yihan He, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31339v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31339v1)

**Summary:** Probabilistic computing has proved useful for combinatorial optimization, but conventional implementations rely on binary stochastic units and sigmoid-based updates. Extending these systems to continuous variables requires binary encoding. Here we introduce a continuous probabilistic computer (CPC) whose continuous probabilistic bits sample bounded states from conditional distributions defined by local energies. Separating random-source generation from conditional sampling provides a route to us...

---

### 2. AgenticEvolve: Evolutionary Program Search with Persistent Language Model Agents that Design and Run Experiments

**Authors:** Ze-Yu Peng, Qing-Yu Lan, Zhan-He Wang, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31326v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31326v1)

**Summary:** Evolutionary program search with large language models keeps the structure of an evolutionary algorithm and uses the model as its variation operator. Typically, the model generates each candidate program in a single request from parent programs and their scores. We present AgenticEvolve, an evolutionary program search framework in which each island is run by a persistent large language model agent. Between evaluations, the agent designs and runs experiments on the candidate program. To measure t...

---

### 3. HGM-Dual: Lineage-Aware Guided Agent Harness Optimization for Long-Horizon Planning

**Authors:** Sudipta Paul, Pengrui Quan, Aounon Kumar, et al.

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.30042v1) | 📄 [PDF](https://arxiv.org/pdf/2610.30042v1)

**Summary:** Harness optimization, which improves an agent's prompts, tools, and workflows, is an increasingly effective way to enhance agents built on frozen or closed-source LLMs. Leading approaches such as the Darwin--Godel Machine and the Huxley--Godel Machine (HGM) rely on recursive self-improvement and were developed mainly for coding, where the competence needed to improve the agent coincides with the competence being improved. Planning tasks, in which an agent must produce a sequence of tool calls th...

---

### 4. Bio-Inspired Auditory Processing: Coupling Parallel Resonate-and-Fire Dynamics with Ternary Recurrent Networks for Speech Recognition

**Authors:** Pavlos Poulos, Katelyn Sadorf, Themos Stafylakis, et al.

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29720v1) | 📄 [PDF](https://arxiv.org/pdf/2610.29720v1)

**Summary:** Spiking Neural Networks (SNNs) promise energy-efficient inference through sparse, event-driven computation, yet remain constrained on continuous, context-dependent tasks such as automatic speech recognition (ASR). A key bottleneck is the Leaky Integrate-and-Fire (LIF) neuron, whose membrane decay erases information across pauses and phonetic boundaries while it must both extract features and retain long-range context. Inspired by cortical separation of nonlinear filtering and somatic integration...

---

### 5. Probing Spatial and Spectral Grounding in EEG Foundation Models

**Authors:** Kleanthis Avramidis, Ivan Tashev, Dimitra Emmanouilidou

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29367v1) | 📄 [PDF](https://arxiv.org/pdf/2610.29367v1)

**Summary:** EEG foundation models are advancing at an unprecedented pace, yet their evaluation is driven by downstream accuracy, which reveals little about whether their predictions rely on physiologically interpretable signal structure. We introduce a set of perturbation probes in two grounding axes: spatial grounding in channel identity and topographic locality, and spectral grounding in oscillatory content and waveform morphology. We apply these probes to five published EEG foundation models across motor...

---

### 6. BrainCodes: A Lightweight EEG Foundation Model over Discrete Neural Codes

**Authors:** Kleanthis Avramidis, Ivan Tashev, Dimitra Emmanouilidou

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29320v1) | 📄 [PDF](https://arxiv.org/pdf/2610.29320v1)

**Summary:** Recent electroencephalography (EEG) foundation models increasingly emphasize model scale, potentially limiting their deployment on resource-constrained devices and in everyday environments. We argue that transferable EEG features can instead be learned with a compact architecture and introduce BrainCodes, a lightweight foundation model pretrained through self-supervised learning on more than 800 hours of recordings from over 1,000 participants. Our architecture combines a quantization-based neur...

---

### 7. Reconstruction differences rival individual differences in the fly compass connectome and break trained circuit models

**Authors:** Md Ali Ashraf Yad, Nazifa Tabassum Nabila

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29205v1) | 📄 [PDF](https://arxiv.org/pdf/2610.29205v1)

**Summary:** Neural network models are increasingly constructed from synapse-resolution connectomes, and the same circuit is now available in reconstructions from other animals and pipelines. We do not know whether such models are dependent on the reconstruction they are built from, and whether connectome differences are biological or measurement errors. We studied the Drosophila head-direction circuit in nine versions: four flies (male CNS, hemibrain, Fly Wire, BANC) and five variants of the same fly varyin...

---

### 8. Gate Initialisation versus Recurrent Dropout and Zoneout in Learning Long Dependencies: A Controlled Study of LSTM and GRU Networks on Synthetic Tasks

**Authors:** Oleksandr Kholodniak, Oleksandr Prokhorov

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29034v1) | 📄 [PDF](https://arxiv.org/pdf/2610.29034v1)

**Summary:** Dropout and zoneout are routinely added to long short-term memory (LSTM) and gated recurrent unit (GRU) networks, but, to our knowledge, their placements have not been crossed with gate initialisation in a factorial design, and it is not known whether early gradient propagation tells which runs will learn long dependencies. We trained one-layer LSTMs and GRUs on the adding problem and on delayed recall in a factorial grid of 720 runs, crossing conventional and chrono gate initialisation with up ...

---

### 9. Unit-Aware Differentially Private Quantum Machine Learning for Clinical and Wearable Health Data

**Authors:** Md Khalid Syfullah, Alvi Ataur Khalil

**Published:** 2026-10-20

🔗 [Paper](http://arxiv.org/abs/2610.28968v1) | 📄 [PDF](https://arxiv.org/pdf/2610.28968v1)

**Summary:** Clinical registries and wearable sensors support early health-risk assessment, yet models trained on these records may leak sensitive information when released. Differential privacy (DP) bounds this leakage by injecting noise whose total magnitude grows with the number of trainable parameters, a cost especially severe for small health cohorts. This motivates parameter efficient models including quantum machine learning (QML), whose variational circuits can represent complex decision boundaries w...

---

### 10. Multi-Objective Evolutionary Semi-Supervised Learning for Resource-Aware Smart City Classification

**Authors:** Francisco José Sedeño, Jamal Toutouh

**Published:** 2026-10-20

🔗 [Paper](http://arxiv.org/abs/2610.27703v1) | 📄 [PDF](https://arxiv.org/pdf/2610.27703v1)

**Summary:** Smart-city applications often combine scarce labeled data with abundant unlabeled observations. Semi-supervised learning (SSL) exploits both labeled and unlabeled data to improve classification under limited supervision. This article presents MOEA-SSL, a multi-objective evolutionary approach for lightweight semi-supervised tabular classification that jointly optimizes predictive quality and feature usage. Experimental evaluation on three Smart City classification datasets, considering 1\%, 5\%, ...

---

### 11. Hybrid metaheuristics for architectural design optimization under small evaluation and wall-clock budgets

**Authors:** Luciano Ambrosini

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26202v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26202v1)

**Summary:** Architectural and structural design optimization in parametric software affords about a thousand evaluations of an expensive model for problems with tens of variables, a regime for which most metaheuristics were not designed. On the side of artificial intelligence, two hybrid metaheuristics are proposed: a covariance matrix adaptation evolution strategy (CMA-ES) whose sampling is enriched with differential-evolution trial vectors, and a particle swarm with success-history parameter adaptation, d...

---

### 12. A Spiking Ring-Attractor Architecture for Representation and Control of Revolute Robot Joints

**Authors:** Aung Htet, Alejandro Rodriguez Jimenez, Ruidong Ma, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26027v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26027v1)

**Summary:** Robotic systems with revolute joints evolve on circular state spaces, yet most control architectures represent these states using Euclidean variables that ignore this underlying geometry. We propose a fully spiking neural control architecture in which ring attractors encode joint states, enforcing representations consistent with the topology of revolute systems. Homeostatic regulation computes goal-state mismatch directly over these distributed representations, and opponent gain-modulated popula...

---

### 13. Sector-Ring Linear Reservoirs: Sector-Wise Decay-Timescale Allocation With State Reuse Across Candidate Settings

**Authors:** Yudai Ebato, Sou Nobukawa, Yusuke Sakemi, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.25806v1) | 📄 [PDF](https://arxiv.org/pdf/2610.25806v1)

**Summary:** In reservoir computing, performance depends on whether the fixed dynamics of the reservoir suit the task, and the appropriate memory length and frequency response differ across tasks. The reservoir settings are found by a search on each task, and driving the reservoir with the input and collecting its states for every candidate setting dominates the cost of the search. In a reservoir with a linear recurrence, the dynamics decompose into modes, one per eigenvalue, and the eigenvalue distribution ...

---

### 14. Migrate Computation, Not Data: Fault Recovery in Neuromorphic Many-Core Systems

**Authors:** Muyang Cao, Di Yu, Peiling Zhu, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26985v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26985v1)

**Summary:** As neuromorphic systems scale to thousands of near-memory cores, aging-induced permanent faults in neuron-update datapaths become an important obstacle to long-term deployment. Existing online recovery methods typically retire a faulty core and migrate its neurons, along with their weights and membrane states, to healthy cores. This whole-core treatment incurs high recovery traffic and makes recovery depend on scarce destinations; at high utilization, there may be enough surviving compute capaci...

---

### 15. Peer-Relative Trust-Guided Update Screening for Robust Semi-Decentralized Federated Learning under Label-Flipping Attacks

**Authors:** Ajay Kumar Shrestha, Sandhya Joshi

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.25714v1) | 📄 [PDF](https://arxiv.org/pdf/2610.25714v1)

**Summary:** Trust and reputation mechanisms can reduce the influence of malicious clients in federated learning (FL), but strict update filtering is difficult under non-independent and identically distributed (non-IID) data because honest local updates may temporarily reduce performance on a shared validation proxy. Building on our earlier trust-based semi-decentralized FL (SDFL) framework, this paper operationalizes the trust signals and introduces peer-relative update screening that combines a robust vali...

---

### 16. Let Them Sleep: Recursive Self-Pruning Memory for Long-Horizon LLM Agents

**Authors:** Kargi Chauhan, Sadiba Nusrat Nur, Pratibha Revankar, et al.

**Published:** 2026-10-18

🔗 [Paper](http://arxiv.org/abs/2610.25561v1) | 📄 [PDF](https://arxiv.org/pdf/2610.25561v1)

**Summary:** Agents that run for a long time have a memory problem, and it is not the one most systems optimize for. Storing every trace and retrieving the nearest neighbors works early and quietly stops working later: the store fills up with failures the agent then repeats, and with facts that were true fifty turns ago. RSPM (Recursive Self-Pruning Memory) borrows the fix biology already found. At intervals the agent sleeps. It clusters its recent failures, distills each cluster into a short rule, and delet...

---

### 17. Small-scale neural simulation of Caenorhabditis elegans on Loihi-2 using NeuroML2Loihi

**Authors:** Danny Rosen, Ramashish Gaurav, Yang Yi

**Published:** 2026-10-18

🔗 [Paper](http://arxiv.org/abs/2610.25424v1) | 📄 [PDF](https://arxiv.org/pdf/2610.25424v1)

**Summary:** Neural simulation is an essential methodology for studying biological nervous systems, but it remains limited by the computational costs of repeatedly updating neural and synaptic states over many timesteps. Neuromorphic hardware is a promising substrate for this class of workloads because such devices combine event-driven execution, localized memory, and spike-based communication. However, neuromorphic \textit{software} remains comparatively fragmented and difficult to integrate with the model-...

---

### 18. Length-Independent Stability and $L_2$-Gain Certificates for Chains of Delayed Neural Modules

**Authors:** Ömer Faruk İşcanlı

**Published:** 2026-10-18

🔗 [Paper](http://arxiv.org/abs/2610.25147v1) | 📄 [PDF](https://arxiv.org/pdf/2610.25147v1)

**Summary:** Networks of repeated neural modules with delayed neighbour coupling need stability guarantees for every number of modules, but delay-dependent criteria certify one network at a time and grow with its size. This paper derives stability and $L_2$-gain certificates of length-independent size for open chains and rings of modules of two alternating types with slope-restricted activations. A local and a transmission delay act independently and are only bounded and continuous. A Lyapunov-Krasovskii fun...

---

### 19. QD-Rec: Open-Ended Evolution of Recommendations via Quality-Diversity

**Authors:** Takashi Ishida, Taro Makino, Issa Sugiura

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23470v2) | 📄 [PDF](https://arxiv.org/pdf/2610.23470v2)

**Summary:** Open-ended search combined with foundation models has produced advances such as faster algorithms, new results on open mathematical problems, and self-improving agents. We extend this paradigm to recommendation for decision-making, focusing on decisions where the set of possible choices is fixed but the reasons for choosing them are not. In high-stakes decisions, e.g., which company to acquire or which customer to target, comparing diverse, well-reasoned options can be more useful than a single ...

---

### 20. Algorithm Modelization: Transforming Optimization Algorithms into Evolvable Intelligence

**Authors:** Jian Yao, Zhiyao Zhang, Yichen Li, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23161v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23161v1)

**Summary:** Can algorithms be learned and evolved as models, rather than repeatedly redesigned as programs? We explore this question by introducing Algorithm Modelization, a new paradigm that turns iterative algorithms into trainable models. Its central idea is to regard algorithm execution trajectories as computational experience: by learning how algorithmic states evolve over iterations, a model can internalize the knowledge embodied in existing algorithms, reproduce their computational behaviors, and fur...

---

### 21. Wavelength Diversity Expands the Expressive Power of Optical Computing

**Authors:** Shiqi Chen, Che-Yung Shen, Parnian Ghapandar Kashani, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23070v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23070v1)

**Summary:** Universal function approximation underpins neural networks' capacity to represent nonlinear relationships, but realizing this capability in optical hardware requires engineering the computational features encoded in light. Here, we show that wavelength diversity enhances optical function-approximation expressivity through wavelength-scaled Fourier features generated by a shared phase encoder, without increasing the number of input-encoded harmonics. Multiple wavelengths contribute to the represe...

---

### 22. SpikeQ: Spike-Guided Post-Training Quantization for Spiking Neural Networks

**Authors:** Kai Sun, Peibo Duan, Zhanglu Yan, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23046v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23046v1)

**Summary:** On neuromorphic chips, spiking neural networks (SNNs) consume far less energy than artificial neural networks (ANNs), but the limited memory of these chips requires low-bit synaptic weights and membrane potentials. Existing post-training quantization (PTQ) methods provide them without retraining and, like those for ANNs, minimize numerical errors such as the mean squared error (MSE). In an SNN, however, a quantization error reaches later layers only through the spikes it flips. We find that erro...

---

### 23. Upper bounds on the number of causal pieces in spiking neural networks

**Authors:** Dominik Dold, Dennis Elbrächter, Philipp Petersen

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22484v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22484v1)

**Summary:** The input space of single-spike neural networks decomposes into causal pieces, and the number of causal pieces has been shown to provide a lower bound on the approximation error for some spiking neural networks. While this decomposition is applicable to a wide range of spiking neuron models, the limits of how many causal pieces can be realised by spiking neural networks are still unknown. In this work, we derive two complementary upper bounds on the number of causal pieces in feedforward single-...

---

### 24. A restart rule for genetic algorithms based on Schnabel census

**Authors:** Anton Eremeev, Yulia Zakharova

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22211v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22211v1)

**Summary:** A new adaptive restart rule for Genetic Algorithms (GAs) is considered. The rule is based on the Schnabel Census method, originally developed for statistical estimation of a size of animal population. In this paper, the Schnabel Census method is applied as a heuristic to estimate the number of different solutions that may be visited with positive probability, given the current distribution of offspring. The rule consists in restarting a GA as soon as the maximum likelihood estimate reaches the n...

---

### 25. Attention over noisy examples: generalization and memorization in the exponential Hopfield network

**Authors:** Francesco Alemanno

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22191v2) | 📄 [PDF](https://arxiv.org/pdf/2610.22191v2)

**Summary:** In Hebbian learning from examples, a Hopfield network retrieves archetypes seen only through noisy examples. We study it in the exponential Hopfield model: one softmax attention step with the unlabelled examples as keys. A signal-to-noise analysis gives the overlap with an unseen archetype in closed form: a majority-rule law in which an attention entropy replaces the dataset entropy. At high temperature the archetype is lost in the crosstalk; at low temperature the softmax freezes on the closest...

---

### 26. Beyond the Hamming Cliff: Compact Spatial Encodings Preserving Semantic Distance in Spiking Neural Networks

**Authors:** Sergio Davies, Muhammad Aitsam, Morgan-Tyler Stone, et al.

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22083v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22083v1)

**Summary:** By pre-processing input signals with Gray, Thermometer, Johnson and hybrid encodings before passing them to spiking neural networks running on SpiNNaker hardware, Davies et al.(2025) address the semantic-spatial disparity that causes the ``Hamming cliff'' in standard binary representations. Continuous semantic patterns are presented as a set of simultaneous spikes at the input layer, preserving ultra-low latency processing. Training the network on multiple continuous values under each scheme, an...

---

### 27. Approaching Backpropagation Accuracy with Weight Perturbation on MNIST

**Authors:** Patrick Inoue

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.21665v1) | 📄 [PDF](https://arxiv.org/pdf/2610.21665v1)

**Summary:** Weight perturbation (WP) estimates learning directions from random parameter perturbations and a scalar change in loss, without backpropagating derivatives. We examine how batch size, training duration, and estimator stabilization affect its attainable accuracy in fully connected MNIST networks. In the shallow configuration, large-batch training reaches approximately 97\% test accuracy, compared with an early backpropagation (BP) reference near 97.5--98\%. The same comparison exposes a substanti...

---

### 28. First Mathematical Runtime Analyses of Evolutionary Multitask Multi-Objective Optimization

**Authors:** Danyang Zhang, Weijie Zheng

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.21311v1) | 📄 [PDF](https://arxiv.org/pdf/2610.21311v1)

**Summary:** To facilitate the solving of complex problems, evolutionary multitask optimization is regarded as a promising technique due to its capacity for cross-task knowledge transfer. In contrast to empirical evidences, no mathematical runtime support exists for this technique within the domain of multi-objective optimization. In this work, we aim to fill this important gap. We analyze how the representative multiobjective multifactorial evolutionary algorithm (MO-MFEA) covers the Pareto fronts of two bi...

---

### 29. IWOO: Wave Optics Optimizer Improved with Hybrid Strategies for Numerical Optimization and Engineering Applications

**Authors:** Rui Du, Yaming Zhang, Yongpeng Wen, et al.

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.23994v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23994v1)

**Summary:** The Wave Optics Optimizer (WOO) incorporates optical diffraction and interference into numerical optimization and has shown competitive performance in benchmarks and engineering applications. However, it can converge slowly, become trapped in local optima, and lose search effectiveness in later iterations. This paper proposes an Improved Wave Optics Optimizer (IWOO) that integrates four complementary strategies. First, a good point set and opposition-based learning are combined in GPS--OBL initi...

---

### 30. Controlling the latency in temporal coded spiking models for neuromorphic datasets

**Authors:** Alban Gattepaille, Alexandre Muzy

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.19732v1) | 📄 [PDF](https://arxiv.org/pdf/2610.19732v1)

**Summary:** Exploiting temporal information in datasets with high temporal dependencies (such as spoken keyword recognition) by spiking models is still an open problem. Promising frameworks include Time-To-First coding (TTFS) and the inclusion of synaptic delays into learning. In TTFS, neurons are forced to spike at most once, forcing the network to found its learning on the spiking times of neurons rather than their spiking rate. Some models use the TTFS framework to directly compute the spiking time of In...

---

### 31. When the implementation matters more than the algorithm: NSGA-II and other multi-objective optimizers in engineering design tools

**Authors:** Luciano Ambrosini

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.22397v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22397v1)

**Summary:** Engineering design tools increasingly embed optimizers as ready-made components that users select by algorithm name, while operator settings and bound, integer and duplicate handling stay fixed inside each tool. This study tests whether the name predicts the result. A tool-agnostic harness exposes one deterministic black box, an emulator of a published 22-variable mixed-integer building-performance problem, to the native optimizers of three Grasshopper plug-ins, to canonical NSGA-II, SMS-EMOA an...

---

### 32. Design and Analysis of Temporal Representations in Neural Networks

**Authors:** Alban Colas-Gattepaille, Alexandre Muzy

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.19730v1) | 📄 [PDF](https://arxiv.org/pdf/2610.19730v1)

**Summary:** The ability to represent temporal information is often hypothesized to underlie the efficiency and learning capabilities of biological neural networks. This motivates the development of spiking neural networks. However, it remains unclear how temporal information is actually represented in neural networks and how different forms of temporal representation affect performance and computational efficiency. We introduce the notion of the degree of temporal representation of a neural network, defined...

---

### 33. A Time-Variant Spiking Neuron from a Unified State-Dynamics Perspective

**Authors:** Jing Yang, Qianhui Liu, Gang Pan, et al.

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.23981v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23981v1)

**Summary:** Spiking neural networks (SNNs) have increasingly incorporated rich neuronal dynamics to enhance temporal processing. However, richer dynamics do not necessarily enable neurons to adapt how information is processed over time. To examine this issue systematically, we introduce a unified state-dynamics framework that characterizes diverse spiking neurons through a common formulation and enables direct comparison of their dynamical designs. The framework reveals a common limitation of existing neuro...

---

### 34. How Long Is the Coast of a Neuron? Resolution-Dependent Interaction Order and Computational Capacity

**Authors:** Nima Dehghani

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.19487v1) | 📄 [PDF](https://arxiv.org/pdf/2610.19487v1)

**Summary:** Mandlebrot's coastline paradox reframes measurement as a joint property of an object and its ruler. Here we ask how observational resolution shapes the apparent structure of neural computation. We introduce a scale-indexed decomposition that separates the predictive information captured by direct dependencies from the residual outside that model family. Exact constructions show that projection can convert higher-order dependence into pairwise structure. Projection can increase the direct fractio...

---

### 35. Riding the Fixed-Point Curve: Image Classification in the Continuous Thought Machine

**Authors:** Thomas Hannagan

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.19220v2) | 📄 [PDF](https://arxiv.org/pdf/2610.19220v2)

**Summary:** The Continuous Thought Machine (CTM) is a recurrent network that attends to inputs and makes predictions based on the synchronization between its neurons. On tasks spanning many domains, it displays emergent thought processes that have not been explained. We report a number of findings about how the CTM classifies images, focusing on ImageNet. Thinking steps are attracting but strongly non-normal maps exhibiting balanced amplification (Murphy and Miller, 2009); while attraction is already presen...

---

### 36. LLM Evolutionary Search Strategies Should be Compared by Tokens

**Authors:** Tal Oved, Roi Pony, Oshri Naparstek, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.23977v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23977v1)

**Summary:** LLM evolutionary search is currently evaluated by counting proposals (candidate programs). We demonstrate this metric hides the true cost of search, and redo the comparison using tokens. By replaying 600 logged runs across 5 tasks and 3 methods, we show that proposal costs vary wildly from 16k to 39k tokens. In equal-proposal comparisons, this silently grants some methods up to 1.9x the compute of others, and gives evolution roughly 6x the budget of independent sampling. When we match token budg...

---

### 37. Same Function, Different Trajectory: No Standard Optimizer Is Equivariant to Transformer Reparameterization

**Authors:** Bum Jun Kim

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18085v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18085v1)

**Summary:** We show that two Transformers representing the same function can follow different training trajectories. For example, doubling a query matrix and halving its key matrix preserves the model's function but changes the gradient scales seen by the optimizer. Our theoretical analysis establishes that standard block-local first-order optimizers fail to scale updates with parameters under a shared learning rate. For AdamW, transforming the first- and second-moment estimates alone does not correct the m...

---

### 38. Saliency-Guided Replay for Continual Learning in Deep Spiking Neural Networks

**Authors:** Francesco Panetta, Federico Di Valerio, Michela Proietti

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.17998v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17998v1)

**Summary:** Spiking Neural Networks (SNNs) are promising for energy-efficient neuromorphic computing, but they still suffer from catastrophic forgetting when learning tasks sequentially. This work investigates the integration of Experience Packing and Replay (EPR) as a memory-efficient continual learning strategy for deep SNNs under low-latency constraints. The proposed framework combines Batch Normalization Through Time stabilized VGG9 SNNs with Spike Activation Maps (SAM), which provide forward-only expla...

---

### 39. Neural Dimensional Analysis: Foundations of Dimensionless and Scale-Consistent Computation

**Authors:** Bum Jun Kim, Makoto Kawano, Yusuke Iwasawa, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.17969v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17969v1)

**Summary:** Modern Transformers rely on many scale-control mechanisms, including normalization, residual scaling, attention temperatures, loss weighting, and adaptive updates. To explain how these mechanisms maintain scale consistency, we introduce Neural Dimensional Analysis (NDA), a unified framework based on dimensional consistency. We define neural units that specify how tensors rescale and which quantities can be added, just as physical units do in physics. Our rules match residual units, nondimensiona...

---

### 40. Collective Benefits and Efficiency in Coupled Echo State Networks

**Authors:** Polyphony Bruna, Rick Dale, Michael J. Spivey, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.17506v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17506v1)

**Summary:** Simple aggregation of independent responses ("wisdom of crowds") generally improves collective performance through statistical facilitation, but interaction among members can sometimes hinder group outcomes. However, under certain circumstances, coordination studies show that interacting groups can outperform their individual members and nominal groups, and interaction can also be more efficient than independence. We present a reservoir computing model to investigate how interaction can enhance ...

---

### 41. FidLIF: Parallel Training of High-Fidelity Spiking Neurons with Exact BPTT

**Authors:** Kaixiang He, Yujie Wu

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.16924v1) | 📄 [PDF](https://arxiv.org/pdf/2610.16924v1)

**Summary:** Although spiking neural networks (SNNs) show promise in energy-efficient computing through event-driven computation and stateful temporal processing, their recurrent membrane dynamics render their training inherently sequential and inefficient for long sequences. Existing methods achieve full-sequence parallelism in SNNs through two main strategies: redesigning or approximating spiking dynamics to avoid reset-coupled temporal dependencies, or relying on iterative relaxed fixed-point solvers that...

---

### 42. Time Window Optimization for Motor Imagery Classification via Temporal Structure Embedded Reinforcement Learning

**Authors:** Huan Luo, Na Lu, Xiaopeng Wang, et al.

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.16921v1) | 📄 [PDF](https://arxiv.org/pdf/2610.16921v1)

**Summary:** Online motor imagery-based brain-computer interfaces (MI-BCIs) typically decode continuous EEG using fixed-length sliding windows that may be misaligned with neural events. Existing window optimization methods often evaluate windows independently, overlooking temporal dependencies and potentially producing fragmented or physiologically implausible selections. We propose Temporal Structure Embedded Reinforcement Learning (TSE-RL), a framework that incorporates prior knowledge of MI event structur...

---

### 43. DTA-GT: Direction- and Topology-Aware Graph Transformer for Neural Network Representation Learning

**Authors:** Yuxiang Zeng, Kun Xie, Yang Wang, et al.

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.16822v1) | 📄 [PDF](https://arxiv.org/pdf/2610.16822v1)

**Summary:** Architecture attribute predictors reduce the cost of neural architecture search by estimating accuracy or latency from a small set of evaluated candidates. The key difficulty is that neural architectures are operation-labeled DAGs: edge direction defines computational flow, but existing predictors often treat direction as a local structural cue. We propose DTA-GT, a Direction- and Topology-Aware Graph Transformer based on encoder-wide directional consistency, which preserves directed computation...

---

### 44. naspaclust: A hybridisation of spatial fuzzy clustering with nature-inspired optimisation

**Authors:** Bahrul Ilmi Nasution, Rezzy Eko Caraka, Robert Kurniawan

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.16356v1) | 📄 [PDF](https://arxiv.org/pdf/2610.16356v1)

**Summary:** We present an overview of R package called \texttt{naspaclust}, a tool for spatial fuzzy clustering improvement by hybridising the Fuzzy Geographically Weighted Clustering (FGWC) with nature-inspired optimisation algorithms. There are seven optimisation algorithms in general, namely Artificial Bee Colony, Flower Pollination Algorithm, Gravitational Search Algorithm, Harris-Hawk Optimisation, Intelligent Firefly Algorithm, Particle Swarm Optimisation, and Teaching-Learning Based optimisation. The...

---

### 45. CIPHEUR: LLM-Guided Structural Search Control for Conflict-Graph Optimization

**Authors:** Yuqing Cheng, Yan Jia, Yanjie Song, et al.

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.16158v1) | 📄 [PDF](https://arxiv.org/pdf/2610.16158v1)

**Summary:** Conflict-graph search can stagnate despite effective operators when interventions fail to address the conflicts blocking progress. A disruptive intervention may also require further search before its value emerges. We propose CIPHEUR, a large language model (LLM)-guided framework that connects conflict evidence to coordinated intervention and recovery through Structured Intervention Units (SIUs). The shared control interface supports offline synthesis of executable policies and online contextual...

---

### 46. Where Polanyi Meets Galois: Tacit Knowing as an Algebro-Deterministic Operation, Toward Re-rooting AI-Generated Science

**Authors:** Hiroyuki Chuma, Kanji Otsuka, Yoichi Sato, et al.

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.16102v2) | 📄 [PDF](https://arxiv.org/pdf/2610.16102v2)

**Summary:** We argue that tacit knowing is better modelled as an operating regime of a memory than as a kind of content. Our substrate is VaCoAl, an algebro-deterministic XOR-and-shift hyperdimensional memory over GF(2), realized as CASRAM and PyVaCoAl. In it, a DAG reads two ways. Repairing every collision (Rescue) makes the trace exactly auditable but ranks no path higher; tolerating them (Don't Care) yields a path confidence, CR$_2$, silently favouring direct routes. This audit-valuation complementarity ...

---

### 47. How Shared Representations Become Specialized: Formation, Maintenance, and Latent Susceptibility

**Authors:** Toru Takahashi

**Published:** 2026-10-11

🔗 [Paper](http://arxiv.org/abs/2610.15830v1) | 📄 [PDF](https://arxiv.org/pdf/2610.15830v1)

**Summary:** When several predictions use the same internal representation, information about some targets can remain easier to recover than information about others. We study how this specialization forms, persists, and changes in minimal artificial learners. With reconstruction errors weighted equally during learning, changing which target is observed precisely selects the favored target and redirects an already specialized learner. Removing current support can reduce a formed bias, whereas state-following...

---

### 48. REPRO: Reflective Evolutionary Prompt Optimizer for Automated LLM Red-Teaming

**Authors:** Abrar Alotaibi, Moataz Ahmed

**Published:** 2026-10-11

🔗 [Paper](http://arxiv.org/abs/2610.15513v1) | 📄 [PDF](https://arxiv.org/pdf/2610.15513v1)

**Summary:** Safety-aligned large language models (LLMs) remain vulnerable to adversarial prompts that bypass their safety training. Existing automated red-teaming methods either require privileged access unavailable in production, rely on manually engineered per-model templates, or optimize a single objective without population-level diversity. We present REPRO (Reflective Evolutionary Prompt Optimization), a pure black-box framework that discovers adversarial prompts through evolutionary optimization drive...

---

### 49. CoFlu-Brain: An fMRI Connectivity Foundation Model with Cofluctuation-Based Pretraining

**Authors:** Ziteng Sui, Junfeng Xia, Wenhao Ye, et al.

**Published:** 2026-10-11

🔗 [Paper](http://arxiv.org/abs/2610.15450v1) | 📄 [PDF](https://arxiv.org/pdf/2610.15450v1)

**Summary:** Functional magnetic resonance imaging (fMRI) commonly characterizes large-scale brain organization through functional connectivity (FC). However, an observed FC matrix is not a fixed brain graph but a statistical estimate determined by the finite BOLD frames used to compute it. Conventional FC-based approaches typically represent each scan with a single Pearson-correlation matrix, leaving frame-resolved variations in regional interactions unexploited. To address this limitation, we introduce CoF...

---

### 50. FENAS: A Few-Shot Meta-Ensembling Framework for Efficient Neural Architecture Search with Synergized Zero-Cost Proxies

**Authors:** Yifeng Mao, Yuze Feng, Yutong Shen, et al.

**Published:** 2026-10-11

🔗 [Paper](http://arxiv.org/abs/2610.15307v1) | 📄 [PDF](https://arxiv.org/pdf/2610.15307v1)

**Summary:** Efficient neural architecture search (NAS) requires accurate performance estimation under limited evaluation budgets. Existing zero-cost proxies (ZCPs) provide fast training-free signals, but each proxy usually captures only a partial property of an architecture, leading to unstable rankings across datasets and search spaces. In contrast, GNN-based predictors can improve accuracy, but often depend on labeled architectures, graph encoders, and costly representation learning, which makes them less...

---

## q-bio.NC

**50 papers**

### 1. Dynamics of random recurrent neural networks: colored noise and sublinear activations

**Authors:** German Mato, Facundo Rigatuso, Gonzalo Torroba

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31575v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31575v1)

**Summary:** We study the dynamics of recurrent neural networks with random couplings, sublinear odd activation functions, and temporally correlated noise. Using large N methods, we determine stationary correlations and distinguish the loss of local linear stability from the onset of chaos, characterized by a positive largest Lyapunov exponent. These thresholds delimit an intermediate regime in which local instability coexists with asymptotic stability under a common noise history. Their separation depends o...

---

### 2. Music Between Two Minds: Individual Signatures, Shared States, and the Emergence of Creative Interaction

**Authors:** Tatsuya Daikoku, Risa Kobayashi, Rina Tabuchi, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31131v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31131v1)

**Summary:** Some of the most valued forms of human creativity arise between people-in conversation, collaboration, and improvised music-yet how two minds jointly regulate the flow of novelty in real time remains unknown. Here we examined the information dynamics of interpersonal improvisation using 986 professional jazz improvisations. Pitch-based fluctuations of uncertainty and surprise behaved as signatures of individual identity: the two partners differed within 90% of takes, performers were identifiable...

---

### 3. Gate-Based Feature Importance in Simulation-Based Inference for EEG: A Cautionary Tale

**Authors:** Shrivatsa Deshmukh, Sasha Brenner, Thomas R. Knösche, et al.

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.30364v1) | 📄 [PDF](https://arxiv.org/pdf/2610.30364v1)

**Summary:** Simulation-based inference (SBI) provides a powerful way to fit mechanistic models to data, but offers little insight into which information in the data shapes the inferred parameter values. It could therefore benefit from robust and inexpensive interpretability methods. Learned weighting mechanisms such as feature gates provide a potential route to low-cost interpretability, although their interpretation assumes that predictive training reveals which inputs drive performance. We examined this a...

---

### 4. The medium is the message: How neurometabolic entanglement generates conscious experience

**Authors:** Terrence W. Deacon, Miguel Garcia-Valdecasas, Michael Jacob

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.30217v1) | 📄 [PDF](https://arxiv.org/pdf/2610.30217v1)

**Summary:** Most neuroscientific accounts of consciousness assume that conscious experience is constituted by the information conveyed between neurons. The physical-chemical details of the metabolic and physiological processes that convey this information are correspondingly presumed to be relevant only insofar as they support the organization of information processes. We describe an alternative perspective that denies this presumed independence of the processing of neural information and the metabolic-phys...

---

### 5. Bio-Inspired Auditory Processing: Coupling Parallel Resonate-and-Fire Dynamics with Ternary Recurrent Networks for Speech Recognition

**Authors:** Pavlos Poulos, Katelyn Sadorf, Themos Stafylakis, et al.

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29720v1) | 📄 [PDF](https://arxiv.org/pdf/2610.29720v1)

**Summary:** Spiking Neural Networks (SNNs) promise energy-efficient inference through sparse, event-driven computation, yet remain constrained on continuous, context-dependent tasks such as automatic speech recognition (ASR). A key bottleneck is the Leaky Integrate-and-Fire (LIF) neuron, whose membrane decay erases information across pauses and phonetic boundaries while it must both extract features and retain long-range context. Inspired by cortical separation of nonlinear filtering and somatic integration...

---

### 6. Vagus nerve stimulation strengthens beta- and gamma-rate auditory steady-state responses in rat cortex

**Authors:** Shinichi Kumagai, Tomoyo Isoguchi Shiramatsu, Karin Oshima, et al.

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29042v1) | 📄 [PDF](https://arxiv.org/pdf/2610.29042v1)

**Summary:** Background: Gamma entrainment using sensory stimulation (GENUS) is under study as a treatment for neurological disease, but cortical engagement is variable. Vagus nerve stimulation (VNS) modulates cortical state and sound-evoked beta-gamma activity, suggesting that it may strengthen responses to rhythmic sensory input. Objective: To determine whether VNS strengthens auditory steady-state responses across beta and gamma rates and whether the effect depends on cortical region and sensory drive. Me...

---

### 7. A Reverse-Gold Theorem: Positive-Data Identification by Substrate-Bounded Contrastive Learners

**Authors:** Rakesh Sengupta

**Published:** 2026-10-20

🔗 [Paper](http://arxiv.org/abs/2610.28747v1) | 📄 [PDF](https://arxiv.org/pdf/2610.28747v1)

**Summary:** Gold's theorem shows that no learner can identify an arbitrary language in a superfinite class from positive presentations alone. We prove a positive result of a different shape. Fix an innate \emph{recursive contrast operator} $R$ mapping any string to a finite set of structurally bounded perturbations of it, and a discriminative scorer of bounded capacity trained by InfoNCE-style contrastive estimation \citep{vandenoord2018,macollins2018} on self-generated perturbations. Under a faithfulness c...

---

### 8. What I Disbelieve: Quantifying Belief With Negative Ranking Functions

**Authors:** Hanbin Go, Britt Anderson

**Published:** 2026-10-20

🔗 [Paper](http://arxiv.org/abs/2610.28357v1) | 📄 [PDF](https://arxiv.org/pdf/2610.28357v1)

**Summary:** A challenge in exploring the psychology of human uncertainty is its measurement and quantification. Prior work has focused almost exclusively on probability, while the formal theories developed in philosophy are rarely tested. We tested Wolfgang Spohn's ranking theory, a normative account in which belief is graded by ordinal ranks of disbelief that combine by minimization rather than addition, as a descriptive model of human belief. Across six experiments, participants assigned ranks of disbelie...

---

### 9. Does a Flux-Defined Markov Blanket Screen Self-Replicating Gray--Scott Spots? A Computational Test of a Blanket Condition from the Free Energy Principle

**Authors:** John E Pearson

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.27235v1) | 📄 [PDF](https://arxiv.org/pdf/2610.27235v1)

**Summary:** Friston's free energy principle holds that a system separated from its environment by a Markov blanket---a boundary whose states statistically screen its interior from its exterior---can be treated as performing approximate Bayesian inference, and that such blankets arise wherever coupling is short-range. We test this blanket condition in a concrete nonlinear pattern-forming system: self-replicating spots in a reaction-diffusion model that persist, compete, and reproduce. Directed boundary excha...

---

### 10. Cross-disorder Learning of Imaging-derived Joint Mophometric Markers in Alzheimer's and Parkinson's Diseases

**Authors:** Yuji Zhao, Boris Gutman

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.27150v1) | 📄 [PDF](https://arxiv.org/pdf/2610.27150v1)

**Summary:** As two most prevalent neurodegenerative diseases (NDDs), Alzheimer's disease (AD) and Parkinson's disease (PD) shared commonalities both in symptomology and pathophysiology. However, to what extent and in what way these two distinct disorders overlap remain underexplored. In this study, we propose an explicit, interpretable and spatially adaptive transfer learning framework to elucidate the morphometric biomarkers linked to AD and PD. We applied such high-dimensional machine learning model to tw...

---

### 11. Representing short-term movement to reveal animal identity and learning progress

**Authors:** Ping Zhang, Quang-Huy Nguyen, Yingtie Lei, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.27140v1) | 📄 [PDF](https://arxiv.org/pdf/2610.27140v1)

**Summary:** How learning progresses over time and varies across individuals is a longstanding question in cognitive and behavioral science. However, a major challenge is identifying observable behavioral measures that faithfully capture learning progression. Existing approaches commonly rely on predefined behavioral features or task-level performance, while fine-scale posture and movement in freely behaving animals remain less explored. In this paper, we ask: can short-term movement trajectories reveal lear...

---

### 12. Ontic state recovery through prediction

**Authors:** Ping Zhang, Quang-Huy Nguyen, Yingtie Lei, et al.

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.27139v1) | 📄 [PDF](https://arxiv.org/pdf/2610.27139v1)

**Summary:** We encounter a system through its responses, yet its state concerns how the system is. Predicting further responses promises knowledge beyond what is immediately observed. What that knowledge tells us about the system's state depends on what we mean by a state in the first place. We give this notion a model-relative meaning: a state is the complete response profile over a specified query universe, and configurations agreeing on every query are regarded as the same state. From this perspective, a...

---

### 13. Affective Valence as the Interoceptive Rate of Change of Jacobian Scale

**Authors:** David Balduzzi

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26350v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26350v1)

**Summary:** Affect is widely held to depend on interoception. This paper proposes that valence is the rate at which interoception moves a self-sustaining system's responsiveness relative to its terminal set (roughly, death). Responsiveness is formalised as the scale of the system's Jacobian and interoception as its internal inputs: receptors, signals and forecasts of its energy reserve. Changes in responsiveness that bypass interoception, such as brain damage, are not felt. Language models have no valence b...

---

### 14. PyGPLA: A Python Package for Generalized Phase Locking Analysis

**Authors:** Amir Khani, Christian Beste, Shervin Safavi

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.26304v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26304v1)

**Summary:** Spike-field couplings measure the links between neuronal spiking and local field potential (LFP) and provide a tool to study how neural populations coordinate activity across spatial and temporal scales. While modern high-density electrophysiology enables the simultaneous recording of numerous LFP channels and neuronal units, this massive scale poses significant statistical and computational challenges for conventional pairwise coupling analyses. The number of channel-unit comparisons grows rapi...

---

### 15. HP-GSBS: Accelerating greedy state boundary search with reusable interval statistics

**Authors:** Yanzhe Zhao, Yongzhang Ji

**Published:** 2026-10-19

🔗 [Paper](http://arxiv.org/abs/2610.25898v1) | 📄 [PDF](https://arxiv.org/pdf/2610.25898v1)

**Summary:** Greedy State Boundary Search (GSBS) identifies transitions between relatively stable neural activity patterns, but repeated candidate evaluation makes large analyses expensive. HP-GSBS is an open-source Python package that reorganizes the search around reusable interval contributions and correlation statistics. Streaming candidate reduction and local refinement further reduce repeated work; CPU, PyTorch CUDA and Triton backends share sequential segmentation decisions. Across seven controlled wor...

---

### 16. Simulating Infant Senses with Age-Tuned Networks

**Authors:** Somesh Mohapatra

**Published:** 2026-10-18

🔗 [Paper](http://arxiv.org/abs/2610.25377v1) | 📄 [PDF](https://arxiv.org/pdf/2610.25377v1)

**Summary:** What a newborn sees, hears and feels, and how this changes month by month, has been measured sense by sense, with different methods and in different units. We bring these measurements together for the first two years of life and ask whether small neural networks tuned to a given age can turn them into a quick, inspectable simulation of sensory perception. Each sense's immaturity is written as a fixed, age-indexed filter on the input, and a small prediction network learns behind it over the first...

---

### 17. Spontaneous brain-wide rotational dynamics constrain cue-evoked behavior

**Authors:** Sihan Chen, Yunlong Xu, Doruk Efe Gökmen, et al.

**Published:** 2026-10-18

🔗 [Paper](http://arxiv.org/abs/2610.25061v1) | 📄 [PDF](https://arxiv.org/pdf/2610.25061v1)

**Summary:** Uncovering low-dimensional representations of brain-wide neural dynamics and their relationship to behavior remains a central challenge. Here, we show that spontaneous brain-wide rotational dynamics constrain cue-evoked behavior and learning. To systematically establish these findings, we developed a dimensionality-reduction technique called Rotational Component Analysis (RCA) that optimizes the detection of low-variance rotational modes even within individual trials. We applied RCA to motor-cor...

---

### 18. Multilingual Brain Decoding Reveals Shared Cortical Semantic Geometry

**Authors:** Yi Guo, Yong Hu, Michael Kwok-Po Ng, et al.

**Published:** 2026-10-17

🔗 [Paper](http://arxiv.org/abs/2610.26927v1) | 📄 [PDF](https://arxiv.org/pdf/2610.26927v1)

**Summary:** Human languages differ markedly in lexical and syntactic form yet can convey similar semantic content. The neural basis of this cross-language semantic commonality remains unclear. Here we developed a multilingual brain decoding framework and analysed brain recordings from 227 participants spanning Chinese, English and French. We found that cortical semantic representations exhibited consistent semantic geometry relationships across languages and individuals, revealing a shared cortical semantic...

---

### 19. Longitudinal fMRI reveals multi-network reconfiguration and a recurrent frontoparietal shift across rest and task states during adult aging

**Authors:** Tingshan Liu, Wanxin Dong, Hairong Zheng, et al.

**Published:** 2026-10-17

🔗 [Paper](http://arxiv.org/abs/2610.24433v1) | 📄 [PDF](https://arxiv.org/pdf/2610.24433v1)

**Summary:** Functional connectivity changes across adult aging, but most evidence is cross-sectional, and covariance-based connectivity depends on blood oxygenation level dependent (BOLD) fluctuation amplitude. Covariance decline can reflect changing fluctuation amplitude, and its interpretation may depend on whether normalization uses signal amplitude or includes estimated noise. It is also unclear which longitudinal changes recur across brain states. We analyzed 852 adults (baseline age 36-89 years) from ...

---

### 20. Spaceflight-associated Motion Sickness in Commercial Crew Astronauts

**Authors:** Torin K. Clark, Aaron A. Allred, Jaime Mateus, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.24216v1) | 📄 [PDF](https://arxiv.org/pdf/2610.24216v1)

**Summary:** Spaceflight-associated motion sickness, including space motion sickness (SMS) and terrestrial readaptation motion sickness (TRMS), has presented as the most operationally limiting effect on the human in the days following a gravity transition. Published data suggest that astronaut head movements provoke symptoms, but those studies rarely controlled for them. Most previous studies use postflight retrospective reporting and have not quantified temporal dynamics or persistence of symptoms; no study...

---

### 21. Deep LLM layers expose passage-level context in EEG during silent reading

**Authors:** Ingo Marquardt, Anthilia Alchanat, Priyanka Jain

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23638v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23638v1)

**Summary:** In a previous report we showed that a decoder can recover open-vocabulary word-level information from 19-channel EEG recorded during silent reading, by aligning short EEG windows with hidden-state embeddings of the presented word taken from a large language model (LLM). That analysis contrasted two of the model's 33 layers: the context-free input embedding and one mid-depth layer. Here we ask how EEG-decodable structure is distributed over the full depth of the language model. We trained one dec...

---

### 22. Distributional signatures of computation: inferring mechanisms from computation time distributions

**Authors:** Céline van Valkenhoef, Catherine Schuman, Nikolaus Kriegeskorte, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23607v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23607v1)

**Summary:** Computational complexity theory provides a framework for analysing abstract models of computation, whereas computational systems operate as finite physical implementations whose behaviour is shaped by their architecture and physical substrate. In such systems, computational organisation cannot be directly characterised from algorithms or internal representations. Building on the use of reaction time distributions to constrain mechanisms in cognitive science, we introduce an empirical framework f...

---

### 23. EEG Lempel-Ziv Complexity vis-à-vis Autocorrelation Function

**Authors:** Pedro Montoya, Ignacio Cifre, José Luis Rosselló Sanz, et al.

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.23231v1) | 📄 [PDF](https://arxiv.org/pdf/2610.23231v1)

**Summary:** Measures of signal complexity have become increasingly popular in electroencephalography (EEG), where they are often interpreted as indicators of neural information processing, dynamical richness, or conscious state. In contrast, classical measures of temporal dependence, such as the autocorrelation function (ACF), remain more directly linked to known physiological mechanisms and are easier to interpret. The present work revisits, for the EEG practicioner, the relation between normalized Lempel-...

---

### 24. What Shapes Brain Alignment of Large Language Models during Dialogue? Insights from Language Production and Comprehension

**Authors:** Yuko Nakagi, Yuya Chiba, Yasue Kishino

**Published:** 2026-10-16

🔗 [Paper](http://arxiv.org/abs/2610.22961v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22961v1)

**Summary:** Brain alignment of large language models (LLMs) offers a way to investigate representational similarities between LLMs and the human brain during language processing. While previous studies have mainly focused on passive language comprehension, little is known about such alignment during dialogue, in which speakers engage in both language production and comprehension. In this study, using fMRI data collected during dialogue, we examine brain alignment during language production and comprehension...

---

### 25. Brain-Aligned Multimodal LLMs for Social and Emotional Understanding of Cartoon Movies

**Authors:** Yiran Huang, Zeyong Zhang, Bharat Biswal, et al.

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22706v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22706v1)

**Summary:** Multimodal large language models (MLLMs) offer scalable annotations of social and affective content, but their temporal agreement with human judgments and neural predictive value require further evaluation. We compared diffusion-based and autoregressive MLLMs with continuous human Theory of Mind (ToM) and affective valence ratings across three short cartoon movies. Behavioral analyses assessed temporally aligned Pearson correlations, rating distributions, and the effects of preceding scene descr...

---

### 26. Alignment of visual brain encoding models with individual perceptual similarity judgments

**Authors:** Daniel Chong, Haomiao Chen, Keith W Jamison, et al.

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22569v2) | 📄 [PDF](https://arxiv.org/pdf/2610.22569v2)

**Summary:** Encoding models that predict brain activation responses to images have traditionally been trained to maximize accuracy when predicting observed brain data. However, their internal representations may not reflect individual human perception. In this work, we investigate whether we can fine-tune brain encoding models to better align their representations with individuals' similarity judgments. Using similarity judgments of 100 images from 8 participants in the Natural Scenes Dataset (NSD), we adap...

---

### 27. Upper bounds on the number of causal pieces in spiking neural networks

**Authors:** Dominik Dold, Dennis Elbrächter, Philipp Petersen

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22484v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22484v1)

**Summary:** The input space of single-spike neural networks decomposes into causal pieces, and the number of causal pieces has been shown to provide a lower bound on the approximation error for some spiking neural networks. While this decomposition is applicable to a wide range of spiking neuron models, the limits of how many causal pieces can be realised by spiking neural networks are still unknown. In this work, we derive two complementary upper bounds on the number of causal pieces in feedforward single-...

---

### 28. Mutual Information in High-Dimensional Neural Coding

**Authors:** Zimo Li, Yuchang Tian, Matthew P. Leighton, et al.

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.22206v1) | 📄 [PDF](https://arxiv.org/pdf/2610.22206v1)

**Summary:** Estimating mutual information in large neural populations is limited by the exponential growth of possible neural response patterns. Here we apply a Monte Carlo framework to make this problem tractable by sampling from a conditionally independent population model fit from single-neuron responses. The estimator accurately recovers analytical ground truth, corrects finite-data bias, and scales to empirical recordings containing 100 to 10,000 neurons from visual cortex, hippocampus, and retina. Acr...

---

### 29. Transferable conditional brain charts link cortico-subcortical structure to Alzheimer's disease progression

**Authors:** Nitin Sharma, Sicheng Dai, Francesco A. Mallus, et al.

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.21660v1) | 📄 [PDF](https://arxiv.org/pdf/2610.21660v1)

**Summary:** Normative models chart how brain measures vary across the lifespan, expressing each individual as a deviation from a healthy reference. However, most regional models of cortical thickness disregard dependencies between cortical and subcortical anatomy, and transferring them to a new site typically requires retraining or a recalibration of location and scale alone. We condition lifespan norms of cortical thickness on subcortical volume, such that each deviation indicates whether an individual's c...

---

### 30. Neural Computation Runs on Dissipative Structures Under Cyclic Calibration: A Systems Perspective on Sleep

**Authors:** Javier Diaz

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.21486v1) | 📄 [PDF](https://arxiv.org/pdf/2610.21486v1)

**Summary:** Biological function operates far from thermodynamic equilibrium, sustained by metastable structures that continuously cycle through synthesis, function execution, and degradation--consuming energy and exporting entropy in the process. Neural computation exemplifies this dissipative organization, relying on low-entropy structures engaged in dynamic processes that define key information transfer and processing parameters such as gain, threshold, and integration time. This perspective proposes that...

---

### 31. Language Models Share a Readout Bottleneck in Working Memory

**Authors:** Dongyu Gong

**Published:** 2026-10-15

🔗 [Paper](http://arxiv.org/abs/2610.21176v1) | 📄 [PDF](https://arxiv.org/pdf/2610.21176v1)

**Summary:** Large language models (LLMs) reproduce a human working-memory signature on the N-back task: performance declines as memory load N increases, and errors concentrate on lures, items that repeat the current stimulus at a neighboring but incorrect serial position. We ask whether this shared behavioral signature reflects a shared mechanism. The literature offers two candidate accounts. On a precision account, softmax attention cannot concentrate its weight on the item N positions back, so adjacent it...

---

### 32. Statistical Mechanics of Spike Trains: Self-Consistent Activity Ensembles and Phase Transitions

**Authors:** Jan Pyrzowski, Laura Messio, Guillaume Marrelec, et al.

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.20971v1) | 📄 [PDF](https://arxiv.org/pdf/2610.20971v1)

**Summary:** We introduce a statistical-mechanical framework for spiking neuronal systems in which entire spike trains, defined as spatiotemporal configurations of discrete events, are treated as microstates of the system. Instead of modeling explicit network dynamics, we construct an ensemble over complete spike histories and assign to each configuration an effective energy functional that quantifies its consistency with intrinsic synaptic interactions.   This formulation leads to a Boltzmann-like distribut...

---

### 33. Cross-subject decoding of imagined speech from scalp EEG: a leakage-controlled evaluation on three public corpora

**Authors:** Blessing Isoyiza Adeika, Onyema Osuagwu

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.20954v1) | 📄 [PDF](https://arxiv.org/pdf/2610.20954v1)

**Summary:** Objective. A decoder of imagined speech that works for a new user without calibration would make a non-invasive speech interface practical. We tested whether imagined-speech content recorded with scalp electroencephalography (EEG) transfers across people, and examined why accuracy within a single person remains low. Approach. We analyzed three public corpora, ds003626, KaraOne and Track 3 of the 2020 International Brain-Computer Interface Competition, under a protocol that enforces split integri...

---

### 34. How large an effect would we have seen? Positive controls, detection floors and dataset pitfalls in scalp-EEG speech decoding

**Authors:** Blessing Isoyiza Adeika, Onyema Osuagwu

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.20942v1) | 📄 [PDF](https://arxiv.org/pdf/2610.20942v1)

**Summary:** Objective. Studies that decode imagined speech from scalp electroencephalography (EEG) commonly validate their pipelines with a positive control, usually overt speech, and report null results without stating what effect size the pipeline could have detected. Approach. Using ds003626 ("Thinking out loud"), KaraOne and Track 3 of the 2020 International Brain-Computer Interface Competition, we audited decoding of overt speech, articulator preparation and imagined speech with artifact-channel subset...

---

### 35. Awakening as a Trait-Level Transformation of Consciousness

**Authors:** Riku Ihalainen, Victor Oswald, Gulshan Kumar, et al.

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.20856v1) | 📄 [PDF](https://arxiv.org/pdf/2610.20856v1)

**Summary:** Awakening is reported across contemplative traditions yet remains poorly defined in science, where it is often conflated with transient states induced by meditation or psychedelics, obscuring its significance for theories of consciousness and cognitive architecture. We treat awakening as a functional construct capturing convergence across Hindu and Buddhist sources, phenomenological and psychometric findings, and neuroimaging evidence. Synthesizing these literatures, we find convergent evidence ...

---

### 36. Two dissociable axes of brain hierarchical dynamics track universal and population-specific effects of mindfulness

**Authors:** Victor Oswald, David Zarka, Riku Johannes Ihalainen, et al.

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.20854v1) | 📄 [PDF](https://arxiv.org/pdf/2610.20854v1)

**Summary:** How mental training reshapes the temporal architecture of large-scale brain dynamics and how these mechanisms differ between healthy and clinically vulnerable populations remains poorly understood. Time-averaged neural measures collapse the multi-scale nature of brain activity, obscuring the dynamic processes through which behavioural interventions reorganise hierarchical brain function. Here, applying a sliding-window Temporal Irreversibility Index to source-reconstructed EEG across three compl...

---

### 37. Semantic Alignment of EEG and Text: A Contrastive Learning Framework for Decoding Imagined Speech

**Authors:** Shahryar G. Namdari, Francesco Iacomi, Riccardo Barbieri, et al.

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.20766v1) | 📄 [PDF](https://arxiv.org/pdf/2610.20766v1)

**Summary:** Imagined speech decoding from EEG offers a promising route toward naturalistic brain-computer interfaces. Traditional closed-set classifiers treat semantic categories as independent labels and do not explicitly exploit relationships among linguistic intents, limiting output flexibility. We adapt a multimodal contrastive learning framework to imagined speech, aligning EEG trials with language representations in the embedding space of a frozen pretrained text encoder. An EEG encoder is trained wit...

---

### 38. EEG Correlates of Verbal and Perceptual Reasoning

**Authors:** Gwyneth Rolph

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.19979v1) | 📄 [PDF](https://arxiv.org/pdf/2610.19979v1)

**Summary:** Identifying the neural underpinnings of intelligence is one of the major goals of modern intelligence research. However, few imaging studies explore the high extremes of intelligence, and most use only a single composite IQ score. This study used quantitative EEG recordings to investigate correlations between the EEG variables of individual alpha peak frequency, relative power, and coherence, and scores on verbal and perceptual reasoning tests in participants with IQs from the low-average to exc...

---

### 39. Reciprocity coordinates a three-way trade-off in recurrent neural circuits

**Authors:** Xiaoyu Zhang, Mingyi Huang, Yixuan Cui, et al.

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.19949v1) | 📄 [PDF](https://arxiv.org/pdf/2610.19949v1)

**Summary:** Biological neural circuits contain both unidirectional and reciprocal connections, but how reciprocity affects circuit computation remains unclear. We varied reciprocity \r{ho} across 21 levels in recurrent-network simulations while holding network size, connection density, and directed-edge count fixed. Low-reciprocity networks produced more diverse stimulus-driven activity and performed better on four continuous-input tasks, whereas higher reciprocity generally improved performance on three de...

---

### 40. How Long Is the Coast of a Neuron? Resolution-Dependent Interaction Order and Computational Capacity

**Authors:** Nima Dehghani

**Published:** 2026-10-14

🔗 [Paper](http://arxiv.org/abs/2610.19487v1) | 📄 [PDF](https://arxiv.org/pdf/2610.19487v1)

**Summary:** Mandlebrot's coastline paradox reframes measurement as a joint property of an object and its ruler. Here we ask how observational resolution shapes the apparent structure of neural computation. We introduce a scale-indexed decomposition that separates the predictive information captured by direct dependencies from the residual outside that model family. Exact constructions show that projection can convert higher-order dependence into pairwise structure. Projection can increase the direct fractio...

---

### 41. Effects of cortisol time-scales in a model of emotion regulation

**Authors:** Michael Buccino, Joshua Ginart, Eva Kaslik, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.19282v1) | 📄 [PDF](https://arxiv.org/pdf/2610.19282v1)

**Summary:** Stress reshapes cortico-limbic dynamics across multiple timescales, with important consequences for healthy and pathological arousal responses. We develop and analyze a Wilson-Cowan model of prefrontal-amygdala circuitry, incorporating excitatory and inhibitory populations involved in emotional regulation. The effects of stress cortisol are represented as history-dependent modulations of two stress-sensitive interactions: recurrent prefrontal excitation and inhibition of basolateral amygdala pri...

---

### 42. Simulating Alzheimer's amyloid-like pathology on a fly central nervous system connectome

**Authors:** Taeho Jo

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.19153v1) | 📄 [PDF](https://arxiv.org/pdf/2610.19153v1)

**Summary:** In Alzheimer's disease, the amount of pathology in the brain is an imperfect predictor of how much function is lost. Pathology leads to that loss through neural circuits, but these cannot be observed neuron by neuron in patients. This study therefore simulated the central nervous system of the adult male Drosophila melanogaster: 166,700 integrate-and-fire neurons wired by the MaleCNS connectome. The simulator reproduced a published fly brain model (rate correlation 0.9997). Three kinds of damage...

---

### 43. Two Routes to Interoceptive Prioritisation: Dissociating Likelihood Precision and Preference Reweighting in Active Inference

**Authors:** St John Grimbly, Nicolas Kuske, Evert A. Boonstra, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18617v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18617v1)

**Summary:** An embodied agent must prioritise among competing bodily needs. In active inference, it can respond to an urgent need by increasing the precision of information about that need or by increasing its preference for outcomes that relieve it. We compare these two interventions, separately and together, in a foraging gridworld with three lethal needs, and ask how each changes survival, perception and the body model the agent learns. Precision sharpens interoceptive posteriors and improves survival. P...

---

### 44. Sense-Making phase transition framework for Affect

**Authors:** Miguel Bosch, Laura Fanfarillo, Gustavo Diez, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18115v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18115v1)

**Summary:** Contemporary accounts of affect emphasize different perspectives, ranging from the regulation of bodily states in allostatic approaches to the relational and sense-making character stressed by enactive theories. Here, we show that affect can be made explicit within the sense-making phase transition framework previously introduced for the perception of an inner sensation. Within this same formal structure, each stable minimum of the sense-making potential defines an affective state: its position ...

---

### 45. Rewiring of adult neural networks - learning from structural plasticity across multiple scales

**Authors:** Michael Fauth, Han Lu, Jannik Luboeinski, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.18024v1) | 📄 [PDF](https://arxiv.org/pdf/2610.18024v1)

**Summary:** Synaptic connections are continuously formed and eliminated even in adult neuronal networks. This process - called structural plasticity - allows networks to change their topology to learn and adapt to their environment or compensate for lesions. Yet, in contrast to synaptic plasticity, structural plasticity is less well studied and understood. We here present the current state of knowledge as well as open problems in the field along three guiding questions: (1) What regulates structural plastic...

---

### 46. Rethinking World Models for Biosignals

**Authors:** Xianglong Bao, Bosong Huang, Xiaoda Wang, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.17510v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17510v1)

**Summary:** World models promise to learn how systems evolve and respond to actions, enabling simulation, planning and decision-making. Bringing this promise to biosignals requires more than accurate prediction of physiological recordings. We examine existing biosignal world models through two requirements for intervention use: a genuine action and evidence of its causal effect. We identify three fundamental bottlenecks rooted in physiology: Temporal Latency, the variable delay between an action and its obs...

---

### 47. Collective Benefits and Efficiency in Coupled Echo State Networks

**Authors:** Polyphony Bruna, Rick Dale, Michael J. Spivey, et al.

**Published:** 2026-10-13

🔗 [Paper](http://arxiv.org/abs/2610.17506v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17506v1)

**Summary:** Simple aggregation of independent responses ("wisdom of crowds") generally improves collective performance through statistical facilitation, but interaction among members can sometimes hinder group outcomes. However, under certain circumstances, coordination studies show that interacting groups can outperform their individual members and nominal groups, and interaction can also be more efficient than independence. We present a reservoir computing model to investigate how interaction can enhance ...

---

### 48. Beyond Successful Play: Diagnosing Opponent Modeling in Large Language Models

**Authors:** Hanbo Xie, Yue Zhao, Robert C. Wilson

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.17310v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17310v1)

**Summary:** Language-model agents are expected to adapt to others whose behavior changes through interaction. Yet adaptation may rely on learned behavioral patterns rather than theory of mind (ToM): the ability to infer others' mental states, including beliefs and intentions. We introduce a benchmark and diagnostic framework for repeated hide-and-seek against algorithmic opponents with explicitly defined recursive belief updates. Their ground-truth beliefs and action probabilities let us distinguish adaptiv...

---

### 49. Learning Perceptual Geometry of Natural Odor Mixtures from LLM-Derived Descriptors

**Authors:** Farhad Pashakhanloo, Venkatesh N. Murthy

**Published:** 2026-10-12

🔗 [Paper](http://arxiv.org/abs/2610.17164v1) | 📄 [PDF](https://arxiv.org/pdf/2610.17164v1)

**Summary:** The relationship between odor chemistry and perception remains incompletely understood. Many existing studies focus on the perception of single molecules, whereas natural odors contain tens to hundreds of components, adding extra layer of complexity to percept formation. Here, we explore the relationship between molecular composition and perceived similarity in natural odor objects. We study this using a database of more than 1,200 volatile-compound-in-food mixtures containing more than 8,000 mo...

---

### 50. Simple model of neurogliovascular unit activity with noradrenaline leading force

**Authors:** Andrey Yu. Verisokin, Darya V. Verveyko, Alexey R. Brazhe, et al.

**Published:** 2026-10-11

🔗 [Paper](http://arxiv.org/abs/2610.15263v1) | 📄 [PDF](https://arxiv.org/pdf/2610.15263v1)

**Summary:** In this work we present a model of a neuroglivascular unit associated with a neuronal ensemble. We combine calcium dynamics in the astrocyte, the cascade of synthesis of arachidonic acid and its derivatives, as well as the activity of the network of inhibitory and excitatory neurons with changes in local blood flow. We add equations to the model for extracellular neurotransmitters such as GABA, glutamate, and norepinephrine. We show that the resulting model can exhibit different types of behavio...

---

## stat.ML

**50 papers**

### 1. Phase Transition from Random Features to Fully Trainable Networks

**Authors:** Xin He, Huan Lao, Xiliang Lu, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31663v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31663v1)

**Summary:** Constructing accurate and computationally tractable approximation spaces is a fundamental task in scientific computing. Partially trainable neural networks bridge fixed random features and fully adaptive representations. This paper quantifies a phase transition pattern in approximation bounds and observes analogous behavior in training errors: a rapid but smooth initial improvement followed by diminishing returns, with a sharper transition under greater initialization mismatch. Under polynomial ...

---

### 2. Reliable AI-Assisted Decisions via Selective Auditing

**Authors:** Isaac Gibbs, Elise L. Han, Ryan J. Tibshirani, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31662v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31662v1)

**Summary:** We consider online monitoring of an AI system that produces a sequence of decisions. At each round, the system outputs a proposed decision together with a confidence score estimating the trustworthiness of the decision. The decision and confidence score need not be produced by the same model: for example, one agent may propose a decision, while a separate verifier agent evaluates it and outputs a correctness or safety score. Based on this information, we must decide whether to accept the AI deci...

---

### 3. SympFormer: Inertial Attention Blocks from Damped Hamiltonian Dynamics on Spaces of Probability Measures

**Authors:** Viktor Stein, Levin Maier, Wuchen Li, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31600v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31600v1)

**Summary:** The attention mechanism underpins modern large language models, yet their dynamics remain only partially understood. Recent perspectives interpret attention blocks as interacting particle systems, whose mean-field limits correspond to gradient flows of energy functionals on spaces of probability densities on $\mathbb R^d$ equipped with Wasserstein-type metrics. We extend this viewpoint by deriving accelerated attention blocks from inertial, Nesterov-type damped Hamiltonian dynamics on these dens...

---

### 4. When to Follow the Teacher: Advantage-Based On-Policy Distillation

**Authors:** Mahdi Sabbaghi, George Pappas, Hamed Hassani, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31563v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31563v1)

**Summary:** Online Policy Distillation (OPD) often outperforms offline methods such as Supervised Fine-Tuning (SFT) by training on trajectories sampled directly from the student. However, standard OPD trains the student to follow the teacher at every state of the trajectory, assuming that teacher guidance is always beneficial. We instead distinguish between what the teacher prefers and what actually helps the current student succeed. We introduce Advantage-Based On-Policy Distillation (AOPD), which weights ...

---

### 5. Diffusion Language Models for Perplexity-Aware Black-Box Attacks

**Authors:** Ali Al-Lawati, Elsayed Eshra, Dongwon Lee, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31558v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31558v1)

**Summary:** \emph{Continuous-space} attacks find prompts that trigger malicious behaviors, such as overthinking, in black-box LLMs by sampling or optimizing over a low-dimensional Gaussian latent space and decoding it to text through a \emph{random mapping} and nearest-token lookup. Because the random mapping is not learned from language, its prompts can be highly unnatural, and as such easily detectable through input guardrails, and the risk estimates they yield are not grounded in natural prompts. In this...

---

### 6. Nonparametric autoregressive estimation of probability distributions with parallel gradient boosting

**Authors:** Rémy Chapelle

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31524v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31524v1)

**Summary:** Nonparametric estimation of joint probability distributions is a core problem in statistics, which is notoriously challenging with high-dimensional data. Such challenges also arise with conditional distribution estimation and have led to flexible algorithms that aim to tackle the ''curse of dimensionality'' by exploiting predictive structures of lower dimension than the ambient space. In this paper, we study the use of such conditional distribution estimators to estimate joint distributions by f...

---

### 7. SABLE: Scalable Affine Bayesian Latent-space Exploration

**Authors:** Erik Bodin, Lisa Maria Kreusser, Donney Fan, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31495v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31495v1)

**Summary:** Complex objects such as engineering designs and proteins are often difficult to optimise because their design spaces exhibit high-dimensional structure and objective evaluations are expensive. Generative models provide continuous latent representations, but their latent spaces can have thousands to tens of thousands of dimensions, creating a regime where the latent dimension $D$ greatly exceeds the evaluation budget. We introduce SABLE, a Bayesian optimisation method for high-dimensional latent ...

---

### 8. Dimension-free regimes for unadjusted Langevin in ridge-separable models: A subspace robust Wasserstein analysis

**Authors:** Yuansi Chen, Francesco Pedrotti, Peter A. Whalley

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31431v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31431v1)

**Summary:** The Unadjusted Langevin Algorithm (ULA) is widely used for high-dimensional Bayesian inference. Classical analyses in Wasserstein-2 distance predict an asymptotic bias and a mixing time that grow with dimension, but this metric is stronger than necessary for many statistical tasks. We instead analyze the bias in subspace robust Wasserstein distance, which controls the mean and arbitrary low-dimensional marginals and is therefore well suited to observables typically estimated in practice. For rid...

---

### 9. Metric Conformal Prediction via the Conditional Expected Local Radius

**Authors:** Rui Qiu, Fang Yao, Zhou Yu

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31336v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31336v1)

**Summary:** We introduce the conditional expected local radius (CELR) and develop a new conformal prediction method for non-Euclidean responses in general metric spaces. CELR measures local conditional probability concentration, allowing prediction sets to accommodate heterogeneity and multimodality without requiring densities or a vector space structure. Its conditional distribution yields a nonconformity score that is comparable across covariate values and avoids costly transport comparisons between dista...

---

### 10. Deep Learning for Random Objects in Metric Spaces: Beyond Manifold Assumptions

**Authors:** Marcos Matabuena, Xiaokai Luo, Oscar Hernan Madrid Padilla

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31328v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31328v1)

**Summary:** Deep learning (DL) methods have substantially improved predictive performance across a wide range of downstream prediction tasks, enabling new discoveries in multiple domains. However, principled DL methods for non-Euclidean random objects remain relatively scarce, despite the growing importance of modern biomedical outcomes taking the form of probability distributions, random graphs, functions, and other random objects in metric spaces. Motivated by a new generation of digital and clinical biom...

---

### 11. Local Discrimination of Binary Classifiers via Localized AUC Functional

**Authors:** Wenye Ren, Anna Győrffy-Kerekes, Tancredi Dorsi, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31216v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31216v1)

**Summary:** Risk prediction models are frequently evaluated with AUC, which means that during evaluation we are blind to performance heterogeneity, which could lead to bad decision-making in clinics. In this work, we aim to change that by identifying patient cohorts for whom the risk prediction model might not be an accurate predictor. To separate these cohorts, we use a version of the weighted AUC, which we call Localized AUC or LAUC. Using this metric, we build a method that we coin LOCATOR. This method i...

---

### 12. Prediction Uncertainty Controlled Computer Model Calibration

**Authors:** Ryan Heejoon Byun, Dayeon Yoon, Won Chang

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31163v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31163v1)

**Summary:** Computer-model calibration is usually undertaken in service of prediction, yet neither Bayesian Kennedy-O'Hagan (KOH) calibration nor amortized simulation-based inference is built to control the predictive error of the calibrated simulator. When parameters are weakly identified or the data-model discrepancy is misspecified, the simulator-output bands induced by a nominal posterior level can be far from nominal. We propose a two-layer framework that targets predictive miscoverage directly. First,...

---

### 13. What Comes Next and Why: Interpretable Next-Event Prediction with Neuro-Symbolic Rules

**Authors:** Tim Nico Bauerschmidt, Isabel Valera, Jilles Vreeken

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31114v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31114v1)

**Summary:** In real-world applications, being able to explain why a prediction is made is often as important - if not more so - than achieving high accuracy. However, existing methods for sequential event prediction typically prioritize accuracy at the expense of interpretability. Neuro-symbolic approaches offer a promising direction to improve interpretability by learning symbolic rules, but extending them to next-event prediction is challenging due to the presence of temporal dependencies. We introduce RU...

---

### 14. Transformers with CoT Discover Heavy-Ball Acceleration Through Training

**Authors:** Yuxuan Cai, Yuan Cao

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.31089v1) | 📄 [PDF](https://arxiv.org/pdf/2610.31089v1)

**Summary:** Modern transformers often solve complex tasks by generating and refining intermediate reasoning steps. To develop a theoretical understanding of chain-of-thought (CoT) reasoning, a notable recent study by Huang et al. (2025) viewed transformers as algorithm executors, and showed that when transformers' CoT steps are supervised by a gradient-descent teacher, they can learn to implement gradient descent for in-context weight prediction in linear regression. In this paper, we study the same in-cont...

---

### 15. Random Projections for Spectral Algorithms: Optimal Rates in Sobolev Norms

**Authors:** Caixing Wang, Yue Wang

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.30948v1) | 📄 [PDF](https://arxiv.org/pdf/2610.30948v1)

**Summary:** Random projections (RP) offer an effective method for reducing computational and storage overhead while preserving the geometric structure of data. However, existing studies have primarily focused on the optimal generalization performance of specific kernel-regularized algorithms with RP in the well-specified setting and under restrictive conditions. In this paper, we provide a comprehensive and improved analysis of the generalization performance of RP-based spectral algorithms under general con...

---

### 16. Continuous-depth Deep Gaussian Processes

**Authors:** Ying Li, Sanyou Wu, Zi Yang, et al.

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.30890v1) | 📄 [PDF](https://arxiv.org/pdf/2610.30890v1)

**Summary:** Deep Gaussian processes (DGPs) are appealing Bayesian regression models, but their standard discrete-depth parameterization often becomes harder to optimize as depth grows. We argue that depth is better treated as a latent continuous evolution than as a long discrete stack. We therefore propose a continuous-depth formulation in which the latent representation follows a stochastic differential equation with a depth-indexed drift family equipped with a GP-based prior. This reframes the core design...

---

### 17. xVGAE: A Hierarchical Variational Graph Autoencoder for Exchangeable Graphs

**Authors:** Daniele Micheletti, Federica Zoe Ricci, Erik B. Sudderth

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.30815v1) | 📄 [PDF](https://arxiv.org/pdf/2610.30815v1)

**Summary:** Graphs play a crucial role in many applications, ranging from drug discovery to social network modeling and astronomy. Generative models for graphs have substantially advanced in recent years, but we identify relatively simple scenarios where state-of-the-art models struggle to converge within a standard compute budget, or exhibit prohibitively slow generation times. We propose a generative architecture that achieves quality competitive with state-of-the-art models and is orders of magnitude fas...

---

### 18. Width and Depth Limits Commute During Training

**Authors:** Ruijia Zhang, Soufiane Hayou

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.30729v1) | 📄 [PDF](https://arxiv.org/pdf/2610.30729v1)

**Summary:** Recent work established that the infinite-width and infinite-depth limits of residual networks commute at initialization when residual branches are scaled by $1/\sqrt{depth}$. In particular, the network output converges to the same limit whether width and depth tend to infinity sequentially or jointly. We extend this commutativity result to training in linear residual networks. Under the same $1/\sqrt{depth}$ residual-branch scaling (Depth-$μ$P) and the $μ$P width parameterization, we prove that...

---

### 19. Residual Calibration via Local Feature-Space Refinement

**Authors:** Xihao Wang, Chengyao Yu, Ruixing Ming

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.30652v1) | 📄 [PDF](https://arxiv.org/pdf/2610.30652v1)

**Summary:** Deep neural networks often struggle to provide reliable confidence estimates, making post-hoc calibration essential for reliable decision-making. Existing post-hoc methods largely rely on score-based transformations, which improve marginal calibration but often fail to capture spatially varying miscalibration in local regions of the learned feature space. To address this gap, we propose Local Adaptive Probability Estimation (LAPE), a post-hoc residual calibration framework. Specifically, LAPE tr...

---

### 20. Lifetime-valid decisions by continually evolving AI analysts

**Authors:** Xiaojing Sun, Yuhan Zeng, Xiao Wang

**Published:** 2026-10-22

🔗 [Paper](http://arxiv.org/abs/2610.30562v1) | 📄 [PDF](https://arxiv.org/pdf/2610.30562v1)

**Summary:** AI agents increasingly act as analysts whose decision can often be cast as hypothesis tests. Classical tests control the Type I error rate, the probability of rejecting a true null hypothesis, for fixed procedures. However, AI analysts introduce internal randomness and can evolve continuously over time. As AI analysts evolve, the risk of approving versions with Type I error rates above the target can accumulate, and adaptive use of evaluation feedback can lead to overfitting. We introduce contin...

---

### 21. Flow-based Spectral Kernel Learning for Nonstationary Attention

**Authors:** Zi Yang, Ying Li, Alejandro Lancho, et al.

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.30465v1) | 📄 [PDF](https://arxiv.org/pdf/2610.30465v1)

**Summary:** Kernelized attention provides a useful perspective for understanding self-attention as a similarity-based aggregation mechanism, but existing approaches often rely on fixed or stationary kernels, limiting their ability to adapt the similarity structure to complex token interactions. In this paper, we propose flow-based spectral kernel attention (FSKA), a framework for learning expressive nonstationary attention kernels. FSKA formulates kernelized attention through spectral density learning and p...

---

### 22. High-Value Training Data from Noisy, Diverse Sources

**Authors:** Hedi Driss, Evan Frick, Anastasios N. Angelopoulos, et al.

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.30421v1) | 📄 [PDF](https://arxiv.org/pdf/2610.30421v1)

**Summary:** Training state-of-the-art models increasingly requires learning from large, heterogeneous datasets whose examples vary in quality, domain relevance, and source of supervision. Dataweighting---assigning different weights to training examples---offers a general way to control how such data influences training, but learning effective weights at scale remains challenging. We develop a scalable approach to learning dataweights: given a small, high-quality target dataset, we use metagradients through ...

---

### 23. Geometric Algebra for Neural Networks: A Survey

**Authors:** Tao Zhong, Kaison Fong, Keqin Wang, et al.

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.30121v1) | 📄 [PDF](https://arxiv.org/pdf/2610.30121v1)

**Summary:** Geometric algebra (GA) unifies geometric primitives and transformations in a single algebraic framework. Neural networks designed around this framework often represent features as multivectors and constrain layer operations to respect the algebraic structure, enabling principled treatment of geometric transformations and, in many cases, built-in equivariance. This survey reviews geometric algebra neural networks, including their building blocks, equivariant properties, application domains, empir...

---

### 24. The role of locality and weight sharing in convolutional neural networks

**Authors:** Francesco Mori, Melanie Weber

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.30118v1) | 📄 [PDF](https://arxiv.org/pdf/2610.30118v1)

**Summary:** The success of convolutional neural networks is often attributed to locality and weight sharing. However, how these two properties separately shape learning, and how their effects depend on the spatial correlations of natural images, remain poorly understood. We address these questions in a teacher-student model with a convolutional teacher acting on $P$ input positions with correlation $c$ between positions. We compare convolutional and locally connected students trained by online stochastic gr...

---

### 25. Mitigating Model Collapse through Dreaming Learning

**Authors:** Matteo Benati, Alessandro Londei, Denise Lanzieri, et al.

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.30009v1) | 📄 [PDF](https://arxiv.org/pdf/2610.30009v1)

**Summary:** Training generative models on synthetic data causes loss of diversity and a decrease in performance, a phenomenon known as model collapse. We study this degeneration spectrally in a controlled Markov setting. The eigenvalue spectrum of the learned transition operator offers a direct view of the process, since the subdominant eigenvalues set how fast the chain mixes and therefore how much of the state space it continues to explore. We find that sampling at temperature $T_s < 1$ acts on the operat...

---

### 26. The Price of Current-Effect Inference in Nonstationary Multi-Armed Bandits

**Authors:** Sharan Sahu, Martin T. Wells

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29982v1) | 📄 [PDF](https://arxiv.org/pdf/2610.29982v1)

**Summary:** Adaptive experiments use bandit algorithms to favor interventions with higher expected rewards. However, decision-makers also require reliable inference on current treatment effects: differences between intervention and reference-arm mean rewards at the present time, rather than historical averages. These objectives conflict: reward maximization favors better interventions, whereas current-effect inference requires continued exploration of potentially suboptimal interventions as outcomes change ...

---

### 27. When Reconstruction Is Not Enough: Doubly Robust Counterfactual and Interventional Mediation Analysis with Learned Multimodal Representations

**Authors:** Cong Cao

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.30220v1) | 📄 [PDF](https://arxiv.org/pdf/2610.30220v1)

**Summary:** Learned representations of high-dimensional multimodal health records are increasingly used to adjust for confounding, yet they are usually trained to reconstruct the data rather than preserve the information that causal identification requires. We study counterfactual outcomes under alternative treatments, including phenotype-specific effects and patient-level counterfactual risk profiles of the kind digital twins provide, and interventional direct and indirect effects under exposure-induced in...

---

### 28. Mastering Model Fit: Applications of the InterModel Vigorish for Interpretable Machine Learning

**Authors:** Jiani Yan, Pengyun Wang, Klint Kanopka, et al.

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29960v1) | 📄 [PDF](https://arxiv.org/pdf/2610.29960v1)

**Summary:** Accuracy alone gives little information about which features or model components improve probabilistic fit, which outcomes benefit, or how fit changes during training. We introduce the InterModel Vigorish (IMV) into the Machine Intelligence space in order to express differences in fit as an expected betting advantage over a reference model. SHAP-IMV attributes gains to features through Shapley-weighted subset comparisons, Multi-IMV evaluates one-vs-rest and pairwise class discrimination, and Abl...

---

### 29. AI Mindmeld: A Latent Interconnect Protocol

**Authors:** Siavash Golkar, Jake Kovalic, Shirley Ho

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.30215v1) | 📄 [PDF](https://arxiv.org/pdf/2610.30215v1)

**Summary:** LLMs can act as scientific agents using tools to consult specialists and run experiments. Yet specialist information must enter their context, generally as text, images, audio or video: a bottleneck between models with rich, high-dimensional representations. We advocate direct representation exchange: a mindmeld conveying many properties, including information an LLM would not think to request. It should be extensible to new specialists, flexible across questions and tasks, and compositional acr...

---

### 30. Silent Alignment in Two-Layer Linear Networks: A High-Dimensional Perspective

**Authors:** Simon Martin, Francis Bach, Giulio Biroli

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29864v1) | 📄 [PDF](https://arxiv.org/pdf/2610.29864v1)

**Summary:** We study gradient flow in a two-layer linear network in the high-dimensional regime where the input, inner and output dimensions diverge proportionally. Under whitened inputs and isotropic imbalance, we combine a closed-form solution of the dynamics with prior random matrix theory results to derive a high-dimensional limit for the dynamics. Our method yields exact asymptotic spectral distributions for the weight matrices at all times and characterizes the evolution of the learned subspace. In th...

---

### 31. How Do DiTs Denoise? An Aggregator-Predictor View of Attention and MLPs

**Authors:** Gyeonghun Kang, William Xingxu Chen, Xiang Cheng

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29854v1) | 📄 [PDF](https://arxiv.org/pdf/2610.29854v1)

**Summary:** How do diffusion transformers (DiTs) represent image content and learn rules for reusing it to generalize? We develop an aggregator--predictor view of DiTs as input-adaptive local denoisers, in which context aggregation and patch prediction provide functional roles for interpreting attention and MLPs. We first establish that, for Gaussian Markov random field (GMRF) priors, the global Bayes denoiser can be approximated using only a subset of context patches, with error decaying exponentially in c...

---

### 32. Asymmetric Likelihood-Free Hypothesis Testing

**Authors:** Gunjan Kumar, Yash Pote, Jonathan Scarlett

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29798v1) | 📄 [PDF](https://arxiv.org/pdf/2610.29798v1)

**Summary:** In likelihood-free hypothesis testing (LFHT), given samples from two unknown distributions $P,Q$ on $[n]$ with $\mathrm{d_{TV}}(P,Q)\geq\varepsilon$, and from a third distribution $D\in\{P,Q\}$, the goal is to identify whether $D=P$ or $D=Q$. We study asymmetric likelihood-free hypothesis testing, where the sample budgets $s_P$ and $s_Q$ for $P$ and $Q$ may differ, and characterize the feasible triples $(s_P,s_Q,s_D)$ up to logarithmic factors. We establish that unequal reference budgets can giv...

---

### 33. Post-hoc Epistemic Uncertainty for Vision-Language-Action Policies

**Authors:** Johannes Keller, Albrecht M. Bloße, Adrian Lindenmeyer, et al.

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29730v1) | 📄 [PDF](https://arxiv.org/pdf/2610.29730v1)

**Summary:** Vision-language-action (VLA) policies need to recognize gaps in their training knowledge to request useful demonstrations or assistance in new situations, especially when failures are costly. Disagreement within an ensemble of independently trained policies can guide these decisions, but requires training and running multiple policies. We propose post-hoc kernel-variance heads that estimate epistemic uncertainty from the embeddings of a single policy. Each head computes the conditional variance ...

---

### 34. Lifting PCA in the Wasserstein Space

**Authors:** Jérémie Bigot, Clément Bonet

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29679v1) | 📄 [PDF](https://arxiv.org/pdf/2610.29679v1)

**Summary:** Principal Component Analysis (PCA) is a fundamental tool for statistical dimension reduction, yet no canonical extension to distribution-valued data has emerged within the framework of optimal transport. While Wasserstein barycenters and Wasserstein least-squares regression provide canonical liftings of Euclidean averaging and linear regression in the Wasserstein space, an analogous principle for PCA has remained unexplored. In this paper, we introduce Lifted PCA, a canonical extension of Euclid...

---

### 35. Near Minimax Rate for Quantile Distributional Reinforcement Learning

**Authors:** Zijie Cheng, Zhihua Zhang

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29595v1) | 📄 [PDF](https://arxiv.org/pdf/2610.29595v1)

**Summary:** In this paper, we study quantile distributional policy evaluation, where the return distribution under a given policy is approximated by the quantile Bellman fixed point $\bmη_m$. We investigate the statistical accuracy of estimating $\bmη_m$ across quantile resolutions under Wasserstein distances. Assuming access to a generative model, we construct a quantile fixed point estimator $\bmη_m^{(n)}$ from an empirical Markov decision process and establish non-asymptotic error bounds under Wasserstei...

---

### 36. Fragment-Level Graph Encoding for Interpretable Molecular Property Prediction

**Authors:** Rafael Lopes Almeida, Ina Pöhner

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29589v1) | 📄 [PDF](https://arxiv.org/pdf/2610.29589v1)

**Summary:** Graph neural networks (GNNs) are among the standard tools for molecular property prediction, but the atom-level explanations of their predictions are hard for medicinal chemists to act on. We propose a change of input representation rather than a new model: molecules are encoded as fragment-level graphs from BRICS decomposition, where each node is a synthetically meaningful fragment whose features are the element-wise sum of its atoms' features. Because only the representation changes, any messa...

---

### 37. Private Online Prediction from Experts with Small Losses

**Authors:** Bo Li, Peng Ye

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29575v1) | 📄 [PDF](https://arxiv.org/pdf/2610.29575v1)

**Summary:** We consider online prediction from experts, a fundamental problem in machine learning, under differential privacy constraints. Existing private algorithms achieve near-optimal regret $\tilde{O}(\sqrt{T})$, where $T$ is the time horizon. However, this bound becomes suboptimal when $L^\star$, the cumulative loss of the best expert, is significantly less than $T$. In this work, we present the first differentially private algorithm with regret $\tilde{O}(\sqrt{L^\star})$, offering a substantial impr...

---

### 38. Residual-Based Causal Discovery via Pretrained In-Context Quantile Regression

**Authors:** Daniel Klippert, Quang Nhat Huynh, Alexander Marx

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29530v1) | 📄 [PDF](https://arxiv.org/pdf/2610.29530v1)

**Summary:** Residual-based causal discovery assumes that each variable is generated from its parents and an independent noise source. It estimates this noise and tests its independence from candidate causes. For identifiable functions such as additive-noise models (ANMs) and the broader class of location-scale noise models (LSNMs), this principle identifies the causal direction, as only the causal model admits this independence. Existing LSNM methods rely on parametric assumptions to obtain standardized res...

---

### 39. BRIDGE: An Acceptance Gate to Block False Improvements in Model Updates, with a Retrospective Clinical Evaluation

**Authors:** Dwi Sunaryono

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29515v1) | 📄 [PDF](https://arxiv.org/pdf/2610.29515v1)

**Summary:** Models are updated repeatedly, and an update that looks better on validation data but not on new data is a false improvement that can misguide clinical decisions. The naive rule accepts every positive validation gain and is optimistic when the same data choose and judge the update. BRIDGE is a model-agnostic acceptance gate that decides each update from predictions and the available labels, with fixed settings. Each fold of the data judges the update chosen on the other folds (cross-fitting) to ...

---

### 40. A unified approach for estimation of unnormalized models via Stein operators

**Authors:** Mitsuki Nagai, Keisuke Yano

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29510v1) | 📄 [PDF](https://arxiv.org/pdf/2610.29510v1)

**Summary:** In this paper, we develop a unified framework connecting proper scoring rules and Stein's method for the estimation of unnormalized models. We construct a class of proper scoring rules that encompasses score matching, ratio matching, pseudolikelihood, and noise contrastive estimation. We show that these proper scoring rules naturally induce Stein operators. This connection yields a new construction principle for Stein operators, and enables us to study estimators based on these scoring rules thr...

---

### 41. Generative Modeling via Nonlinear Schrödinger Bridges and Branching Diffusions

**Authors:** Mathias Grau, Pierre Henry-Labordère

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29476v1) | 📄 [PDF](https://arxiv.org/pdf/2610.29476v1)

**Summary:** We propose a new generative modeling framework grounded in forward-backward partial differential equations (PDEs). These equations arise naturally in mean-field game (MFG) theory, and are closely related to nonlinear Schrödinger systems. Our main contribution is to reinterpret this connection within the setting of generative modeling and to develop an efficient numerical methodology for its practical implementation. Specifically, we derive and characterize a nonlinear extension of the classical ...

---

### 42. Density-Level Backward Error for Low-NFE Generative Flows

**Authors:** Ewsey Obzherin, Valentin Khrulkov

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29475v1) | 📄 [PDF](https://arxiv.org/pdf/2610.29475v1)

**Summary:** Low-NFE generative ODE sampling is constrained not only by solver order, but also by how a fixed budget of network evaluations is distributed along the flow. We develop a density-level backward-error framework that identifies the component of a solver's modified-equation defect that changes the evolving marginal, while excluding solenoidal trajectory distortion that is invisible in Wasserstein tangent geometry. The resulting residual induces a solver-order-aware compute-allocation rule and, thro...

---

### 43. One Act, Many Masks: Effect-Marginal Policy Optimization for Long-Horizon Agents

**Authors:** Shaojin Ma, Ruitao Wang, Pengyi Li, et al.

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29427v1) | 📄 [PDF](https://arxiv.org/pdf/2610.29427v1)

**Summary:** Recent advances in multi-turn reinforcement learning (RL) have substantially improved the performance of LLM agents on complex, long-horizon interactive tasks. However, despite progress in fine-grained credit assignment, policy optimization still applies these learning signals through response-specific probability ratios. Different textual responses can induce the same executable effect, yet credit differences arising from subsequent outcomes remain tied to their individual textual realizations....

---

### 44. When Thoughts Become Memory: Unifying In-Context Learning and Fine-Tuning

**Authors:** Leon Chlon, Julie Huang

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29419v1) | 📄 [PDF](https://arxiv.org/pdf/2610.29419v1)

**Summary:** We are the first to give a certified rule for whether unseen data belong in a pretrained model's context or its weights, built on an exact law for their information value. That value, the code length saved on held-out queries, equals in expectation the bits stored about the query, plus a prior repair, minus a decoding loss, for any model, architecture, dataset and task. The law's ceilings certify the choice from one measurement, and an anytime-valid test makes it from held-out queries, with erro...

---

### 45. The Predictive--Optimization Gap in GuanDan Self-Play

**Authors:** Qicheng Zou, Biao Yuan, Siyu Song, et al.

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29411v1) | 📄 [PDF](https://arxiv.org/pdf/2610.29411v1)

**Summary:** Outcome-predictive signals are often treated as promising optimization targets in reinforcement learning, but predictive validity and optimization utility are different claims. We expose this distinction in GuanDan, a multi-round imperfect-information game in which the implication of a round outcome depends on the public match state. Held-out analysis shows that state--gain interactions provide incremental predictive value beyond a constant signed-gain effect, establishing that match progress is...

---

### 46. Cascading Bandits with Noisy Observations: Algorithms and Regret Bounds

**Authors:** Yashaswini Kaluguri, Nikhil Karamchandani

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29381v1) | 📄 [PDF](https://arxiv.org/pdf/2610.29381v1)

**Summary:** We propose a novel stochastic cascading bandit setup where probing an ordered shortlist of $K$ out of $L$ arms incurs position-dependent costs, and the learner observes only noisy feedback regarding each arm's true output. We identify a sub-class of noise models for which the optimal shortlist can be found by sorting arms according to a per-arm score: such a score exists for both selection and ordering when the channel has no false positives, and for ordering alone (but not selection) when measu...

---

### 47. GaP-MoE : Explicit Expert Specialization in Mixture-of-Experts via Orthogonal Gradient Accumulation and Projection

**Authors:** Donghyun Jeong, Yoon-Yeong Kim

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29355v1) | 📄 [PDF](https://arxiv.org/pdf/2610.29355v1)

**Summary:** Sparse Mixture-of-Experts (SMoE) models improve scalability by routing input tokens to only a subset of expert networks, but they often suffer from representation collapse, in which multiple experts converge toward similar functions and lose their intended diversity. Prior work has addressed this limitation either by improving router architectures or by introducing auxiliary loss terms that implicitly penalize similarity among experts. However, router-based approaches remain vulnerable to routin...

---

### 48. Differentially Private Synthetic Data via Generalized Moment Matching

**Authors:** Rundong Ding, Yiyun He, Yizhe Zhu

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.30196v1) | 📄 [PDF](https://arxiv.org/pdf/2610.30196v1)

**Summary:** We study $(\varepsilon,δ)$-differentially private synthetic data for arbitrary databases of $n$ records in $[-1,1]^d$ under a specified integral probability metric (IPM). We introduce generalized moment matching, which estimates moments privately, fits a probability measure, and samples synthetic records. A general error theorem applies when moment error controls the target IPM. This framework extends Chebyshev moment matching for $1$-Wasserstein distance and smooth queries. We apply the framewo...

---

### 49. ExpEvolve: Structuring and Reusing Experience for Open-Ended Discovery

**Authors:** Yongqiang Chen, Chenxi Liu, Deyu Zou, et al.

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29303v1) | 📄 [PDF](https://arxiv.org/pdf/2610.29303v1)

**Summary:** Evolutionary coding agents such as AlphaEvolve are one of the notable successes in using Large Language Models (LLMs) to build AI Scientists. These agents tackle open-ended scientific problems by iteratively improving and evolving programs, leveraging the prior knowledge and reasoning capabilities of LLMs. Despite their success, mutations over programs are mostly low-level upon surface heuristics, without a persistent unit of control. In contrast, science compounds through ideas. In this work, w...

---

### 50. Approximate Solomonoff Induction: On the Robustness of Learned Universal Predictors

**Authors:** Qian Li, Shang-Hua Teng

**Published:** 2026-10-21

🔗 [Paper](http://arxiv.org/abs/2610.29289v1) | 📄 [PDF](https://arxiv.org/pdf/2610.29289v1)

**Summary:** Why large language models trained via log-loss minimization over massive and diverse datasets exhibit broad capabilities and generalizable skills is not yet fully understood. Grau-Moya et al. (ICML 2024) offer a conceptual explanation through the lens of meta-learning: if sequence-generating environments $ν$ are drawn from a prior $w_ν$, minimizing population log-loss recovers the corresponding Bayesian mixture predictor $ξ=\sum_νw_νν$. In the idealized limit in which $w$ is a universal prior, t...

---

