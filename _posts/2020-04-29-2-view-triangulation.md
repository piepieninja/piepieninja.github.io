---
layout: blogpost
title:  "Two View Triangulation of 3D Skew Lines"
date:   2020-04-29 1:16:01 -0600
categories:
---

<h2>Two View Triangulation of 3D Skew Lines</h2>

---

Assume that we have parametric lines $$L_0$$ and $$L_1$$, the challenge is to find the points $$s_0$$ and $$s_1$$ of
closest approach. First, we must test the assumption that our lines are skew, meaining they
are not parallel and do not intersect. To frame this, we take the forms of $$L_0$$ and $$L_1$$
and simplify them by thinking of them as parametic vectors where $$C_0$$ and $$C_1$$, represent the camera
position vectors and $$v_0$$ and $$v_1$$ represent the vector was previously calculated from the subtraction
of match coordinates with the camera vector. We make the simple equations:

$$
L_0 = v_0 t_0 + C_0 \hspace{1cm} L_1 = v_1 t_1 + C_1
$$

To make sure that the lines are not parallel, which is unlikely, we must verify that their cross product
is not zero. if $$v_0 \times v_1 = 0$$ then we have a degenerate case with infinitely many solutions. As long
as we know this is not the case we can proceed. We know that the cross product of the two vectors
$$c = v_0 \times v_1$$ is perpendicular to the lines $$L_0$$ and $$L_1$$. We know that the plane $$P$$, formed by the
translation of $$L1$$ along $$c$$, contains $$C_1$$. We also know
that the point $$C_1$$ is perpendicular to the vector $$n_0 = v_1 \times (v_0 \times v_1)$$. Thus, the intersection
of $$L_0$$ with $$P$$ is also the point, $$s_0$$, that is nearest to $$L_1$$, given by the equation:

$$
  s_0 = C_0 + \frac{(C_1 - C_0) \cdot n_0}{v_0 \cdot n_0} \cdot v_0
$$

This also holds for the second line $$L_1$$, the point $$s_1$$, and vector $$n_1 = v_0 \times (v_1 \times v_0)$$.
with the equation:

$$
  s_1 = C_1 + \frac{(C_0 - C_1) \cdot n_1}{v_1 \cdot n_1} \cdot v_1
$$

Now, given to points that represent the closest points of approach, we simply find the midpoint $$m$$:

$$
  m = \begin{bmatrix}
    (s_0[x] + s_1[x])/2\\
    (s_0[y] + s_1[y])/2\\
    (s_0[z] + s_1[z])/2
  \end{bmatrix}
$$



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
