# arXiv Daily Digest - 2026-09-15

Total papers: 50

---

## cs.CL

**50 papers**

### 1. Bellman Policy Optimization

**Authors:** Zhuoqing Song, Haotian Xu, Xikun Zhang, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15987v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15987v1)

**Summary:** Reinforcement learning with verifiable rewards (RLVR) improves the reasoning capabilities of large language models (LLMs). We introduce Bellman Policy Optimization (BPO), a critic-free method derived from Policy Mirror Descent (PMD). For autoregressive generation with terminal rewards, BPO uses the Bellman equations to reformulate PMD as a trajectory-level objective. The reformulation avoids estimating state values at intermediate states. We prove that it has the same unique optimal solution as ...

---

### 2. Stellar Colosseum: A Many-Agent Harness for Long-Horizon Research in Mathematics and Theoretical Computer Science

**Authors:** Honghao Lin, David P. Woodruff, Yuan Deng, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15983v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15983v1)

**Summary:** Language models can produce plausible short proofs, but may still be unreliable on long-horizon research problems, where progress depends on a sequence of uncertain and interdependent decisions. We introduce Stellar Colosseum, a model-agnostic harness for allocating inference across research in mathematics and theoretical computer science. Colosseum explores alternative strategies before proof construction, uses a readiness gate to decide when a route is mature enough to decompose, represents th...

---

### 3. The Router Within: Eliciting Native Skill Routing from a Frozen LLM

**Authors:** Ruishuo Chen, Xun Wang, Yu Chen, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15982v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15982v1)

**Summary:** Skills extend an LLM agent beyond its parametric knowledge, and the gain they promise rests on picking the right one. Deployed harnesses route by preloading every skill's metadata into the context, which disperses the agent's attention and caps the library size. Retrieval pipelines move the selection out of the context, but also out of the agent's capability. We show that the frozen agent LLM already carries the routing signal in its own forward passes, and that two linear maps suffice to read i...

---

### 4. Disentangling Representation Evolution in Transformers through Directional Decomposition

**Authors:** Shwai He, Haichao Zhang, Shen Yan

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15975v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15975v1)

**Summary:** Transformer representations evolve through learned additive transformations that either preserve their current direction or redirect it. We study this evolution as a functional geometry, decomposing learned updates into parallel and perpendicular components. Across pretrained models, we find substantial parallel components beyond the residual identity path. We then apply the decomposition in two spaces: to attention and MLP updates relative to the hidden state, and to attention value aggregation...

---

### 5. Discovery Foundation Models: Toward Open-Ended Discovery Intelligence

**Authors:** Ling Yang, Zhenfei Yin, Yingcheng Wu

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15973v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15973v1)

**Summary:** Foundation models have progressed from learning and reasoning over existing knowledge, to increasingly learning through action, tool use, and outcome feedback. We argue that the next frontier is a further transition: from solving and acting within problems specified by humans to participating in the process by which new problems, representations, explanations, and knowledge are created. We refer to this capability as Discovery Intelligence. We formulate Discovery Foundation Models (DFMs) as gene...

---

### 6. Mind2Dialogue: Training Human-Aware Language Models by Simulating User Mental States

**Authors:** Zixuan Wang, Yufan Zhou, Jinzhou Tang, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15972v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15972v1)

**Summary:** As language models become more capable, long-term collaboration in learning, reasoning, and decision-making calls for a deeper understanding of the people they serve. Yet training such human-aware language models faces a fundamental supervision gap because current datasets for LLM assistant training contain few if any well-informed responses explicitly grounded in users' unspoken beliefs and goals. Scaling such supervision is inherently constrained, as users' underlying states are not directly o...

---

### 7. Verifiable by Construction: Claim-Level Evaluation of Verbatim Citation in Clinical Question Answering

**Authors:** Jiashuo Zhang, Yuling Chen, Yvonne Commodore-Mensah, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15964v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15964v1)

**Summary:** Large language models (LLMs) have been widely adopted for clinical question answering (QA). Current systems can attach citations to their answers, but these often point to broad texts, leaving time-pressed clinicians unable to verify them efficiently. An alternative is to ensure that responses are verifiable by construction: providing fine-grained verbatim quotes from reference material that substantiate claims, so users can verify an answer without opening other documents. In this paper, we eva...

---

### 8. HypoEvolve: Genetic Algorithms Enable Multi-Agent LLMs to Discover Scientific Hypotheses

**Authors:** Jieyuan Liu, Mengzhou Hu, Jefferson Chen, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15938v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15938v1)

**Summary:** Scientific agents contribute to hypothesis discovery by synthesizing evidence, assessing proposals, and developing new explanations. Recent systems combine scientific agents with evolutionary search through critique, comparison, and revision. However, how different forms of agent collaboration affect hypothesis quality remains an open question. Answering this question requires separating the effects of agents' scientific capabilities from those of their collaboration. A framework must therefore ...

---

### 9. Inoculation Midtraining with Learned Neologisms

**Authors:** Kyle O'Brien, Edward James Young, Puria Radmard, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15886v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15886v1)

**Summary:** Large language models (LLMs) often learn both desirable and undesirable properties during post-training. We study whether midtraining, an earlier training stage, can shape which of these properties later generalise. We introduce Inoculation Midtraining, a technique that teaches a base model that unsafe behaviour belongs to a designated <quarantine_token> context, as indicated by the <quarantine_token> neologism (a new token) introduced during midtraining, and then post-trains the model on unsafe...

---

### 10. K-Bench: a clinically calibrated benchmark for evaluating large language models in high-risk mental health conversations

**Authors:** Laura M. Vowels, Matthew J. Vowels, Shivali Sharma, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15855v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15855v1)

**Summary:** % !TEX root = ../main.tex People increasingly use large language models (LLMs) for mental health support, yet their safety in evolving, high-risk conversations remains poorly characterised. We developed K-Bench, a clinician-calibrated, protected benchmark evaluating 125 model configurations representing 33 base models from 14 providers across a fixed cohort of 200 multi-turn vignettes involving suicide, self-harm, domestic violence, substance misuse, and no-risk presentations. Synthetic patient ...

---

### 11. Learning to Coach for Experiential Learning

**Authors:** Guanheng Chen, Tianzhu Ye, Li Dong, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15851v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15851v1)

**Summary:** Language models can learn from experience, but raw solution trajectories are often too long and noisy to provide effective guidance. In this work, we propose Learning to Coach (L2C), a framework that trains a dedicated LLM-as-a-Coach to extract actionable experiential knowledge from an actor model's previous trajectory. The actor remains frozen, while the LLM-as-a-Coach is trained to maximize a reward given by the correctness of the actor's guided response. We study two such rewards: a same-inst...

---

### 12. Before You Poll with LLMs: A Deliberative Diagnostic Framework

**Authors:** Ahmed Wali, Hassaan Tayyab

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15849v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15849v1)

**Summary:** Can LLMs reason through new information like humans, or do they merely retrieve cached opinions? This is critical for silicon sampling, where LLM personas simulate public opinion at scale. Current evaluations test only whether personas hold the right opinions -- a static snapshot. But opinion research increasingly depends on dynamic fidelity: whether personas update beliefs in response to new arguments, as humans do during deliberation. No existing benchmark tests this. We introduce the Delibera...

---

### 13. CiteGuard-RAG: A Validation-Centered AI System for Evidence-Grounded Question Answering

**Authors:** Sumit Barua, Guan Hong, Halil Dursunoglu, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15830v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15830v1)

**Summary:** Retrieval-augmented generation (RAG) can improve access to complex information; however, retrieving evidence alone does not ensure that answers are grounded, citation-valid, or appropriately refused. This paper introduces CiteGuard-RAG, a validation-centered AI system for evidence-grounded question answering. The system integrates hybrid semantic-lexical retrieval, citation-constrained generation, sentence-level grounding validation, and single-pass regeneration. Validation is used at runtime to...

---

### 14. EvoOntology: A Self-Evolving Ontology Layer for Data Agents

**Authors:** Meiduo Chong, Shaolei Zhang, Ju Fan, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15779v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15779v1)

**Summary:** Data agents aim to fulfill natural-language instructions over heterogeneous data, including tables, files, and databases. However, data agents face a challenging agent-data gap: heterogeneous data resides outside the agent, while the agent can access it (e.g., column names and file paths) only through generic tools. Existing approaches either let agents directly explore raw data sources or inject manually constructed semantic layers into prompts. However, neither scales well to large heterogeneo...

---

### 15. Enabling Streaming User Transcription in Full-Duplex Speech-to-Speech Models

**Authors:** Ke Hu, Nourchene Ferchichi, Edresson Casanova, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15759v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15759v1)

**Summary:** Full-duplex speech-to-speech (S2S) models enable natural conversational AI by allowing simultaneous listening and speaking. However, these models typically lack inherent user speech transcription, which is essential for applications such as conversation logging, accessibility features, and quality monitoring. In this work, we propose an efficient method to add streaming ASR capabilities to an existing duplex S2S model by introducing a lightweight ASR head in parallel to the agent text head. Our ...

---

### 16. Sequential Adapter Stacking for Cross-Lingual Low-Resource ASR

**Authors:** Thai Thi Thanh Thao Dang, Mengjie Qian, Kate Knill

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15758v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15758v1)

**Summary:** Extending large-scale multilingual automatic speech recognition (ASR) models to low-resource languages remains challenging. Model performance is skewed toward high-resource languages and degrades sharply for languages with limited labeled data and pre-training exposure. To address this, we investigate parameter-efficient approaches for transferring knowledge from resource-rich source languages to low-resource target languages on Whisper. Alongside warm initialization and attention-based fusion, ...

---

### 17. Look Before You Leap: Factual Decoding with Internal Attribution Signals

**Authors:** Hayeong Ryu, JungMin Yun, Byeonggeuk Lim, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15745v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15745v1)

**Summary:** Hallucination remains a critical challenge in large language models (LLMs), where early factual errors compound through autoregressive generation in a snowballing effect that neither post-hoc correction nor weight-level intervention can effectively preempt. We propose DescaPE (DEcoding Signal Control Against Path Error-snowballing), a decoding framework that leverages internal model signals to suppress hallucination-prone trajectories at inference time. Through sliding-window MLP ablation, we id...

---

### 18. Merging the Knowledge of LLMs for Automatic Speech Recognition

**Authors:** Hayato Futami, Tatsuya Kawahara

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15743v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15743v1)

**Summary:** Automatic speech recognition (ASR) systems, trained on paired speech-text data, have been improved by leveraging language models (LMs) trained on text-only data. LM fusion methods such as shallow fusion and density ratio are well-established methods that incorporate external LMs during ASR decoding. However, they incur additional computational costs due to LM inference, which is particularly problematic for recent larger LMs. In this study, we propose incorporating external LMs via model merging...

---

### 19. Data storytelling meets interpretable machine learning: Decoding AI decisions for non-experts without revealing sensitive data and model details

**Authors:** Lemen Chao, Zixuan Yang, Anran Fang, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15722v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15722v1)

**Summary:** AI-driven automated decision-making requires both predictive performance and interpretability. Recent advances in interpretable machine learning (IML) provide tools for explaining model predictions, but the technical complexity of these explanations may hinder accessibility to non-experts. To address this challenge, this study integrates data storytelling with IML to enhance the explainability of AI-generated decisions for a broader audience. Following the design science research (DSR) paradigm,...

---

### 20. RESKILL: Explicit Failure Attribution and Structured Repair for Interactive Language Agents

**Authors:** Mengyi Deng, Xin Li, Duyi Pan, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15684v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15684v1)

**Summary:** Language agents increasingly rely on reusable skills, but post-failure repair is often handled by opaque one-shot reflection: a model generates a skill patch without explicitly maintaining how failure explanations relate to candidate repairs or how unsuccessful retests should influence later edits. We introduce RESKILL, a structured repair framework that maintains an explicit repair state across repair rounds. Given a failed rollout, the framework links failure hypotheses to candidate skill patc...

---

### 21. CiteShade: Citation Laundering in Multi-Source Retrieval-Augmented Generation and Its Counterfactual Defense

**Authors:** Guo Fuzheng

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15660v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15660v1)

**Summary:** Retrieval-augmented generation (RAG) grounds a language model's answers on retrieved external knowledge and returns each answer with citations that identify its sources. Those citations are the user's audit trail: they let a reader verify a claim without trusting the model. Prior security work on RAG asks whether an attacker can corrupt the answer, leaving the citation channel unexplored. We show that this channel is a new and practical attack surface. We propose CiteShade, the first citation la...

---

### 22. Empathy Is Steerable but Multi-Axial: Mechanism Geometry and Persona Effects in LLMs

**Authors:** JuHeon Ha, Byounghan Lee, Yunseo Choi, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15654v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15654v1)

**Summary:** Activation steering has been used to control traits such as honesty, refusal, and sycophancy, yet supportive empathy is evaluated along multiple dimensions that need not correspond to independently controllable activation directions. Using the EPITOME framework, which decomposes supportive empathy into Emotional Reactions, Interpretations, and Explorations, we study three instruction-tuned LLMs and ask whether candidate directions derived from these labels produce distinguishable intervention ef...

---

### 23. Human-Grounded Calibration for Long-Text Image-Text Congruence in Vision-Language Models

**Authors:** Alessandro Gambetti, Qiwei Han

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15640v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15640v1)

**Summary:** Long-text image--text congruence scoring is increasingly important for vision-language systems that must evaluate whether detailed textual descriptions match visual content. However, raw similarity scores from dual-encoder models are difficult to interpret as calibrated congruence measures, especially under the modality gap between image and text embeddings. This paper proposes Congruency Score (CS), a lightweight calibration layer that maps image--text similarity evidence into a bounded score. ...

---

### 24. IROH: Insightful Ranking Of Humor using Multi-Stage Hybrid Retrieval with Rationale-Distilled LLM Judges for JOKER 2026 Track Task 1 English

**Authors:** Ana-Maria Luisa Mocanu, Sebastian Mocanu, Ciprian-Octavian Truică, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15618v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15618v1)

**Summary:** Our team, VANGUARD, presents IROH (Insightful Ranking of Humor), a three-stage retrieval system for JOKER Task 1 English at CLEF 2026, achieving first place on the leaderboard with 0.6347 MAP. Our pipeline combines hybrid sparse-dense retrieval, cross-encoder reranking, and a LoRA-adapted Large Language Model judge ensemble. We employ Gemma 4 to generate query-aware rationales under two prompt strategies, generic and typed, and produce up to four types of structured hard negatives for training d...

---

### 25. Through the Eyes of the Beholder: Biometric and Demographic Conditioning for Multimodal Sexism Detection

**Authors:** Ana-Maria Luisa Mocanu, Sebastian Mocanu, Ciprian-Octavian Truică, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15608v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15608v1)

**Summary:** Detecting sexism on the internet is a fundamentally subjective task; our team, VANGUARD, addresses this challenge in the EXIST 2026 Task 2 by proposing a human-centered multimodal framework that analyses and incorporates the psychological and demographic characteristics of human annotators into the detection pipeline. We fuse five input modalities through a cross-attention architecture with Feature-wise Linear Modulation conditioning. Meme text is extracted and visually described with Gemma 4, t...

---

### 26. Can We Trust the Judges? Validation of Factuality Evaluation Methods via Answer Perturbation

**Authors:** Sarra Gharsallah, Adele Robaldo, Mariia Tokareva, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15561v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15561v1)

**Summary:** Evaluating the factual correctness of large language models (LLMs) is vital for many applications. But are our evaluation tools themselves trustworthy? Despite the rise of factuality-based metrics, their sensitivity and reliability remain underexplored. This paper introduces a meta-evaluation framework that systematically tests these metrics using controlled corruptions of gold standard answers. Our method generates ranked outputs with known degrees of degradation to probe how metrics capture nu...

---

### 27. Don't Count the Edits, Judge by the Outcome Alone: Reward-Based Evaluation for Grammatical Error Correction

**Authors:** Hayeong Ryu, Sunhee Jo, Seunguk Yu, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15559v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15559v1)

**Summary:** Grammatical error correction (GEC) evaluation has traditionally relied on reference or edit overlap, which can penalize valid rewrites that differ from gold corrections. Reference-free metrics reduce this dependence, but evaluating whether a fluent output is a valid correction of the source remains challenging. We propose SURE, a source-conditioned reward evaluator trained on within-source preferences spanning minimal-edit and rewrite-oriented corrections. SURE jointly learns an overall reward w...

---

### 28. Option-Aware Retrieval and Task-Specific VLM Adaptation for Medical VQA

**Authors:** Tristan Kirscher, Niklas C. Koser, Soren Pirk

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15530v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15530v1)

**Summary:** We describe our submission to the MedReason 2026 challenge, covering multiple-choice (MCQ) and open-ended (OE) medical visual question answering (VQA) under fully offline, containerized inference. Our first finding is that MCQ retrieval must compare answer \emph{semantics} rather than answer labels: labels are independently assigned per question, so copying a retrieved neighbor's label transfers no useful information, whereas scoring each current option's text against correct-answer text from si...

---

### 29. To Each Language Its Tokenizer: Modular Tokenizers for Efficient Multilingual LLMs

**Authors:** Franck Signe, Hippolyte Pilchen, François Yvon, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15528v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15528v1)

**Summary:** Multilingual Large Language Models (LLMs) traditionally rely on a single vocabulary shared by all supported languages, which can lead to uneven compression across them. Moreover, their large embedding and output matrices increase memory usage and slow inference, notably for small-scale models. It is also wasteful as models are often used for only a subset of languages. To address these issues, we introduce a modular framework for multilingual model training. First, we propose methods to learn la...

---

### 30. Psychosis involves a deficit of information compression in connected speech

**Authors:** Samuele Vallisa, Claudio Palominos, Rui He, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15522v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15522v1)

**Summary:** Large language models (LLMs) with human-like performance on linguistic tasks have transformed the study of language in neurodiverse conditions. LLMs provide representations of linguistic input in the form of high-dimensional vectors (embeddings), and next-token predictions computed from these embeddings. Previous crosslinguistic evidence suggests a complexity reduction in the form of both lower intrinsic dimensionality (ID) of LLM representations and higher mean surprisal (prediction error) in p...

---

### 31. Beyond Safe Answers: Segment-Aware Listwise Alignment for Reasoning Safety in Large Reasoning Models

**Authors:** JungMin Yun, Junehyoung Kwon, Hayeong Ryu, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15517v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15517v1)

**Summary:** Large Reasoning Models (LRMs) pose a dual-surface safety challenge: both intermediate reasoning traces and final answers can contain harmful content. Existing alignment methods often operate at the whole-response level, allowing unsafe reasoning to be masked by a safe-looking final answer. We propose Segment-aware Listwise Target DPO (SaLT-DPO), which addresses this gap through three mechanisms: (1) segment-aware listwise alignment that decomposes responses into reasoning and answer segments, in...

---

### 32. Authorship attribution and aesthetic evaluation of AI poetry: a case study with Haiku

**Authors:** Livia Oddi, Simone Scardapane, Toru Sugimoto, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15511v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15511v1)

**Summary:** This paper investigates the generation and human evaluation of Japanese haiku by contemporary Large Language Models (LLMs), focusing on authorship perception and aesthetic judgment within a constrained poetic form. Using a few-shot prompting strategy, Japanese haiku were generated across a heterogeneous set of large language models, including open- and closed-source systems, medium-scale and large-scale architectures, models with native or adapted Japanese support, and multilingual proprietary m...

---

### 33. How Lossless Is Lossless Speculative Decoding? The Role of Numerical Precision in Orthrus

**Authors:** Ilya Koziev, Leonid Sinev, Ivan Oseledets

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15504v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15504v1)

**Summary:** Orthrus is a hybrid autoregressive-diffusion architecture that accelerates autoregressive language-model inference by generating multiple tokens in parallel while using a frozen autoregressive backbone. Its central claim is that an intra-model consensus mechanism enables lossless speculative decoding, producing the same output sequence as the autoregressive model.   We independently reproduce Orthrus and examine this claim under different numerical precisions. Under BF16 inference, exact traject...

---

### 34. Temperature Fragility and the Conditional Benefits of Truncation Sampling

**Authors:** Francesco La Rosa

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15476v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15476v1)

**Summary:** Large language models generate text by sampling each token from a predicted distribution, and a temperature parameter sets how far the draw strays from the most probable tokens. Truncation samplers such as top-p and min-p discard the least probable tokens before the draw, so that sampling at high temperature stays coherent. Their reported accuracy gains come from temperatures of 1.5 to 3, while the defaults of deployed systems cluster between 0.6 and 1.0. Whether they change accuracy at those de...

---

### 35. Turkish MMLU Pro: Traceable Option Augmentation and Its Validity Limits in Turkish Multiple-Choice Evaluation

**Authors:** M. Ali Bayram

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15467v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15467v1)

**Summary:** Adding answer options can lower multiple-choice scores without improving assessment validity. Turkish MMLU Pro examines this distinction using 12,000 Turkish-source questions across 58 sections. Each question retains its stem, five original options and source key, and receives five options copied from other questions in the same section. Sentence-embedding retrieval proposes candidates; a language model selects existing identifiers. Deterministic verification reconstructs all 60,000 additions. A...

---

### 36. MarKey: Marginal Utility Guided Greedy Keyframe Selection for Long Video Understanding

**Authors:** Hongchang Shi, Jinpeng Hu, Ao Wang, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15408v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15408v1)

**Summary:** Long-video understanding remains challenging for multimodal large language models (MLLMs) because densely encoding long frame sequences is computationally expensive, while uniform sampling under a limited visual budget can miss sparse yet decisive evidence. Recent training-free keyframe selection methods have enabled more efficient inference and yielded promising performance gains. However, many existing methods score frames largely in isolation without explicitly considering how each candidate ...

---

### 37. SlopShape: Identifying AI-Generated Commercial Web Content

**Authors:** Jochen Madler

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15369v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15369v1)

**Summary:** Word-level detectors identify unedited AI-generated text almost perfectly, but the literature documents their brittleness under rewording, and a word-level score neither characterizes a text nor identifies which AI model wrote it. We ask whether AI-generated text can be identified one level deeper, from structural signatures: how information is presented, in what order, with what evidence, and in what voice. We replicate StoryScope (Russell et al., 2026), which showed such patterns for AI-genera...

---

### 38. RSIAgent: Autonomous Exploration for Recursive Self-improvement in New Environments

**Authors:** Sibo Zhu, Shicheng Fan, Xinyue Wang, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15364v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15364v1)

**Summary:** Digital agents must often adapt to new environments whose interfaces, tools, and failure modes are not fully captured by pretrained models. We introduce \textbf{RSIAgent}, a training-free multi-agent framework for recursive self-improvement through autonomous memory construction. RSIAgent coordinates curriculum, actor, and verifier agents to continually explore the environment, validate outcomes, and retain environment-specific knowledge, including reusable causal relationships between actions, ...

---

### 39. Parameter-Efficient Adaptation of Pretrained Language Models for Time-Series Forecasting

**Authors:** Tamanna Kumavat, Georg Brunner, Kyriakos Flouris

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15344v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15344v1)

**Summary:** We study the adaptation of pretrained language models to univariate time-series forecasting through a parameter-efficient transfer learning framework, with the goal of understanding which design choices drive effective cross-modal transfer. While language models operate on discrete textual tokens, time series consist of continuous numerical observations with temporal dependencies. To bridge this modality gap, we project fixed-length time-series patches directly into the embedding space of a pret...

---

### 40. Dynamic Semantic Compression for Efficient Latent-Space Inference in Large Language Models

**Authors:** Peipei Li, Dongsen Zhang, Yuchen Liu, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15338v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15338v1)

**Summary:** Large Language Models (LLMs) primarily perform inference at the token level, resulting in substantial memory overhead and compromised computational efficiency. In this paper, we propose a Dynamic Semantic Extraction and Inference (DSEI) framework, which achieves segment-level inference within the latent space through a two-stage training strategy. First, we construct a Dynamic Semantic Autoencoder (DSAE) via self-supervised learning. DSAE dynamically extracts segment-level semantics and compress...

---

### 41. Clean Scores, Buried Evidence, and Confident Wrong: A Receipt-Based Audit of Frontier Agentic QA

**Authors:** Luis M. Sánchez

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15319v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15319v1)

**Summary:** Frontier models score well on shallow document/chart reading tasks. In a controlled data-room audit, moving evidence into buried conditions reduced accuracy, increased forced declarations, increased tool calls, and increased cost per correct answer. Confidence and benchmark calibration did not fully capture wrong answers; a documented production incident shows fabricated structural claims can be mixed with accurate numeric tables. Agentic evaluations need claim-level receipts (statement-level pr...

---

### 42. Reducing the Output-Mode Gap in Speech Language Models via Joint-Output On-Policy Distillation

**Authors:** Daxin Tan, Dehua Tao, Chengxi Deng, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15313v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15313v1)

**Summary:** Autoregressive generation of interleaved text and acoustic tokens is a common approach to spoken-response generation in speech large language models. Although this design enables streaming generation with explicit textual guidance, generated acoustic tokens become part of the context for subsequent text predictions. Given identical speech inputs, we observe markedly lower answer accuracy for the internal text generated in speech-to-text-and-speech (S2TS) mode than for speech-to-text (S2T) respon...

---

### 43. When Agents Slow Down: Understanding LLM Agents' Test-Time Strategies via Elo-per-token Analysis

**Authors:** Kaiyuan Liu, Qiuyang Mang, Bo Peng, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15309v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15309v1)

**Summary:** Large language model (LLM) agents allocate test-time compute adaptively as they revise solutions, use tools, explore alternatives, and decide when to stop. This test-time strategy makes it difficult to measure how agent performance scales. We study open-ended tasks that provide continuous scores for intermediate submissions, making progress observable throughout long trajectories. We propose Elo-per-token analysis, which tracks the best solution found at each token budget and uses a Bradley-Terr...

---

### 44. Reason What Matters: Retrieval-Grounded Reasoning for Universal Multimodal Embeddings

**Authors:** Mingzhou Jiang, Peixi Wu, Hang Cheng, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15296v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15296v1)

**Summary:** Universal multimodal embedding (UME) learns unified representations across modalities, enabling a single model to support diverse retrieval tasks. Recent methods use Chain-of-Thought (CoT) reasoning to better interpret multimodal inputs before generating embeddings for complex retrieval tasks and further optimize this reasoning process through GRPO with retrieval-based rewards. However, two limitations hinder corpus-scale deployment. GRPO assigns all CoT tokens the same advantage, without identi...

---

### 45. Artificial entrepreneurial cognition: Locating and causally steering an opportunity recognition dial inside large language models (LLMs)

**Authors:** Christian Fisch, Angela Altmeier, Martin Obschonka, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15277v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15277v1)

**Summary:** Entrepreneurial cognition is a foundation of entrepreneurship research. Yet the growing involvement of large language models (LLMs) in entrepreneurial work extends the cognition question beyond human actors to systems whose internal representations remain largely unexplored. We introduce artificial entrepreneurial cognition, the functional organisation of entrepreneurship-relevant representations and computations inside artificial intelligence (AI) systems. We bring mechanistic interpretability ...

---

### 46. Semiotic Relations and Proof Methods: A Cross-Genre Study of Argument Structure with Large Language Models

**Authors:** Edirlei Soares de Lima, Marco A. Casanova, Antonio L. Furtado

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15194v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15194v1)

**Summary:** When a direct proof of a statement $S$ seems hard or even impossible to obtain, there may exist another statement (or set of statements) $S^{*}$, somehow related to $S$, on the basis of which $S$ can be proved. In order to investigate what options can be used to move from $S$ to $S^{*}$, four kinds of semiotic relations inspired by the four master tropes of semiotic research are briefly reviewed. Specifically, our syntagmatic, paradigmatic, antithetic and meronymic relations correspond, respecti...

---

### 47. What Limits Us? Analyzing Self-Reported Limitations in NLP Research

**Authors:** Tawan Thaepprasit, Peeranuth Kehasukcharoen, Ding Wang, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15191v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15191v1)

**Summary:** Since late 2022, a Limitations section has become mandatory at many top-tier NLP conferences. The growing number of accepted papers at these venues has resulted in a vast corpus of self-reported limitations that cannot all be manually reviewed, yet remains systematically unanalyzed. Therefore, in this paper, we conduct a large-scale analysis of the Limitations sections from ACL and EMNLP papers published between 2020 and 2025 to understand what researchers disclose about their own work. To do so...

---

### 48. MUSE: A Theory-Harnessed Story Engine for Vibe Narrativizing

**Authors:** Jianxiang Ma, Xiaocui Yang, Daling Wang, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15188v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15188v1)

**Summary:** LLMs can generate fluent prose. Story quality depends on how decisions about plot, character, and language work together across planning, drafting, and revision. Guiding these decisions presents two bottlenecks: the quality of story guidance and its sustained use. We formulate Vibe Narrativizing as the task of turning natural-language writing requirements into a finished story and present MUSE, a Theory-Harnessed Story Engine. MUSE organizes story knowledge as guidance for specific decisions and...

---

### 49. CITECHOICE: A Causal Audit of How Document Presentation Redistributes Citation Credit in Agentic Search

**Authors:** Sriram Selvam, Anneswa Ghosh

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15164v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15164v1)

**Summary:** When several retrieved sources support the same claim, an answer engine cites some but not others. We call this decision citation allocation and introduce CITECHOICE, a causal audit of authentic multi-turn agentic search. From 129 everyday-query transcripts, CITECHOICE selects 113 same-call document pairs with independently verified support for the same pre-specified fact, without observing ranks or answer outcomes; blinded human review confirms 103. It runs a hash-verified 2-by-2 replay crossin...

---

### 50. EMR: Self-Evolving Medical Multi-Agent System via Experience Mining and Reuse

**Authors:** Dongsheng Shi, Yue Li, Xin Yi, et al.

**Published:** 2026-09-14

🔗 [Paper](http://arxiv.org/abs/2609.15161v1) | 📄 [PDF](https://arxiv.org/pdf/2609.15161v1)

**Summary:** Large language model (LLM) driven multi-agent systems have shown promise in complex clinical reasoning, yet existing approaches rely on static strategies and lack persistent clinical memory, preventing self-evolving from prior diagnostic successes and failures. We present EMR, a self-evolving medical multi-agent system via Experience Mining and Reuse. EMR introduces a hierarchical clinical experience library that organizes accumulated knowledge into three levels: clinical principles, diagnostic ...

---

