# DRL_portfolio_optimisation

# Code Summary

- **Libraries**:  
  Pandas, NumPy, Gym, PyTorch, CVXPY, Matplotlib, Optuna, TensorBoard

- **Data Preprocessing**:  
  - Loads CSV data with stock, bond, macro, and technical indicators  
  - Cleans missing/infinite values  
  - Splits data into training and testing sets  
  - Computes daily stock returns and a covariance matrix

- **Environment (PortfolioEnv)**:  
  - Uses state data from the CSV  
  - Action space represents portfolio weights for stocks  
  - Step function calculates percentage returns, portfolio return, volatility (via covariance matrix), a Sharpe-like reward, and cumulative portfolio value

- **PPO Agent**:  
  - Uses Multi-Head Attention for state feature projection  
  - Actor network outputs Gaussian policy parameters (mean, log_std) for sampling actions  
  - Critic network estimates state values  
  - Optimized with Adam and learning rate schedulers; loss includes PPO surrogate, critic, entropy, and L2 regularization

- **Hyperparameter Optimization (Optuna)**:  
  - Objective function runs a few episodes and returns negative average reward  
  - Finds best values for hidden_dim, lr, eps_clip, gamma, entropy_weight, num_heads, and output_dim_base

- **Training & Evaluation**:  
  - Trains the PPO agent in the custom environment with checkpointing and TensorBoard logging  
  - Evaluates a combined strategy mixing PPO weights with MVO weights (using a mixing parameter, alpha)  
  - Computes performance metrics: ROI, Sharpe Ratio, Sortino Ratio, Maximum Drawdown, Calmar Ratio

- **Benchmark Portfolios**:  
  - Equal Weight Portfolio: assigns equal weights to all stocks  
  - Minimum Variance Portfolio: solves for lowest variance weights using CVXPY  
  - Compares these benchmarks with the PPO-MVO combined strategy via plots
