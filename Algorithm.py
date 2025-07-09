# eurekax/algorithm.py

import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from memory import save_to_memory

# Sample mini knowledge base
knowledge_base = {
    "AI": [
        "reinforcement learning for decision making",
        "neural networks for image recognition",
        "language models for text generation"
    ],
    "Aerospace": [
        "satellite attitude control systems",
        "aerodynamic flow modeling",
        "multi-stage rocket propulsion"
    ],
    "Neuroscience": [
        "neuron firing patterns and learning",
        "synaptic plasticity for adaptation",
        "brain-inspired spiking networks"
    ],
    "Quantum Computing": [
        "qubit entanglement and decoherence",
        "quantum tunneling algorithms",
        "superposition-based optimization"
    ]
}

# 1. Extract vectorized topic embeddings
def extract_vectors(domain_texts):
    vectorizer = TfidfVectorizer(stop_words='english')
    docs = [text for domain in domain_texts.values() for text in domain]
    vectors = vectorizer.fit_transform(docs)
    return vectorizer, vectors, docs

# 2. Calculate novelty (low cosine similarity = novel)
def calculate_novelty(h1, h2, vectorizer):
    vectors = vectorizer.transform([h1, h2])
    score = 1 - cosine_similarity(vectors[0], vectors[1])[0][0]
    return score

# 3. Combine domains and generate hypothesis
def generate_insight():
    d1, d2 = random.sample(list(knowledge_base.keys()), 2)
    t1 = random.choice(knowledge_base[d1])
    t2 = random.choice(knowledge_base[d2])
    hypothesis = f"Can we use '{t1}' from {d1} to solve '{t2}' in {d2}?"
    return d1, d2, hypothesis, t1, t2

# 4. Score feasibility with fake simulator
def simulate_feasibility(t1, t2):
    return round(random.uniform(0.3, 0.9), 2)  # placeholder score

# 5. Main Algorithm Loop
def run_discovery(k=5, novelty_threshold=0.6):
    vectorizer, _, _ = extract_vectors(knowledge_base)
    found = 0
    while found < k:
        d1, d2, hypothesis, t1, t2 = generate_insight()
        novelty = calculate_novelty(t1, t2, vectorizer)
        feasibility = simulate_feasibility(t1, t2)
        score = novelty * feasibility

        if score >= novelty_threshold:
            verdict = "Breakthrough" if score > 0.7 else "Promising"
            save_to_memory(hypothesis,
                           f"[FOR] This is plausible due to similarity in {d1} and {d2}",
                           f"[AGAINST] May fail due to domain incompatibility",
                           verdict)
            print(f"✅ {verdict.upper()} ({score:.2f}) → {hypothesis}")
            found += 1
        else:
            print(f"❌ Rejected ({score:.2f}) – Not novel or feasible enough")

