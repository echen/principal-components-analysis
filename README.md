# How to use
Calling `pca(x)` performs principal component on `x`, a matrix with observations in the rows. It returns the projection matrix (the eigenvectors of x^T x, ordered with largest eigenvectors first) and the eigenvalues (ordered from largest to smallest).

# Algorithm Description

## A simpler eigenvector calculation
Suppose we want to perform PCA on an $m \times n$ observation matrix $A$, where each row is an observation and each column is a dimension of the observation. For example, in the context of [eigenfaces](http://en.wikipedia.org/wiki/Eigenface), each row may be an image and each column a pixel.

Let's suppose we have already normalized the columns of $A$ to have zero mean, so that to find the PCA of $A$, we need to compute the eigenvectors of the $n \times n$ covariance matrix $A^T A$.

It's often the case that $n >> m$ (i.e., we have many more dimensions than datapoints), so finding the eigenvectors of the large $n \times n$ matrix $A^T A$ is computationally difficult. How can we make this problem more tractable?

It turns out that the eigenvectors of $A^T A$ have a simple relationship with the eigenvectors of $A A^T$, so we can solve the simpler problem of finding the eigenvectors of the smaller $m \times m$ matrix $A A^T$ instead. More precisely, **if $v$ is an eigenvector of $A A^T$, then $A^Tv$ is an eigenvector of $A^T A$ with the same eigenvalue**.

## Proof
Here's a proof of the above fact. Let $v$ be an eigenvector of $A A^T$ with eigenvalue $\lambda$. Then

$(A A^T) v = \lambda v$

$A^T(A A^T v) = A^T(\lambda v)$

$(A^T A)(A^T v) = \lambda (A^T v)$

so $A^Tv$ is an eigenvector of $A^T A$, with eigenvalue $\lambda$. Thus, instead of finding the eigenvectors of $A^T A$ directly, we can instead find the eigenvectors of $A A^T$ and multiply these on the left by $A^T$.