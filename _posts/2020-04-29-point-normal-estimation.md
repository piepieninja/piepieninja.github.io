---
layout: blogpost
title:  "Estimation of Point Normals in Point Clouds"
date:   2020-04-29 1:20:01 -0600
categories:
---

<h2>Estimation of Point Normals in Point Clouds</h2>

---

The estimation of point normals is vital for accurate 3D meshing of point clouds, as normals give additional information on curvature and enable smoother non-linear mesh interpolation. Thus, a critical step in the computer vision pipeline of the MOCI satellite is to estimate point normals. Though point cloud meshing is not currently implemented int the MOCI computer vision software, it should be considered reasonable future work.

Aside from the point cloud coordinates, the only information needed in the point normal calculation is the camera position $$(C_x, C_y, C_z)$$ which generated each point. The final result will be the same list of input point coordinates along with the computed normal vector of each point. The problem of determining the normal to a point on the surface is approximated by estimating the tangent plane of the point, and then taking the normal vector to the plane. However, there are two valid normals for estimated tangent plane but only one is suitable for reconstruction. The correct orientation of the normal vector cannot be directly inferred, so an additional subroutine is needed to choose the correct normal vector.

Let a given point cloud be referenced as $$PC = { p_1 , p_2 , p_3 , ... , p_n }$$ where a given point is $$p_i = (x_i , y_i , z_i)$$ and for each point $$p_i \in PC$$ we seek to find the correct normal vector $$n_i = (n_x, n_y, n_z)$$. Also note that each point has an associated camera of the form $$C_i = (C_x, C_y, C_z)$$.

First, the $$k$$ nearest neighbors of point $$p_i$$ must be retrieved, let these points be defined as $$Q_{i,k} = { q_1 , q_2, q_3, ... q_k  } $$ where any neighbor $$q_i \in PC$$. Then a centroid of the subset $$Q_{i,k}$$ is calculated with the following equation:

$$
\begin{equation}
  m = \frac{1}{k} \sum_{q \in Q} q
\end{equation}
$$

Next we seek to produce an approximation of a plane by calculating two vectors $$v_1$$ and $$v_2$$ from the given subset of $$k$$ points. First, let $$A$$ be a k x 3 matrix built from the centroid being subtracted from each point in the nearest neighbor subset. To find the desired vectors we must perform a singular value decomposition (SVD), seen in the equation below, and notice that the covariance matrix $$A^T A$$ can be diagonalized so that the eigenvectors of the covariance matrix are the columns of vector V (or the rows of vector $$V^T$$).

$$
\begin{equation}
  \begin{split}
    A &= U \Sigma V^T \\
    A^T A &= ( U \Sigma^T U^T ) ( U \Sigma V^T ) = V ( \Sigma^T \Sigma ) V^T
  \end{split}
\end{equation}
$$

 In general, the best r-rank approximation of an (n x n) matrix, $$r < n$$, is found by diagonalizing the matrix as above, only keeping the first r columns of V (similarly only the first r rows of $$V^T$$), and only the first r diagonal elements of $$ \Sigma^T \Sigma $$ (or only first r rows and columns), assuming that the values on the diagonal of $$\Sigma$$ were in descending order. More precisely, for randomly ordered diagonal elements $$ (\sigma_i)^2 \in \Sigma^T \Sigma  $$ we keep only the maximum r many of them, along with their corresponding eigenvectors in matrix V. The reason for choosing the maximum valued eigenvalues is that it minimizes the amount of information lost in moving to a lower rank approximation matrix. Therefore, to produce the best approximation of a plane in $$\mathbb{R}^{3}$$ we would take the two eigenvectors, $$v_1$$ and $$v_2$$, of the covariance matrix (which are exactly the columns of V), with the highest corresponding eigenvalues. Those two eigenvectors span the plane we are looking for. Thus, the normal vector $$n_i$$ is simply the cross product of these eigenvectors: $$n_i = v_1 \times v_2$$.

 The reason for introducing the SVD is because in computing the covariance matrix $$A^TA$$ we may lose some level of precision in the calculation. By simply factoring matrix A into its singular value decomposition and taking the cross product of the first two rows of $$V^T$$, we can avoid this problem.

As previously mentioned, there are two viable normals that could be computed with this method, but only one normal is the desired normal. To solve this issue we could simply compute the vector from the camera position $$C$$ to point $$p_i$$ such that $$(C - p_i) \cdot n_i < 0$$ holds. If this does not hold then the vector can be flipped by changing the signs of its components. However, because there are likely to be many camera locations, say $$C = { C_{i,1} , C_{i,2} , C_{i,3}, ... , C_{i,N} }$$ for all $$N$$ cameras of a given point $$p_i$$, a point's normal can be considered ambiguous if the following is true:


 &nbsp; &#8226; There exists a $$\bar{C_1} \in C$$ such that $$(\bar{C_1} - p_i) \cdot n_i < 0$$

 &nbsp; &#8226; There exists a $$\bar{C_1} \in C$$ such that $$(\bar{C_1} - p_i) \cdot n_i > 0$$


Such points cannot easily be oriented and thus additional computation is needed; fortunately, in most cases there are very few such normals. When these normals are discovered they are added to a queue of unfinished normals while the rest are placed in a list of correct normals. The algorithm iterates through the queue of ambiguous normals and tries to determine the orientation by looking at the neighboring points of $$p_i$$. If the neighboring points of $$p_i$$ have already finished normals, then $$n_i$$ is oriented such that it is consistent with the neighboring normals $$m_i$$ by setting $$n_i \cdot m_i > 0$$ . If the neighboring points do not have already finished normals, then we move $$p_i$$ to the back of the queue, and continue until all normals are finalized.





<br><br><br><br><br><br><br><br><br><br>
<small>This is copied from a section of my thesis. If you found this useful to your research please consider using the following bibtex:</small>

<p class="bibtex">
  @mastersthesis{CalebAdamsMSThesis, <br>
    &nbsp; author={Caleb Ashmore Adams}, <br>
    &nbsp; title={High Performance Computation with Small Satellites and Small Satellite Swarms for 3D Reconstruction}, <br>
    &nbsp; school={The University of Georgia}, <br>
    &nbsp; url={http://piepieninja.github.io/research-papers/thesis.pdf},<br>
    &nbsp; year=2020, <br>
    &nbsp; month=may <br>
  }
</p>

<br><br><br><br>
