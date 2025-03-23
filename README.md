# Code Summary

- **Data Input & Preparation**  
  - Load CSV data with stocks, bonds, macro indicators, and technical indicators  
  - Clean data (handle missing/infinite values) and split into training and testing sets  
  - Compute daily returns for stocks and a covariance matrix for volatility estimation

- **Custom Environment (PortfolioEnv)**  
  - Uses the cleaned state data  
  - **Action Space:** Portfolio weights for stocks  
  - **Step Function:**  
    - Computes percentage returns from today to tomorrow  
    - Calculates portfolio return as a weighted sum of asset returns  
    - Computes portfolio volatility using the covariance matrix  
    - Generates a reward based on a Sharpe-like ratio (return minus volatility penalty)  
    - Tracks the cumulative portfolio value

- **DRL Model Architecture (PPO Agent)**  
  - **Multi-Head Attention:** Projects the state features into multiple heads  
  - **Actor Network:**  
    - Outputs parameters (mean and log_std) for a Gaussian distribution  
    - Samples continuous actions (portfolio weights) using the tanh function  
  - **Critic Network:**  
    - Estimates the state value (for advantage calculation)  
  - **Optimization:**  
    - Uses Adam optimizers with learning rate schedulers  
    - Loss includes PPO surrogate loss, critic loss, entropy regularization, and L2 penalty

- **Hyperparameter Optimization with Optuna**  
  - Objective function runs a few episodes and returns negative average reward  
  - Searches for best values for: hidden_dim, lr, eps_clip, gamma, entropy_weight, num_heads, output_dim_base

- **Alpha and Combined Strategy**  
  - **Alpha Parameter:**  
    - Blends PPO-generated portfolio weights with Mean-Variance Optimization (MVO) weights  
    - Combined weights = (1 - alpha) * PPO weights + alpha * MVO weights  
    - Alpha is swept (e.g., from 0 to 1) to find the best mix

- **Evaluation & Benchmarks**  
  - Evaluate performance metrics (ROI, Sharpe Ratio, Sortino Ratio, Maximum Drawdown, Calmar Ratio)  
  - Compare the combined PPO-MVO strategy with:  
    - Equal Weight Portfolio (same weight for every stock)  
    - Minimum Variance Portfolio (solved using CVXPY)
