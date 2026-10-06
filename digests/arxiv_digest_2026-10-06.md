# arXiv Daily Digest - 2026-10-06

Total papers: 350

---

## cs.AI

**50 papers**

### 1. One Figure, Every Canvas: Editable Flowchart Relayout via Agentic Pipeline

**Authors:** Shih-Chen Tseng, Chih-Hsuan Chen, Ryan Yang, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06852v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06852v1)

**Summary:** Pipeline figures in ML papers must be repurposed across many canvases, including paper columns, 16:9 slides, portrait posters, 1:1 social teasers, 9:16 phone previews. Each format imposes a different aspect ratio on the same computational graph, where any silently broken connection misrepresents the method. We formulate aspect-ratio-adaptive flowchart relayout as a distinct task: given a raster flowchart and a target ratio, produce a structurally faithful, hallucination-free, editable layout. Ex...

---

### 2. Base Models Can Reason By Taking a Cue From Training Data

**Authors:** Sophie L. Wang, Amil Dravid, Rulin Shao, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06851v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06851v1)

**Summary:** In this paper, we study how training data creates associations between the tokens at the start of a base model's response and the reasoning behavior that follows. First, we demonstrate that fixing particular starting token cues makes a base model's performance competitive with that of its reinforcement learning (RL)-trained counterparts on math and coding. For instance, the cue ".\n\nOkay" raises Olmo-3-7B's MATH-500 pass@1 accuracy from 42% to 78%, while "Alright," raises Qwen3-14B's from 72% t...

---

### 3. BiasFlow: Geometric Monitoring and Backbone Regularization for Spurious Feature Reliance

**Authors:** Haojin Deng, Zhiping Lin, Yimin Yang

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06846v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06846v1)

**Summary:** Worst-group accuracy (WGA) evaluates a trained predictor but does not characterize how its frozen backbone behaves when a new head is learned. We introduce BiasFlow, a hook-based toolkit for monitoring class-attribute centroid alignment (IBMI), within-class centroid separation (W-IBMI), and feature-projection sensitivity. IBMI is confounded by class-attribute correlation and is not a measure of causal feature reliance. We pair these diagnostics with BiasFlow Regularization (BFR), a supervised, c...

---

### 4. Learning to Read the Contextual Tokens in Diffusion Transformers

**Authors:** Omer Dahary, Etai Sella, Hadar Averbuch-Elor, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06844v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06844v1)

**Summary:** Multimodal Diffusion Transformers (MM-DiTs) jointly process visual and textual representations throughout generation. These models repeatedly update the text tokens through multimodal attention, forming dynamic contextual tokens whose function is not well understood. In this work, we introduce a framework for reading this contextual space through natural-language interrogation. We train a lightweight bottleneck network that maps intermediate contextual tokens into the input space of a frozen Lar...

---

### 5. Recursive Video In-Context Learning for Agentic Robot

**Authors:** Wenrui Bao, Xinxin Liu, Bingxin Xu, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06843v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06843v1)

**Summary:** LLM agents that orchestrate frozen vision-language-action (VLA) policies improve across episodes through text memory, which records what the agent did but not how the task is done. A demonstration video shows it, but fits poorly into an agent's context. The full video slows every turn, fixed keyframes lose the contact detail that decides whether a grasp holds, and what the agent needs shifts from the task's structure while planning to the frames around each contact. We introduce Recursive Video ...

---

### 6. UniSlider: Perceptually Uniform Sliders for Continuous Image Editing

**Authors:** David Serrano-Lozano, Duygu Ceylan, Yannick Hold-Geoffroy, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06831v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06831v1)

**Summary:** Sliders provide an intuitive interface for continuous image editing. In current generative approaches, however, the slider is simply a rescaling of the method's strength parameter, such as an adapter coefficient, a prompt weight, or an interpolation factor. This strength relates poorly to perceptual change. The image can partially revert as the slider moves, long stretches of the range produce no visible difference, and short intervals transform the image abruptly. Remapping the strength could f...

---

### 7. MemPilot: Orchestrating On-Demand Multimodal Memory Curation for LLM Agents

**Authors:** Haozhen Zhang, Haodong Yue, Quanyu Long, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06830v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06830v1)

**Summary:** Memory has become integral to the LLM agent ecosystem, supporting information retention and reuse across interactions. However, most existing agent memory systems construct memory in a query-agnostic manner, which can incur unnecessary preprocessing cost and discard details that later prove essential. Recent studies have begun shifting memory processing toward runtime adaptation, but typically specialize in particular operations or fixed processing schemes, leaving flexible control over performa...

---

### 8. CLIFT: Conformal Self-Verification for Web Agent Training and Test-Time Scaling

**Authors:** Yifan Zhang, Yutong Dai, Viraj Prabhu, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06829v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06829v1)

**Summary:** Open-source web agents are now strong enough to execute realistic browser tasks, but training them with reinforcement learning still depends on weak supervision: binary task success is too sparse for credit assignment, while frontier-language-model judges are too expensive to call at every step and cannot be assumed available at deployment. We introduce CLIFT, a training and test-time scaling method built around conformal self-verification. During training, the agent answers natural-language ver...

---

### 9. TasteVal: Measuring the Experimental Research Taste of AI Systems Against Human Experts

**Authors:** Oliver Jaffe, Dane Sherburn

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06824v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06824v1)

**Summary:** We introduce TasteVal, a benchmark to evaluate the experimental research taste of frontier models. We define research taste as the ability to pick interesting problems to solve, design experiments, and interpret experimental results. TasteVal measures the experimental component of research taste; given a fixed research problem, we measure how well a model iteratively designs experiments and draws conclusions from their outcomes. We operationalize experimental research taste as compute efficiency...

---

### 10. Deep Learning for Sleep Heart Rate Estimation from Accelerometers: Toward Population-Scale Cardiac Insight Without Optical Sensors

**Authors:** Tanbin Islam Rohan, Pranjol Sen Gupta, Tanusree Debi, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06823v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06823v1)

**Summary:** Large longitudinal cohorts often contain wrist accelerometry without optical heart-rate sensing, motivating recovery of cardiac information from motion signals already collected during sleep. We present SeqSmoother, a transformer-based temporal corrector for sleep heart rate (HR) estimation from wrist accelerometry. SeqSmoother combines spectral descriptors with an intermediate Nightbeat-derived frequency anchor and a physics-motivated sub-harmonic feature designed to identify harmonic frequency...

---

### 11. Paradee: Distilling Kokoro-82M into an 8M-Parameter Single-Voice Text-to-Speech Model

**Authors:** Sahil Mahendrakar

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06817v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06817v1)

**Summary:** We distill Kokoro-82M, a widely used open text-to-speech model with 54 voices, into Paradee, an 8.07M-parameter model that speaks one of them. Paradee keeps Kokoro's architecture with much narrower layers, and each of its two halves is trained separately against the frozen teacher. It has 10x fewer parameters and needs 15x less compute. We first synthesize a corpus with the teacher and keep its durations, pitch, energy and phoneme features. We then train a small text side to predict these values...

---

### 12. TAPDreamer: Transferable Adversarial Patches for World Action Models

**Authors:** Xuanyu Lu, Fengqing Jiang, Kaiyuan Zheng, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06814v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06814v1)

**Summary:** World models learn to predict how their environment will evolve, making them an important foundation for general-purpose robotic control. Yet world action models depend on camera inputs whose manipulation can corrupt the visual representations used across tasks and action policies. Existing attacks on these models optimize against the victim's actions or predicted futures and therefore require access to target-model outputs. In this paper, we propose an attack, TAPDreamer, against world action m...

---

### 13. Sharpen Without Search: On-Policy Distillation of Sequence-Level Power Distribution

**Authors:** Erfan Baghaei Potraghloo, Seyedarmin Azizi, Arya Fayyazi, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06804v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06804v1)

**Summary:** A language model can give a correct answer more probability than any single incorrect answer and still usually sample an incorrect one, because the incorrect answers together hold more probability. The power distribution raises each complete answer's probability to a power above one and renormalizes, shifting probability toward answers the model finds most likely (sharpening). Sampling from it improves reasoning without changing parameters, but needs many scored candidates per query. We show tha...

---

### 14. MC-Sparse: Deconstructing and Closing the Dense-Sparse Attention Gap in Diffusion Transformers

**Authors:** Jiarui Chen, Zeqiang Lai, Jiangshan Wang, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06801v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06801v1)

**Summary:** Sparse attention is a primary approach to reducing the latency of diffusion transformers in long-sequence generation tasks, such as video and high-resolution 3D asset generation. However, existing methods can degrade generation quality and fidelity at high sparsity levels. Through controlled oracle comparisons, we trace this degradation to three sources: constraints imposed by token grouping, inaccurate interaction selection, and the attention contributions lost when tokens are discarded. Guided...

---

### 15. Back to the Future: Rethinking EDA Infrastructure for Agentic Systems in Chip Design Verification

**Authors:** Je Yang, Ivan Lobov, Thomas Karpati

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06790v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06790v1)

**Summary:** The unprecedented computational scale of modern artificial intelligence depends on complex, multi-billion-transistor Systems-on-Chip, yet the workflows that verify these chips remain stubbornly manual. Although Large Language Models (LLMs) have made rapid inroads into Electronic Design Automation (EDA), approximately 74.6% of existing studies target static Register-Transfer Level (RTL) code generation, leaving post-simulation verification and interactive waveform debugging largely untouched. We ...

---

### 16. IdeaLens: Detecting AI Ideas in Long-form Writing

**Authors:** Rishanth Rajendhran, Minjoon Choi, Jenna Russell, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06778v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06778v1)

**Summary:** While modern AI detectors identify who wrote the words, emerging policies on AI use increasingly hinge on a different question: who came up with the ideas? We introduce IdeaLens, a detector that identifies whether a document's ideas came from a human or AI (idea provenance), regardless of who wrote its words. To focus IdeaLens on ideas rather than prose, we represent documents as outlines: lists of items that each pair a discourse role with a brief, paraphrased description of the content, minimi...

---

### 17. Conditional Rank Allocation for Taxonomy-Aware Medical Language Model Adaptation

**Authors:** Guangyuan Dong, Ziwei Hong, Xuehao Zhou, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06765v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06765v1)

**Summary:** Medical question answering spans specialties and clinical operations that may benefit from different adaptation directions. We propose ARBOR, a parameter-efficient method that selects rank-one components from a shared low-rank basis for each question. An additive gate combines question representations, specialty tags, operation tags, and their interaction; a learned coefficient scales the adapter residual. An illustrative separation under orthogonal, equiprobable subtasks shows how conditional s...

---

### 18. MatrixFormer: A Foundation Model for Matrix Completion

**Authors:** Dwaipayan Saha, Jacob Feitelberg, Kyuseong Choi, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06751v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06751v1)

**Summary:** Matrix completion underlies problems from tabular imputation to causal inference, yet existing tabular foundation models treat it as entry-by-entry prediction, repeating context for every target and discarding the matrix's two-dimensional structure. We introduce MatrixFormer, a pre-trained matrix-native transformer that predicts a full distribution for every missing entry in a single forward pass. MatrixFormer is trained entirely on synthetic low-rank and latent-factor matrices under diverse mis...

---

### 19. Balancing Memory Pathways: Analyzing and Improving Memory Utilization in Hybrid LMs

**Authors:** Hyunji Lee, Joykirat Singh, Zaid Khan, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06750v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06750v1)

**Summary:** Recurrent-attention hybrid language models (LMs), which interleave attention and recurrent layers, are increasingly used to combine the efficiency of the recurrent layers with the strong performance of attention layers. Prior work suggests that attention and recurrent layers offer complementary pathways to use past information: attention supports precise memory recall from earlier tokens, while recurrent layers support consolidation of disparate information over long contexts. However, we observ...

---

### 20. BazaarBench: Delegation Safety in Decentralized C2C Marketplaces Run by LLM Agents

**Authors:** Ziyan Wang, Shuqing Shi, James Oldfield, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06748v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06748v1)

**Summary:** In decentralized consumer-to-consumer (C2C) marketplaces, people list goods, negotiate with strangers, and rate one another, so trust rests on reputation. Large language model (LLM) agents now act for users, raising risks to their money, privacy, and reputation. We introduce BazaarBench, a simulated C2C marketplace and benchmark for evaluating the safety of these agents. It tracks ownership, item condition, and commitments across transactions, combining record checks with rubric-based LLM judgme...

---

### 21. BRANCH-MoE: Balance-Aware Tree Routing for Large Embedding Models

**Authors:** Gang Fu, Adel Javanmard, MohammadHossein Bateni, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06725v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06725v1)

**Summary:** Mixture-of-experts (MoE) layers increase model capacity without a proportional increase in per-example computation. However, conventional flat routers can yield imbalanced expert utilization and treat experts as an unstructured collection, whose indices carry no topological meaning. We introduce {\bf BRANCH-MoE}, a routing architecture that places \(E\) experts at the leaves of a binary decision tree of depth \(\log_2 E\). At each internal node the branching probability is centered on the arriva...

---

### 22. Closing the Context Gap: Activation Alignment for Tabular In-Context Learning

**Authors:** Yoel Zeldes

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06679v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06679v1)

**Summary:** Tabular foundation models perform in-context learning (ICL) by conditioning predictions on labeled training examples provided as context. Unlike traditional models that separate training from inference, these models must process all training examples in every forward pass, making each prediction expensive. Restricting the number of training examples reduces this cost but substantially degrades performance. Instead of discarding context, we propose activation alignment, a method that leverages th...

---

### 23. The Pushback Paradox: A Two-Probe Diagnostic for Language Model Compliance

**Authors:** Stefan Bühler, David Exler, Markus Reischl, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06673v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06673v1)

**Summary:** Are language models compliant with user instructions? A model that always complies can be stopped but also exploited, while one that always resists can be neither exploited nor stopped. We contribute an open two-probe benchmark that can place any language model on this spectrum. In the active probe, a user instructs the model to act and accept a lower payoff, which measures exploitability. In the passive probe, the user instructs it to wait and give up a higher payoff, which measures stoppabilit...

---

### 24. VideoTapestry: Query-Adaptive Memory Refinement for Multi-Agent Long-Video Understanding

**Authors:** Yucheng Liu, Yufei Yin, Mingxiao Feng, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06672v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06672v1)

**Summary:** Long-video understanding places substantial demands on memory, as answering questions often requires retrieving information distributed across extended temporal spans. Existing approaches broadly follow two paradigms: query-driven exploration, which is sensitive to localization errors, and query-independent memory construction, which may omit question-specific details. We introduce VideoTapestry, a training-free multi-agent framework that adapts a preconstructed hierarchical video memory through...

---

### 25. Language models can notice an impossible engineering problem yet still report it as solved

**Authors:** Shaoliang Yang, Jun Wang

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06668v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06668v1)

**Summary:** Language models draft engineering calculations, but answer accuracy does not show whether they reject an impossible problem. We tested 14 models on 30 pairs of mechanics problems, each with a valid version and one made impossible by changing a given value or assumption. Two independent solvers verified every answer key and showed that each flawed problem was physically impossible. We scored solving of valid problems separately from rejection of their flawed counterparts. Each reply required a "s...

---

### 26. Collective intelligence through aggregation

**Authors:** Franz Dietrich, Christian List

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06652v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06652v1)

**Summary:** Suppose a committee, expert panel, or other group is making judgments on some issues, where these may be not just yes/no-questions, such as whether a defendant is guilty, but also variables with many possible values, such as macroeconomic or meteorological variables or travel directions. Furthermore, there may be interconnections between different issues, as in the case of economic or climate variables. How can the group arrive at "intelligent" collective judgments, based on the group members' i...

---

### 27. AffordCraft: Scalable Construction of Task-Ready Simulation Assets from Single Images

**Authors:** Haoyun Yang, Xueyang Zhou, Ziyi Xie, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06643v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06643v1)

**Summary:** Robot learning in simulation depends on the objects the simulator offers. Many tasks need objects with separate parts, joints that allow the required motion, and physical properties that remain valid under contact. Existing methods recover this structure anew for every image: generative models predict parts and joints that mostly fail to settle or move in simulation, and general-purpose agents need a long session of model calls for each photograph. AffordCraft builds such an asset from a single ...

---

### 28. Differentially Private Mixing of Public Datasets Improves Private Learning

**Authors:** Yufei Chen, Tejumade Afonja, Anvith Thudi, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06636v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06636v1)

**Summary:** Many machine learning applications involve sensitive data and therefore require training under differential privacy (DP). However, DP training often degrades model utility. In some cases, first pre-training the model on "public" data before finetuning with DP on the sensitive data can reduce the drop in utility. However, the success of this depends on how relevant the selected public dataset is to the sensitive data. We introduce the first pipeline that privately learns the mixture of several pu...

---

### 29. Large Language Model-Guided Discovery of Weight-Five Bivariate Bicycle Codes

**Authors:** Juan Cruz-Benito

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06623v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06623v1)

**Summary:** Building on our earlier program-evolution workflow guided by large language models (LLMs), we study weight-five bivariate bicycle (BB) and perturbed bivariate bicycle (PBB) codes. The resulting catalogue contains 1,142 distinct code proposals, including 1,081 nonbaseline proposals attributable to LLM-generated programs. Across the catalogue, we certify connected Calderbank--Shor--Steane (CSS) realizations [[96,4,10]], [[140,6,10]], and [[180,4,14]]. A post-search comparison certifies seven impor...

---

### 30. Frozen Factor or Spectral Band? Disentangling Two Choices in Low-Rank LoRA

**Authors:** Adnan Slimane Ali, Ayoub Belfatmi, David Ngwe Pouth

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06621v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06621v1)

**Summary:** Spectral variants of low-rank adaptation (LoRA) choose both a subspace and which factor to freeze. We separate these choices by freezing the input factor A or output factor B on the top or bottom singular directions of pretrained weights, with learning rates selected separately. At rank 2, the same-band advantage of freezing A is larger than either within-factor band difference on all four task-model pairs with complete comparisons. Freezing B also trails comparable-budget free LoRA by 8-18 perc...

---

### 31. FREA: A Multi-Source Expert Benchmark for Reaction Feasibility Verification

**Authors:** Botao Yu, Bo Zhou, Daniel Adu-Ampratwum, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06614v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06614v1)

**Summary:** As generative models and AI agents propose chemical reactions at a scale beyond expert review, feasibility verifiers decide which proposals enter synthesis planning. But do their decisions agree with chemists across different kinds of candidates? We introduce FREA, a benchmark of 751 reactions labeled by expert chemists under an explicit feasibility criterion, drawn from retrosynthesis model proposals, zero-yield experimental records, edits by large language models (LLMs), and five negative cand...

---

### 32. Word-Level Text Unmixing via Evidence-Preserving Ownership Routing with Language Models

**Authors:** Jinglin He, Siyang Jiang, Lixing He, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06603v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06603v1)

**Summary:** Text from multiple sources can become interleaved into a single sequence when attribution metadata is lost, such as overlapping speech transcripts, document reading flows, or concurrent agent streams. We formalize this challenge as Word-Level Text Unmixing: given an interleaved lexical stream and source count K, recover the original source sequences while preserving every word occurrence and its within-source order exactly. Directly generating separated texts with LLMs can omit, duplicate, or ha...

---

### 33. SimForcing: Distilling Simulation Motion Priors into Real-Domain Robot World Models

**Authors:** Xiaodong Wang, Tianle Li, Chuanxin Song, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06598v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06598v1)

**Summary:** Action-conditioned robot world models must respond precisely to robot trajectories while preserving realistic visual dynamics, yet learning both from heterogeneous robot videos remains challenging. Simulation offers structured motion supervision, but appearance differences hinder direct transfer, and inaccurate simulation predictions can misguide real-video generation. We present SimForcing, a simulation-guided framework that uses simulation both as a source of transferable motion knowledge and ...

---

### 34. Can Agent Harnesses and Inference Engines Hear Each Other? The HEAR Protocol for Agentic LLM Serving

**Authors:** Jiaqi Zhao, Haodong Chen, Jitai Hao, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06597v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06597v1)

**Summary:** LLM agents increasingly execute complex workflows involving multi-turn reasoning, tool use, and parallel agents. Efficient serving requires decisions that span two layers with complementary information: the agent harness understands workflow dependencies, context lifecycles, and execution objectives, whereas the inference engine observes request queues, KV-cache state, resource pressure, and execution capabilities. Existing interfaces do not systematically connect these views, limiting workflow-...

---

### 35. The Review Lottery: Calibrating an Observational Estimator of Peer-Review Noise (ICLR 2017-2025)

**Authors:** Feilian Huang

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06591v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06591v1)

**Summary:** How much of a conference accept/reject decision would change if the same paper were reviewed by a different set of reviewers? Running a second independent program committee is the gold standard for answering this, but it is prohibitively expensive: done only twice (NeurIPS 2014 and 2021). We build an observational estimator of this quantity from public review data alone, calibrate it twice, and apply it to nine years of ICLR (2017-2025; 36,113 papers, 134,912 reviews). The estimator decomposes s...

---

### 36. Mind the Accent Gap: British Accent Robustness in Speech-Driven Financial Voice Assistants

**Authors:** Aadam Haq, Oggi Rudovic, Malcolm Chadwick, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06587v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06587v1)

**Summary:** AI voice assistants often use Automatic Speech Recognition (ASR) with LLM-based reasoning, yet existing systems struggle with regional British accents, including Scottish, Irish, and Welsh accents, since most ASR models are trained predominantly on American English voice data. Consequently, errors can carry through to the LLM stage, corrupting tool-call arguments and producing wrong or missing responses, which is especially costly in finance. Deployable ASR must also meet tight latency and memor...

---

### 37. Does AI Help Cyber Attackers or Defenders? Evidence from Nonpublic Vulnerabilities and Subsequent Attacks

**Authors:** Tobias Heldt, Matt Turk, Christoph Landolt, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06584v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06584v1)

**Summary:** The release decision for frontier AI systems increasingly relies on cyber capability benchmarks, yet public vulnerability benchmarks can expose agents to previously published advisories, exploits, and fixes, making it difficult to distinguish prior exposure from capability on unseen vulnerabilities. We evaluate open-weight and proprietary AI models on exploit generation, vulnerability repair and subsequent attacks in five nonpublic software environments, including vulnerabilities we privately di...

---

### 38. Mind the Execution Gap: Action-Semantic Mismatch in World-Model Control

**Authors:** Shengtao Wen, Xiang Chen, Yu Tian, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06582v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06582v1)

**Summary:** World-model controllers rely on action-conditioned dynamics for prediction and planning, yet real control systems often execute commands asynchronously due to communication delay, packet loss, reordering, and actuator buffering. We study how asynchronous execution changes the action semantics assumed within world-model controllers, rather than treating it only as an external control disturbance. Through controlled interventions, we identify two architecture-dependent failure modes: planning-base...

---

### 39. DGA-Muon: Decoupled Geometry-Aligned Adaptive Scaling for Muon

**Authors:** Wenpeng Zhang, Runsheng Yu

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06578v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06578v1)

**Summary:** While NorMuon has achieved strong empirical performance in large-scale pretraining by enhancing Muon with row-wise adaptive scaling, its underlying adaptive mechanism remains poorly understood. In this work, we provide the first systematic analysis of NorMuon's adaptivity, revealing that it originates primarily from orthogonalization-induced geometry rather than genuine optimization-relevant information. Under exact orthogonalization, the adaptive scaling factors degenerate into a single global ...

---

### 40. BrainTRACE: Tracing Longitudinal, Multimodal, and Volumetric Evidence in Brain MRI Clinical Reasoning

**Authors:** Qizhen Lan, Mengchen Fan, Hang Zhang, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06571v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06571v1)

**Summary:** Brain MRI interpretation is a longitudinal clinical reasoning problem: radiologists compare serial studies, integrate information across MRI sequences, localize findings within volumetric anatomy, and translate this evidence into report-grounded assessments. Existing medical VQA and 3D imaging benchmarks capture important parts of this workflow, but often evaluate brain MRI through isolated images, static volumes, or ungrounded report-style answers, thereby obscuring failures in the evidence cha...

---

### 41. HERA: Harness-Environment Co-Evolution for Reliable Agentic Abstention

**Authors:** Han Luo, Bingbing Wen, Guang Yang, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06563v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06563v1)

**Summary:** Large language model (LLM) agents are increasingly capable of acting in complex tool-use environments, yet they often fail to recognize when tasks are infeasible and no valid solution exists. Recent work has formalized this reliability gap as the problem of agentic abstention, and existing approaches typically optimize a model or agent harness against a fixed set of tasks, leading to limited generalization to unseen failure modes. We introduce HERA, a framework for harness-environment co-evoluti...

---

### 42. Signature-Based Feature Learning for Human Activity Recognition: A Reproducible Machine Learning Study of Representation, Depth, and Model Choice

**Authors:** Kamal Jarrar, Jacky Cresson, Christian Paroissin

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06553v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06553v1)

**Summary:** Human activity recognition (HAR) relies on transforming sensor signals into informative representations for classification. Although deep learning and handcrafted features are widely used, the role of representation itself is often not systematically isolated. Signature transforms provide a mathematically grounded way to encode temporal order and cross-channel interactions, but their value for HAR under a fully reproducible and leakage-aware framework remains unclear. To evaluate whether signatu...

---

### 43. Proof-Grounded Patient-Specific Clinical Explanations from Knowledge-Graph Reasoning

**Authors:** Surajit Das

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06549v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06549v1)

**Summary:** Clinical decision-support outputs can lack an au- ditable link between patient observations, encoded knowledge, conclusions, and recommendations. We present the CKG Clinical Explanation Engine, a downstream layer for a frozen, training-free clinical knowledge-graph reasoner that converts patient inference states and disease knowledge into typed facts, explicit rule-application traces, provenance-linked conclusions, and policy-licensed recommendations. The design separates measurement availabilit...

---

### 44. Symmetry and AI-assisted discovery of magic-state factories

**Authors:** Shubham P. Jain, Adam Wills, Shraddha Singh

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06535v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06535v1)

**Summary:** Magic-state distillation is a major resource cost in fault-tolerant quantum computing. The cost of a magic-state factory depends strongly on its failure rate, which grows with the number of input magic states. Although symmetry-restricted methods have recently made distance two searches tractable, distance three and above have remained elusive at moderate input counts. We develop symmetry- and AI-assisted methods to search this regime. We present a unified binary-matrix formulation encompassing ...

---

### 45. Anatomy of LLM Sycophancy: What a Flip Rate Hides

**Authors:** Haonan Huang

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06522v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06522v1)

**Summary:** A model under pushback can correct itself, capitulate, or hold, and one flip rate counts a correction and a capitulation alike. Using SycoLens, a modular replay protocol, we test how user pressure and evaluation settings shape measured flip rates. Each measurement is one stateless replay of an item, a committed answer, and one scripted user line in a fixed form. Every effect is read against a matched control with the line deleted. Pushback wording, committed text, answer format, boundary distanc...

---

### 46. GCTAuto-encoder: A Cross modal Framework for Security Flaw Detection in IoT Networks

**Authors:** Najmieh Sadat Safarabadi

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06517v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06517v1)

**Summary:** IoT encompasses diverse physical entities, from smart home devices to autonomous vehicles, creating a complex environment with heterogeneous security models. This heterogeneity makes IoT sub-systems vulnerable to various network attacks. Modern security systems must therefore be more robust to ensure security and privacy for IoT applications. A highly secure IoT system also demands real time insight, requiring data collection at the edge of the computing layer. This diversity calls for a unified...

---

### 47. ANT: A Multi-Granularity Network Traffic Dataset and Benchmark for Agents Behavior Auditing

**Authors:** Fan Li, Xiangyu Gao, Zixuan Liu, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06514v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06514v1)

**Summary:** The growing adoption of large language model (LLM) agents creates a need for network administrators and security teams to audit agent behavior within organizational networks without inspecting private user content. Network traffic offers an observable source of evidence, but how much it reveals about agent tasks and operations remains unclear. Existing traffic datasets lack the joint task and stage annotations needed to evaluate this question. We introduce ANT (Agent Network Traffic), a dataset ...

---

### 48. ArtifactArena: Evaluating Models by What They Build in the Physical World

**Authors:** Kushagra Tiwary*, David Mayo*, Nikhil Behari, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06511v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06511v1)

**Summary:** To evaluate the frontier, we must measure models not by what they say, but by what they can engineer and build in grounded physical environments. We introduce \textsc{ArtifactArena}, an open-ended platform where models face a physically grounded hardware-software co-design challenge: engineering fully functional robots to compete in a simulated arena. We evaluate a frontier model's zero-shot, verifier guided refinement, and open-ended physical design capabilities through three harnesses that ref...

---

### 49. Harmful Content Generation in Text-to-Image Models: Capabilities and Moderation Limitations

**Authors:** Paschalis Giakoumoglou, Manos Schinas, Symeon Papadopoulos

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06503v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06503v1)

**Summary:** Text-to-image generative models can produce highly realistic imagery but also raise concerns about harmful misuse. While safety mechanisms exist, systematic evaluations of their effectiveness against realistic attacks remain limited. We present a systematic evaluation of harmful content generation across five open text-to-image models using an automated pipeline that transforms legitimate news captions into unsafe prompts targeting sexually explicit content, violence/gore, harmful stereotypes, s...

---

### 50. You Changed Your Mind, The Model Didn't: Demystifying Intent in Multi-Turn Dialogue

**Authors:** Junle Chen, Wei Chen, Zhengjun Huang, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06496v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06496v1)

**Summary:** When a large language model handles a multi-turn task and a user proposes a change but ultimately rejects it, the model should continue as if nothing changed. We find a surprising failure: merely mentioning a rejected change can derail task execution, even when the user's final intent remains unchanged. To systematically study language model behavior under evolving user intent, we introduce Intent-Eval, a controlled benchmark spanning tool actions, code, databases, and mathematics. Across divers...

---

## cs.CL

**50 papers**

### 1. Base Models Can Reason By Taking a Cue From Training Data

**Authors:** Sophie L. Wang, Amil Dravid, Rulin Shao, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06851v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06851v1)

**Summary:** In this paper, we study how training data creates associations between the tokens at the start of a base model's response and the reasoning behavior that follows. First, we demonstrate that fixing particular starting token cues makes a base model's performance competitive with that of its reinforcement learning (RL)-trained counterparts on math and coding. For instance, the cue ".\n\nOkay" raises Olmo-3-7B's MATH-500 pass@1 accuracy from 42% to 78%, while "Alright," raises Qwen3-14B's from 72% t...

---

### 2. Recursive Video In-Context Learning for Agentic Robot

**Authors:** Wenrui Bao, Xinxin Liu, Bingxin Xu, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06843v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06843v1)

**Summary:** LLM agents that orchestrate frozen vision-language-action (VLA) policies improve across episodes through text memory, which records what the agent did but not how the task is done. A demonstration video shows it, but fits poorly into an agent's context. The full video slows every turn, fixed keyframes lose the contact detail that decides whether a grasp holds, and what the agent needs shifts from the task's structure while planning to the frames around each contact. We introduce Recursive Video ...

---

### 3. MemPilot: Orchestrating On-Demand Multimodal Memory Curation for LLM Agents

**Authors:** Haozhen Zhang, Haodong Yue, Quanyu Long, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06830v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06830v1)

**Summary:** Memory has become integral to the LLM agent ecosystem, supporting information retention and reuse across interactions. However, most existing agent memory systems construct memory in a query-agnostic manner, which can incur unnecessary preprocessing cost and discard details that later prove essential. Recent studies have begun shifting memory processing toward runtime adaptation, but typically specialize in particular operations or fixed processing schemes, leaving flexible control over performa...

---

### 4. CLIFT: Conformal Self-Verification for Web Agent Training and Test-Time Scaling

**Authors:** Yifan Zhang, Yutong Dai, Viraj Prabhu, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06829v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06829v1)

**Summary:** Open-source web agents are now strong enough to execute realistic browser tasks, but training them with reinforcement learning still depends on weak supervision: binary task success is too sparse for credit assignment, while frontier-language-model judges are too expensive to call at every step and cannot be assumed available at deployment. We introduce CLIFT, a training and test-time scaling method built around conformal self-verification. During training, the agent answers natural-language ver...

---

### 5. PlotGround: Grounding Plot Digitization in Real Scientific Figures and Their Source Data

**Authors:** Yaohui Zhang, Binxu Li, Haoyi Duan, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06825v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06825v1)

**Summary:** Scientific figures often encode quantitative results that are not readily available in machine-readable form, making accurate plot digitization important for verifying and reusing published findings. Yet it remains unclear how accurately current models recover plotted values from real scientific figures, as existing benchmarks rely largely on synthetic charts or cover only a limited range of chart types. We introduce PlotGround, an automated pipeline for building plot digitization benchmarks fro...

---

### 6. Paradee: Distilling Kokoro-82M into an 8M-Parameter Single-Voice Text-to-Speech Model

**Authors:** Sahil Mahendrakar

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06817v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06817v1)

**Summary:** We distill Kokoro-82M, a widely used open text-to-speech model with 54 voices, into Paradee, an 8.07M-parameter model that speaks one of them. Paradee keeps Kokoro's architecture with much narrower layers, and each of its two halves is trained separately against the frozen teacher. It has 10x fewer parameters and needs 15x less compute. We first synthesize a corpus with the teacher and keep its durations, pitch, energy and phoneme features. We then train a small text side to predict these values...

---

### 7. T-Search: An Open Agentic Retriever and Playground for Hard Multi-Step Search

**Authors:** Olga Tsymboi, Ramil Latypov, Aleksandr Medvedev, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06782v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06782v1)

**Summary:** We present T-Search, an open-weight agentic retriever for hard multi-step search. Given a question and a search tool over a fixed corpus, it runs a bounded multi-round search and returns a ranked list of evidence chunks with short justifications, leaving answer generation to a downstream model, so backend and generator can be swapped without retraining. T-Search is built on Qwen3.6-35B-A3B and trained on adversarially filtered synthetic search tasks with round-sliced supervised fine-tuning follo...

---

### 8. IdeaLens: Detecting AI Ideas in Long-form Writing

**Authors:** Rishanth Rajendhran, Minjoon Choi, Jenna Russell, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06778v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06778v1)

**Summary:** While modern AI detectors identify who wrote the words, emerging policies on AI use increasingly hinge on a different question: who came up with the ideas? We introduce IdeaLens, a detector that identifies whether a document's ideas came from a human or AI (idea provenance), regardless of who wrote its words. To focus IdeaLens on ideas rather than prose, we represent documents as outlines: lists of items that each pair a discourse role with a brief, paraphrased description of the content, minimi...

---

### 9. Balancing Memory Pathways: Analyzing and Improving Memory Utilization in Hybrid LMs

**Authors:** Hyunji Lee, Joykirat Singh, Zaid Khan, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06750v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06750v1)

**Summary:** Recurrent-attention hybrid language models (LMs), which interleave attention and recurrent layers, are increasingly used to combine the efficiency of the recurrent layers with the strong performance of attention layers. Prior work suggests that attention and recurrent layers offer complementary pathways to use past information: attention supports precise memory recall from earlier tokens, while recurrent layers support consolidation of disparate information over long contexts. However, we observ...

---

### 10. ufakzeka-karar: An Open Turkish Typed-Decision Model with Order-Invariant Option Scoring

**Authors:** Sait Furkan Teke

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06744v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06744v1)

**Summary:** ufakzeka-karar is an open Turkish decision model with 182,494,466 parameters. Given a Turkish text and questions of a fixed answer type (a choice, a level on an ordered scale, or yes or no), it returns a temperature-scaled probability for every option and an expected error that serves as a "not sure" signal, without generating text and in one CPU forward pass for up to ten options. Built on the lab's ufakzeka-1-base, its head scores each option blind to the others at shared positions, so the ans...

---

### 11. Improving Diversity in LLM Short Story Generation

**Authors:** Zahra Solati Dehkordi, Vasileios Lampos

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06729v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06729v1)

**Summary:** Large language models (LLMs) can generate accurate responses, but these are void of diversity. We attempt to address this for the task of creative short story generation. Drawing on established writing conventions and known LLM limitations, we target variation in genre, tone, style, and named entities. To promote diversity across these dimensions, we introduce DivLM, an LLM post-training framework consisting of two phases. First, we perform continued pre-training on a creative writing corpus and...

---

### 12. Domain adaptation of Russian ModernBERT for long legal documents

**Authors:** I. Litvak, D. Gvozdetsky, F. Lashkin, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06715v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06715v1)

**Summary:** We investigate whether continued pretraining on Russian legislative documents improves a Russian ModernBERT encoder on legal text. The adapted model, RuModernBERT-ruLaw, was trained on a corpus reported to contain 304,382 legislative documents and 194,425,905 corpus tokens. Corpus token counts are distinguished from positions produced by the model tokenizer. We compare the original and adapted encoders on a fixed external collection of 1,031 court-decision segments. Both models receive the same ...

---

### 13. SAFE-MR: Evidence Sufficiency Learning for Selective Multimodal Rumor Detection

**Authors:** Shiwen Ni

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06708v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06708v1)

**Summary:** Multimodal rumor detectors increasingly rely on retrieved evidence, yet relevant evidence is not necessarily sufficient for verification. Missing provenance, duplicated reports, and unresolved contradictions can produce confident predictions without adequate support. We introduce SAFE-MR, a framework that separates claim veracity from evidence sufficiency. The method decomposes image-text posts into verifiable claims, constructs a relation-aware claim-evidence graph, and aggregates evidence usin...

---

### 14. Reading the Mood: Emotion-Guided Book-to-Music Recommendation via CGANs and LLMs

**Authors:** Manousos Linardakis, Georgios Alexandridis

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06703v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06703v1)

**Summary:** Background music that matches the mood of a text has been shown to make readers feel more immersed and improve their reading experience, motivating recommender systems that pair books with mood-matched music. In this direction, we present Sentiment Aware Generative Adversarial Network for Cross Domain Recommendation (SAGA-CDR), a two-phase cross-domain recommendation framework that personalizes music suggestions and emotionally aligns them with the book being read. In the first phase, transforme...

---

### 15. MedPrune: Topology-Efficient Multimodal Multi-Agent Communication Evolution for Medical VQA Tasks

**Authors:** Jiuheng Wan, Runze Li, Chen Chen, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06695v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06695v1)

**Summary:** While medical multimodal large language models (Med-MLLMs) advance medical visual question answering (VQA), existing clinical workflow-inspired multi-agent frameworks suffer from interaction patterns and excessive computational overhead caused by redundant communication topologies. In this paper, we propose MedPrune, an efficient medical multimodal multi-agent collaboration framework that dynamically prunes both nodes and edges from the communication topology to enhance reasoning ability and tok...

---

### 16. Programmatic Search Agents: Extending Agentic Search Beyond Query Reformulation

**Authors:** Jiaming Qian, Huiyan Yang, Mandi Liu, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06689v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06689v1)

**Summary:** Search agents adapt their queries, yet fixed search interfaces leave candidate processing and evidence presentation outside the agent's direct control. Our trajectory analysis shows that supporting passages can be retrieved yet never delivered to the agent; a same-page oracle intervention shows that changing the returned evidence can reduce subsequent search. We introduce Programmatic Search Agent (PSA), which makes a local executable computation over candidates the unit of a search action. PSA ...

---

### 17. Aligning Multimodal Patient Evidence with Biomedical Knowledge Graphs for Clinical LLMs

**Authors:** Jiawen Du, Arshan Ali Khan, Chenhao Zhang, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06685v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06685v1)

**Summary:** Clinical questions often depend on linking a patient's multimodal evidence to external biomedical knowledge, yet existing predictive systems rarely represent such links explicitly, so they can neither be traced to their evidence sources nor removed to measure their contributions. We present MM-KG (Multimodal Knowledge Graph), which represents heterogeneous, multimodal patient observations and biomedical concepts as separate layers in one typed graph, joined by explicit alignment edges. First, mo...

---

### 18. How Sparse Probability Maps Shape Mixture-of-Experts Routing

**Authors:** Tomás Brogueira, Marcos Treviso, Miguel Couceiro

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06677v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06677v1)

**Summary:** Mixture-of-experts (MoE) routers typically apply softmax to the router scores and keep the top-K experts, making every token use exactly K experts. Sparsity-inducing probability maps such as sparsemax, alpha-entmax and normmax can adaptively assign exact zeros to selected experts, and therefore appear to offer token-dependent expert participation, even when using the same top-K machinery. In this work, we study whether and how this sparsity survives training. We train matched 300M and 1B top-2 M...

---

### 19. The Pushback Paradox: A Two-Probe Diagnostic for Language Model Compliance

**Authors:** Stefan Bühler, David Exler, Markus Reischl, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06673v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06673v1)

**Summary:** Are language models compliant with user instructions? A model that always complies can be stopped but also exploited, while one that always resists can be neither exploited nor stopped. We contribute an open two-probe benchmark that can place any language model on this spectrum. In the active probe, a user instructs the model to act and accept a lower payoff, which measures exploitability. In the passive probe, the user instructs it to wait and give up a higher payoff, which measures stoppabilit...

---

### 20. Reward Stealing Attack on Large Language Models

**Authors:** Jiaming Qian, Pengyang Zhou, Jiahe Xu, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06670v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06670v1)

**Summary:** Adversarial attacks on Large Language Models (LLMs) aim to induce harmful content. However, existing methods suffer from high computational costs or strict model-pairing dependencies, limiting their scalability and transferability. We propose Reward Stealing Attack (ReSA), an adversarial attack framework that targets the latent safety reward underlying LLM alignment. ReSA employs maximum entropy inverse reinforcement learning to recover a proxy reward model solely from the aligned model's behavi...

---

### 21. Language models can notice an impossible engineering problem yet still report it as solved

**Authors:** Shaoliang Yang, Jun Wang

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06668v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06668v1)

**Summary:** Language models draft engineering calculations, but answer accuracy does not show whether they reject an impossible problem. We tested 14 models on 30 pairs of mechanics problems, each with a valid version and one made impossible by changing a given value or assumption. Two independent solvers verified every answer key and showed that each flawed problem was physically impossible. We scored solving of valid problems separately from rejection of their flawed counterparts. Each reply required a "s...

---

### 22. What Matters for Latent Reasoning with Flow Matching

**Authors:** Yassine Ouali, Adrian Bulat, Georgios Tzimiropoulos

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06666v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06666v1)

**Summary:** Latent reasoning lets a large language model (LLM) think in a continuous space and verbalize only the answer. We argue that an effective latent thought must meet five requirements: it should be useful, helping produce the correct answer rather than merely changing it, diverse, so that resampling yields different reasoning trajectories, explainable, so that a decoded chain of thought (CoT) reflects reasoning the answer actually follows, refinable with more inference compute, and efficient, costin...

---

### 23. Wikidata Search Traces: A Dataset for Training Knowledge Graph Search Agents

**Authors:** Mohamed Chenene, Carlos Rosas-Hinostroza, Pierre-Carl Langlais, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06650v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06650v1)

**Summary:** Wikidata is one of the largest open knowledge bases, yet answering a complex question over it still requires a SPARQL query that names the right entities and properties and chains their relations. Language models offer a natural-language alternative but answer largely from memory, which is least reliable for less prominent entities. We study agents that instead answer by exploring the graph, and argue that two obstacles limit them: the lack of training data recording how a solver explores, and i...

---

### 24. Representation-Space MMD for Diffusion Language Models

**Authors:** Ilya Drobyshevskiy, Ilia Sudakov, Maksim Semenov, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06648v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06648v1)

**Summary:** We introduce a post-training method for diffusion language models (DLMs) that minimizes Maximum Mean Discrepancy (MMD) between generated and reference distributions in the feature space of a frozen pretrained DLM. To estimate MMD, we retain contextual features at individual token positions, obtaining multiple observations per sequence from a single extractor pass. We optimize this objective using policy gradients for discrete models and direct differentiation through generated latents for contin...

---

### 25. LoGRA: Scaling LLM Reinforcement Learning with Low-Rank Gradient Sketches

**Authors:** Shaokun Zhang, Yifan Zhang, Jian Hu, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06647v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06647v1)

**Summary:** Reinforcement learning (RL) has greatly advanced the capabilities of large language models (LLMs), but its memory demands remain a barrier to broader adoption. We introduce LoGRA, an approach to RL post-training that reduces memory by retaining useful learning signals in low-rank gradient sketches. These compact representations support both model updates and efficient policy synchronization. To prevent overly large updates from disrupting learning, we complement gradient compression with predict...

---

### 26. Long-Horizon Textual World Modeling through Structured Reasoning

**Authors:** Fangxin Wang, Xiang Gao, Yuguang Yao, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06637v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06637v1)

**Summary:** World models must predict how an environment evolves under sequences of actions, enabling agents to compare possible futures and reason about counterfactual actions before acting. Long-horizon prediction is commonly obtained by recursively applying a one-step transition model, but intermediate errors can compound over time. Multi-step dynamics models instead condition on a sequence of future actions and predict their consequences directly, but become harder to learn as horizon grows: the model m...

---

### 27. JEV versus LLMs: Accuracy, Cost and Calibration on Seven Political Science Replications

**Authors:** Matthew DiGiuseppe, Steven Denney

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06625v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06625v1)

**Summary:** Large language models (LLMs) annotate and scale political text or constructs by generating text tokens. A new class of models, which TypeSafe markets as "System One" models, instead returns decisions and probability distributions across a user-supplied fixed answer set. A commercial model, JEV, is advertised as having a dramatic cost and speed advantage over traditional LLMs along with better calibrated decisions. As such, it might be useful for social scientists looking to quickly and cost-effe...

---

### 28. Frozen Factor or Spectral Band? Disentangling Two Choices in Low-Rank LoRA

**Authors:** Adnan Slimane Ali, Ayoub Belfatmi, David Ngwe Pouth

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06621v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06621v1)

**Summary:** Spectral variants of low-rank adaptation (LoRA) choose both a subspace and which factor to freeze. We separate these choices by freezing the input factor A or output factor B on the top or bottom singular directions of pretrained weights, with learning rates selected separately. At rank 2, the same-band advantage of freezing A is larger than either within-factor band difference on all four task-model pairs with complete comparisons. Freezing B also trails comparable-budget free LoRA by 8-18 perc...

---

### 29. COMPASS 2.0: psychometric representational similarity analysis distinguishes symptom structure from personal signal

**Authors:** Baihan Lin

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06615v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06615v1)

**Summary:** Language models can score psychiatric questionnaires from speech, but agreement with self-report may reflect the questionnaire rather than the person. We introduce psychometric representational similarity analysis, a framework for comparing the structure of speech-derived scores, self-report, item wording and theory, and implement it alongside person-level construct scoring in COMPASS 2.0. We show how similarly worded items induce covariance without psychological signal. In pre-registered discov...

---

### 30. Word-Level Text Unmixing via Evidence-Preserving Ownership Routing with Language Models

**Authors:** Jinglin He, Siyang Jiang, Lixing He, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06603v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06603v1)

**Summary:** Text from multiple sources can become interleaved into a single sequence when attribution metadata is lost, such as overlapping speech transcripts, document reading flows, or concurrent agent streams. We formalize this challenge as Word-Level Text Unmixing: given an interleaved lexical stream and source count K, recover the original source sequences while preserving every word occurrence and its within-source order exactly. Directly generating separated texts with LLMs can omit, duplicate, or ha...

---

### 31. Molecules of a Story: Community Detection in PMI-weighted Narrative Networks

**Authors:** Kasper Fyhn, Rebekah Baglini

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06600v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06600v1)

**Summary:** Automatically extracted narrative networks -- graphs with entities as nodes and their relations as edges -- have proven useful for revealing central narrative structures through salient entities and their connections (Tangherlini et al. 2020; Labatut and Bost 2019). But a narrative is more than those central structures that everything else revolves around. This work is concerned with the everything else: brief sub-plots, small clusters of descriptions, or associations between minor characters th...

---

### 32. Mind the Accent Gap: British Accent Robustness in Speech-Driven Financial Voice Assistants

**Authors:** Aadam Haq, Oggi Rudovic, Malcolm Chadwick, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06587v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06587v1)

**Summary:** AI voice assistants often use Automatic Speech Recognition (ASR) with LLM-based reasoning, yet existing systems struggle with regional British accents, including Scottish, Irish, and Welsh accents, since most ASR models are trained predominantly on American English voice data. Consequently, errors can carry through to the LLM stage, corrupting tool-call arguments and producing wrong or missing responses, which is especially costly in finance. Deployable ASR must also meet tight latency and memor...

---

### 33. Mind the Execution Gap: Action-Semantic Mismatch in World-Model Control

**Authors:** Shengtao Wen, Xiang Chen, Yu Tian, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06582v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06582v1)

**Summary:** World-model controllers rely on action-conditioned dynamics for prediction and planning, yet real control systems often execute commands asynchronously due to communication delay, packet loss, reordering, and actuator buffering. We study how asynchronous execution changes the action semantics assumed within world-model controllers, rather than treating it only as an external control disturbance. Through controlled interventions, we identify two architecture-dependent failure modes: planning-base...

---

### 34. Before Agent Tells The Lie: Has Deception Already Been Represented?

**Authors:** Xinling Li, Dadi Guo, Qingyu Liu, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06576v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06576v1)

**Summary:** Large language model (LLM)-based agents can exhibit deceptive behavior during task execution, including hiding failures, fabricating results, or falsely signaling task completion. Existing monitoring approaches mainly detect deception after it appears in observable actions or outputs. In this paper, we investigate whether deceptive behavior can be predicted from an agent's internal representations before it becomes externally visible. We frame deception monitoring as a trajectory-level represent...

---

### 35. Synthetic Cultural Agents from Aggregate Anchors

**Authors:** Augusto Gonzalez-Bonorino, Kseniia Biriukova, Monica Capra

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06562v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06562v1)

**Summary:** Population prompts are widely used to generate synthetic survey responses, but they combine information supplied at inference with associations already encoded during pretraining. We introduce an alternative construction that maps declared aggregate preference anchors into group-indexed choice policies. For each population, the signs of six Global Preferences Survey (GPS) coordinates deterministically label a shared bank of paired synthetic responses, and Direct Preference Optimization fits a pa...

---

### 36. Anatomy of LLM Sycophancy: What a Flip Rate Hides

**Authors:** Haonan Huang

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06522v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06522v1)

**Summary:** A model under pushback can correct itself, capitulate, or hold, and one flip rate counts a correction and a capitulation alike. Using SycoLens, a modular replay protocol, we test how user pressure and evaluation settings shape measured flip rates. Each measurement is one stateless replay of an item, a committed answer, and one scripted user line in a fixed form. Every effect is read against a matched control with the line deleted. Pushback wording, committed text, answer format, boundary distanc...

---

### 37. Test-Time Adaptation of Reasoning Strategies with Bayesian Nonparametric Memory

**Authors:** Keshav Ramji, Tahira Naseem, Ramón Fernandez Astudillo

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06516v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06516v1)

**Summary:** While modern large language models (LLMs) have been trained to reason through verbalized chains-of-thought, the generation cost grows substantially due to suboptimal paths to reach the final answer. Furthermore, as new insights are discovered while observing various input queries (e.g. through self-reflection), limited mechanisms exist for carrying forward these findings to be applied to subsequent problems. One can view the list of such strategies or behaviors as a growing cheatsheet, with elem...

---

### 38. SOL: Measuring Gaps between Text Distributions by Double Sliced Wasserstein Metrics

**Authors:** Gregor Kornhardt, Moritz Piening, Jannis Chemseddine, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06513v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06513v1)

**Summary:** Evaluating text generation requires measuring how well the generated distribution matches the data distribution. For autoregressive models, this is done by the perplexity. Diffusion and flow-based language models can only provide a likelihood bound, whose tightness differs between model families. Sample-based substitutes such as generative perplexity with entropy do not consider the distribution fit. We propose SOL,   a distance between text distributions. Each sequence is represented by the emp...

---

### 39. AECP: Artifact-Exclusive Communication Protocol for Multi-Agent Code Generation

**Authors:** Jiaqi Xue, Yanjun Wang, Xiangci Li, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06481v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06481v1)

**Summary:** As AI agents increasingly tackle complex repository-level coding tasks, distributing work across multiple agents is a natural way to scale beyond the capabilities of a single agent. To coordinate their interdependent work, these agents share findings and agree on interfaces between modules. However, exchanged information often serves only as context, leaving individual agents to interpret it and incorporate it into subsequent work. Consequently, shared findings may go unused and deviations from ...

---

### 40. Behavior-Preserving KV Cache Compression

**Authors:** Doo Hwan Hwang, Junyoung Jang, Junho Na, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06479v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06479v1)

**Summary:** KV caches are a major bottleneck in long-context inference and long-form generation with large language models. Existing training-free eviction policies largely rely on proxy importance signals, such as attention mass, to decide which past tokens to retain. We argue that cache compression should instead preserve the predictive behavior of the full-cache model, retaining entries whose removal would substantially change the model's output distribution. We propose Behavior-Preserving KV Cache Compr...

---

### 41. The Assistance Dilemma: Learning to Teach via Multi-Turn Reinforcement Learning

**Authors:** Jakub Macina, Manu Kapur, Mrinmaya Sachan

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06446v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06446v1)

**Summary:** Large language models (LLMs) trained to answer questions are natively poor at teaching. Reinforcement Learning (RL) against a simulated student is a promising approach to improve their pedagogy, but existing RL-trained tutors reward the student's success on the tutored problem with the tutor's words still in context. The reward is then easiest to raise by telling the student the answer, and a tuned penalty is needed to reduce telling. Drawing on learning sciences, we introduce a masked near-tran...

---

### 42. Better Call Reward: Reward Hacking as Strategic Abstention in Legal Reasoning Models

**Authors:** Subramanyam Sahoo, Justin Shenk

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06439v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06439v1)

**Summary:** What happens when a legal AI model learns to look like a lawyer instead of reasoning like one? We fine tune Qwen3-8B with Group Relative Policy Optimisation (GRPO) against a proxy built from three surface features: citation count, legalese density, and response length. The model does not learn to reason more effectively. It learns to withhold commitment. Across 16 yes or no legal reasoning tasks from LegalBench (N=320), overall accuracy collapses from 0.500 (chance) to 0.072 (McNemar p < 10^-36)...

---

### 43. HeuFouFT: Task-Guided Metaheuristic Coordinate Search for Fourier Fine-Tuning

**Authors:** Ruiheng Wang, Yubo Hou, Yakun Zhu, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06437v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06437v1)

**Summary:** We introduce Heuristic-Guided Fourier Fine-Tuning (HeuFouFT), a task-guided framework for selecting trainable frequency coordinates in Fourier fine-tuning. Existing uniform and Gaussian band-pass schemes allocate a limited spectral budget through fixed, task-agnostic rules. HeuFouFT instead searches for coordinates using downstream performance. A coarse intensity map from lightweight block-level probes initializes three metaheuristic optimizers: Genetic Algorithm with Simulated Annealing (GA-SA)...

---

### 44. Do Speech Representations Preserve Regional Accent Across Read and Spontaneous Speech?

**Authors:** Paula A. Perez-Toro, Tomas Arias-Vergara, Annette Schwarz, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06430v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06430v1)

**Summary:** Regional accent cues can be captured under matched conditions, but it remains unclear whether they persist between read and spontaneous speech. We study RVG1, with 500 German speakers from nine regions, comparing ten speech representations on regional classification and continuous geolocation under matched conditions and speaker-independent read--spontaneous transfer. Whisper performs best under matched conditions, reaching 0.489 nine-way UAR and 148 km median geolocation error, but drops to 0.1...

---

### 45. SpatialChain: A Benchmark for Auditing Spatial Reasoning Faithfulness in VLMs

**Authors:** Rafael Teixeira Sousa, Vinícius Paulo Lopes de Oliveira, Elisa Ayumi Masasi de Oliveira, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06413v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06413v1)

**Summary:** Thinking-enabled vision-language models (VLMs) report ever-higher accuracy on spatial benchmarks, yet final-answer scores cannot reveal whether a correct prediction reflects faithful spatial reasoning or a linguistic shortcut. We introduce SpatialChain, a dataset of 28,350 training and 899 test examples pairing spatially-oriented GQA questions with scene-graph-grounded reasoning chains, retained only when the generated answer matches the symbolic ground truth, and a two-axis evaluation combining...

---

### 46. What Did the Agent Actually Do? Evidence-Grounded Oversight for Long-Horizon Agents

**Authors:** Zhongxiang Sun, Jiahao Yan, Hongkang Zhao, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06406v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06406v1)

**Summary:** As agents take on long-horizon tasks, users shift from making individual decisions to overseeing autonomous execution. Yet the volume of agent activity and the fragmentation of supporting evidence make it difficult to determine which decisions warrant user verification. We study monitors that identify consequential decisions and locate evidence to help users assess their implications. We introduce AgentMonBench, a software-engineering benchmark comprising three subsets that cover two complementa...

---

### 47. RAISED: Self-Distillation for Robustness to Prompt Injection in LLM Agents

**Authors:** Mohamed Dhouib, Clement Elliker, Alexi Canesse, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06401v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06401v1)

**Summary:** Tool-using language-model agents are vulnerable to indirect prompt injection because they must act on untrusted external content. Existing training-time defenses can reduce attack success rates, but often at the cost of general capabilities. We show that training-based defenses induce substantial drift in the model's output distribution, altering its behavior even in benign settings and providing a potential mechanism for utility degradation. We further identify a failure mode of these defenses:...

---

### 48. Steering by Influence: Curvature Aware Data Weighting for Activation Steering

**Authors:** James A. E. Dixon, Stephen J. Roberts, Francesco Quinzan

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06383v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06383v1)

**Summary:** Inference-time steering offers cheap, fine-grained control over a language model's outputs by estimating a concept's representation in activation space and shifting activations towards it. Existing methods build these representations from activation averages over contrastive datasets. These averages incorporate unrelated concepts and noise, and are dominated by a few tokens, meaning the activation transport encodes token-level rather than thematic concepts. In this work, we steer towards example...

---

### 49. Ontology Concept Overlap as a Training Signal: Knowledge-Grounded Reinforcement Learning for Clinical Question Answering

**Authors:** Aditya Tanna, Abhishek Jindal

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06360v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06360v1)

**Summary:** Reinforcement learning post-training for language models relies on two reward designs: human preferences (RLHF, DPO) and binary verifiers (RLVR). Clinical question answering fits neither. Near-correct answers differ by a single substituted entity, and no executable check decides clinical correctness. We instantiate a soft verifier from a maintained controlled vocabulary: UMLS Concept Unique Identifier overlap (via scispaCy, set-level F1) gives a graded, externally specified reward computed witho...

---

### 50. Breaking Bureaucracy: Evaluating open-source LLMs for legal document review

**Authors:** Farrukh Baratov, Niki van Stein, Suzan Verberne

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06345v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06345v1)

**Summary:** In this paper, we evaluate open-source generative LLMs on legal Natural Language Inference (NLI). Legal inspectorial processes take place in specific domains and often deal with confidential data. This creates a need for working with local models that do not require labeled training data. We evaluate our models on the ContractNLI benchmark and two NLI4Wills datasets. We successfully reproduce the baseline for the task (Span NLI BERT) and we evaluate multiple open-source LLMs on the same task. We...

---

## cs.CV

**50 papers**

### 1. One Figure, Every Canvas: Editable Flowchart Relayout via Agentic Pipeline

**Authors:** Shih-Chen Tseng, Chih-Hsuan Chen, Ryan Yang, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06852v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06852v1)

**Summary:** Pipeline figures in ML papers must be repurposed across many canvases, including paper columns, 16:9 slides, portrait posters, 1:1 social teasers, 9:16 phone previews. Each format imposes a different aspect ratio on the same computational graph, where any silently broken connection misrepresents the method. We formulate aspect-ratio-adaptive flowchart relayout as a distinct task: given a raster flowchart and a target ratio, produce a structurally faithful, hallucination-free, editable layout. Ex...

---

### 2. InterMimicGen: Scaling Humanoid Loco-Manipulation through Self-Evolving Motion Imitation

**Authors:** Yucheng Zhang, Sirui Xu, Jinhong Li, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06850v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06850v1)

**Summary:** Captured human-object interactions provide rich supervision for humanoid loco-manipulation, but they are sparse, heterogeneous, and not directly executable by robots. We introduce InterMimicGen, a self-evolving motion-imitation framework in which robot motion data and a tracking policy improve each other. First, we consolidate motion-captured human-object interaction datasets and retarget them into humanoid robot references while preserving whole-body coordination and dexterous hand-object relat...

---

### 3. S2PD: Serial-to-Parallel Diffusion for Physically and Logically Consistent Video Generation

**Authors:** Jeffrey Hu, Daniel Olmeda Reino, Ayush Tewari

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06847v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06847v1)

**Summary:** Bidirectional video diffusion models denoise entire videos in parallel, yet when trained on effectively unlimited in-distribution data from procedural generators, continue to violate physical laws and simple symbolic rules. We introduce Serial-to-Parallel Diffusion (S2PD), which performs autoregressive diffusion at high noise before switching to parallel diffusion at low noise. The autoregressive phase provides the serial computation needed to coordinate interdependent events and produce valid s...

---

### 4. Learning to Read the Contextual Tokens in Diffusion Transformers

**Authors:** Omer Dahary, Etai Sella, Hadar Averbuch-Elor, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06844v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06844v1)

**Summary:** Multimodal Diffusion Transformers (MM-DiTs) jointly process visual and textual representations throughout generation. These models repeatedly update the text tokens through multimodal attention, forming dynamic contextual tokens whose function is not well understood. In this work, we introduce a framework for reading this contextual space through natural-language interrogation. We train a lightweight bottleneck network that maps intermediate contextual tokens into the input space of a frozen Lar...

---

### 5. Anatomy-aware Fine-grained Multimodal Fusion for Laryngopharyngeal Cancer T-Staging Prediction Using CT and Radiology Report

**Authors:** Xingyue Zhao, Yanzhou Su, Fang Zhang, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06837v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06837v1)

**Summary:** Accurate T-staging is crucial for guiding personalized treatment strategies for laryngopharyngeal cancer. However, current clinical practice relies on invasive biopsy procedures, whereas CT-based staging remains challenging due to the complex patterns of tumor invasion. Recent computer-aided approaches face two key challenges: 1) Structural relationship modeling: existing methods underrepresent anatomically structured patterns of tumor invasion, as they either process whole CT volumes without tu...

---

### 6. UniSlider: Perceptually Uniform Sliders for Continuous Image Editing

**Authors:** David Serrano-Lozano, Duygu Ceylan, Yannick Hold-Geoffroy, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06831v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06831v1)

**Summary:** Sliders provide an intuitive interface for continuous image editing. In current generative approaches, however, the slider is simply a rescaling of the method's strength parameter, such as an adapter coefficient, a prompt weight, or an interpolation factor. This strength relates poorly to perceptual change. The image can partially revert as the slider moves, long stretches of the range produce no visible difference, and short intervals transform the image abruptly. Remapping the strength could f...

---

### 7. PlotGround: Grounding Plot Digitization in Real Scientific Figures and Their Source Data

**Authors:** Yaohui Zhang, Binxu Li, Haoyi Duan, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06825v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06825v1)

**Summary:** Scientific figures often encode quantitative results that are not readily available in machine-readable form, making accurate plot digitization important for verifying and reusing published findings. Yet it remains unclear how accurately current models recover plotted values from real scientific figures, as existing benchmarks rely largely on synthetic charts or cover only a limited range of chart types. We introduce PlotGround, an automated pipeline for building plot digitization benchmarks fro...

---

### 8. TAPDreamer: Transferable Adversarial Patches for World Action Models

**Authors:** Xuanyu Lu, Fengqing Jiang, Kaiyuan Zheng, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06814v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06814v1)

**Summary:** World models learn to predict how their environment will evolve, making them an important foundation for general-purpose robotic control. Yet world action models depend on camera inputs whose manipulation can corrupt the visual representations used across tasks and action policies. Existing attacks on these models optimize against the victim's actions or predicted futures and therefore require access to target-model outputs. In this paper, we propose an attack, TAPDreamer, against world action m...

---

### 9. Less Context, Better Geometry: Masked Geometric Encoder for Robust 3D Foundation Models

**Authors:** Zhimin Shao, Xijun Liu, Zhaoliang Zhang, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06813v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06813v1)

**Summary:** Recent progress in 3D foundation models has enabled rapid 3D reconstruction and camera calibration by leveraging learned 3D priors from vast amount of spatial data. However, the all-to-all global attention design leads to quadratic complexity and limits long-sequence inference; unconstrained cross-view interactions also can propagate unreliable evidence from occluded or visually similar but geometrically distant views. In this paper, We introduce a Masked Geometric Encoder (MGE), which promotes ...

---

### 10. MC-Sparse: Deconstructing and Closing the Dense-Sparse Attention Gap in Diffusion Transformers

**Authors:** Jiarui Chen, Zeqiang Lai, Jiangshan Wang, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06801v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06801v1)

**Summary:** Sparse attention is a primary approach to reducing the latency of diffusion transformers in long-sequence generation tasks, such as video and high-resolution 3D asset generation. However, existing methods can degrade generation quality and fidelity at high sparsity levels. Through controlled oracle comparisons, we trace this degradation to three sources: constraints imposed by token grouping, inaccurate interaction selection, and the attention contributions lost when tokens are discarded. Guided...

---

### 11. Extending Dynamic World Surface Water Mapping to Sentinel-1 with AlphaEarth Embeddings

**Authors:** Rohit Mukherjee, Frederick Policelli, Beth Tellman, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06704v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06704v1)

**Summary:** Dynamic World (DW) maps land use and land cover globally at 10 m from Sentinel-2 (S2) imagery, but only for cloud-free observations, which limits where and when surface water can be mapped. We use the DW water class as weak supervision for a Sentinel-1 (S1) synthetic aperture radar (SAR) model so that DW-like water maps can be produced for every S1 acquisition. Google's AlphaEarth Foundations (AEF) annual embedding supplies spatial context, while S1 backscatter supplies the acquisition-time obse...

---

### 12. GS-Pool: Object-Level Change Detection in 3D Gaussian Splatting

**Authors:** Boaz Keren-Gil, James Gain, Patrick Marais

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06688v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06688v1)

**Summary:** Factories, museums and surveyors photograph the same space months apart and need to know which objects changed. When each visit is reconstructed with 3D Gaussian Splatting (3DGS), a direct comparison of the two reconstructions does not answer this. Training is stochastic, so two reconstructions of an unchanged space never coincide, and the second visit is often a quick re-scan with far fewer photographs. We propose GS-Pool, which takes two independently reconstructed Gaussian fields of the same ...

---

### 13. ChronoWorld: Camera-Controlled Consistent 4D World Generation via Spatiotemporal Cues and Geometric Reflections

**Authors:** Xiaoyu Zhou, Dingwei Xian, Zhenyu Wang, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06687v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06687v1)

**Summary:** While existing camera-controllable video generation models can produce visually compelling sequences, preserving intrinsic 4D spatiotemporal coherence remains challenging. To address this limitation, we propose ChronoWorld, an "Observation--State--Reflection" framework that leverages spatiotemporal causal cues and reconstruction priors to generate globally consistent, free-view 4D scenes. Given a context video, we introduce a Spatiotemporal Epipolar Causal Attention mechanism that enforces multi...

---

### 14. Detecting Nighttime Anomalies from NASA Black Marble Using a Generalized Spatio-Temporally Robust Framework of Machine Leaning Ensembles

**Authors:** Srija Chakraborty

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06674v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06674v1)

**Summary:** Nighttime lights from NASA's Black Marble product suite capture thermal and light emission signals from anomalous events including fires, volcanic eruptions, and gas flaring. Existing detection approaches rely primarily on thermal bands, limiting sensitivity to weaker signals. We propose a novel machine learning framework that jointly models Black Marble M-band and Day/Night Band (DNB) signals to derive a generalized, spatio-temporally robust ensemble of anomaly detectors. The framework iterativ...

---

### 15. VideoTapestry: Query-Adaptive Memory Refinement for Multi-Agent Long-Video Understanding

**Authors:** Yucheng Liu, Yufei Yin, Mingxiao Feng, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06672v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06672v1)

**Summary:** Long-video understanding places substantial demands on memory, as answering questions often requires retrieving information distributed across extended temporal spans. Existing approaches broadly follow two paradigms: query-driven exploration, which is sensitive to localization errors, and query-independent memory construction, which may omit question-specific details. We introduce VideoTapestry, a training-free multi-agent framework that adapts a preconstructed hierarchical video memory through...

---

### 16. Cross-dataset harmonization for robust endoscopic image analysis

**Authors:** Romil Imtiaz, Dimitris K. Iakovidis

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06663v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06663v1)

**Summary:** A significant problem in endoscopic image analysis is that the machine learning (ML) models used for this purpose usually underperform when applied on images acquired from endoscopes that are different from those used to acquire the images of their training set. The main difference of the images originating from different endoscopes is their color distributions, which depend both on the image sensors and the light sources used. Although previous studies have highlighted this challenge, to the be...

---

### 17. Talk Like You: Imitating How You Speak in Real-Time Talking Head Generation

**Authors:** Baiqin Wang, Zhixing Ding, Jijie Li, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06658v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06658v1)

**Summary:** In daily life, each person exhibits unique speaking habits, leading to subtle yet consistent lip-shape variations even when pronouncing the same word. Although recent talking head generation methods have achieved impressive visual fidelity and lip synchronization, they largely overlook user-specific customization, especially the motion patterns that characterize individual speaking habits. These habits are difficult to model and capture, as their motion patterns are highly fine-grained and often...

---

### 18. AffordCraft: Scalable Construction of Task-Ready Simulation Assets from Single Images

**Authors:** Haoyun Yang, Xueyang Zhou, Ziyi Xie, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06643v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06643v1)

**Summary:** Robot learning in simulation depends on the objects the simulator offers. Many tasks need objects with separate parts, joints that allow the required motion, and physical properties that remain valid under contact. Existing methods recover this structure anew for every image: generative models predict parts and joints that mostly fail to settle or move in simulation, and general-purpose agents need a long session of model calls for each photograph. AffordCraft builds such an asset from a single ...

---

### 19. RealtimeWAM: One-Step Asynchronous World Action Models

**Authors:** Chengtao Lv, Jinyang Du, Shuyi Feng, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06617v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06617v1)

**Summary:** World Action Models (WAMs) incorporate visual representations from video generation backbones to guide action prediction. Recent efficient WAMs adopt Mixture-of-Transformers (MoT) architectures and compute video representations once for reuse by the action expert. However, intra-expert iteration (\ie, multi-step action denoising) and inter-expert waiting (\ie, sequential execution of the video and action experts) still limit inference efficiency. To this end, we present RealtimeWAM, an extremely...

---

### 20. Video Encoders Built on Image Representations

**Authors:** Jusheng Zhang, Wenhao Wang, Longqi Cai, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06616v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06616v1)

**Summary:** The design of a video encoder determines when frames begin to interact and which frame-specific visual evidence remains accessible to the language model. Native video pathways couple neighboring frames during visual encoding, whereas image pathways preserve independently computed frame representations but incur a much larger visual-token cost when all image tokens are forwarded. We ask a basic question: whether a compact video encoder can instead be built on image representations. To answer this...

---

### 21. Lens3D: Target-Conditioned Visual Foveation for Fine-Grained 3D Understanding

**Authors:** Junming Huang, Zini Chen, Shuaiying Hou, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06611v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06611v1)

**Summary:** Existing 3D large language models often overlook fine-grained attributes and less visually salient objects and parts, even when relevant evidence is present in scene videos. We introduce Lens3D to improve fine-grained object understanding through external visual assistance and knowledge transfer. Its LensUnd pipeline adopts 3D localization to select informative, complementary views for an external 2D vision-language model, supporting fine-grained object captioning, small-object grounding, and fi...

---

### 22. Multitask Conditional Generative Adversarial Network Enables Automatic Whole Knee Cartilage and Menisci Segmentation and Reliable T1\r{ho} and T2 Quantification Without High-Resolution Morphological Images

**Authors:** Ahmed Tahseen Minhaz, Richard Lartey, Zhiyuan Zhang, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06602v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06602v1)

**Summary:** Early osteoarthritis detection through quantitative MRI (qMRI) requires accurate cartilage and meniscus segmentation, traditionally necessitating time-consuming, costly 3D high-resolution Double Echo Steady-State (DESS) MRI scans. This study developed a multi-task conditional generative adversarial network (MT-cGAN) to simultaneously synthesize DESS-like images and segment tissues directly from qMRI echo images. This retrospective study evaluated 508 knee MRI volumes from 361 subjects (mean age:...

---

### 23. SimForcing: Distilling Simulation Motion Priors into Real-Domain Robot World Models

**Authors:** Xiaodong Wang, Tianle Li, Chuanxin Song, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06598v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06598v1)

**Summary:** Action-conditioned robot world models must respond precisely to robot trajectories while preserving realistic visual dynamics, yet learning both from heterogeneous robot videos remains challenging. Simulation offers structured motion supervision, but appearance differences hinder direct transfer, and inaccurate simulation predictions can misguide real-video generation. We present SimForcing, a simulation-guided framework that uses simulation both as a source of transferable motion knowledge and ...

---

### 24. Analysis of SWIR Imaging Detection Performance Under Adverse Environmental Conditions for Autonomous Driving Systems

**Authors:** Rohan Mehra, Alexandre Riffard, Yannis Loumouamou, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06596v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06596v1)

**Summary:** Short-wave infrared (SWIR) imaging has emerged as a promising modality for autonomous driving, yet its practical benefits over RGB remain poorly characterized across diverse conditions. This paper presents a systematic comparative study of paired RGB and SWIR object detection on the RASMD dataset, covering four weather conditions and two real-time detection architectures, with various fine-tunings evaluated against a unified ground truth. Overall, RGB demonstrates comparable or superior performa...

---

### 25. VGGT-Bridge: Beyond Sequential Pose Graphs via Coarse-Stride Skip Edges

**Authors:** Sungjae Choi, Hanna Bae, Sunghyun Baek, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06594v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06594v1)

**Summary:** Feed-forward visual geometry transformers such as VGGT reconstruct dense 3D structure from images in a single forward pass, simplifying multi-view 3D reconstruction. However, their quadratic attention complexity makes them difficult to scale to long sequences with thousands of frames. Chunk-and-align frameworks address this by splitting a long sequence into overlapping chunks and stitching their local reconstructions into a pose graph. Yet existing methods connect only sequentially adjacent chun...

---

### 26. Keepsake: Selective Spatial Memory for Long-Horizon Video Generation

**Authors:** Abdul Mohaimen Al Radi, Kunyang Li, Yuzhang Shang, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06588v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06588v1)

**Summary:** Long-horizon camera-controlled video generation relies on persistent memory to maintain scene consistency. Existing systems follow two strategies to achieve this consistency. Full-history approaches retain all generated observations, causing unbounded storage and retrieval costs. Selective-construction approaches reduce redundancy, but make one-time retention decisions that are never revisited, even as an observation's value changes with the evolving memory bank. Both strategies leave a shared q...

---

### 27. FrontVeg V2: A Training-Free Software Framework for Foreground-Aware Zero-Shot Plant Trait Segmentation in High-Resolution Images of Trellised Crops

**Authors:** Abdoul Djalil Ousseini Hamza, Herearii Metuarea, Corentin Lothod{é}, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06575v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06575v1)

**Summary:** FrontVeg V2 is an open-source, training-free software framework for foregroundaware zero-shot segmentation of plant traits in high-resolution images of trellised crops. The pipeline combines monocular depth estimation, automatic foreground extraction using Valley-Aware Depth Thresholding, tiled zero-shot segmentation, Graph-Based Mask Assembly, and geometry-aware fusion. This design enables plant organs and disease symptoms to be segmented while reducing detections arising from neighboring veget...

---

### 28. BrainTRACE: Tracing Longitudinal, Multimodal, and Volumetric Evidence in Brain MRI Clinical Reasoning

**Authors:** Qizhen Lan, Mengchen Fan, Hang Zhang, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06571v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06571v1)

**Summary:** Brain MRI interpretation is a longitudinal clinical reasoning problem: radiologists compare serial studies, integrate information across MRI sequences, localize findings within volumetric anatomy, and translate this evidence into report-grounded assessments. Existing medical VQA and 3D imaging benchmarks capture important parts of this workflow, but often evaluate brain MRI through isolated images, static volumes, or ungrounded report-style answers, thereby obscuring failures in the evidence cha...

---

### 29. A General Pipeline for Dense Illuminant Estimation via Physically Based Synthetic Data

**Authors:** Luca Cogo, Gianmarco Corti, Simone Bianco, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06508v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06508v1)

**Summary:** Illuminant estimation is a fundamental problem in computational photography, as it enables the correction of color shifts induced by varying lighting conditions. While learning-based methods have demonstrated strong performance, their progress is hindered by the limited availability of large-scale datasets with accurate illuminant ground-truth. In this work, we propose a general and reusable pipeline to derive dense illuminant chromaticity maps from physically based 3D-rendered scenes. By repurp...

---

### 30. Improving Proactive AI Assistance with Hierarchical Procedural Understanding

**Authors:** Jin-Seop Lee, TaeYeon Won, SeongJun Jung, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06505v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06505v1)

**Summary:** Proactive AI assistants continuously observe a user's activity and decide whether to provide new guidance or remain silent. They should provide appropriate guidance for the task, determine when to provide the next guidance based on task progress, and adjust the guidance level to the user's expertise and needs. Supporting these capabilities requires training and evaluation data that reflect procedural structure and capture how guidance should adapt to task progress and user needs. However, existi...

---

### 31. Harmful Content Generation in Text-to-Image Models: Capabilities and Moderation Limitations

**Authors:** Paschalis Giakoumoglou, Manos Schinas, Symeon Papadopoulos

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06503v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06503v1)

**Summary:** Text-to-image generative models can produce highly realistic imagery but also raise concerns about harmful misuse. While safety mechanisms exist, systematic evaluations of their effectiveness against realistic attacks remain limited. We present a systematic evaluation of harmful content generation across five open text-to-image models using an automated pipeline that transforms legitimate news captions into unsafe prompts targeting sexually explicit content, violence/gore, harmful stereotypes, s...

---

### 32. NeuroCBIR: A Fast and Accurate Image Retrieval System for Whole-Brain and Region-Specific MRI

**Authors:** Felix Nieto-del-Amor, Jingru Fu, J. -Sebastian Muehlboeck, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06502v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06502v1)

**Summary:** Content-based image retrieval (CBIR) in neuroimaging enables the identification of structurally similar brain scans, supporting diagnosis, prognosis, and treatment planning; however, existing methods are often limited to small datasets, single brain regions, or coarse class labels, thereby restricting their clinical utility and generalizability.   Here, we present NeuroCBIR, a framework for fast and flexible retrieval of both whole-brain and region-specific 3D T1w MRI scans. A total of 103 corti...

---

### 33. Topology-Informed Prompt-Conditioned Universal Segmentation of Uterine Structures from Ultrasound and MRI

**Authors:** Yongheng Sun, Yuexi Gu, Jingwen Sun, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06494v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06494v1)

**Summary:** Multi-structure segmentation of the uterus is important for computer-assisted screening, diagnosis, and treatment planning of uterine diseases, where ultrasound and MRI provide complementary clinical information. However, developing a unified model across these modalities is challenging due to their substantially different image appearances, anatomical contexts, spatial resolutions, and label spaces. Moreover, existing datasets often define different segmentation targets, making joint learning c...

---

### 34. MaRO-GS: Mask-Robust Object-Centric Gaussian Splatting from Inconsistent Multi-view Masks

**Authors:** Eunji Kim, Gahyeon Kim, Gianella Cravioto, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06472v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06472v1)

**Summary:** We address the challenge of accurate 3D object reconstruction from multi-view images in Gaussian Splatting. Existing object-level 3DGS methods reconstruct the entire scene rather than directly optimizing the target object, even when only the target object is needed, which incurs substantial computational overhead. They also rely on 2D segmentation masks to associate Gaussians with objects, but these masks are often inconsistent across views. Such inconsistencies corrupt Gaussian optimization and...

---

### 35. Toward Reliable Infant Pose Estimation: A Training-Dynamics Approach to Noisy Annotation Detection

**Authors:** Emanuele Cardinale, Sara Moccia, Alessandro Cacciatore, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06423v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06423v1)

**Summary:** Spontaneous movement analysis in preterm infants relies increasingly on markerless pose estimation (PE) to derive clinically relevant motion biomarkers directly from video recordings. Training accurate infant PE models requires large sets of manually annotated keypoints, and human annotation is inherently prone to error. Noisy keypoints (i.e., keypoints mislocalized with respect to their true anatomical position) are especially problematic in this clinical setting, since they can propagate as ar...

---

### 36. SpatialChain: A Benchmark for Auditing Spatial Reasoning Faithfulness in VLMs

**Authors:** Rafael Teixeira Sousa, Vinícius Paulo Lopes de Oliveira, Elisa Ayumi Masasi de Oliveira, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06413v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06413v1)

**Summary:** Thinking-enabled vision-language models (VLMs) report ever-higher accuracy on spatial benchmarks, yet final-answer scores cannot reveal whether a correct prediction reflects faithful spatial reasoning or a linguistic shortcut. We introduce SpatialChain, a dataset of 28,350 training and 899 test examples pairing spatially-oriented GQA questions with scene-graph-grounded reasoning chains, retained only when the generated answer matches the symbolic ground truth, and a two-axis evaluation combining...

---

### 37. Harnessing Multimodal Large Language Models for Training-Free Human-Object Interaction Detection

**Authors:** Zhaolin Cai, Huiyu Duan, Liu Yang, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06394v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06394v1)

**Summary:** Human-object interaction (HOI) detection aims to localize human-object pairs and recognize their interactions. Traditional supervised methods perform strongly but rely on task-specific training. Recent multimodal large language models (MLLMs) offer a promising route to training-free HOI detection through their broad visual-semantic knowledge and versatile perceptual and reasoning capabilities. However, existing approaches largely invoke these capabilities through loosely coordinated inference st...

---

### 38. Multi-Task Partially Supervised Learning for Super-Resolution and Semantic Segmentation on Earth Observation data

**Authors:** Hoàng-Ân Lê, Minh-Tan Pham, Solange Lemai-Chenevier, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06389v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06389v1)

**Summary:** Super-resolution and semantic segmentation are known to benefit one another, especially in the Earth observation context. However, learning both tasks in a joint model often requires both task annotations, which is impractical and expensive. In this paper, we study the multi-task partially supervised learning paradigm for both tasks, where each example is assumed to have only a single-task annotation. To that end, we examine two multi-task architectural variations, the sequential and shared vari...

---

### 39. MTOR: Generalizable AI-Generated Video Detection with Multimodal Semantics and Temporal Over-Regularity

**Authors:** Hang Wang, Chao Shen, Lei Zhang, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06378v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06378v1)

**Summary:** The rapid evolution of video generation has narrowed the perceptual gap between authentic and synthetic videos, making generalizable AI-generated video detection increasingly challenging. Existing detectors predominantly rely on visual representations, leaving caption-derived textual semantics underexplored. Meanwhile, temporal regularity in fine-grained visual representations has received limited attention. We find that caption-derived textual representations provide complementary discriminativ...

---

### 40. Environmental sensor readings in two crop disease image datasets identify the session in which each image was taken

**Authors:** Sungwoo Kang

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06369v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06369v1)

**Summary:** Integrating environmental sensor data with leaf imagery is widely reported to boost crop disease classification accuracy. In this work, we reveal that these reported gains are often artifacts of dataset construction: because a single sensor reading is shared across many images collected in a single session (one farm on one date), multimodal networks can predict disease simply by memorizing session identities. Analyzing two widely used Korean datasets, the Crop Disease Diagnosis (CDD) benchmark a...

---

### 41. KineWorld: Action-Induced Transport Fields for Embodied World Modeling

**Authors:** Ziying Song, Yuchen Liu, Zhuoran Xu, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06349v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06349v1)

**Summary:** Embodied world models predict the visual consequences of candidate actions before execution. However, existing action-conditioned world models often adopt uniformly weighted visual generation objectives that can be misaligned with embodied prediction needs. Even with explicit motion conditioning, these objectives can underemphasize spatially sparse changes that are critical to interaction. We propose KineWorld, a transport-aware world-modeling framework that extends robot kinematics from motion ...

---

### 42. MeSD: Multi-Evidence Self-Distillation for VideoLLM

**Authors:** Weijie Zhu, Han Fang, Hanyu Fu, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06342v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06342v1)

**Summary:** While reinforcement learning with verifiable rewards provides reliable outcome supervision for VideoLLMs, sequence-level rewards offer limited token-level guidance. On-policy self-distillation addresses this limitation by conditioning a self-teacher on privileged information to provide dense token-level supervision. However, aggregating heterogeneous evidence within a single teacher context obscures cross-evidence agreement and conflict. A further challenge lies in determining whether teacher gu...

---

### 43. BabelFake: A Multilingual Audio-Visual DeepFake Benchmark

**Authors:** Carlotta Segna, Joel Tschesche, Anna Rohrbach

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06339v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06339v1)

**Summary:** Reliable and practical audio-visual DeepFake detection requires benchmarks that reflect diverse linguistic contexts and modern data synthesis pipelines for visual as well as audio manipulations. However, existing datasets predominantly contain footage of English-speakers, often include outdated manipulation types, or overlook the audio modality. Further, many datasets feature individuals who did not consent to be used in DeepFake creation. We introduce BabelFake, a multilingual audio-visual Deep...

---

### 44. SPIN: Image Immunization Against Diffusion Editing via Single-Step Projection in Stochastic Neighborhoods

**Authors:** Fengming Gu, Jie Zhang, Zhongqi Wang, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06334v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06334v1)

**Summary:** Diffusion models have greatly advanced instruction-guided image editing, while also raising concerns about unauthorized image manipulation. Image immunization addresses this risk by adding imperceptible perturbations to an input image to disrupt subsequent edits. Since editing requests are unknown at image release, protection should remain effective beyond the instruction used to construct the perturbation. Existing immunization methods either require costly full-trajectory backpropagation or us...

---

### 45. Dual Variational Autoencoders for Efficient Sim-to-Real Transfer in Low-Cost Robotic Navigation

**Authors:** Álvaro Díez, Fidel Aznar

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06327v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06327v1)

**Summary:** Vision-based autonomous navigation for low-cost robots remains a fundamental challenge, primarily due to the significant gap between simulated training environments and real-world operational conditions. Direct policy transfer from simulation is often ineffective, while training exclusively on real data is impractical. We propose a hybrid transfer learning framework that effectively bridges the sim-to-real gap by combining domain randomization with feature-level domain adaptation. Our method emp...

---

### 46. Readout Blindness: VLM Scores Miss the Spatial Direction Their Frozen Encoders Retain

**Authors:** Guangyuan Li, Tianming Du, Yan Jiang, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06324v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06324v1)

**Summary:** CLIP-like vision-language models remain a cornerstone of multimodal systems, yet their scores stay near chance on directed spatial relations, such as whether one object is left of another. We call this failure readout blindness and analyze, theoretically and empirically, why deployed scores miss the direction: when scoring rules treat the subject and object symmetrically, direction cancels regardless of encoder training. Guided by this analysis, we introduce Antisymmetric Displacement Readout (A...

---

### 47. Wiring Matters: Injection Topology and Initialization of Affordance Heads in Vision-Language-Action Policies

**Authors:** Zijian An, Linhan Wang, Jiayan Wang, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06318v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06318v1)

**Summary:** Dense affordance supervision is an appealing auxiliary signal for vision-language-action (VLA) policies, yet naively co-training an affordance head can severely damage instruction following. We present a controlled study of how to wire such a head into a modern VLA on the LIBERO benchmark. Our recipe reads the backbone through a stop-gradient and re-injects an intermediate head feature into the action expert via a learned bridge. The stop-gradient is a precondition: letting affordance gradients ...

---

### 48. VepAgent: Bridging Causal-Transition via Tool-Augmented Reinforcement Learning for Video Event Prediction

**Authors:** Qiutong Chen, Yuchan Guo, Zhenlong Yuan, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06293v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06293v1)

**Summary:** Multimodal Large Language Models (MLLMs) have demonstrated remarkable potential in video understanding, yet their reliance on retrospective summarization and text-centric priors often limits their ability to bridge unobserved causal transitions when applied to Video Event Prediction (VEP). To address this, we propose VepAgent, an agentic framework that integrates causal-transition reasoning with tool-augmented reinforcement learning (RL) for robust VEP. Unlike prior methods that passively projec...

---

### 49. CentriQ: Calibration-Free Quantization of Diffusion Transformers via Exact Mean Centering

**Authors:** Nataša Jovanović, Mathieu Salzmann, Saqib Javed

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06260v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06260v1)

**Summary:** Diffusion transformers (DiTs) achieve state-of-the-art image generation, but their sampling cost limits deployment. Quantizing both weights and activations to 4 bits reduces this cost, yet existing methods fall short in one of two ways. Calibration-based methods are tied to a specific checkpoint and prompt distribution, whereas data-free Hadamard rotation, effective for LLMs, loses quality on DiTs. We show that this loss has a structural cause. Adaptive layer-norm conditioning adds a per-token m...

---

### 50. Joint Class-Time Learning for Video Classification with Multi-Instance Partial-Label Learning

**Authors:** Lingyu Shen, Wei Tang, Fakhri Karray, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06234v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06234v1)

**Summary:** Multi-instance partial-label learning (MIPL) addresses inexact supervision in both the instance and label spaces, which can be applied to video classification. However, bag-level labels do not explicitly supervise the correspondence between candidate classes and temporal evidence. We propose {\ours}, which couples label disambiguation with temporal evidence allocation through a joint class--time assignment. Occupancy-regularized spherical matching associates contextualized video features while l...

---

## cs.LG

**50 papers**

### 1. Base Models Can Reason By Taking a Cue From Training Data

**Authors:** Sophie L. Wang, Amil Dravid, Rulin Shao, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06851v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06851v1)

**Summary:** In this paper, we study how training data creates associations between the tokens at the start of a base model's response and the reasoning behavior that follows. First, we demonstrate that fixing particular starting token cues makes a base model's performance competitive with that of its reinforcement learning (RL)-trained counterparts on math and coding. For instance, the cue ".\n\nOkay" raises Olmo-3-7B's MATH-500 pass@1 accuracy from 42% to 78%, while "Alright," raises Qwen3-14B's from 72% t...

---

### 2. Learning to Read the Contextual Tokens in Diffusion Transformers

**Authors:** Omer Dahary, Etai Sella, Hadar Averbuch-Elor, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06844v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06844v1)

**Summary:** Multimodal Diffusion Transformers (MM-DiTs) jointly process visual and textual representations throughout generation. These models repeatedly update the text tokens through multimodal attention, forming dynamic contextual tokens whose function is not well understood. In this work, we introduce a framework for reading this contextual space through natural-language interrogation. We train a lightweight bottleneck network that maps intermediate contextual tokens into the input space of a frozen Lar...

---

### 3. Direct Intermediate Initialization for Tilted Diffusion Samplers

**Authors:** Gregory D. Bellchambers

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06834v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06834v1)

**Summary:** Some diffusion posterior samplers construct Gaussian-tilted intermediate distributions along the reverse process. We observe that these targets can be pulled back to clean-space posteriors with weaker conditioning, with samples transported analytically to the corresponding noisy-space target through a Gaussian bridge. For the sequential Monte Carlo (SMC) sampler MCGDiff, the effective observation variance of this pulled-back problem is up to twice the diffusion-noise variance. We exploit this st...

---

### 4. Towards Looped Models Done Right, Part II: Rethinking at Fixed Points

**Authors:** Benhao Huang, Chufan Shi, Junlin Chen, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06833v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06833v1)

**Summary:** Every recurrence of a looped language model adds cost in training, decoding, prefill, and reinforcement learning (RL). The closer recurrent states get to fixed points, the less the path to them matters. This enables truncated backpropagation in training; terminal key-value (KV) sharing for decoding with almost no loss in accuracy; a distilled student that prefills up to 1.79x faster; and RL updates that compute gradients from saved rollout states, 2x faster than backpropagating through the repla...

---

### 5. MemPilot: Orchestrating On-Demand Multimodal Memory Curation for LLM Agents

**Authors:** Haozhen Zhang, Haodong Yue, Quanyu Long, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06830v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06830v1)

**Summary:** Memory has become integral to the LLM agent ecosystem, supporting information retention and reuse across interactions. However, most existing agent memory systems construct memory in a query-agnostic manner, which can incur unnecessary preprocessing cost and discard details that later prove essential. Recent studies have begun shifting memory processing toward runtime adaptation, but typically specialize in particular operations or fixed processing schemes, leaving flexible control over performa...

---

### 6. CLIFT: Conformal Self-Verification for Web Agent Training and Test-Time Scaling

**Authors:** Yifan Zhang, Yutong Dai, Viraj Prabhu, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06829v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06829v1)

**Summary:** Open-source web agents are now strong enough to execute realistic browser tasks, but training them with reinforcement learning still depends on weak supervision: binary task success is too sparse for credit assignment, while frontier-language-model judges are too expensive to call at every step and cannot be assumed available at deployment. We introduce CLIFT, a training and test-time scaling method built around conformal self-verification. During training, the agent answers natural-language ver...

---

### 7. Deep Learning for Sleep Heart Rate Estimation from Accelerometers: Toward Population-Scale Cardiac Insight Without Optical Sensors

**Authors:** Tanbin Islam Rohan, Pranjol Sen Gupta, Tanusree Debi, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06823v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06823v1)

**Summary:** Large longitudinal cohorts often contain wrist accelerometry without optical heart-rate sensing, motivating recovery of cardiac information from motion signals already collected during sleep. We present SeqSmoother, a transformer-based temporal corrector for sleep heart rate (HR) estimation from wrist accelerometry. SeqSmoother combines spectral descriptors with an intermediate Nightbeat-derived frequency anchor and a physics-motivated sub-harmonic feature designed to identify harmonic frequency...

---

### 8. Private online learning and prediction for Littlestone classes

**Authors:** Amartya Sanyal

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06822v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06822v1)

**Summary:** We study mistake bounds for differentially private online learning and online prediction under oblivious realisable adversaries. Online learning requires the learner to release a hypothesis at each time step whereas in online prediction, the learner only needs to make predictions without releasing a hypothesis. Using a novel lower bound for private online learning and an upper bound for private prediction, we show that the sample complexity of these two problems are separated by a factor that gr...

---

### 9. Paradee: Distilling Kokoro-82M into an 8M-Parameter Single-Voice Text-to-Speech Model

**Authors:** Sahil Mahendrakar

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06817v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06817v1)

**Summary:** We distill Kokoro-82M, a widely used open text-to-speech model with 54 voices, into Paradee, an 8.07M-parameter model that speaks one of them. Paradee keeps Kokoro's architecture with much narrower layers, and each of its two halves is trained separately against the frozen teacher. It has 10x fewer parameters and needs 15x less compute. We first synthesize a corpus with the teacher and keep its durations, pitch, energy and phoneme features. We then train a small text side to predict these values...

---

### 10. Finding Gaussian Structure in Bosonic States

**Authors:** Alvan Arulandu, Sitan Chen, Ziyun Chen, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06810v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06810v1)

**Summary:** We study agnostic tomography of pure bosonic Gaussian states: given copies of an arbitrary $n$-mode bosonic state $ρ$, the goal is to output a pure Gaussian state whose infidelity with $ρ$ is at most $\mathrm{opt} + ε$, where $\mathrm{opt}$ is the minimum infidelity achievable by any pure Gaussian state.   We give efficient protocols achieving this in both the high and low fidelity regimes. When $\mathrm{opt}$ is below some universal constant, our protocol has runtime and copy complexity which i...

---

### 11. Block Disentanglement in CRL: Bridging Identifiability and Visual State Estimation

**Authors:** Emre Acartürk, Pranamya Kulkarni, Puranjay Datta, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06809v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06809v1)

**Summary:** Causal representation learning (CRL) is the process of recovering causally-related latent variables from high-dimensional observations. As a label-free inference method, CRL is particularly attractive for applications where data labels are unavailable or impractical to obtain. While there has been significant progress in understanding the identifiability guarantees of CRL, such guarantees often hold under highly stylized assumptions, which temper the direct application to real-world problems. Th...

---

### 12. H-JEPA: End-to-End Learning of Hierarchical World Models for Visual Planning

**Authors:** Wancong Zhang, Basile Terver, Michael Rabbat, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06805v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06805v1)

**Summary:** Long-horizon planning with latent world models requires reasoning across timescales and levels of abstraction. Existing task-agnostic JEPA world models predict and plan at a single timescale or with multiple horizons in one shared latent space. We introduce H-JEPA, an end-to-end recipe for training a hierarchy of action-conditioned JEPAs in which each level predicts farther ahead in its own learned latent space. Planning proceeds top-down: the top level optimizes progress toward the goal, and ea...

---

### 13. Sharpen Without Search: On-Policy Distillation of Sequence-Level Power Distribution

**Authors:** Erfan Baghaei Potraghloo, Seyedarmin Azizi, Arya Fayyazi, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06804v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06804v1)

**Summary:** A language model can give a correct answer more probability than any single incorrect answer and still usually sample an incorrect one, because the incorrect answers together hold more probability. The power distribution raises each complete answer's probability to a power above one and renormalizes, shifting probability toward answers the model finds most likely (sharpening). Sampling from it improves reasoning without changing parameters, but needs many scored candidates per query. We show tha...

---

### 14. A Response Theory Probe for Learned Stochastic AI Simulators, Tested on Lorenz-63

**Authors:** João Böger, Simon Driscoll, Niccolò Zagli, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06798v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06798v1)

**Summary:** Machine-learning emulators of chaotic and stochastic systems are usually validated on forecast skill and long-run statistics. Neither certifies that an emulator responds correctly to forcing, the property that projection and attribution studies rely on. Linear response theory makes this testable: the forced response follows from unperturbed correlations through a generalized fluctuation-dissipation relation, and decomposes over the stochastic Ruelle-Pollicott resonances of the Koopman generator....

---

### 15. Round-Trip KNN Clustering: multiscale hierarchical cluster detection on directed nearest-neighbour graphs

**Authors:** Eraldo Pereira Marinho, Caetano Mazzoni Ranieri, Fabricio Aparecido Breve

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06795v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06795v1)

**Summary:** We introduce Round-Trip KNN Clustering (RTKNNC), a graph-based method for finding cluster structure at several neighbourhood scales without requiring the number of clusters in advance. Unlike approaches that first make a $k$-nearest-neighbour (KNN) graph undirected, RTKNNC keeps both directions of the neighbour relation: which points a given point selects and which points select it. Incoming selections are treated as weighted votes that help decide which local connections remain visible during a...

---

### 16. How to scale your HEP ML models: A recipe for robust architecture comparisons at scale

**Authors:** Matthias Vigl, Nikita Pond, Jackson Barr, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06784v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06784v1)

**Summary:** Much of the recent progress in machine learning domains such as language models has come from scaling laws that predict performance as a function of training effort. In high-energy physics (HEP) similar behavior has now been observed. To aid further study, we present a systematic procedure to derive robust scaling laws and compare design choices on the relevant budget axes for HEP tasks. We first validate the full scaling trajectory on toy problems and then apply the procedure to multi-task tran...

---

### 17. IdeaLens: Detecting AI Ideas in Long-form Writing

**Authors:** Rishanth Rajendhran, Minjoon Choi, Jenna Russell, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06778v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06778v1)

**Summary:** While modern AI detectors identify who wrote the words, emerging policies on AI use increasingly hinge on a different question: who came up with the ideas? We introduce IdeaLens, a detector that identifies whether a document's ideas came from a human or AI (idea provenance), regardless of who wrote its words. To focus IdeaLens on ideas rather than prose, we represent documents as outlines: lists of items that each pair a discourse role with a brief, paraphrased description of the content, minimi...

---

### 18. On Learning Optimal Corners in Orthogonal Partially Observable Cooperative Guard Art Galleries

**Authors:** Yassin Ben Mansour, Edwin Meriaux

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06777v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06777v1)

**Summary:** The CADENCE algorithm solves the Partially Observable Cooperative Guard Art Gallery Problem (POCGAGP) with formal coverage and connectivity guarantees, but leaves unspecified which valid corner each agent should be deployed to, a choice that strongly affects efficiency. We introduce two learned corner-selection heuristics that preserve these guarantees: a CNN scoring candidates on a grid encoding, and a GATv2 network trained with Deep Q-Learning (DQN) on a visibility graph. Across 7,500 runs on ...

---

### 19. Singular parameters and missing limits in neural PDE solvers

**Authors:** Daniel Fernández

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06770v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06770v1)

**Summary:** Neural solvers for partial differential equations (PDEs) can approach an accurate solution while their parameters grow without bound. In such cases, the limiting solution may have no finite representation in the chosen model, leaving the best loss unattained. Our analysis connects missing limits in deep neural tanh- networks to unbounded hidden parameters or increasingly redundant neurons. For a class of models built from translated kernels, we describe the missing functions and recover them by ...

---

### 20. MatrixFormer: A Foundation Model for Matrix Completion

**Authors:** Dwaipayan Saha, Jacob Feitelberg, Kyuseong Choi, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06751v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06751v1)

**Summary:** Matrix completion underlies problems from tabular imputation to causal inference, yet existing tabular foundation models treat it as entry-by-entry prediction, repeating context for every target and discarding the matrix's two-dimensional structure. We introduce MatrixFormer, a pre-trained matrix-native transformer that predicts a full distribution for every missing entry in a single forward pass. MatrixFormer is trained entirely on synthetic low-rank and latent-factor matrices under diverse mis...

---

### 21. BazaarBench: Delegation Safety in Decentralized C2C Marketplaces Run by LLM Agents

**Authors:** Ziyan Wang, Shuqing Shi, James Oldfield, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06748v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06748v1)

**Summary:** In decentralized consumer-to-consumer (C2C) marketplaces, people list goods, negotiate with strangers, and rate one another, so trust rests on reputation. Large language model (LLM) agents now act for users, raising risks to their money, privacy, and reputation. We introduce BazaarBench, a simulated C2C marketplace and benchmark for evaluating the safety of these agents. It tracks ownership, item condition, and commitments across transactions, combining record checks with rubric-based LLM judgme...

---

### 22. Hyperbolic Graph Representation Learning: Embed in One Metric, Optimize with Another

**Authors:** Federico Larroca, Paola Bermolen, Marcelo Fiori, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06745v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06745v1)

**Summary:** Hierarchical graphs embed in hyperbolic space with lower distortion than in Euclidean space owing to its negative curvature. However, their gradient-based learning is hampered at large radii, where the Poincaré ball and the Lorentz hyperboloid models fail numerically. Polar coordinates avoid this problem, but the hyperbolic metric scales the angular step by the hyperbolic sine of the radius, freezing angular motion. We observe that this factor is a choice, silently fixed by existing implementati...

---

### 23. ufakzeka-karar: An Open Turkish Typed-Decision Model with Order-Invariant Option Scoring

**Authors:** Sait Furkan Teke

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06744v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06744v1)

**Summary:** ufakzeka-karar is an open Turkish decision model with 182,494,466 parameters. Given a Turkish text and questions of a fixed answer type (a choice, a level on an ordered scale, or yes or no), it returns a temperature-scaled probability for every option and an expected error that serves as a "not sure" signal, without generating text and in one CPU forward pass for up to ten options. Built on the lab's ufakzeka-1-base, its head scores each option blind to the others at shared positions, so the ans...

---

### 24. Decoupling Time and Space: A Temporally Conditioned Refinement for EEG Source Imaging

**Authors:** Marco Morik, Jesse Palarus, Carmen Vidaurre, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06726v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06726v1)

**Summary:** Electroencephalography (EEG) offers millisecond temporal resolution, but inferring underlying neural sources is a severely ill-posed spatial inverse problem. While deep learning has advanced spatial reconstruction, current architectures face a critical dilemma: frame-by-frame models discard vital temporal context, whereas full 4D spatiotemporal networks introduce an architectural trade-off between reconstruction accuracy and inference cost. We propose a novel two-stream framework that explicitly...

---

### 25. BRANCH-MoE: Balance-Aware Tree Routing for Large Embedding Models

**Authors:** Gang Fu, Adel Javanmard, MohammadHossein Bateni, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06725v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06725v1)

**Summary:** Mixture-of-experts (MoE) layers increase model capacity without a proportional increase in per-example computation. However, conventional flat routers can yield imbalanced expert utilization and treat experts as an unstructured collection, whose indices carry no topological meaning. We introduce {\bf BRANCH-MoE}, a routing architecture that places \(E\) experts at the leaves of a binary decision tree of depth \(\log_2 E\). At each internal node the branching probability is centered on the arriva...

---

### 26. Out-of-control Hamiltonian Learning

**Authors:** Weiyuan Gong, Muzhou Ma, Sitan Chen, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06709v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06709v1)

**Summary:** Learning the Hamiltonian of a many-body system from its dynamics is a central task in quantum science, yet the algorithms with the strongest provable guarantees assume some level of quantum control--fast, arbitrary single-qubit gates interleaved with time evolution, and measurements in arbitrary bases--that is beyond the capabilities of near-term analog quantum simulators. Motivated by analog atom- and ion-based platforms, we study Hamiltonian learning under minimal access models.   Uniform stat...

---

### 27. Reading the Mood: Emotion-Guided Book-to-Music Recommendation via CGANs and LLMs

**Authors:** Manousos Linardakis, Georgios Alexandridis

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06703v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06703v1)

**Summary:** Background music that matches the mood of a text has been shown to make readers feel more immersed and improve their reading experience, motivating recommender systems that pair books with mood-matched music. In this direction, we present Sentiment Aware Generative Adversarial Network for Cross Domain Recommendation (SAGA-CDR), a two-phase cross-domain recommendation framework that personalizes music suggestions and emotionally aligns them with the book being read. In the first phase, transforme...

---

### 28. A Solvable Model of Adaptive Learning Rate Rescaling: Acceleration, Stability & Scaling

**Authors:** Itay Lavie, Clarissa Lauditi, Cengiz Pehlevan

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06701v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06701v1)

**Summary:** A recurring design principle in modern optimizers is to decouple update magnitude from the raw gradient norm, yet its consequences for learning-curve and resource scaling remain unclear. We isolate this mechanism by studying normalized SGD in a random-feature model with power-law teacher and data covariance. Fixed-norm updates induce an effective learning rate that grows as gradients shrink. We derive a dynamical mean-field theory (DMFT) describing the joint dependence of the loss on training ti...

---

### 29. To Learn is to Wander: Learning Across Graphs and Tasks with Random Walks

**Authors:** Louis Tichelman, Xingyue Huang, Jinwoo Kim, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06694v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06694v1)

**Summary:** Graph foundation models aim to transfer across graphs, feature spaces, relational schemas, and prediction tasks, yet existing approaches typically generalize only within particular graph modalities or tasks. We propose Wander, a graph foundation model designed to operate across these settings within a single pretrained checkpoint. Following the prior-predictive perspective, we formulate graph learning as completion of a partially observed graph. We realize this task-general view through a common...

---

### 30. Adapting prior-data fitted networks for tabular anomaly detection

**Authors:** Maximilian Bershtman, Niv Cohen

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06693v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06693v1)

**Summary:** While deep features have transformed anomaly detection in images and video, their impact on tabular data has been less substantial, partly due to the limited availability of strong deep representations. Recently, prior-data fitted networks (PFNs) have emerged as a promising source of such representations for tabular data. In this work, we investigate how PFN representations can be adapted and leveraged for anomaly detection. The question is harder than it looks. No anomalies are available before...

---

### 31. Revisiting Label-Free Speaker Embedding Enhancement with vMF Profile Likelihood

**Authors:** Seunghwan Kim, Jinyong Kim, Sooyoung Yang, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06691v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06691v1)

**Summary:** Embedding enhancement improves speaker verification under acoustic mismatch without modifying a frozen backbone. Recent work has established a practical label-free setting for this task, but often adopts increasingly structured formulations. Here, the clean target is directly observed during training, making enhancement a matching problem on the unit hypersphere. We model the clean target with a von Mises--Fisher (vMF) likelihood and profile out a sample-wise concentration parameter, yielding a ...

---

### 32. OVAL: Output-Aware Local Page Bases for KV Cache Retrieval

**Authors:** Ashkan Shahbazi, Chayne Thrash, Soheil Kolouri

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06686v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06686v1)

**Summary:** Long context inference with large language models becomes increasingly expensive as attention must operate over an ever growing KV cache. Page sparse attention reduces this cost by representing each KV page compactly and retrieving only a subset for each query. Existing retrieval methods are designed to estimate attention scores or page relevance, but their objectives do not directly account for how approximation errors affect the resulting value weighted attention output. We introduce \method{}...

---

### 33. Aligning Multimodal Patient Evidence with Biomedical Knowledge Graphs for Clinical LLMs

**Authors:** Jiawen Du, Arshan Ali Khan, Chenhao Zhang, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06685v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06685v1)

**Summary:** Clinical questions often depend on linking a patient's multimodal evidence to external biomedical knowledge, yet existing predictive systems rarely represent such links explicitly, so they can neither be traced to their evidence sources nor removed to measure their contributions. We present MM-KG (Multimodal Knowledge Graph), which represents heterogeneous, multimodal patient observations and biomedical concepts as separate layers in one typed graph, joined by explicit alignment edges. First, mo...

---

### 34. Closing the Context Gap: Activation Alignment for Tabular In-Context Learning

**Authors:** Yoel Zeldes

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06679v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06679v1)

**Summary:** Tabular foundation models perform in-context learning (ICL) by conditioning predictions on labeled training examples provided as context. Unlike traditional models that separate training from inference, these models must process all training examples in every forward pass, making each prediction expensive. Restricting the number of training examples reduces this cost but substantially degrades performance. Instead of discarding context, we propose activation alignment, a method that leverages th...

---

### 35. How Sparse Probability Maps Shape Mixture-of-Experts Routing

**Authors:** Tomás Brogueira, Marcos Treviso, Miguel Couceiro

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06677v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06677v1)

**Summary:** Mixture-of-experts (MoE) routers typically apply softmax to the router scores and keep the top-K experts, making every token use exactly K experts. Sparsity-inducing probability maps such as sparsemax, alpha-entmax and normmax can adaptively assign exact zeros to selected experts, and therefore appear to offer token-dependent expert participation, even when using the same top-K machinery. In this work, we study whether and how this sparsity survives training. We train matched 300M and 1B top-2 M...

---

### 36. Improved Convergence of Large Stepsize Gradient Descent for Logistic Regression

**Authors:** Xiaochuan Gong, Ang Li

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06675v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06675v1)

**Summary:** We study gradient descent (GD) with a large constant stepsize for logistic regression on linearly separable data. Existing analysis shows an accelerated rate of $\widetilde{O}(1/\sqrtε)$ to reach loss $ε$ with an aggressive stepsize, although the loss may initially oscillate. Tighter control of the oscillatory dynamics has been available only for two-dimensional data. We prove a substantially faster rate in arbitrary dimension: GD with a large stepsize $η=1/ε$ reaches loss $ε$ within $O(\ln^{p}(...

---

### 37. Detecting Nighttime Anomalies from NASA Black Marble Using a Generalized Spatio-Temporally Robust Framework of Machine Leaning Ensembles

**Authors:** Srija Chakraborty

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06674v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06674v1)

**Summary:** Nighttime lights from NASA's Black Marble product suite capture thermal and light emission signals from anomalous events including fires, volcanic eruptions, and gas flaring. Existing detection approaches rely primarily on thermal bands, limiting sensitivity to weaker signals. We propose a novel machine learning framework that jointly models Black Marble M-band and Day/Night Band (DNB) signals to derive a generalized, spatio-temporally robust ensemble of anomaly detectors. The framework iterativ...

---

### 38. Learning What to Imitate: Entropy-Aware Distribution Mixing

**Authors:** Juan Garcia Giraldo, Matteo Santelmo, Eduard Durech, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06671v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06671v1)

**Summary:** Small language models are often post-trained as students on reasoning traces from stronger teacher models to efficiently learn new skills. However, token-level imitation on traces that lie far outside the student's expected distribution often produces \textit{confident conflicts}, whereby the student is required to imitate a continuation that it deems unlikely (i.e., low-probability) despite being confident in a different continuation (i.e., in a low-entropy state). To mitigate the degradation i...

---

### 39. What Matters for Latent Reasoning with Flow Matching

**Authors:** Yassine Ouali, Adrian Bulat, Georgios Tzimiropoulos

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06666v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06666v1)

**Summary:** Latent reasoning lets a large language model (LLM) think in a continuous space and verbalize only the answer. We argue that an effective latent thought must meet five requirements: it should be useful, helping produce the correct answer rather than merely changing it, diverse, so that resampling yields different reasoning trajectories, explainable, so that a decoded chain of thought (CoT) reflects reasoning the answer actually follows, refinable with more inference compute, and efficient, costin...

---

### 40. TrustmeWatcher: An Application for Workplace Micro-Sensing and Explainable Well-Being Feedback

**Authors:** Chengyu Yu, Leon Jacopo Costa, Zoja Anžur, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06657v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06657v1)

**Summary:** Workplace sensing studies combine long-running behaviour traces with self-reports, yet the tools that collect those data often sit apart from the interface that returns results. We present TrustmeWatcher, the application built for the TRUST-ME project to connect this work. TrustmeWatcher reuses ActivityWatch's OS-level watchers for computer-activity collection and adds its own application layer. It turns the collected traces into an interactive screen-time dashboard, synchronizes responses from ...

---

### 41. The Birkhoff Geometry of Manifold-Constrained Hyper-Connections: Two Channels, Vertex Viscosity, and Sinkhorn as a Retraction

**Authors:** Xiaoyu Li, Zhizhou Sha, Chiwun Yang

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06653v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06653v1)

**Summary:** Hyper-connections widen the residual stream of a Transformer to $n$ parallel streams. Their manifold-constrained version (mHC) mixes the streams at each layer with a doubly stochastic matrix, which it computes by Sinkhorn normalization of exponentiated logits. We give a geometric theory of this design on the Birkhoff polytope. First, a doubly stochastic mixer splits the stream into a mean channel, on which mHC is exactly a residual network, and a difference channel, which each layer contracts by...

---

### 42. Considering Context: When World Models Need Context Encoders

**Authors:** Oleg Smirnov, Sofiane Ennadir, John Pertoft, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06651v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06651v1)

**Summary:** Methods for generalization in model-based reinforcement learning typically assume that an agent cannot recover the latent context governing the environment dynamics from its own experience, and therefore supplies it externally. We formalize and test this assumption with \emph{predictive sufficiency}, which quantifies what access to the context adds to next-step prediction under the visitation distribution an agent induces, and separates that quantity into a history-recoverable part, a residual r...

---

### 43. Representation-Space MMD for Diffusion Language Models

**Authors:** Ilya Drobyshevskiy, Ilia Sudakov, Maksim Semenov, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06648v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06648v1)

**Summary:** We introduce a post-training method for diffusion language models (DLMs) that minimizes Maximum Mean Discrepancy (MMD) between generated and reference distributions in the feature space of a frozen pretrained DLM. To estimate MMD, we retain contextual features at individual token positions, obtaining multiple observations per sequence from a single extractor pass. We optimize this objective using policy gradients for discrete models and direct differentiation through generated latents for contin...

---

### 44. Beyond the Model: The Critical Role of Data Filtering in Clinical Machine Learning

**Authors:** Noah Subedar, Colin Campbell, Wenjing Zhang, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06640v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06640v1)

**Summary:** Machine learning (ML) studies using clinical data often rely on preprocessing and filtering pipelines before model development. The filtering decisions made in these pipelines can alter the dataset's statistical structure and may artificially reduce or increase the complexity of the prediction task. We argue that filtering choices should be treated as part of the scientific method rather than as a routine preprocessing step. We further discuss the need for explainable and transparent preprocessi...

---

### 45. Differentially Private Mixing of Public Datasets Improves Private Learning

**Authors:** Yufei Chen, Tejumade Afonja, Anvith Thudi, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06636v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06636v1)

**Summary:** Many machine learning applications involve sensitive data and therefore require training under differential privacy (DP). However, DP training often degrades model utility. In some cases, first pre-training the model on "public" data before finetuning with DP on the sensitive data can reduce the drop in utility. However, the success of this depends on how relevant the selected public dataset is to the sensitive data. We introduce the first pipeline that privately learns the mixture of several pu...

---

### 46. Inverse Cross-spectral Neural Networks for Multivariate Time Series

**Authors:** Lorenzo Marinucci, Leonardo Di Nino, Gabriele D'Acunto, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06630v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06630v1)

**Summary:** CoVariance Neural Networks and their extensions have emerged as effective tools for processing multivariate data, deriving graph shift operators directly from second-order statistics. These architectures, however, are designed for independent and identically distributed observations and do not fully capture the joint structure of temporal and cross-variable dependencies in multivariate time series. In this work, we introduce Inverse Cross-Spectral Neural Networks (iCSNNs), a class of graph neura...

---

### 47. On the Cardinality of Optimal Representations in the Binary-Source Information Bottleneck

**Authors:** Dier Tang, Jun Chen

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06627v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06627v1)

**Summary:** The information bottleneck (IB) seeks a representation $U$ of a source $X$ that retains as much information as possible about a target $Y$, subject to a constraint on $I(U;X)$. A classical argument shows that it suffices to consider representations with at most $|\mathcal{X}|+1$ symbols, and this bound is known to be tight whenever $|\mathcal{X}| \geq 3$. We show that the binary case behaves differently: if $X$ is binary and $Y$ is finite, then for every joint distribution of $(X,Y)$ and every r...

---

### 48. Frozen Factor or Spectral Band? Disentangling Two Choices in Low-Rank LoRA

**Authors:** Adnan Slimane Ali, Ayoub Belfatmi, David Ngwe Pouth

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06621v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06621v1)

**Summary:** Spectral variants of low-rank adaptation (LoRA) choose both a subspace and which factor to freeze. We separate these choices by freezing the input factor A or output factor B on the top or bottom singular directions of pretrained weights, with learning rates selected separately. At rank 2, the same-band advantage of freezing A is larger than either within-factor band difference on all four task-model pairs with complete comparisons. Freezing B also trails comparable-budget free LoRA by 8-18 perc...

---

### 49. RealtimeWAM: One-Step Asynchronous World Action Models

**Authors:** Chengtao Lv, Jinyang Du, Shuyi Feng, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06617v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06617v1)

**Summary:** World Action Models (WAMs) incorporate visual representations from video generation backbones to guide action prediction. Recent efficient WAMs adopt Mixture-of-Transformers (MoT) architectures and compute video representations once for reuse by the action expert. However, intra-expert iteration (\ie, multi-step action denoising) and inter-expert waiting (\ie, sequential execution of the video and action experts) still limit inference efficiency. To this end, we present RealtimeWAM, an extremely...

---

### 50. The Surrogate Is Not the Reward: Post-Surrogate Primary-Outcome Acquisition in Contextual Bandits

**Authors:** Kyungbok Lee, Michael R. Kosorok

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06610v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06610v1)

**Summary:** We study contextual bandits in which a surrogate is observed after the action but before the learner decides whether to acquire the primary outcome that defines action value and regret. The value of acquiring the primary outcome depends on both decision relevance (how much the current outcome matters for comparing policies) and the residual uncertainty after observing the surrogate. The Audited Surrogate Bandit (ASB) learns a contextual policy while allocating a budget of $B$ primary-outcome acq...

---

## cs.NE

**50 papers**

### 1. Visual Swarm Navigation via Deep Reinforcement Learning and Evolutionary Hybrid Design

**Authors:** Álvaro Díez, Fidel Aznar

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06400v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06400v1)

**Summary:** Swarm robotics presents a robust and cost-effective paradigm for advanced automation in complex, dynamic environments, such as those encountered in search and rescue or environmental monitoring. A fundamental challenge for this field is the data-driven design of decentralized controllers capable of generating emergent collective behaviors. This paper proposes a novel, AI-driven hybrid methodology for the automatic synthesis of swarm robotic controllers for autonomous visual navigation. This appr...

---

### 2. A Flexible and Generic Approach for Explainable Landscape Analysis and the pyXla Toolbox

**Authors:** Tony Ombaso, Anna S. Bosman, Arnaud Liefooghe, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06359v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06359v1)

**Summary:** Landscape analysis has been successfully applied to understand complex optimisation problems, gain insights into algorithm behaviour, and automate algorithm selection and configuration. Although many landscape analysis techniques have been developed over the last decades, it remains difficult for researchers and practitioners to decide which approaches are appropriate and to implement them in practice. Some tools are available, but these are either restricted to particular problem domains (e.g.,...

---

### 3. From communication to computation in neurons-on-a-chip: an in silico study of neurotopomorphic computing

**Authors:** Michael Taynnan Barros

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06065v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06065v1)

**Summary:** Living neuronal networks transform inputs through recurrent cellular and population dynamics, yet it is unknown which network architecture supports which computation. Neurons-on-a-chip turn this question into a design problem because microchannels guide axonal growth and set the network architecture. We introduce IC$^3$, an Integrated Characterisation of Communication-Driven Computation, which characterizes network state through neuronal dynamics, functional communication, and structural support...

---

### 4. Optimization Geometry of QAOA and Variational Quantum Algorithms

**Authors:** Vojtěch Novák, Ivan Zelinka, Silvie Illésová, et al.

**Published:** 2026-10-04

🔗 [Paper](http://arxiv.org/abs/2610.05524v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05524v1)

**Summary:** Variational quantum algorithms turn choices of Hamiltonian, ansatz, and parameterization into a classical nonconvex optimization problem. We study how this objective function can be visualized and characterized in ways that help explain optimizer behavior. We distinguish two properties of the objective: the number of local minima encountered along sampled directions and the differences in quality among local-search endpoints. We then ask how a local optimizer, represented by BFGS, compares with ...

---

### 5. AgentDiscover: Autonomous Discovery with Minimal Search Scaffolding

**Authors:** Mahdi Farahbakhsh, Ilan Sela, Fatemeh Doudi, et al.

**Published:** 2026-10-04

🔗 [Paper](http://arxiv.org/abs/2610.05334v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05334v1)

**Summary:** Frameworks that use large language models for scientific discovery typically rely on a fixed, human-designed algorithm that decides what the model sees at each step, leaving the model only the role of proposer. The model knows nothing of the search beyond what it is shown. As models grow more capable, a question arises: does a search strategy chosen by a human before the run scale better than promoting the model from proposer to planner and letting it own the search? The Bitter Lesson suggests t...

---

### 6. MOXIE: Discovering Alternative Explanations for Biomedical Image Classifiers

**Authors:** Abiha Tahsin Chowdhury, Rahul Dubey

**Published:** 2026-10-03

🔗 [Paper](http://arxiv.org/abs/2610.04814v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04814v1)

**Summary:** Segment-based explanation methods such as LIME return a single explanation for each prediction, computed from one fixed image segmentation. This hides two important facts: a prediction can be supported by many different sets of image segments, and the segmentation itself shapes which explanations can be found. We introduce MOXIE (Multi-Objective eXplanation Imaging Engine), an evolutionary framework that searches for segment subsets that preserve the classifier's confidence while keeping as litt...

---

### 7. Active-DiNTS: Active Differentiable Network Topology Search

**Authors:** Gean Trindade Pereira, Thierry Urruty, Muriel Visani, et al.

**Published:** 2026-10-03

🔗 [Paper](http://arxiv.org/abs/2610.04787v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04787v1)

**Summary:** Neural Architecture Search (NAS) has proved to be a strong alternative to manual network design, but applying it to 3D medical image segmentation is limited by two well-known costs, large annotation budgets and multi-GPU clusters. Thus, this paper introduces Active-DiNTS (Active Differentiable Network Topology Search), an approach that embeds pool-based Active Learning (AL) into a bi-level differentiable topology search to perform architecture discovery and label curation jointly. At each query ...

---

### 8. Robust Optimization of Spring Design under Variable Manufacturing Tolerances

**Authors:** Grzegorz Sroka, Slawomir T. Wierzchon

**Published:** 2026-10-03

🔗 [Paper](http://arxiv.org/abs/2610.04656v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04656v1)

**Summary:** A reliable assessment of an optimizer robustness requires tracking controlled changes in parameters to identify sources of algorithmic weakness. Such an approach was applied to the problem of designing tension/compression springs with three continuous variables describing the spring geometry.   Three additional independent binary parameters reflect material variability, manufacturing-related geometric deviations, and an additional safety margin. Without expanding the decision space, these parame...

---

### 9. Chance-Constrained Bi-Objective Evolutionary Optimization for the Open-Pit Mining Operational Planning Problem

**Authors:** Ishara Hewa Pathiranage, Aneta Neumann

**Published:** 2026-10-03

🔗 [Paper](http://arxiv.org/abs/2610.04227v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04227v1)

**Summary:** Open-pit mining operational planning involves allocating limited resources while satisfying production, equipment, and ore-quality requirements. Existing approaches often assume deterministic ore grades or rely on simulation-based evaluation under uncertainty. In this paper, we propose a chance-constrained bi-objective formulation of the open-pit mining operational planning problem under uncertain ore grades. We aim to maximize ore production and minimize fleet cost while satisfying stochastic q...

---

### 10. Adaptive Operator Selection in Bilevel Large Neighborhood Search for Electric Autonomous Dial-a-Ride Problem under Uncertainty

**Authors:** Ishara Hewa Pathiranange, Aneta Neumann

**Published:** 2026-10-03

🔗 [Paper](http://arxiv.org/abs/2610.04219v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04219v1)

**Summary:** The electric autonomous dial-a-ride problem (EADARP) extends the classical dial-a-ride problem by incorporating battery and charging constraints for electric vehicles. In practice, travel-time uncertainty can cause violations of time-window constraints. Large neighborhood search is effective for solving the EADARP, but its performance can depend on the choice of insertion operator during the repair phase. This paper investigates insertion-operator selection within a bilevel large neighborhood se...

---

### 11. AdaEva: Accelerating LLM-Driven Algorithm Design with Adaptive Partial Evaluation

**Authors:** Tai Nguyen, Fei Liu, Phong Le, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03896v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03896v1)

**Summary:** Large Language Models (LLMs) are increasingly used for automated algorithm design. However the computational cost of evaluating the generated algorithms can be excessive. We consider the common LLM-driven automated algorithm design (LLM4AD) setting in which a candidate algorithm is evaluated by aggregating its performance over a shared set of training instances. This instance-wise structure raises a natural question: must every candidate be evaluated on the entire instance set before deciding wh...

---

### 12. FrugalEvo: Towards Cost-Aware LLM-Guided Program Evolution

**Authors:** Hui Chen, Xuan Qi, James Xu Zhao, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03675v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03675v1)

**Summary:** LLM-guided evolutionary methods, such as AlphaEvolve, have emerged as powerful approaches for challenging computational optimization problems, such as circle packing. However, prior work typically optimizes performance gain over a fixed number of iterations. We argue that practical optimization should maximize gain per unit cost. To this end, we propose FrugalEvo, a cost-aware evolutionary framework where a stronger, higher-cost LLM explores solution strategies, and a cheaper LLM implements them...

---

### 13. Parallel Time-Aligned Spiking Self-Attention for Consistent Integer-Valued Training and Spike-Driven Inference

**Authors:** Peng Xue, Wei Fang, Kaiwei Che, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03291v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03291v1)

**Summary:** Integer-valued leaky integrate-and-fire (I-LIF) neurons and spike firing approximation (SFA) reduce temporal training cost by representing spike trains as firing counts and normalized firing rates, respectively. However, applying spiking self-attention (SSA) directly to these compressed query, key, and value representations introduces cross-time interactions that are absent during spike-driven inference. We term this operator-level discrepancy Temporal Interaction Mismatch (TIM). We propose Para...

---

### 14. The Investment Acceleration Principle Revisited by means of a Neural Network

**Authors:** Guido Fioretti

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03282v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03282v1)

**Summary:** The investment acceleration principle is a heuristic for modelling investment time series out of consumption time series. The model presented herein develops a disaggregated accelerator equation whose coefficients are the weights of a Kohonen neural net that represents firms' decision-making. According to this model, investments take place when managers recognise emerging technological patterns. Furthermore, a technique borrowed from the theory of self-organising systems is used in order to dise...

---

### 15. Self-Repairing Recurrent Ensembles for Real-Time Recovery from Distribution Shift

**Authors:** Julian Lemmel, Pedro D. Wendel Garcia, Taisuke Kobayashi, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03249v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03249v1)

**Summary:** Deploying a pretrained controller exposes it to conditions that are absent from its training data. Sensor drift, outright sensor failure and accumulating measurement noise all induce a distribution shift that can collapse an otherwise competent policy; typically at a point in time where no expert is available to supply corrective labels. We present a method that lets a policy recover from such shifts online and without supervision. Our controller is an ensemble of recurrent networks, each of whi...

---

### 16. Evolving Hybrid Quantum-Classical Architectures for Image Classification

**Authors:** Devroop Kar, Daniel Krutz, Travis Desell

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03220v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03220v1)

**Summary:** Hybrid quantum classical neural networks integrate parameterized quantum circuits (PQCs) with established deep learning architectures, but their performance depends strongly on the choice of quantum circuit architecture, a choice that remains largely manual. Most existing approaches rely on hand-designed or fixed circuit ansätze, requiring circuit structure, gate composition, and qubit connectivity to be specified in advance with no guarantee that they suit the task. This limitation is especiall...

---

### 17. Distribution Matching Evolutionary Algorithms for Rare Event Sampling

**Authors:** Yonatan Gideoni, Yarin Gal

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03833v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03833v1)

**Summary:** A novel discovery is one which is both useful and surprising: a generative model's output is a useful discovery if it has a low probability of being generated (it's surprising) and a high reward (it's useful). Global optimization can directly increase the probability of sampling high rewards but typically requires updating model weights. Such gradient based optimization is expensive and bars using capable closed-source models. Instead, modern search methods for discovery sacrifice the global tar...

---

### 18. Aggregate accuracy conceals concentrated temporal vulnerability in a spiking speech classifier

**Authors:** İsmail Can Dikmen

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03155v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03155v1)

**Summary:** Aggregate accuracy cannot reveal which utterances are locally vulnerable or how internal activity changes when labels remain stable. We retain every prediction for 725,070 adjacent-bin, one-count changes around 100 validation utterances of a frozen SpikeSCR-based classifier. The canonical native-horizon GPU singleton path reaches 86.0836% validation accuracy. Equal-source expected accuracy under a uniformly chosen neighbor rises from 84.00% to 84.54%, although 13 of 84 initially correct sources ...

---

### 19. Learning While Inferring: Local and Parallel Learning for Edge SNNs across Sensing Modalities

**Authors:** Yanxun Zhang, Yifei Wang, Changze Lv, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03149v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03149v1)

**Summary:** Edge intelligence requires models to sense continuously in real time and to keep adapting on-device, all under tight compute, energy, and memory budgets. Although spiking neural networks (SNNs) enable efficient event-driven inference, standard surrogate-gradient backpropagation (BP) serializes updates and blocks ongoing inference. We investigate Bidirectional Spike-Based Distillation (BSD) as an on-device learning principle that lets edge SNNs learn while inferring. BSD couples a stimulus-driven...

---

### 20. Small universal multiset reaction systems

**Authors:** Andrei Paun, Annemarie-Beatrix Messner

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03021v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03021v1)

**Summary:** This paper presents a construction of a small universal machine within the framework of Multi-set Reaction Systems. We encode the machine state using elements that represent registers and instruction labels, and we enforce sequential execution by ensuring that reaction chains for a given instruction can only activate after the corresponding label element appears. We implement a universal register machine with 8 registers and 23 instructions, showing that the priority-based model requires 87 dist...

---

### 21. Temporal Geometry of Deep Networks: Hyperbolic Representations of Training Dynamics for Intrinsic Explainability

**Authors:** Ambarish Moharil

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03000v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03000v1)

**Summary:** Intrinsic explainability remains a challenging problem, particularly in contexts where multilayer perceptrons (MLPs) require dynamic re-training within an optimization environment. This paper investigates how MLPs and their training dynamics can be represented and studied in non-Euclidean spaces; our representation features the Poincaré model of hyperbolic geometry. We aim to capture the geometric evolution of their weighted topology and self-organization over time. Instead of restricting the an...

---

### 22. Evolutionary Computation for Trustworthy AI: From Attacks and Defenses to Self-Evolving Era

**Authors:** Junhao Dong, Chenkai Wang, Xuanhui Lin, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.02996v1) | 📄 [PDF](https://arxiv.org/pdf/2610.02996v1)

**Summary:** As Artificial Intelligence (AI) has evolved from task-specific models to foundation models and agents, the scope of trustworthy AI has expanded from model-level robustness to the reliability and safety of broader AI systems. This evolution has also expanded the attack surface from individual models to broader system-level interactions, including tool use, context, and interaction trajectories with dynamic environments. As a result, maintaining reliable and safe behavior under changing or deliber...

---

### 23. Evolutionary Giant Tour for CVRP using NSE and ML Heuristic]{Evolutionary Giant Tour approach for CVRP using Node Shift Encoding and Machine Learning repair heuristic

**Authors:** Souad Abdoune, Menouar Boulif

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.03816v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03816v1)

**Summary:** The Capacitated Vehicle Routing Problem (CVRP) remains a central concern in logistics research, as route optimisation under rigid capacity and fleet restrictions directly affects operational performance. Genetic Algorithms are widely used for this problem, yet their effectiveness depends heavily on the choice of solution encoding and on the mechanisms used to preserve feasibility during the search. This paper proposes a sequential framework that separates the evolutionary process from route cons...

---

### 24. SEDIMA: Cross-Run Hierarchical Insight Memory for Evolutionary Search Agents

**Authors:** Amirhossein Abaskohi, Mahdi Mostajabdaveh, Zirui Zhou

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.02361v1) | 📄 [PDF](https://arxiv.org/pdf/2610.02361v1)

**Summary:** Large language model (LLM)-driven evolutionary search is a powerful paradigm for automated program and algorithm discovery, yet existing systems are largely memoryless: each run explores from scratch, so agents repeatedly rediscover the same improvements and re-encounter the same dead ends. We introduce SEDIMA, a persistent hierarchical insight memory for evolutionary search agents. SEDIMA distills raw traces into natural-language insights, clusters them by semantic similarity using attention-we...

---

### 25. Spiking neural networks for streaming qubit readout

**Authors:** Barry M. Dillon, Aqib Javed, Jim Harkin, et al.

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.02129v1) | 📄 [PDF](https://arxiv.org/pdf/2610.02129v1)

**Summary:** Fast and accurate qubit-state assignment is essential for feedback, calibration, and error correction in quantum processors. In superconducting platforms, frequency-multiplexed readout makes this task intrinsically multivariate as measured traces can encode crosstalk, qubit-state relaxation events, and other transient nonidealities that are not fully captured by conventional matched filtering. Here, we introduce spiking neural network (SNN) discriminators for superconducting qubit readout. By pr...

---

### 26. TRACE: Tackling Real-World Resource Assignment Problems via Agentic Heuristic Design

**Authors:** Jose A. Ayala-Romero, Andres Garcia-Saavedra, Xavier Costa-Perez

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01887v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01887v1)

**Summary:** Dynamic resource assignment, the real-time allocation of task streams to heterogeneous processing nodes, is the backbone of modern computing infrastructure. While learning-based schedulers excel in research, industrial deployments still rely on hand-written rules that operators can read, audit, and execute within tight latency budgets. LLM-based Automatic Heuristic Design (AHD) promises to automate writing such rules. However, existing AHD frameworks were developed for combinatorial problems ful...

---

### 27. Continual Reinforcement Learning with Neuroevolution

**Authors:** Eleni Nisioti, Andrea Cossu, Kathrin Korte, et al.

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01583v2) | 📄 [PDF](https://arxiv.org/pdf/2610.01583v2)

**Summary:** Despite many studies about causes and remedies of plasticity loss in Reinforcement Learning (RL) under continual task changes, no RL method has yet consistently achieved a good balance between adaptation and forgetting. Here we turn to an alternative optimization paradigm, neuroevolution (NE): algorithms that search directly in weight space through mutation and selection over a population of neural networks. Across a wide array of environments and environmental changes, with policies ranging fro...

---

### 28. Controllable Stochastic Quantization Encoding for Adversarially Robust Spiking Neural Networks

**Authors:** Yujia Liu, Peiyu Liu, Yajing Zheng, et al.

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01558v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01558v1)

**Summary:** Spiking Neural Networks (SNNs) have attracted increasing attention due to their impressive temporal dynamics, energy efficiency, and brain-inspired mechanisms. Although SNNs have demonstrated promising performance in image classification tasks, recent studies have shown that they remain vulnerable to adversarial attacks, where imperceptible perturbations are added to input images to mislead model predictions. Existing defense methods mainly focus on training strategies, while the role of input e...

---

### 29. LESS: Lightweight Evolutionary Supernet Search in Minutes

**Authors:** Aviral Gandhi, Jinglue Xu, Jialong Li, et al.

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01468v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01468v1)

**Summary:** Low-cost NAS must both explore high-performing architectures and identify them reliably, yet reducing evaluation cost often weakens the fidelity of candidate comparisons. Training-free methods reduce evaluation cost by replacing learned task feedback with proxy signals measured at initialization. We introduce LESS (Lightweight Evolutionary Supernet Search), a data-driven method that combines a brief fair hard-path warm-up with discrete search under a single CMA-ES distribution. Each proposal is ...

---

### 30. Inherited Learning in an Artificial Ecology: How Controls and Update Allocation Shape Benefits

**Authors:** Xuening Wu, Lei Li, Shan Yu

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01232v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01232v1)

**Summary:** Learning can improve an individual's behavior, yet a population risks losing that experience whenever individuals die and are replaced. Inheriting learned preferences offers a way to preserve useful behavior across generations, raising a question for artificial populations: when does inheritance improve collective performance, and how can its benefits be measured fairly? The challenge is that inheritance changes not only offspring behavior but also survival, reproduction, and opportunities for f...

---

### 31. Increasing Width Allows Greedy Layer-wise Training to Rival End-to-End Backpropagation in Self-Supervised Learning

**Authors:** Syon Mansur, Joel Zylberberg

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2610.00753v1) | 📄 [PDF](https://arxiv.org/pdf/2610.00753v1)

**Summary:** End-to-end backpropagation has been the dominant mode of training in deep learning, allowing for the coordination of parameter updates across layers of a neural network. Prior studies have explored alternative -- and, in some cases, simpler -- training mechanisms, showing that they can sometimes achieve performance similar to backpropagation. However, the architectural conditions under which locally optimized networks, which avoid end-to-end backpropagation of error, can learn representations co...

---

### 32. Neuromorphic Pseudo-Random Number Generators with a Low Power Hardware Implementation

**Authors:** Jafar Shamsi, Navid Akbari, Sonia Sennik, et al.

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2610.00719v1) | 📄 [PDF](https://arxiv.org/pdf/2610.00719v1)

**Summary:** Pseudo-random number generation often requires trade-offs among quality, power consumption, and bandwidth to produce unpredictable sequences of numbers. The brain, on the other hand, efficiently generates unpredictable output complex network dynamics occurring in a high-dimensional state. This state, which is hypothesized to be chaotic, relies on the balance between excitation and inhibition. Here, we investigated if computational models of these chaotic balanced states can be harnessed for Neur...

---

### 33. The Quantum Sphere: A Physically Realizable Optimization Benchmark with Provable Linear Convergence in White- and Black-Box Settings

**Authors:** Ofer M. Shir

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2610.03788v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03788v1)

**Summary:** We revisit an established Quantum Control objective, characterize its exact local metric geometry, and reposition it as a rigorous benchmark for Search and Optimization. The trap-free topology of the landscape, established two decades ago, guarantees unhindered optimal pathways, but global topology alone does not govern convergence speed. Although the so-called Quantum Sphere is defined by the fourth power of the control field, we show that its yield gap admits an exact representation as a nonne...

---

### 34. Large Language Model-Guided Evolutionary Discovery of Native Neural Architectures for Spiking Sequence Modeling

**Authors:** Ruoyu Zhao, Jiaqi Wu, Chenyu Zhu, et al.

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.40258v1) | 📄 [PDF](https://arxiv.org/pdf/2609.40258v1)

**Summary:** Spiking neural networks (SNNs) offer low-energy sequence modeling through sparse, event-driven computation. However, interactions among spike encoding, neuronal dynamics, and information propagation complicate architecture design. Existing SNN sequence models often adapt artificial neural network (ANN) architectures designed for real-valued activations, potentially underusing spike-based communication and temporal state updates, motivating automated discovery of native SNN architectures. Most ev...

---

### 35. From DNA Design to DNA Slimming: Auditable Agentic Discovery of a Deletion-Only Designer

**Authors:** Joel Shor

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.40143v1) | 📄 [PDF](https://arxiv.org/pdf/2609.40143v1)

**Summary:** Compact regulatory DNA can free up space in vector payloads, reduce synthesis and assay burden, and expose which sequence features drive predicted activity. Yet most model-based nucleic-acid designers optimize fixed-length sequences through substitutions; they do not ask which bases of an existing functional element can be removed while retaining predicted activity. We define the task of sequence slimming as selecting an exact-length, order-preserving subsequence while retaining activity. Modele...

---

### 36. Toward Controlling Biology with Language:Offline Learning of Prompt-Conditioned Interventions for Cells, Organoids, and Biobots

**Authors:** Nam H. Le, Douglas Blackiston, Michael Levin, et al.

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2610.02247v1) | 📄 [PDF](https://arxiv.org/pdf/2610.02247v1)

**Summary:** Artificial intelligence increasingly serves as a natural-language interface to complex technical systems, letting people accomplish sophisticated tasks by describing what they want rather than specifying how to do it. Extending this interface to living systems is harder: unlike code or images, a biological intervention has no closed-form linguistic meaning, and the paired language-intervention-outcome data needed to learn such a mapping is expensive to collect, since each example requires its ow...

---

### 37. An Island-Based Parallel Biased Random-Key Genetic Algorithm for the Three-Dimensional Trailer Loading Problem

**Authors:** A. del Río, L. Díaz, L. C. de Vicente, et al.

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.39272v1) | 📄 [PDF](https://arxiv.org/pdf/2609.39272v1)

**Summary:** The Three-Dimensional Trailer Loading Problem (3D-TLP) involves determining the optimal placement and orientation of heterogeneous items within the confined space of a trailer while maximizing volume utilization and satisfying a wide range of complex logistical and safety constraints. The 3D-TLP is NP-hard, rendering exact optimization approaches computationally impractical for large-scale industrial applications. To address this challenge, we propose an enhanced Biased Random-Key Genetic Algori...

---

### 38. Null-model treatment of the sensory-motor boundary changes an evolutionary connectome comparison

**Authors:** Gyujeong Park

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.39248v1) | 📄 [PDF](https://arxiv.org/pdf/2609.39248v1)

**Summary:** Randomised copies of a connectome are the usual baseline for asking whether measured wiring matters, and the answer depends on what the randomisation preserves. We evolved embodied foraging agents whose brains are a compressed adult Drosophila connectome (FlyWire v783; 512 cell-type groups and 1,000 Kenyon cells) alongside agents built on randomised wiring, in pre-registered experiments with ten seeds, four ecologies and 600 generations. Two standard randomisations, a column shuffle and degree-p...

---

### 39. Evolutionary foraging in grids: Intermittent search dynamics emerge in finite, depletable landscapes

**Authors:** Shailendra Bhandari, Alex Szorkovszky, Anis Yazidi, et al.

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.39239v1) | 📄 [PDF](https://arxiv.org/pdf/2609.39239v1)

**Summary:** How search strategies evolve in finite, depletable landscapes remains a question in foraging theory. We study this problem with an evolutionary simulation in which agents forage on a two-dimensional toroidal lattice containing non-renewable resources distributed uniformly or as Lévy dust. Each agent carries a heritable genome encoding step lengths, velocities, and turning angles, and selection acts on a fitness function combining energetic gain, movement cost, and coverage efficiency. By allowin...

---

### 40. T-Router: Learning Thalamic Routing for Reasoning with Parameter-Efficient Reinforcement Learning

**Authors:** Liuxian Ma, Jiale Dai, Jiaqi Li, et al.

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.39109v1) | 📄 [PDF](https://arxiv.org/pdf/2609.39109v1)

**Summary:** Parameter-efficient reinforcement learning aims to improve reasoning with a compact trainable interface to a pretrained model. We introduce the Thalamic Router (T-Router), which concentrates adaptation on the reuse of completed computations. A compressed, addressable bank preserves block changes; a depth-recurrent controller conditions their selection and relative-scale writeback. This coupling gives thalamic context-dependent routing a concrete computational form: learn which earlier contributi...

---

### 41. Self-Evolving Algorithm-Design Agents: Escaping In-Context Evolutionary Stagnation via Population-Curated Policy Optimization

**Authors:** Chen Lu, Ke Xue, Siyuan Xu, et al.

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.38757v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38757v1)

**Summary:** Large language models are increasingly participating in complex real-world tasks in the form of algorithm-design agents, designing and refining algorithms. Many successful algorithm-design agents adopt pure in-context evolutionary frameworks, but they may quickly plateau in domains that require specialized knowledge. Parametric adaptation offers a way to internalize specialized knowledge, but conventional training requires abundant domain-specific corpora while high-quality algorithms are scarce...

---

### 42. How much of fly walking is written in the wiring?

**Authors:** Isabel Guan, Yuntian Zhao, Dingyuan Zhang, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38665v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38665v1)

**Summary:** Connectome models of the fly nerve cord generate walking-like motor rhythms, but oscillation alone does not show that the specific wiring matters. Here we provide, to our knowledge, the first test of which features of motor output depend on the specific wiring. We simulated the leg motor systems of two independent Drosophila connectomes, with synapse counts as fixed weights and glutamatergic synapses treated as inhibitory, and compared each with six families of rewired networks that preserve pro...

---

### 43. Behavioral Persistence and Incomplete Functional Transfer of Co-evolved Communication in Evolutionary Robotics

**Authors:** Fernando Montes-Gonzalez

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38527v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38527v1)

**Summary:** This work evaluates the direct transfer of a co-evolved communication protocol from a 2D simulation to a 3D physical environment, without retraining the network weights. Two e-puck-type robots, controlled by a GRU network with residual connection, were evaluated in a food-seeking task with social signaling. The sensory and motor translation layer required three corrections for stable physical operation, including the calibration of a hunger term based on a measurable asymmetry in the trained res...

---

### 44. Derandomizing Dense Binary Hypervector Codebooks for Quantized Scalars

**Authors:** Dmitri Rachkovskij, Evgeny Osipov, Olexander Volkov, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38471v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38471v1)

**Summary:** Hyperdimensional computing and vector symbolic architectures often represent quantized scalar levels by dense binary codebooks whose level-to-level similarity is intended to follow a prescribed function of scalar separation. At finite dimensionality, randomized scalar codebook constructions deviate from this target because of sampling noise, random-start imbalance, update-count fluctuations, component dependence, and finite-capacity effects. We develop a transition-based derandomization framewor...

---

### 45. Simulating Synchrony Loop Networks in the Open Source RISP Neuroprocessor

**Authors:** Jackson Mowry, Patrick Abbs

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38432v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38432v1)

**Summary:** Neuromorphic spiking neural networks (SNNs) offer a promising alternative to conventional deep neural networks for tasks with computational resource or data constraints. However, their practical applications have been limited by comparatively weak performance on complex learning tasks. Experimental approaches such as Synchrony Loop Propagation (SLP) increasingly seek to address this problem through more sophisticated and heterogeneous neuron models, and have achieved encouraging initial results....

---

### 46. Brain-SAD: A Brain-Inspired Safe Autonomous Driving Control Framework with Dynamic Fear-Oriented Constraint on Dual-Policy

**Authors:** Huan Rong, Chao Yin, Anouar Imel, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38016v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38016v1)

**Summary:** Constrained Reinforcement Learning has recently gained increasing attention in the field of Safe Autonomous Driving, where the general mechanism is to maximize the expected reward while keeping the overall action risk bounded. In this way, the safety issues arising in AD can be mitigated through constrained actions. However, existing Constrained RL methods still lack dynamics on the imposed constraints. For instance, the action cost adopted by the existing Primal-Dual/soft-constrained methods is...

---

### 47. Kolmogorov-Arnold Classifier Systems as Universal Approximators

**Authors:** Hiroki Shiraishi, Hisao Ishibuchi, Masaya Nakata

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37958v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37958v1)

**Summary:** As the input dimension $n$ grows, rule-based machine learning, such as Learning Classifier Systems (LCSs), faces a fundamental scalability bottleneck for function approximation: both rule count and parameter count grow exponentially with $n$. Traditional LCSs partition the $n$-dimensional input space directly, requiring $\mathcal{O}(m^n)$ rules for adequate coverage, where $m$ is the per-variable resolution. This article breaks from this paradigm by reorganizing rules dimension-wise, guided by t...

---

### 48. A neural network that maintains and retrieves memories based on context

**Authors:** Hayoung Song, JeongJun Park, Qihong Lu, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37791v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37791v1)

**Summary:** Every day, people continuously infer situational context and adjust the way they understand and remember the world. Context, signaled by the prefrontal cortex, is known to modulate working memory and episodic memory, but the algorithmic understanding of this modulation remains limited. Here, we train a recurrent neural network (RNN), augmented with an episodic memory buffer, to infer context using Bayesian inference as it continuously makes predictions of upcoming scenes while watching naturalis...

---

### 49. Hybrid Joint-Selective Optimization: Reduced-Space Levenberg-Marquardt Refinement of Low-Dimensional Parameters of Interest

**Authors:** Muhammad Luthfi Shahab, Gabriella Alfa Indahsari, Imam Mukhlash, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37308v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37308v1)

**Summary:** This paper introduces a hybrid joint-selective optimization (HJSO) framework for large-scale numerical problems in which a small subset of trainable quantities is of primary interest. We partition the full parameter vector into a high-dimensional remaining block and a low-dimensional block of parameters of interest (POIs), perform joint first-order optimization over the full parameter set, and then freeze the remaining variables while applying a reduced-space Levenberg-Marquardt (LM) refinement ...

---

### 50. Adaptive Rotation for iSOMA: Geometry, Benchmarking, and Noise Robustness in Variational Quantum Objectives

**Authors:** Vojtěch Novák, Ivan Zelinka

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37193v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37193v1)

**Summary:** We study whether the coordinate dependence of the improved Self-Organizing Migrating Algorithm (iSOMA) can be reduced while retaining its inexpensive leader-directed migration mechanism. We introduce iSOMA-AR, which learns a basis from successful migration displacements and selectively applies the standard perturbation mask in that basis. On the complete noiseless BBOB suite, iSOMA- AR significantly outperformed baseline iSOMA across matched conditions, with the largest gains on geometrically di...

---

## q-bio.NC

**50 papers**

### 1. Interplay between Excitability and Noise in Analog Spiking Neurons

**Authors:** Léopold Van Brandt, Alon Ascoli, Michele Bonnin, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06720v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06720v1)

**Summary:** A spiking neuron is a dynamical system exhibiting a limit cycle (a spike) when subject to sufficiently excitatory input. Famous neuroscience experiments by Bryant and Segundo as well as Mainen and Sejnowski revealed that the spike times of some biological neurons are more reliable when subject to time-varying stimuli compared to constant ones. Provided with an industrial physics-based transient noise SPICE simulation framework compatible with foundry transistor compact models, we have demonstrat...

---

### 2. COMPASS 2.0: psychometric representational similarity analysis distinguishes symptom structure from personal signal

**Authors:** Baihan Lin

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06615v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06615v1)

**Summary:** Language models can score psychiatric questionnaires from speech, but agreement with self-report may reflect the questionnaire rather than the person. We introduce psychometric representational similarity analysis, a framework for comparing the structure of speech-derived scores, self-report, item wording and theory, and implement it alongside person-level construct scoring in COMPASS 2.0. We show how similarly worded items induce covariance without psychological signal. In pre-registered discov...

---

### 3. NeuroCBIR: A Fast and Accurate Image Retrieval System for Whole-Brain and Region-Specific MRI

**Authors:** Felix Nieto-del-Amor, Jingru Fu, J. -Sebastian Muehlboeck, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06502v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06502v1)

**Summary:** Content-based image retrieval (CBIR) in neuroimaging enables the identification of structurally similar brain scans, supporting diagnosis, prognosis, and treatment planning; however, existing methods are often limited to small datasets, single brain regions, or coarse class labels, thereby restricting their clinical utility and generalizability.   Here, we present NeuroCBIR, a framework for fast and flexible retrieval of both whole-brain and region-specific 3D T1w MRI scans. A total of 103 corti...

---

### 4. From communication to computation in neurons-on-a-chip: an in silico study of neurotopomorphic computing

**Authors:** Michael Taynnan Barros

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06065v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06065v1)

**Summary:** Living neuronal networks transform inputs through recurrent cellular and population dynamics, yet it is unknown which network architecture supports which computation. Neurons-on-a-chip turn this question into a design problem because microchannels guide axonal growth and set the network architecture. We introduce IC$^3$, an Integrated Characterisation of Communication-Driven Computation, which characterizes network state through neuronal dynamics, functional communication, and structural support...

---

### 5. CoHyFuse: Condition-wise Hypergraph Fusion with Global Connectome in Task-fMRI

**Authors:** Boseong Kim, Haejun Chung, Ikbeom Jang

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.05913v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05913v1)

**Summary:** Task-fMRI connectomes reveal state-dependent neural reconfigurations, yet conventional methods marginalize these signals by aggregating distinct conditions into static pairwise graphs, thereby obscuring condition-specific multi-ROI organization. We introduce CoHyFuse, a condition-aware ROI-centered hypergraph framework that constructs a task-state-specific incidence matrix from condition-wise functional connectivity (FC)-profile embeddings, allowing the same ROI to form different multi-ROI hyper...

---

### 6. Lightweight Semantic EEG Foundation Model for Frozen Cross-Disorder Transfer

**Authors:** Rita Huan-Ting Peng, Nhat Bui

**Published:** 2026-10-04

🔗 [Paper](http://arxiv.org/abs/2610.05503v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05503v1)

**Summary:** Large-scale EEG foundation models have demonstrated promising transferability across neurological disorders, but often require millions of parameters and substantial computational resources. In this paper, we present the Universal Semantic EEG Foundation Model (USE-FM), a lightweight EEG foundation model that learns transferable neural representations through self-supervised signal reconstruction on the Temple University Hospital EEG Corpus (TUEG). After pretraining, the encoder is frozen and ev...

---

### 7. Recurrent network dynamics explain the time course of perceptual grouping in natural scenes

**Authors:** Sami Mollard, Alekh K. Ashok, Lore Goetschalckx, et al.

**Published:** 2026-10-04

🔗 [Paper](http://arxiv.org/abs/2610.05419v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05419v1)

**Summary:** How the brain groups image elements into coherent objects in natural scenes remains unclear. Existing models for grouping in biological vision rely on simplified stimuli with explicit boundaries and cannot explain human behavior in naturalistic settings. We propose a mechanistic framework in which recurrent interactions propagate enhanced neuronal activity within and between cortical areas. The framework links computational principles, neural circuitry and perceptual psychology. Local boundary s...

---

### 8. Efficiency and robustness partition the solution space for memory in recurrent networks

**Authors:** William Qian, Cengiz Pehlevan

**Published:** 2026-10-03

🔗 [Paper](http://arxiv.org/abs/2610.04697v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04697v1)

**Summary:** In computational neuroscience, task-trained recurrent neural networks (RNNs) are commonly used as a testbed for exploring the space of recurrent circuit solutions compatible with a particular function. However, these networks are subject to inductive biases that may be misaligned with those of biological circuits, which operate under various efficiency and robustness constraints. Here, using a minimal stimulus recall task, we systematically characterize how the solution space of recurrent neural...

---

### 9. Heterarchy in the Brain: Control as a Spectrum, Not a Chain of Command

**Authors:** Luiz Pessoa, Andrea Gambarotto

**Published:** 2026-10-03

🔗 [Paper](http://arxiv.org/abs/2610.04643v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04643v1)

**Summary:** Neuroscience treats the brain as a control hierarchy, with cortical systems governing subcortical mechanisms. We argue that this mistakes a configuration for an architecture. Local asymmetries of influence are real, but control is relational and process-specific; because neural elements constrain one another across concurrent processes, relations can form cycles that resist a stable ranking. Evidence from learned action, cortico-cerebellar and thalamocortical loops, and defensive behavior shows ...

---

### 10. Beyond Completion Time: A Multimodal Approach to Characterizing Eye-Hand Coordination During the Nine-Hole Peg Test in Multiple Sclerosis

**Authors:** Mahya Beheshti, Rajvardhan Gadde, Diana Maloku, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.04145v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04145v1)

**Summary:** Multiple sclerosis (MS) can impair upper-extremity function through motor, sensory, cognitive, and visual deficits. Although the Nine-Hole Peg Test (9-HPT) is widely used to assess dexterity, completion time alone provides limited insight into the eye-hand coordination underlying performance. We characterized 9-HPT performance in nine people with MS (PwMS) and nine healthy controls using simultaneous eye tracking, markerless hand tracking, and object detection. Each peg cycle was divided into tr...

---

### 11. Multimodal Physiological Decoding Reveals Individualized Arousal Dynamics in Closed-Loop Neurofeedback

**Authors:** Anirudh Natarajan, Paul Sajda

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.04113v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04113v1)

**Summary:** Most arousal-based brain-computer interfaces (BCIs) use EEG to decode cognitive state. But arousal is an autonomic process. We examined if peripheral physiological signals give a better decode of task-related arousal. We used a public dataset from a difficult boundary-avoidance flight task. In this task, participants received EEG-based BCI neurofeedback, sham feedback, or no feedback. We trained a multimodal deep learning decoder on heart rate, heart rate variability (HRV), respiration, electrod...

---

### 12. MEM as an Extension of Recurrent Processing Theory: Toward a Motivational Account of Consciousness

**Authors:** Wiesław L. Galus, Janusz A. Starzyk

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.04057v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04057v1)

**Summary:** Victor Lamme's Recurrent Processing Theory (RPT) proposes that the feedforward sweep (FFS) can extract and categorize visual features unconsciously, while conscious vision emerges through recurrent processing and feedback interactions across representational levels. The Motivated Emotional Mind (MEM) model, developed by Wiesław L. Galus and Janusz A. Starzyk, retains this core principle but embeds it in an embodied architecture integrating multilayer networks, semi-hierarchical semblions, recept...

---

### 13. Stability of Phase-locked States of Weakly Coupled Izhikevich Neurons

**Authors:** XinYe Cheng, Sue Ann Campbell

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.04025v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04025v1)

**Summary:** The Izhikevich model is a computationally efficient neuron model that can exhibit a wide range of firing patterns observed in the brain. However, it is a discontinuous dynamical system, which means the methods for applying weakly coupled oscillator theory developed for continuous dynamical systems cannot be applied. Therefore, the collective behaviour of coupled Izhikevich model has not been fully studied. To our knowledge, we carry out the first computation of the phase model for an Izhikevich ...

---

### 14. Broken scale symmetries in undercomplete linear autoencoders

**Authors:** Farhad Pashakhanloo, Jacob A. Zavatone-Veth

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03640v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03640v1)

**Summary:** Neural network loss landscapes have many symmetries, which are preserved by gradient flow but broken by finite-stepsize stochastic gradient descent (SGD). A canonical example of such a symmetry is scale in homogeneous networks: one can scale up the parameters in one layer and down in the next without changing the network output. Previous work has documented cases in which SGD breaks this symmetry in favor of balancing gradient noise or minimizing fluctuations. Here, we show that the solution geo...

---

### 15. Contrastive Neural Embeddings Reveal Individual Traits Beyond Conversational Role

**Authors:** Hubert Huang, Michelle McCleod, Brendan Ames, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03410v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03410v1)

**Summary:** Contrastive representation learning is increasingly used to recover low-dimensional structure from neural recordings, but its output is typically validated by decoding accuracy rather than by the geometry of the manifold it produces. We apply CEBRA to EEG recorded from dyads in conversation, and analyze the resulting embedding, which training constrains to the 2D sphere. Labels describing the dyads, including the absolute difference between partners' autism-quotient scores, decode well above cha...

---

### 16. The Score Is Not the Structure: Brain Alignment and Cross-Lingual Transfer

**Authors:** Saman Rahbar

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03827v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03827v1)

**Summary:** Researchers often support the claim that a model shares structure with the brain, or across languages, by reporting a similarity score. We ask what such a score reads when the shared structure is absent, or when the tool that measures it does not work. We check two settings, and in both the score is not what it appears. First, a probe trained to tell grammatical from ungrammatical sentences in one language transfers worse to more distant languages, the usual evidence for shared structure. But th...

---

### 17. Response Variability and Stability in Human Reasoning

**Authors:** Clemens Bombach, Rajmadan Lakshmanan, Marco Ragni

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.03008v1) | 📄 [PDF](https://arxiv.org/pdf/2610.03008v1)

**Summary:** Understanding how humans reason -- and how reasoning responses vary across tasks and individuals -- remains a core challenge for modeling and explanation in cognitive science. We investigate the stability of response patterns within reasoners and whether variation in these patterns can be used to predict learning effects. We introduce a formal, geometry-based method to quantify distances between individual reasoning patterns and their internal variability, grounded in heuristic theories. The pro...

---

### 18. NeuroLens: Learning Latent Embeddings of Neural Semantics from Chronic Recordings

**Authors:** Hanrui Lyu, Baiyuan Chen, Tianshu Tan, et al.

**Published:** 2026-10-02

🔗 [Paper](http://arxiv.org/abs/2610.02864v1) | 📄 [PDF](https://arxiv.org/pdf/2610.02864v1)

**Summary:** Understanding how neural activity represents higher-order cognition and how these representations evolve over time has long been a central pursuit in neuroscience. However, current analytical tools cannot easily distinguish representational plasticity from recording instability in chronic neural recordings. Here, we introduce NeuroLens (Latent Embeddings of Neural Semantics), a self-supervised model based on the Joint-Embedding Predictive Architecture (JEPA) framework that learns denoised, seman...

---

### 19. A foundation for systematic analysis of transformers and RNNs for tractography

**Authors:** Emmanuelle Renauld, Philippe Poulin, Hugo Larochelle, et al.

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01894v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01894v1)

**Summary:** Machine learning (ML) has emerged as a promising approach for improving diffusion MRI (dMRI) tractography, a task that remains limited by the intrinsic tension between local diffusion information and global anatomical plausibility. In this work, we systematically evaluate recurrent neural networks (RNNs) and Transformer models for iterative tractography, with particular attention to training strategies, input representations (including convolutional neural network (CNN)-based embeddings and end-...

---

### 20. Inferring Multi-Timescale Neural Dynamics with Switching Linear Dynamical Systems

**Authors:** Lulu Gong, Yongxu Zhang, Shreya Saxena

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01786v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01786v1)

**Summary:** Neural activity often exhibits multiple timescales that can vary with behavioral states and task conditions. Identifying these timescales from neural recordings is important for better understanding neural computation and function. However, traditional approaches based on autocorrelation fitting are difficult to scale to high-dimensional population recordings and can become unreliable when neural dynamics change with behavior. State-space models have been a powerful framework for modeling high-d...

---

### 21. A High-Density EEG Dataset for Stimulus-Driven Auditory Attention

**Authors:** Ruofan Yan, Na Lu, Shu Peng, et al.

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.01303v1) | 📄 [PDF](https://arxiv.org/pdf/2610.01303v1)

**Summary:** Stimulus-driven auditory attention determines which sound gains priority when multiple sources compete without an explicit listening goal, yet most computational studies focus either on acoustic salience or on decoding predefined attended targets. This study investigates instruction-free auditory competition using the Stimulus-driven Auditory Attention (SAAD) paradigm and develops a neurophysiologically informed framework that integrates stimulus-derived sound priority with trial-specific EEG ev...

---

### 22. Selection rules for the harmonic spectroscopy of animal decisions

**Authors:** Mohammad Salahshour

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.00990v1) | 📄 [PDF](https://arxiv.org/pdf/2610.00990v1)

**Summary:** Spectroscopy reads structure by sending a structured probe into a system and measuring what comes back. Here we apply this principle to animal decision-making. Harmonic Theory casts choice as motion on an angular landscape over heading, whose Fourier components form an animal's decision spectrum. We show that the arrangement of cues enters that landscape as a structure factor, so it factors like a diffraction amplitude, and symmetry imposes selection rules: a p-fold cue array annihilates every h...

---

### 23. One Inference, Four Failure Modes: Formal Models of Why Pain Location Fails

**Authors:** Adam Y. Shavit

**Published:** 2026-10-01

🔗 [Paper](http://arxiv.org/abs/2610.00866v1) | 📄 [PDF](https://arxiv.org/pdf/2610.00866v1)

**Summary:** Patient-reported pain location is diagnostically decisive for some presentations and nearly uninformative for others. A companion paper argues this is not one gradient of diagnostic utility but three distinct failures of localization. This paper gives those failures their mathematics and shows they are one object: a single Bayesian generative model failing at different nodes - the likelihood, the model class, and group- or context-dependence in that same likelihood. The count is not in dispute: ...

---

### 24. Increasing Width Allows Greedy Layer-wise Training to Rival End-to-End Backpropagation in Self-Supervised Learning

**Authors:** Syon Mansur, Joel Zylberberg

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2610.00753v1) | 📄 [PDF](https://arxiv.org/pdf/2610.00753v1)

**Summary:** End-to-end backpropagation has been the dominant mode of training in deep learning, allowing for the coordination of parameter updates across layers of a neural network. Prior studies have explored alternative -- and, in some cases, simpler -- training mechanisms, showing that they can sometimes achieve performance similar to backpropagation. However, the architectural conditions under which locally optimized networks, which avoid end-to-end backpropagation of error, can learn representations co...

---

### 25. MEG-Mamba: A Scalable State-Space Foundation Model for Magnetoencephalography

**Authors:** Chetan Gohil, SungJun Cho, Oiwi Parker Jones, et al.

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2610.00746v1) | 📄 [PDF](https://arxiv.org/pdf/2610.00746v1)

**Summary:** Magnetoencephalography (MEG) is an imaging technique that offers a non-invasive, millisecond-resolution view of human brain activity. The increasing availability of MEG data presents an opportunity to take advantage of a recent advance in artificial intelligence, namely self-supervised foundation models. Existing foundation models for MEG (and electroencephalography) have been built on a transformer architecture. Here, we introduce MEG-Mamba: a generative foundation model for neural activity (so...

---

### 26. Neuromorphic Pseudo-Random Number Generators with a Low Power Hardware Implementation

**Authors:** Jafar Shamsi, Navid Akbari, Sonia Sennik, et al.

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2610.00719v1) | 📄 [PDF](https://arxiv.org/pdf/2610.00719v1)

**Summary:** Pseudo-random number generation often requires trade-offs among quality, power consumption, and bandwidth to produce unpredictable sequences of numbers. The brain, on the other hand, efficiently generates unpredictable output complex network dynamics occurring in a high-dimensional state. This state, which is hypothesized to be chaotic, relies on the balance between excitation and inhibition. Here, we investigated if computational models of these chaotic balanced states can be harnessed for Neur...

---

### 27. Synaptic placement reflects shared input in Drosophila descending neurons

**Authors:** Xizhe Zhang

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2610.00690v1) | 📄 [PDF](https://arxiv.org/pdf/2610.00690v1)

**Summary:** Network topology describes connections between neurons, whereas synaptic placement specifies how those connections are arranged within individual cells. How these levels of organization correspond remains incompletely understood. Here we show that connectivity between presynaptic neurons is reflected in relative input placement within Drosophila descending neurons (DNs). Across thousands of one-way DN connections in the independently reconstructed MaleCNS and FlyWire brains, inputs from sources ...

---

### 28. Stochastic Dynamics of Large-Scale Motif-Embedded Spiking Neuronal Networks

**Authors:** Gurpreet Jagdev, Richard Bertram, Na Yu

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2610.00616v1) | 📄 [PDF](https://arxiv.org/pdf/2610.00616v1)

**Summary:** We examine how local motif structure and global network topology jointly shape spiking dynamics in stochastic neuronal networks. Using networks of Izhikevich neurons with Erdős-Rényi (ER) and scale-free (SF) background connectivity, we compare motif-embedded networks with synapse-count-matched, non-motif controls under noise- and stimulus-driven protocols. Motif embedding increases noise-induced coherence in both topologies and provides a smaller improvement in signal transmission, while SF-base...

---

### 29. Stochastic dynamics and synchronization in motif-based neuronal networks

**Authors:** Gurpreet Jagdev, Yifei Lu, Richard Bertram, et al.

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2610.00597v1) | 📄 [PDF](https://arxiv.org/pdf/2610.00597v1)

**Summary:** Neuronal networks exhibit complex dynamics shaped by connectivity and stochastic input. Empirical studies show that neuronal networks contain recurring subgraphs, or motifs, but the collective influence of different motif types after embedding in large stochastic networks remains less well understood. We construct a spiking network composed of six representative structural classes and examine how intrinsic noise, coupling strength, inter-motif connectivity, network size, and neuronal heterogenei...

---

### 30. Removing Timing Shortcuts Improves Non-Invasive Brain-to-Text

**Authors:** Dulhan Jayalath, Oiwi Parker Jones

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.40359v1) | 📄 [PDF](https://arxiv.org/pdf/2609.40359v1)

**Summary:** We find that major reported improvements in decoding words from non-invasive brain recordings are largely reproducible without any brain data. In the influential work of d'Ascoli et al. (2025), time series of brain activity from subjects perceiving continuous speech are segmented into fixed-length windows starting at each word. A neural network then generates predictions for all of the words in a sentence together. Neighbouring windows partially overlap, implicitly revealing the interval between...

---

### 31. Disentangling Computation in Multi-Task Neural Networks with the Green's Operator

**Authors:** James Hazelden

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.40292v1) | 📄 [PDF](https://arxiv.org/pdf/2609.40292v1)

**Summary:** How is computation organized and reused across tasks and time in a trained recurrent network? Most analyses emphasize the geometry of neural activity, dynamical motifs, or local perturbation growth. We instead study the network's global first-order perturbation response. The finite-horizon Green's operator maps perturbations at each source along a trajectory to their downstream state-space responses and therefore directly represents perturbation routing. Simple reductions of this operator provid...

---

### 32. Attraction to hierarchical feature memory explains orientation bias

**Authors:** Kira Michaela Düsterwald, Peter Vincent, Ana Kapros, et al.

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.40204v1) | 📄 [PDF](https://arxiv.org/pdf/2609.40204v1)

**Summary:** When recalling the orientation of recent stimuli, observers are systematically biased away from the cardinal axes. The prevailing explanation is that this ''anti-cardinal bias'' arises because cardinal orientations are encoded with greater neural resources and therefore less noise, consistent with efficient coding of environmentally common features. Under this account, the bias should occur independently for each stimulus; any serial attraction towards previously seen orientations should be inde...

---

### 33. Belief-Based Maximum Occupancy Principle and Active Inference

**Authors:** Manolis Mylonas, Rubén Moreno Bote

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.39342v1) | 📄 [PDF](https://arxiv.org/pdf/2609.39342v1)

**Summary:** Intrinsic motivation plays a central role in adaptive and goal-directed behavior by conferring agents reward-independent objectives and biases useful to act in noisy and uncertain environments. Active Inference addresses the problem of acting in a partially observable environment through a principled framework for belief updating and action selection. A key component of Active Inference is the specification of prior preferences, which shapes behavior by encoding desirable future outcomes. An int...

---

### 34. Null-model treatment of the sensory-motor boundary changes an evolutionary connectome comparison

**Authors:** Gyujeong Park

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.39248v1) | 📄 [PDF](https://arxiv.org/pdf/2609.39248v1)

**Summary:** Randomised copies of a connectome are the usual baseline for asking whether measured wiring matters, and the answer depends on what the randomisation preserves. We evolved embodied foraging agents whose brains are a compressed adult Drosophila connectome (FlyWire v783; 512 cell-type groups and 1,000 Kenyon cells) alongside agents built on randomised wiring, in pre-registered experiments with ten seeds, four ecologies and 600 generations. Two standard randomisations, a column shuffle and degree-p...

---

### 35. Association profile conditioning in a set-temporal transformer for cross-session intracortical motor decoding

**Authors:** Xinyuan Zhang, Handong Mo, Pengfei Wen, et al.

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.39080v1) | 📄 [PDF](https://arxiv.org/pdf/2609.39080v1)

**Summary:** Intracortical motor decoders degrade across sessions because the set of recorded units changes and persisting units can alter how their firing relates to behavior. Most existing methods update network weights on each new session or rely on unlabeled activity, which does not directly reveal such changes. We present APST, an Association Profile-conditioned Set-Temporal transformer that adapts to new sessions with all network weights frozen. From a few labeled calibration trials, APST summarizes ho...

---

### 36. Not all solutions are created equal: An analytical dissociation of functional and representational similarity in deep linear neural networks

**Authors:** Lukas Braun, Erin Grant, Andrew M. Saxe

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.38998v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38998v1)

**Summary:** A foundational principle of connectionism is that perception, action, and cognition emerge from parallel computations among simple, interconnected units that generate and rely on neural representations. Accordingly, researchers employ multivariate pattern analysis to decode and compare the neural codes of artificial and biological networks, aiming to uncover their functions. However, there is limited analytical understanding of how a network's representation and function relate, despite this bei...

---

### 37. Future Video Generation Better Aligns with the Human Visual Cortex than Observed Video

**Authors:** Chang-Bae Bang, Hyungjin Chung, Byung-Hoon Kim

**Published:** 2026-09-30

🔗 [Paper](http://arxiv.org/abs/2609.38819v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38819v1)

**Summary:** Studying the alignment between the internal representations of vision models and the responses of the visual cortex to the same observed visual stimuli has enabled us to better understand human visual processing. However, studies so far have largely overlooked the fact that the human brain not only processes observed visual stimuli, but also predicts upcoming stimuli based on what has been observed. Accordingly, we hypothesize that internal representations for generating future video frames are ...

---

### 38. How much of fly walking is written in the wiring?

**Authors:** Isabel Guan, Yuntian Zhao, Dingyuan Zhang, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38665v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38665v1)

**Summary:** Connectome models of the fly nerve cord generate walking-like motor rhythms, but oscillation alone does not show that the specific wiring matters. Here we provide, to our knowledge, the first test of which features of motor output depend on the specific wiring. We simulated the leg motor systems of two independent Drosophila connectomes, with synapse counts as fixed weights and glutamatergic synapses treated as inhibitory, and compared each with six families of rewired networks that preserve pro...

---

### 39. TERRA: Terrain-Aware Reconstruction, Retargeting and Control for Musculoskeletal Locomotion

**Authors:** Merkourios Simos, Chengkun Li, Bianca Ziliotto, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38653v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38653v1)

**Summary:** Recent advances in musculoskeletal modeling and reinforcement learning have enabled muscle-actuated agents to reproduce increasingly complex human motions. Yet these capabilities remain largely confined to flat ground, in part because motion datasets rarely include aligned terrain geometry and because retargeting terrain interactions to complex musculoskeletal bodies is challenging. We present TERRA, an end-to-end pipeline for terrain-aware retargeting and control of musculoskeletal locomotion. ...

---

### 40. Autoregressive Frontier Expansion: Growing Trees with Graph Machine Learning

**Authors:** Umer Gupta, Saku Peltonen, Martin Ritzert

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38506v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38506v1)

**Summary:** Tree-like branching structures are common in nature, from botanical trees to neurons, blood vessels and respiratory trees. Their branching shape often reflects function, making structural modelling central to understanding how these systems work. Because acquiring real-world 3D data is often expensive or infeasible, realistic generative models are valuable for simulation and data augmentation. Existing morphology-specific models either constrain how topology is generated or rely on hand-tuned, m...

---

### 41. Does Global Neuronal Workspace Theory Explain Phenomenal Consciousness? The Motivated Emotional Mind Challenge

**Authors:** Wiesław L. Galus, Janusz A. Starzyk

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38495v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38495v1)

**Summary:** Global Neuronal Workspace Theory (GNWT) is one of the most extensively developed empirical research programmes on access consciousness. By contrast, the Motivated Emotional Mind (MEM) model proposes an embodied, semi-hierarchical associative memory in which representational selection, action, recurrent reconstruction of modality-specific fields, interoception, and valence form a single functional cycle. This article assesses whether MEM mechanisms can reproduce the functions explained by GNWT an...

---

### 42. Embodiment-aware control by inference over the operator: a simulation study

**Authors:** Sara Falcone

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38437v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38437v1)

**Summary:** Teleoperation systems are tuned for channel fidelity, while whether the operator experiences the device as part of the body, the Sense of Embodiment (SoE), is measured only afterwards, by questionnaire. Predictive-processing accounts suggest controlling devices to reduce the mismatch between the operator's predictions and the returned feedback, but those predictions are unobservable, and an objective that only penalizes mismatch is minimized by removing feedback. We formulate an embodiment-aware...

---

### 43. Traversing the solution space of neural networks with Hessian Null Space Continuation

**Authors:** Ann Huang, Mitchell Ostrow, Zhouyang Lu, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.38081v1) | 📄 [PDF](https://arxiv.org/pdf/2609.38081v1)

**Summary:** On a single task, deep networks can learn many solutions, depending on their optimizer, training data, architecture, and hyperparameters. Many of these solutions are mode-connected: rather than isolated points in weight space, they are connected by low-loss regions. Yet how their internal computation varies within these regions is unknown. A parallel line of work has identified the degeneracy of neural representations: many networks reach similar training loss with distinct internal structures. ...

---

### 44. Which Attention Heads are like the Human Head? Not the Ones that Compute

**Authors:** Christopher Pinier, Gustaw Opiełka, Hannes Rosenbusch, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37991v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37991v1)

**Summary:** Brain-AI alignment is often interpreted as a sign that model and brain perform similar computations. Whether the aligned units are causally involved in model computation is rarely checked. On an abstract pattern-completion task (AAABAAA $\rightarrow$ B), we compare LLM attention-head representations with human EEG and test how ablating those heads affects task performance. Alignment and causation dissociate: brain-aligned heads contribute to performance, but their removal is substantially less d...

---

### 45. Flattening the Connectome Spectrum: A Spectral Filter for FC Induces a Pretraining Target for fMRI Encoders

**Authors:** Giovanni Marraffini, Victoria Shevchenko, Carlo Alberto Barbano, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37642v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37642v1)

**Summary:** Self-supervised pretraining reshaped prediction in language and vision, and brain foundation models (BFMs) inherited its promise. Representations learned from large unlabelled corpora should capture individual functional dynamics and generalise across cohorts. However, kernel ridge regression (KRR) fitted on functional connectivity (FC) matrices still predicts individual phenotypes more accurately than any BFM we tested. In this paper, we show that KRR is weighted by the eigenvalues of the FC wh...

---

### 46. An adaptive fractional state links circuit mechanisms to cortical dynamics across the visual hierarchy

**Authors:** Brendan Harris, Pulin Gong

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.37355v1) | 📄 [PDF](https://arxiv.org/pdf/2609.37355v1)

**Summary:** Cortical circuits must respond flexibly to new inputs while integrating information about the past, yet the way in which neural activity reconciles these competing demands remains unclear. Combining Neuropixels recordings from six mouse visual areas with mechanistic circuit modeling, we identify a dynamical regime in which heavy-tailed superdiffusive fluctuations coexist with long-range temporal dependence and oscillations. We formalize this regime as the adaptive fractional (AF) state, using an...

---

### 47. Volcanite: Commodity-Hardware Segmentation Volume Visualization for Connectomics and Beyond

**Authors:** Max Piochowiak, Reiner Dolp, Julian Herold, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.36898v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36898v1)

**Summary:** Modern imaging produces terabyte-scale segmentation volumes, assigning each voxel an object label. These categorical, boundary-sensitive and label-rich data underpin connectomics and other imaging-driven fields, yet their scale often forces interpretation through slices, approximate meshes or distributed workflows that obscure spatial context and voxel-level defects. Here we show that such volumes can be explored directly on commodity hardware with Volcanite, an open-source framework for dense-s...

---

### 48. From Neurons to Conversation: Speech Brain-Computer Interfaces

**Authors:** Moein Khajehnejad, Forough Habibollahi, Tommaso Boccato, et al.

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.36736v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36736v1)

**Summary:** Speech brain-computer interfaces (BCIs) aim to restore communication by transforming neural activity related to speech, language, or communicative intent into external outputs such as text, synthesized voice, or avatar control. Recent advances in intracortical and electrocorticographic recording, deep sequence models, and language-model-assisted decoding have enabled rapid progress, including high-performance attempted-speech decoding and increasingly naturalistic speech synthesis. Yet these ach...

---

### 49. Neural Structural Reasoner: A Brain-inspired Architecture for Reasoning over Structured Knowledge

**Authors:** Zixing Jia, Yuhang Pan, Ni Ji

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.36620v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36620v1)

**Summary:** Structural reasoning, the ability to recognize and make inferences over the relational structure between objects and concepts, is a hallmark of human cognition, yet prevailing methods often collapse relational topology into flat embeddings, cannot discover hidden structure and lack interpretability. We introduce Neural Structural Reasoner (NSR), a brain-inspired network that preserves relational structure directly in the connectivity and dynamics of coupled neuronal populations. NSR draws inspir...

---

### 50. Large-scale factor analysis shows machine intelligence is only partially interpretable

**Authors:** Faiz Ghifari Haznitrama, Afrizal Hasbi Azizy, Faeyza Rishad Ardi

**Published:** 2026-09-29

🔗 [Paper](http://arxiv.org/abs/2609.36515v1) | 📄 [PDF](https://arxiv.org/pdf/2609.36515v1)

**Summary:** A common assumption in language model development is that cognitive abilities are organized around a general, domain-free intelligence factor, like fluid intelligence in humans. This assumption is rarely tested directly, and prior attempts have done so only at a much smaller scale. We take a latent variable approach to intelligence in language models, similar to how psychometricians study psychological constructs. Performance in every specific problem set is influenced by a domain-specific and a...

---

## stat.ML

**50 papers**

### 1. Direct Intermediate Initialization for Tilted Diffusion Samplers

**Authors:** Gregory D. Bellchambers

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06834v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06834v1)

**Summary:** Some diffusion posterior samplers construct Gaussian-tilted intermediate distributions along the reverse process. We observe that these targets can be pulled back to clean-space posteriors with weaker conditioning, with samples transported analytically to the corresponding noisy-space target through a Gaussian bridge. For the sequential Monte Carlo (SMC) sampler MCGDiff, the effective observation variance of this pulled-back problem is up to twice the diffusion-noise variance. We exploit this st...

---

### 2. Private online learning and prediction for Littlestone classes

**Authors:** Amartya Sanyal

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06822v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06822v1)

**Summary:** We study mistake bounds for differentially private online learning and online prediction under oblivious realisable adversaries. Online learning requires the learner to release a hypothesis at each time step whereas in online prediction, the learner only needs to make predictions without releasing a hypothesis. Using a novel lower bound for private online learning and an upper bound for private prediction, we show that the sample complexity of these two problems are separated by a factor that gr...

---

### 3. Block Disentanglement in CRL: Bridging Identifiability and Visual State Estimation

**Authors:** Emre Acartürk, Pranamya Kulkarni, Puranjay Datta, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06809v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06809v1)

**Summary:** Causal representation learning (CRL) is the process of recovering causally-related latent variables from high-dimensional observations. As a label-free inference method, CRL is particularly attractive for applications where data labels are unavailable or impractical to obtain. While there has been significant progress in understanding the identifiability guarantees of CRL, such guarantees often hold under highly stylized assumptions, which temper the direct application to real-world problems. Th...

---

### 4. Round-Trip KNN Clustering: multiscale hierarchical cluster detection on directed nearest-neighbour graphs

**Authors:** Eraldo Pereira Marinho, Caetano Mazzoni Ranieri, Fabricio Aparecido Breve

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06795v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06795v1)

**Summary:** We introduce Round-Trip KNN Clustering (RTKNNC), a graph-based method for finding cluster structure at several neighbourhood scales without requiring the number of clusters in advance. Unlike approaches that first make a $k$-nearest-neighbour (KNN) graph undirected, RTKNNC keeps both directions of the neighbour relation: which points a given point selects and which points select it. Incoming selections are treated as weighted votes that help decide which local connections remain visible during a...

---

### 5. Hyperbolic Graph Representation Learning: Embed in One Metric, Optimize with Another

**Authors:** Federico Larroca, Paola Bermolen, Marcelo Fiori, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06745v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06745v1)

**Summary:** Hierarchical graphs embed in hyperbolic space with lower distortion than in Euclidean space owing to its negative curvature. However, their gradient-based learning is hampered at large radii, where the Poincaré ball and the Lorentz hyperboloid models fail numerically. Polar coordinates avoid this problem, but the hyperbolic metric scales the angular step by the hyperbolic sine of the radius, freezing angular motion. We observe that this factor is a choice, silently fixed by existing implementati...

---

### 6. A Solvable Model of Adaptive Learning Rate Rescaling: Acceleration, Stability & Scaling

**Authors:** Itay Lavie, Clarissa Lauditi, Cengiz Pehlevan

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06701v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06701v1)

**Summary:** A recurring design principle in modern optimizers is to decouple update magnitude from the raw gradient norm, yet its consequences for learning-curve and resource scaling remain unclear. We isolate this mechanism by studying normalized SGD in a random-feature model with power-law teacher and data covariance. Fixed-norm updates induce an effective learning rate that grows as gradients shrink. We derive a dynamical mean-field theory (DMFT) describing the joint dependence of the loss on training ti...

---

### 7. The Birkhoff Geometry of Manifold-Constrained Hyper-Connections: Two Channels, Vertex Viscosity, and Sinkhorn as a Retraction

**Authors:** Xiaoyu Li, Zhizhou Sha, Chiwun Yang

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06653v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06653v1)

**Summary:** Hyper-connections widen the residual stream of a Transformer to $n$ parallel streams. Their manifold-constrained version (mHC) mixes the streams at each layer with a doubly stochastic matrix, which it computes by Sinkhorn normalization of exponentiated logits. We give a geometric theory of this design on the Birkhoff polytope. First, a doubly stochastic mixer splits the stream into a mean channel, on which mHC is exactly a residual network, and a difference channel, which each layer contracts by...

---

### 8. Inverse Cross-spectral Neural Networks for Multivariate Time Series

**Authors:** Lorenzo Marinucci, Leonardo Di Nino, Gabriele D'Acunto, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06630v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06630v1)

**Summary:** CoVariance Neural Networks and their extensions have emerged as effective tools for processing multivariate data, deriving graph shift operators directly from second-order statistics. These architectures, however, are designed for independent and identically distributed observations and do not fully capture the joint structure of temporal and cross-variable dependencies in multivariate time series. In this work, we introduce Inverse Cross-Spectral Neural Networks (iCSNNs), a class of graph neura...

---

### 9. The Surrogate Is Not the Reward: Post-Surrogate Primary-Outcome Acquisition in Contextual Bandits

**Authors:** Kyungbok Lee, Michael R. Kosorok

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06610v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06610v1)

**Summary:** We study contextual bandits in which a surrogate is observed after the action but before the learner decides whether to acquire the primary outcome that defines action value and regret. The value of acquiring the primary outcome depends on both decision relevance (how much the current outcome matters for comparing policies) and the residual uncertainty after observing the surrogate. The Audited Surrogate Bandit (ASB) learns a contextual policy while allocating a budget of $B$ primary-outcome acq...

---

### 10. LinearPFN: Amortized Variable Selection for Linear Models with Interactions

**Authors:** Louis Schiekiera, Max Zimmer, Christophe Roux, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06580v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06580v1)

**Summary:** Spike-and-slab regression is a standard Bayesian formulation of variable selection: it returns a posterior distribution over which candidate effects are active rather than a single selected subset, so that every candidate effect carries an inclusion probability. Its cost grows exponentially with the number of candidate effects, so the posterior can be enumerated exactly only when the number of predictors is small. Beyond that reach, the posterior has to be approximated, typically by Markov chain...

---

### 11. SOL: Measuring Gaps between Text Distributions by Double Sliced Wasserstein Metrics

**Authors:** Gregor Kornhardt, Moritz Piening, Jannis Chemseddine, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06513v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06513v1)

**Summary:** Evaluating text generation requires measuring how well the generated distribution matches the data distribution. For autoregressive models, this is done by the perplexity. Diffusion and flow-based language models can only provide a likelihood bound, whose tightness differs between model families. Sample-based substitutes such as generative perplexity with entropy do not consider the distribution fit. We propose SOL,   a distance between text distributions. Each sequence is represented by the emp...

---

### 12. KESurv: A Kernel Ensemble Method for Patient-Specific Survival Prediction

**Authors:** Rahul Goswami

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06434v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06434v1)

**Summary:** Predicting patient-specific survival functions is crucial for clinicians in making informed decisions about patient care and treatment strategies. Among the various models available, the Survival Forest has demonstrated significant effectiveness in numerous scenarios. In this work, we propose an ensemble method that leverages the strengths of the Survival Forest as the master model, complemented by several base models. This ensemble incorporates the Beran estimator, a type of kernel estimator, t...

---

### 13. Valid Stopping in Adaptive Generator-Verifier Loops

**Authors:** Mahmoud Hegazy, Michael I. Jordan, Aymeric Dieuleveut

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06432v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06432v1)

**Summary:** Numerous agentic workflows are based on a generator-verifier loop: a generator proposes candidates, a cheap verifier scores them, and the workflow terminates when a proposal is verified as good enough. The verifier typically proxies a more costly ground-truth oracle, and as the generator searches adaptively against it, false acceptances may accumulate. Proposals can pass the proxy but fail under the costlier ground-truth check. We study when to stop these loops while controlling the false discov...

---

### 14. On the Comparison of Optimizers for Imbalanced Learning

**Authors:** Cl{é}ment Lezane, Fran{\c c}ois Bachoc, J{é}r{ô}me Bolte, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06421v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06421v1)

**Summary:** Data imbalance is pervasive in machine learning, from rare words and anomalies to underrepresented patterns in heterogeneous or cross-tabulated data. We study idealized optimizers geometries in continuous time to model small-step training in deep learning. We assume that the source of imbalance is unobserved: the optimizer has only access to the aggregate training loss ignoring the exact contributions of the majority and minority groups. In this setting, we characterize a region where majority l...

---

### 15. Quantifying the Stability of Multi-Step Reasoning via Error Amplification

**Authors:** Dongyue Li, Ziniu Zhang, Minxuan Duan, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06404v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06404v1)

**Summary:** We consider the stability of multi-step reasoning processes, which have extensive applications in language models, including chain-of-thought and algorithmic reasoning. While longer sequences of reasoning can improve a model's generation capability at test time, the errors due to intermediate reasoning steps can accumulate in autoregressive generation, and thus grow substantially at the end. In this paper, we ask: What are the key factors determining the stability of multi-step reasoning? First,...

---

### 16. Latent Similarity Gaussian Processes: A Theory-Grounded Approach to Personalized Suicide-Risk Forecasting for Clinical Decision-Support

**Authors:** Yaniv Yacoby, Weiwei Pan, Hope Neveux, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06355v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06355v1)

**Summary:** Forecasting suicide risk is difficult due to the high heterogeneity of patients and the low base rate of suicide-related events (SREs). We present Latent Similarity Gaussian Processes (LSGPs), which embed patients in a continuous latent space to jointly model similarity and forecast risk. By selectively drawing information from latent peers, LSGPs better capture individualized risk trajectories, generalizing nomothetic (pooled), idiographic (per-patient), and hierarchical frameworks. Our contrib...

---

### 17. Watermarking: from Impossibility to Auditable Compliance

**Authors:** Fernando Delbianco, Fernando Tohmé, Hugo Acciarri

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06317v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06317v1)

**Summary:** Article 50 (2) of the EU Artificial Intelligence Act requires providers of generative systems to make synthetic outputs machine-readable and detectable, while qualifying the effectiveness, interoperability, robustness, and reliability by technical feasibility, cost, content-specific limits, and the state of the art. For free-form text, one important implementation route is the implementation of a generative watermarking procedure, which poses a compliance problem that is hard to address. Strong ...

---

### 18. Reconstruction-Aware Distribution Matching for Inverse Problems with Unpaired Data

**Authors:** Thomas Ryckeboer, Giacomo Meanti, Julien Mairal

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06297v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06297v1)

**Summary:** Recovering the forward operator of an imaging system from unpaired data avoids both calibration hardware and the clean/degraded pairs that supervision requires-pairs that, for a real lens, are often impossible to acquire. Existing unpaired approaches that explicitly estimate the forward operator by distribution matching evaluate a candidate only through the measurements it generates, whose distribution should match that of the real ones. Components suppressed by the operator are barely present i...

---

### 19. When Are Concept Bottleneck Model Explanations Faithful and Compact?

**Authors:** Stefano Teso, Emanuele Marconato, Steve Azzolin, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06285v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06285v1)

**Summary:** Concept bottleneck models (CBMs) are neural classifiers that allow to explain their decisions via high-level concepts, potentially enabling understanding, steering and debugging. However, their explanations are often derived heuristically. Building on formal explainability, we argue they should also be faithful, i.e., not misreport which concepts actually matter. We show that, for widespread CBM architectures, including recent VLM-based variants, faithful explanations must include all concepts i...

---

### 20. Bradley-Terry model under general comparison graphs

**Authors:** Ruijian Han, Yuanhang Luo, Yiming Xu

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06237v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06237v1)

**Summary:** The Bradley-Terry model is a parametric model for ranking from pairwise comparisons. Existing asymptotic theory for the maximum likelihood estimator (MLE) in regimes where the number of objects grows often requires homogeneity assumptions or compatibility conditions on comparison graphs, which limits its applicability to many practical settings. In this work, we establish uniform consistency of the MLE under general deterministic comparison designs. Our pairwise error bound consists of a pair-sp...

---

### 21. Sampling Allocation of LinUCB: Optimal Design Limits in the Small-Gap Regime

**Authors:** Yujie Liu, Vincent Y. F. Tan, Yunbei Xu

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06213v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06213v1)

**Summary:** We study the sampling allocation of LinUCB in the small-gap regime, where the reward gaps are of order at most $n^{-1/2}$ over the decision horizon $n$. This scaling captures the hard instances underlying worst-case regret lower bounds, for which LinUCB is known to be near optimal up to logarithmic factors in $n$. Using a mean-field perspective, we characterize this allocation through the empirical sampling distribution, a macroscopic object that averages the effect of adaptive decisions over th...

---

### 22. DAG-CLIP: A DAG Learning Framework in the Presence of Latent Variables

**Authors:** Siliang Zhang, Yunxiao Chen, Irini Moustaki

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.06086v1) | 📄 [PDF](https://arxiv.org/pdf/2610.06086v1)

**Summary:** Learning directed acyclic graphs (DAGs) to uncover causal mechanisms has attracted substantial attention in machine learning. While most existing methods focus exclusively on observed variables, many variables of substantive interest are latent constructs defined by statistical measurement models. Such constructs are particularly common in the social and behavioral sciences. In this paper, we propose a general statistical framework for DAG learning when some or all nodes of the graph are latent ...

---

### 23. Global Communication or Graph-Specific Memory?

**Authors:** Hamed Shirzad, Danica J. Sutherland

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.05874v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05874v1)

**Summary:** Scalable Graph Transformers are commonly trained and evaluated on static large graphs in a transductive setup. Many scalable Graph Transformer components can be formulated as a constant-size shared memory, similar to virtual nodes, providing compressed information about the whole graph. The counterpart of these models in language models and other domains is justified as the input changes, and this mechanism learns to compress some useful information about the input. In transductive learning on a...

---

### 24. Finite-Sample Distribution Theory and Efficient Large-Scale Inference for Online Quantile Regression

**Authors:** Ziyang Wei, Jiaqi Li, Lan Wang, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.05869v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05869v1)

**Summary:** This paper studies online quantile regression for large-scale and streaming data using Stochastic SubGradient Descent (SSGD) with constant learning rates. Classical offline inference for quantile regression is computationally and memory intensive. Existing works of online inference for quantile regression provide only asymptotic guarantees and typically require sub-exponential tail conditions for distribution theory. To bridge these gaps, we introduce new techniques to prove a quenched central l...

---

### 25. On the Sequentially Semiseparable Structure of SDE-Induced Kernels and Efficient Algorithms for Kernel-Based Estimation Problems

**Authors:** Mikkel Paltorp, Luigi Caglio, Tianshi Chen, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.05856v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05856v1)

**Summary:** We study kernel functions induced by a linear time-invariant (LTI) stochastic differential equation (SDE), an approach that embeds prior knowledge about the function to be estimated directly into the state-space description of the SDE. This kernel-design perspective is relevant across the many settings where kernels play a central role, including kernel methods in statistics, Gaussian process (GP) regression in machine learning, and kernel-based regularization methods in system identification. T...

---

### 26. The Blind Spot Paradox: When Adaptive Classifiers Defeat Drift Detectors

**Authors:** Raphaël Minato, Fabrice Popineau, Arpad Rimmel, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.05853v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05853v1)

**Summary:** Monitoring concept drift from an adaptive classifier's error stream creates an operational conflict with the model's own update loop. When internal adaptation outpaces evidence accumulation, accuracy recovers before cumulative detectors (CUSUM, Page-Hinkley) can reach threshold. Instrumenting an Adaptive Random Forest (ARF) shows that surviving trees absorb 98.6% of the post-drift error transient through incremental leaf updates alone. The first background tree swap accounts for just 0.71% of th...

---

### 27. Isotropic Gaussian Processes Improve Vanilla Bayesian Optimization in High Dimensions

**Authors:** Wei-Ting Tang, Madhav Muthyala, Joel A. Paulson

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.05780v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05780v1)

**Summary:** High-dimensional Bayesian optimization (BO) often fits Gaussian process (GP) surrogates from far fewer observations than input dimensions. Modern Vanilla BO can perform well in this regime with dimension-aware priors, initialization, and acquisition optimization, but it typically retains automatic relevance determination (ARD), fitting one lengthscale per input coordinate. We study this modeling choice and propose Iso-BO, a controlled modification that replaces the ARD GP with an isotropic GP us...

---

### 28. Global error estimators for parametric monotone nonlinearities and neural approximations

**Authors:** Pablo Cortés Castillo, Wolfgang Dahmen, Jay Gopalakrishnan

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.05767v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05767v1)

**Summary:** We construct computable error estimators, which double as loss functions for neural networks, for a class of parametric nonlinear partial differential equations with a monotonicity property, and prove that they are globally reliable and efficient. The value of such a loss function is bounded above and below by the squared error in the natural trial norm, for every trial function, not merely for those near the exact solution; this global property rests on monotonicity. The construction rests on s...

---

### 29. Retrieval-Based In-Context Learning: A Domain Adaptation Framework

**Authors:** Yilun Zhu, Naihao Deng, Yingcong Li, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.05717v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05717v1)

**Summary:** In-context retrieval (ICR) is a retrieval-based form of in-context learning (ICL) in which demonstrations are retrieved from a source database based on similarity to the query, rather than sampled independently. In this work, we formulate ICR as a type of domain adaptation problem, where the source distribution $P$ of the database may differ from the target distribution $Q$ of the test query-label pair. We investigate the performance of ICR under a flexible class of distributional shifts that su...

---

### 30. From Pixels, Without Pre-training: Joint Generative and Self-Supervised Representation Learning in One Model

**Authors:** Vicente Balmaseda, Ching-Long Lin, Tianbao Yang

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.05711v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05711v1)

**Summary:** Strong image generation models are conditioned on class labels, aligned to frozen pretrained encoders, or built on separately trained autoencoders. While effective, generation then depends on supervision or pretraining: labels must be annotated, and encoders or autoencoders pretrained for the target domain. We study joint generative and self-supervised representation learning in a single model, enabling self-conditioned generation without labels or pretrained models. This is challenging because ...

---

### 31. Two-Sample Testing via Path-based Inference

**Authors:** Eshant English, Wei-Cheng Lai, Yanfeng Yang, et al.

**Published:** 2026-10-05

🔗 [Paper](http://arxiv.org/abs/2610.05684v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05684v1)

**Summary:** Modern deep generative models are primarily studied for their ability to generate realistic samples, yet the generative dynamics they learn can also serve as objects of statistical inference. We develop this idea for two-sample testing, the problem of deciding whether the same distribution generated two finite datasets. Using stochastic interpolants, we connect both distributions to a shared Gaussian bottleneck, so that each half of the resulting path is a Gaussian channel acting on a single pop...

---

### 32. Gaussian Limits for SGD Without Stationary Moments

**Authors:** Xiaoli Li, Wei Biao Wu

**Published:** 2026-10-04

🔗 [Paper](http://arxiv.org/abs/2610.05599v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05599v1)

**Summary:** Temporal dependence can separate the Gaussian approximation of stochastic gradient descent from its stationary moments. For unmodified least-squares SGD, we construct a design with standard Gaussian marginals whose stationary error has every positive moment infinite. Independent observations with the same marginals instead give finite stationary variance. Both regimes retain a Gaussian small-step limit. Our general theory establishes pathwise contraction from a finite second design moment, then ...

---

### 33. Moment-Accurate Gaussian Mixtures for Constant-Step Stochastic Approximation

**Authors:** Xiaoli Li, Wei Biao Wu

**Published:** 2026-10-04

🔗 [Paper](http://arxiv.org/abs/2610.05595v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05595v1)

**Summary:** Local Gaussian models of constant-step learning predict output variability and expected losses, but weak convergence alone does not justify these moment predictions. We establish moment-accurate Gaussian mixtures by matching stationary energy with local Ornstein--Uhlenbeck limits, ruling out quadratic tail mass invisible to weak convergence. For step size $a$, the second-order Wasserstein error is $o(\sqrt a)$, uniformly over invariant laws, using each law's actual root weights. The assumptions ...

---

### 34. G-CARB: Graph-Localized Conformal Agent Risk Budget for Compositional Harm

**Authors:** Zijun Yu, Yu Gu, Vahid Partovi Nia, et al.

**Published:** 2026-10-04

🔗 [Paper](http://arxiv.org/abs/2610.05563v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05563v1)

**Summary:** Small language model (SLM) agents need safety controls that track consequences across tool calls with little monitoring overhead. A private read, for example, becomes a leak when a later action sends that data outside the system. We introduce CARB (Conformal Agent Risk Budget), which calibrates when to stop an agent using a ledger of harm incurred before stopping. Under exchangeable episodes, standard conformal risk control bounds this declared loss in expectation over calibration and a future e...

---

### 35. Taylor Representations for Model-Free RL in Networked MDPs

**Authors:** Salah Chikhi, Abdelhaq Chaoui, Asuman Ozdaglar, et al.

**Published:** 2026-10-04

🔗 [Paper](http://arxiv.org/abs/2610.05456v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05456v1)

**Summary:** In Networked Markov Decision Processes, transition dynamics are often unknown and the state--action space grows rapidly with the number of agents. In this setting, Taylor representations naturally approximate $Q$-functions, but a naive order-$n$ expansion over $N$ agents requires $Θ(N^n)$ coefficients. We justify these expansions under smooth expected future local rewards with controlled derivatives. Under this condition, finite-speed information propagation and discounting imply that local-crit...

---

### 36. Poisson Autoregression on a Large Network with a Stochastic Block Model Structure

**Authors:** Mahmoud Khabou, Joanna Marks, Joshua Corneck, et al.

**Published:** 2026-10-04

🔗 [Paper](http://arxiv.org/abs/2610.05365v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05365v1)

**Summary:** We consider multivariate Poisson autoregressive processes evolving on random networks generated by a Stochastic Block Model. This framework extends existing network Poisson autoregressions by incorporating latent community structure and allowing for non-Markovian dependence, both excitatory and inhibitory. We establish a mean-field approximation and prove that the finite system converges to its limit at the optimal rate $N^{-1/2}$ in the quenched setting with overwhelming probability, both on av...

---

### 37. Diffusion Transformers are Provably Optimal In-context Generators

**Authors:** Guoji Fu, Tomoya Wakayama, Ryotaro Kawata, et al.

**Published:** 2026-10-04

🔗 [Paper](http://arxiv.org/abs/2610.05333v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05333v1)

**Summary:** Generative foundation models are attracting interest for their ability to produce desired outputs from demonstrations given at inference time, without updating parameters. However, since a few demonstrations cannot uniquely identify the intended task, the challenge is how to learn and sample from an output distribution that reflects this task uncertainty. In this work, we theoretically analyze how a Diffusion Transformer (DiT), pretrained across diverse tasks, learns and generates predictive dis...

---

### 38. Quantitative Universality of Approximate Message Passing for Rank-One Quadratic Sensing

**Authors:** Duy Thuc Nguyen, Yue M. Lu, Subhabrata Sen

**Published:** 2026-10-04

🔗 [Paper](http://arxiv.org/abs/2610.05327v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05327v1)

**Summary:** Approximate Message Passing (AMP) algorithms are attractive as they are computationally efficient and simultaneously admit a precise characterization in terms of the low-dimensional "state-evolution" recursion. In this work, we establish quantitative universality for AMP with centered rank-one sensing matrices $Z_i=(x_ix_i^\top-I_d)/\sqrt d$, where $x_i$ are independent standard Gaussian vectors. These matrices arise in quadratic regression and learning quadratic neural networks. Their normalize...

---

### 39. Measuring Learned Monotone Temporal Aggregation at Matched Admissibility

**Authors:** Yew Lee Tan

**Published:** 2026-10-04

🔗 [Paper](http://arxiv.org/abs/2610.05196v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05196v1)

**Summary:** Risk regulation imposes directional constraints on scores; we adopt their strict per-input form -- the score monotone non-decreasing in every exposure input -- as a normative commitment. Deployed pipelines -- monotone hand-crafted aggregates feeding sign-constrained gradient boosting -- already satisfy it by composition, so constrained-versus-unconstrained comparisons price a guarantee the incumbent has for free. We instead hold admissibility fixed on both sides and measure what learning the agg...

---

### 40. Selecting Repetition Counts Across Model Scales in Data-Constrained Pretraining

**Authors:** Ziyue WANG, T. Kanamori

**Published:** 2026-10-04

🔗 [Paper](http://arxiv.org/abs/2610.05126v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05126v1)

**Summary:** The repetition count that works best for a small language model may not remain best at a larger scale. We study this effect in pretraining with a finite target corpus mixed with generic data at a fixed target fraction. On Wikipedia-derived data and Proof-Pile-2, the ranking of measured repetition counts changes with model size, and a 520M Proof-Pile-2 experiment confirms that reducing repetition from sixteen to eight improves loss while using fewer training tokens. We use loss curves from severa...

---

### 41. A Statistical Inference Framework for PMI Estimation and SGNS Word Embeddings

**Authors:** Zhongqi Fan

**Published:** 2026-10-04

🔗 [Paper](http://arxiv.org/abs/2610.05058v1) | 📄 [PDF](https://arxiv.org/pdf/2610.05058v1)

**Summary:** Pointwise Mutual Information (PMI) is a core measure of testing word association, and Skip-gram with Negative Sampling (SGNS) is essentially a method that implicitly factorizes a shifted PMI matrix. However, a systematic and well-rounded characterization of finite-sample uncertainty in PMI estimation remains absent and imperative to venture into.   We provide a statistical framework for PMI estimation and its connection to SGNS. We prove consistency, asymptotic unbiasedness, and asymptotic norma...

---

### 42. Beyond Overparameterization: Provable Learning of Input-Convex Multi-Layer Polynomial Networks with Active Queries

**Authors:** Jinqi Tang, Qian Chen, Shihong Ding, et al.

**Published:** 2026-10-04

🔗 [Paper](http://arxiv.org/abs/2610.04999v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04999v1)

**Summary:** The theoretical understanding of multi-layer neural networks is largely confined to overparameterized settings, which obscure parameter identifiability and incur high sample complexity. Neural tangent kernel (NTK) provides a general theory for wide networks, but does not offer efficient sample-complexity guarantees. Recent feature-learning results go beyond kernel methods for single-neuron, multi-index, and hierarchical targets. However, the analysis is often restricted to shallow or specific ar...

---

### 43. When Is a Graph a Covariance? Bayesian Residual Propagation under Covariance Uncertainty

**Authors:** Robert Richardson

**Published:** 2026-10-04

🔗 [Paper](http://arxiv.org/abs/2610.04989v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04989v1)

**Summary:** Observing a prediction error at one node can help correct predictions elsewhere, but the benefit depends on the residual dependence between nodes. A graph suggests where that dependence might occur, yet does not establish its sign or strength. We develop a Bayesian model of residual covariance to determine how revealed errors should update a fixed feature-based predictor. For a fixed set of revealed nodes, we derive an exact identity for the change in expected squared error under linear residual...

---

### 44. Efficient Mass Matrix Estimation with Gaussian Cooling

**Authors:** Jake Hofgard, Michael Lindsey

**Published:** 2026-10-03

🔗 [Paper](http://arxiv.org/abs/2610.04806v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04806v1)

**Summary:** We introduce an algorithm for efficiently preconditioning log-concave and log-smooth distributions that scales logarithmically with the condition number of the underlying distribution. Based on Gaussian cooling, our multistage method approximately samples from a sequence of well-conditioned distributions to construct a preconditioner for each subsequent stage of the cooling schedule. This method is motivated by existing practical approaches for mass matrix estimation in Markov chain Monte Carlo ...

---

### 45. Calibration Assessment for Nested Uncertainty Sets

**Authors:** Matthew LeDuc

**Published:** 2026-10-03

🔗 [Paper](http://arxiv.org/abs/2610.04790v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04790v1)

**Summary:** We present a Bayesian framework for assessing the calibration of nested uncertainty sets from simulation studies. Calibration is typically evaluated by repeatedly simulating data from a known model and comparing empirical coverage probabilities with their nominal values, an approach that often requires hundreds or thousands of independent model evaluations to obtain reliable estimates. Such computational demands can be prohibitive when the forward models are expensive to evaluate, for example in...

---

### 46. When Is Enough Enough in Self-Evolving LLM Systems?

**Authors:** Enoch Yin, Bin Liu, Zhengling Qi

**Published:** 2026-10-03

🔗 [Paper](http://arxiv.org/abs/2610.04756v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04756v1)

**Summary:** Self-evolving large language model (LLM) systems repeatedly propose, evaluate, and incorporate updates to prompts, skills, or other persistent artifacts. Despite their growing effectiveness, these systems typically operate under a predetermined iteration or compute budget, without a principled criterion to determine when further evolution is no longer worthwhile. This can lead to two undesirable consequences: unnecessary computation after performance has saturated and the risk of returning late ...

---

### 47. Variance-Aware Fine-Grained Gap-Dependent Bounds for Online Reinforcement Learning

**Authors:** Haochen Zhang, Lingzhou Xue, Zhong Zheng

**Published:** 2026-10-03

🔗 [Paper](http://arxiv.org/abs/2610.04752v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04752v1)

**Summary:** We study model-free online reinforcement learning (RL) for episodic tabular Markov decision processes, focusing on both gap-dependent regret and policy switching cost. While fine-grained gap-dependent analysis has been established for model-free RL algorithms using Hoeffding-type exploration bonuses, such results for model-free algorithms with variance-based exploration bonuses remain unknown, despite their superior worst-case and coarse-grained gap-dependent guarantees. In this paper, we resolv...

---

### 48. Exact Fast Batch Simulation for Tabular Reinforcement Learning

**Authors:** Haochen Zhang, Lingzhou Xue, Zhong Zheng

**Published:** 2026-10-03

🔗 [Paper](http://arxiv.org/abs/2610.04746v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04746v1)

**Summary:** Simulation is a fundamental computational primitive in reinforcement learning (RL), yet conventional simulation explicitly generates individual trajectories even when downstream procedures use only aggregate statistics. To address this, we develop an exact fast-simulation framework for finite-horizon tabular Markov decision processes. Our framework has two complementary modes. In direct batch simulation, a batch is represented by its aggregate Markov flow. With sufficient parallel simulation res...

---

### 49. Hypergraph Representation Learning with Hyperlink Random Effects

**Authors:** Zimeng Li, Shihao Wu, Gongjun Xu, et al.

**Published:** 2026-10-03

🔗 [Paper](http://arxiv.org/abs/2610.04640v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04640v1)

**Summary:** Hypergraphs record multi-way interactions among entities. Extracting information from the combinatorial structure underlying observed multi-way interactions is a central task in many real-world problems. Existing methods face several limitations. First, many deep architectures for hypergraphs do not explicitly exploit the potential low-rank structure, which can sacrifice parsimony and interpretability in the learned representations. Second, many low-rank-based methods operate on tensor represent...

---

### 50. Gradient-Free Sampling from Generative Models via Stochastic Bounded Extremum Seeking

**Authors:** Alexander Scheinker

**Published:** 2026-10-03

🔗 [Paper](http://arxiv.org/abs/2610.04568v1) | 📄 [PDF](https://arxiv.org/pdf/2610.04568v1)

**Summary:** We introduce a sampling approach for energy- and score-based generative models that requires no gradient evaluations of the model. Replacing the drift term that would normally contain the score $\nabla_\mathbf{x} \log p_θ(\bf{x})$ with a high-frequency dithered cosine of the model's \textit{value}, $\sqrt{αω}\,\cos(ωt + k \log p_θ(\bf{x}))$, produces, in the high-frequency averaging limit, Langevin Markov chain Monte Carlo for energy-based models and the reverse-time SDE of score-based diffusion...

---

