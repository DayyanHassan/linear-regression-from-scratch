# Linear Regression From Scratch

## Overview

This project implements **Linear Regression completely from scratch**
using only **NumPy**. No machine learning libraries such as
Scikit-learn, TensorFlow, or PyTorch were used.

The objective of this project was not only to train a linear regression
model, but also to understand every mathematical and programming concept
behind it.

This project was built as part of my self-study journey through
Stanford's **CS229: Machine Learning** course.

------------------------------------------------------------------------

# Features

-   Implemented Linear Regression from first principles
-   Matrix-based implementation using NumPy
-   Forward Pass
-   Mean Squared Error (MSE) Cost Function
-   Gradient Computation
-   Gradient Descent Optimization
-   Weight and Bias Updates
-   Prediction on unseen data

------------------------------------------------------------------------

# Mathematical Model

The model predicts using:

`ŷ = Xw + b`

where:

-   **X** = Input feature matrix
-   **w** = Weight vector
-   **b** = Bias
-   **ŷ** = Predicted output

The objective is to minimize the Mean Squared Error:

`J = (1 / 2m) * Σ(ŷ - y)^2`

Parameters are updated using Gradient Descent:

`w = w - α * ∂J/∂w`

`b = b - α * ∂J/∂b`

------------------------------------------------------------------------

# Dataset

  Study Hours     Exam Score
  ------------- ------------
  1                        2
  2                        4
  3                        6
  4                        8
  5                       10

------------------------------------------------------------------------

# Results

**Training Results**

-   Initial Cost: **22.0**
-   Final Cost: **0.0008198617528571869**
-   Learned Weight: **1.97375488**
-   Learned Bias: **0.0947532153**

**Prediction**

Input:

``` text
Study Hours = 6
```

Output:

``` text
Predicted Score = 11.93728249
```

Expected Score:

``` text
12
```

The model successfully converges very close to the optimal solution.

------------------------------------------------------------------------

# Project Structure

``` text
linear-regression-from-scratch/
│
├── main.py
├── README.md
└── requirements.txt
```

------------------------------------------------------------------------

# Requirements

``` text
numpy
```

Install dependencies:

``` bash
pip install numpy
```

------------------------------------------------------------------------

# Running the Project

``` bash
python main.py
```

------------------------------------------------------------------------

# Learning Objectives

Through this project I gained a practical understanding of:

-   Matrix Multiplication
-   NumPy Arrays
-   Matrix Shapes
-   Broadcasting
-   Linear Regression
-   Cost Functions
-   Mean Squared Error
-   Gradient Descent
-   Weight Updates
-   Bias Updates
-   Machine Learning from First Principles

------------------------------------------------------------------------

# Future Improvements

-   Multiple Linear Regression
-   Logistic Regression
-   Neural Networks
-   Computer Vision
-   Real-world datasets
-   Regularization
-   Visualization of the cost function

------------------------------------------------------------------------

## Author

**Dayyan Hassan**

This repository is part of my self-study journey in Artificial
Intelligence and Computer Vision while following Stanford's CS229
Machine Learning curriculum.
