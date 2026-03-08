import os

# --- Hyperparameters of the Multiverse ---
K_LEVELS = 3  # Depth of hierarchy (0: Local, 1: Meta, 2: Meta-Meta, 3: Multiverse)
LAMBDA_0 = 1.0
ALPHA_DECAY = 0.5  # 0 < alpha < 1 for weight decay across levels

# --- Agent Configuration ---
NUM_AGENTS_TARGET = 1000000  # Goal: 1M agents
SPECIALIZATION_RATIOS = {
    "reasoning": 0.40,  # GRA-Heisenberg
    "creativity": 0.30, # Genie-like simulations
    "intuition": 0.20,  # Beauty score evaluators
    "meta": 0.10        # Meta-controller
}

# --- Thresholds ---
COHERENCE_THRESHOLD = 0.95  # If B(phi) < 0.95 -> Reset
FOAM_EPSILON = 1e-6         # Convergence criteria for Phi

# --- API Keys (Set via ENV) ---
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "your_key_here")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")

# --- Paths ---
DATA_DIR = "./data_multiverse"
LOG_DIR = "./logs"