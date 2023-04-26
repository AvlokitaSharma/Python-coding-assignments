#!/usr/bin/env python
# coding: utf-8

# # CECS 229: Coding Assignment #2
# 
# #### Due Date: 
# 
# Sunday, 2/20 @ 11:59 PM
# 
# #### Submission Instructions:
# 
# To receive credit for this assignment you must submit the following by the due date:
# 
# 1. **To the BB Dropbox Folder:** this completed .ipynb file
# 
# 2. **To CodePost:** this file converted to a Python script named `ca2.py`
# 
# #### Objectives:
# 
# 1. Use the Sieve of Eratosthenes to find all primes in a given range.
# 2. Design a computational algorithm for finding the Bézout coefficients of two integers.
# 3. Use Bézout coefficients to calculate the GCD.
# 

# -------------------------------------------------------
# #### Problem 1:
# 
# Create a function `primes(a, b)` that uses the Sieve of Eratosthenes to find all the primes $p$ satisfying $a \leq p \leq b$.  You may not use any built-in functions that perform entire or part of this algorithm.
# 
# 1. INPUT:
#   
#   * `a` - a positive integer greater than or equal to 1 (raise a `ValueError` if an integer less than 1 is given), that is the lower bound
#   * `b` - a positive integer greater than or equal to `a` (raise a `ValueError` if `b` < `a`)
#   
# 2. OUTPUT:
#     
#     * a set of all the primes $p$ satisfying `a` $\leq p \leq$ `b`
#     
# EXAMPLE:
# 
# `>> primes(1, 10)`
# 
# `{2, 3, 5, 7}`
# 
# `>> primes(50, 100)`
# 
# `{53, 59, 61, 67, 71, 73, 79, 83, 89, 97}`
# 
# Note: the order of the elements might be different in your output, and that is okay! As long as you have all the primes.

# In[1]:


def primes(a, b):
    # FIXME: Implement this function
    elements = []
    if 1 <= a < b:
        for i in range(a, b + 1):
            j = 0     #lets say j = 0
            for k in range(2, i):
                if i % k == 0:          #if i mod k will be equal to 0, then j will be 1
                    j = 1
            if j == 0:
                elements.append(i)
        print(elements)
    else:
        raise ValueError("a has to be greater than 1 or b has to be greater than a")


primes(2, 10)
pass


# ----------------------------------------------
# 
# #### Problem 2:
# 
# Create a function `bezout_coeffs(a, b)` that computes the Bezout coefficients `s` and `t` of `a` and `b`.
# 
# 1. INPUT: 
#     * `a`,`b` - distinct integers
# 
# 2. OUTPUT: `{a: s, b: t}` - dictionary where keys are the input integers and values are their corresponding Bezout coefficients.
# 
# EXAMPLE:  
#  
# `>> bezout_coeffs(414, 662)` 
# 
# `{414 : 8, 662 : -5}`
# 
# 

# #### HINT:
# 
# 
# To come up with an algorithm for the function `bezout_coeff(a,b)` consider the following example:
# 
# Suppose $a = 13,\;\; b = 21$.  We seek $s$ and $t$ such that gcd$(13, 21) = 13s + 21t$
# 
# Let's begin by defining $s_0 = 1, \;\; t_0 = 0, \;\; a_1 = 13,\;\; b_1 = 21$.  At every round in attempting to attain the gcd, we will refer to $s_i$ and $t_i$ as the current coefficients of 13 and 21.
# 
# 
# **Round 1:**
# 
# $21 = 1 \cdot 13 +8  $
# 
# $\hspace{2cm} \implies 8 = 21 - 1 \cdot 13$  We will call this EQN 1
# 
# $\hspace{2cm} \implies s_1 = - \; ( \; b_1 \textbf{ div } a_1 \; ) = -(21 \textbf{ div } 13) = -1 $
# 
# $\hspace{2cm} \implies t_1 = 1$
# 
# **Round 2:**
# 
# $a_2 = 8,\;\; b_2 = 13$
# 
# $13 = 1 \cdot 8 + 5 $
# 
# $\hspace{2cm} \implies 5 = 13 - 1 \cdot 8$
# 
# $\hspace{3.5cm} = 1 \cdot 13 - 1 (21 - 1 \cdot 13) $  from EQN 1
# 
# $\hspace{3.5cm} = 2 \cdot 13 - 1 \cdot 21 $
# 
# $\hspace{2cm} \implies s_2 = 2$
# 
# $\hspace{2cm} \implies t_2 = -1$
# 
# NOTICE:
# 
# $\hspace{2cm} s_2 = s_0 -  s_1\; (\; b_2\textbf{ div }a_2 ) $
# 
# $\hspace{2.5cm} = 1 -  1\; (\; 13\textbf{ div }8) $
# 
# $\hspace{2.5cm} = 1 -\;( -1)(1) $
# 
# $\hspace{2.5cm} = 2$
# 
# $\hspace{2cm} t_2 = t_0 - t_1\; (\; b_2\textbf{ div }a_2 )$
# 
# $\hspace{2.5cm} = 0 - 1\; (\; 13\textbf{ div }8 )$
# 
# $\hspace{2.5cm} = 0 - 1\; (1)$
# 
# $\hspace{2.5cm} = -1$
# 
# 
# **Round 3:**
# 
# $a_3 = 5,\;\; b_3 = 8$
# 
# $8 = 1 \cdot 5 + 3$
# 
# $\hspace{2cm} \implies 3 = 8 - \underbrace{1}_{b_3\textbf{ div }a_3} \cdot 5$
# 
# $\hspace{3.5cm} = 1 \cdot (\underbrace{1}_{t_1}  \cdot 21 \underbrace{-1}_{s_1}  \cdot 13) - \underbrace{1}_{b_3\textbf{ div }a_3} (\underbrace{2}_{s_2}  \cdot 13 \underbrace{-1}_{t_2}  \cdot 21 ) $
# 
# $\hspace{3.5cm} = - 3 \cdot 13 + 2 \cdot 21$
# 
# $\hspace{2cm} \implies s_3 = -3$
# 
# $\hspace{2cm} \implies t_3 = 2$
# 
# 
# NOTICE:
# 
# $\hspace{2cm} s_3 = s_1 -s_2 \; ( \; b_3\textbf{ div }a_3) $
# 
# $\hspace{2.5cm} = -1 -(2)(1) $
# 
# $\hspace{2.5cm} = -3$
# 
# $\hspace{2cm} t_3 = t_1 - t_2 \; ( \; b_3\textbf{ div }a_3)$
# 
# $\hspace{2.5cm} = 1 -(-1)(1) $
# 
# $\hspace{2.5cm} = 2$
# 
# $\vdots$
# 
# **Round $k$:**
# 
# For any round $k \geq 2$, the corresponding $s_k$ and $t_k$ values are given by
# 
# * $s_k = s_{k-2} - s_{k-1} \;(\; b_{k} \textbf{ div } a_{k})$
# 
# * $t_k = t_{k-2} - t_{k-1} \; (\; b_{k} \textbf{ div } a_{k})$
# 
# 
# 
# You should verify for yourself that for any $a, b$,
# * $s_0 = 1$
# * $t_0 = 0$
# * $s_1 = -(\; b \textbf{ div } a)$
# * $t_1 = 1$
# 
# 
# 

# In[3]:


def bezout_coeffs(a, b):
    # FIXME: Implement this function
    if a != b:
        if a < b:
            a, b = b, a
            r_1, r_2 = a, b
            s_1, s_2 = 0, 1
            t_1, t_2 = 1, 0
            while r_2 > 0:
                q, r = divmod(r_1, r_2)
                r_1, r_2 = r_2, r
                t_1, t_2 = t_2, t_1 - q * t_2
                s_1, s_2 = s_2, s_1 - q * s_2
            output = {b: s_1, a: t_1}
            return output


print(bezout_coeffs(414, 662))
pass


# ----------------------------------------------------------------------
# #### Problem 2:
# 
# Create a function `gcd(a, b)` that computes the greatest common divisor of `a` and `b` using the `bezout_coeff` function you implemented for problem 2 lecture.  No credit will be given to functions that employ any other implementation.  For example, using the built-in function `math.gcd()` as part of our implementation will not receive any credit.
# 
# 1. INPUT: 
#     * `a`,`b` - integers
# 
# 2. OUTPUT: `d` - the gcd
# 
# EXAMPLE:  
#  
# `>> gcd(414, 662)` 
# 
# `2`

# #### HINT
# 
# The GCD of any two numbers must be positive by definition.

# In[2]:


def gcd(a, b):
    # FIXME: Implement this function
    if a >= 0 and b >= 0:
        if a > b:
            bigger_number = a
            lesser_number = b
        else:
            bigger_number = b
            lesser_number = a
    for i in range(1, bigger_number + 1):
        if a % i == 0:
            if b % i == 0:
                g_c_d = i

    print(g_c_d)


gcd(414,662)
pass


# ------------------------------------
# #### Testing Your Functions
# 
# You can test your functions by running the cell below and verifying that your answers agree with the expected outcomes.

# In[4]:


""" TESTER CELL """
print("\nTesting primes(1, 10)\nResult:", primes(1, 10), "\nExpected: {2, 3, 5, 7}")
print("\nTesting primes(2, 37)\nResult:", primes(2, 37), "\nExpected: {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37}")
print("\nTesting primes(2, 100)\nResult:", primes(2, 100), "\nExpected: {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}")
print("\nTesting bezout_coeffs(414, 662)\nResult:", bezout_coeffs(414, 662), "\nExpected: {414: 8, 662: -5}")
print("\nTesting bezout_coeffs(26, 7)\nResult:", bezout_coeffs(26, 7), "\nExpected: {26: 3, 7: -11}")
print("\nTesting gcd(101, 4620)\nResult:", gcd(101, 4620), "\nExpected: 1")
print("\nTesting gcd(1011, 4620)\nResult:", gcd(1011, 4620), "\nExpected: 3")
print("\nTesting gcd(2349, 36)\nResult:", gcd(2349, 36), "\nExpected: 9")


# In[ ]:




