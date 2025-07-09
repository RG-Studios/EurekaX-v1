# 🚀 EurekaX v1.0 – Autonomous Cross-Domain Discovery Engine

_EurekaX v1_ is a lightweight but powerful algorithm that generates scientific hypotheses by combining knowledge from distinct fields such as AI, Aerospace, Neuroscience, and Quantum Computing.

It uses simple NLP techniques (TF-IDF + cosine similarity) to calculate **novelty**, simulates **feasibility**, and outputs classified insights into a growing memory database.

---

## 🎯 What It Does

- 🔁 Combines random topics from 2 different scientific domains
- 💡 Forms a hypothesis like:  
  _“Can we use ‘X’ from AI to solve ‘Y’ in Quantum Computing?”_
- 📈 Scores novelty using **cosine similarity of TF-IDF vectors**
- 🧪 Simulates feasibility (randomized placeholder)
- 🧠 Calculates a final insight score and gives a **verdict**
- 💾 Stores top hypotheses in a memory file (`eurekax_memory.json`)

---

## 🧠 Sample Output

```text
✅ PROMISING (0.63) → Can we use 'language models for text generation' from AI to solve 'aerodynamic flow modeling' in Aerospace?
❌ Rejected (0.41) – Not novel or feasible enough
✅ BREAKTHROUGH (0.75) → Can we use 'qubit entanglement and decoherence' from Quantum Computing to solve 'synaptic plasticity for adaptation' in Neuroscience?
