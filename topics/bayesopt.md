# Bayesian Optimization

#### Problem statement

We are interested in solving
\begin{align}
    x^* = arg \min_{x \in \mathcal{X}} f(x)
\end{align}
under the constraints that
- $f$ is a black box for which no closed form is known (nor its gradients)
- $f$ is expensive to evaluate
- evaluations of $f$ are noisy

#### Bayesian optimization loop
For $t=1 \ldots T$:
1. Given observations $\{x_i, y_i=f(x_i)\}$ for $i=1 \ldots t$, build a probabilistic surrogate model $p_f(x)$ that predicts the distribution of evaluations of $f$.
2. Formulate a utility/acquisition function $u(x)$ that specifies a trade-off between exploration (to reduce uncertainty in the predictions of $p_f$) and exploitation (to find the minimum of $p_f$). 
    Find the minimizer of $a(x)$:
    \begin{align}
    x_{t+1} = arg \min_{x \in \mathcal{X}} u(x)
    \end{align}
3. Evaluate $y_{t+1} = f(x_{t+1})$.

#### Modalities
* **Multiple objectives**: 
    When $f$ is vector-valued, i.e. there are multiple outputs that we care to minimize, there is generally no single optimal point.
    Here the acquisition function needs to guide the search towards exploring the Pareto front of the best possible compromises.
* **Batched / delayed evaluations**
    Due to the experimental settings, evaluations of $f$ may need to be done in batch, or there may be delays until the results of the previous evaluations are known.


* [Comparison of frameworks](bayesopt_frameworks.ipynb)
* Surrogate models
* Single objective acquisition functions
* Multi-objective acquisition functions
