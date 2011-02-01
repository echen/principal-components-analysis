from numpy import *

def pca(x):
	"""Performs principal component on x, a matrix with observations in the rows.
	Returns the projection matrix (the eigenvectors of x^T x, ordered with largest eigenvectors first) and the eigenvalues (ordered from largest to smallest).
	"""
	
	x = (x - x.mean(axis = 0)) # Subtract the mean of column i from column i, in order to center the matrix.
	
	num_observations, num_dimensions = x.shape
	
	# Often, we have a large number of dimensions (say, 10,000) but a relatively small number of observations (say, 75). In this case, instead of directly computing the eigenvectors of x^T x (a 10,000 x 10,000 matrix), it's more efficient to compute the eigenvectors of x x^T and translate these into the eigenvectors of x^T x by using the transpose trick. 
	# The transpose trick says that if v is an eigenvector of M^T M, then Mv is an eigenvector of MM^T.
	# We arbitrarily select "100" as the switching threshold. Another approach is to switch by comparing num_observations and num_dimensions.
	if num_dimensions > 100:
		eigenvalues, eigenvectors = linalg.eigh(dot(x, x.T))
		v = (dot(x.T, eigenvectors).T)[::-1] # Unscaled, but the relative order is still correct.
		s = sqrt(eigenvalues)[::-1] # Unscaled, but the relative order is still correct.
	else:
		u, s, v = linalg.svd(x, full_matrices = False)
		
	return v, s