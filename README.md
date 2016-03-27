# CPE593 Project , by Xiao Wang and Ling Ma**

## Project name: Support vector machine implementation in Java

## Project scope:

- Create a support vector machine classifier for binary classification problem. Input: a dataset (x1, y1), ..., (xn, yn), where xi is an input vector and yi ∈ {-1, +1} is a binary label corresponding to it. Output: A SVM classifier.

- Implement four basic methods for this SVM classifier, including svm.train, svm.fit, svm.prob, svm.predict

- Explore different algorithms to solve the underlying quadratic programming(unconstrained non-smooth convex problem) behind SVM, study converge speed and complexity, including:         
1) Gradient descent, with modification
2) Newton's method
3) Stochastic gradient descent
4) Sequential minimal optimization, if possible, this is implemented in the popular LibSvm library       

- Implement different kernel option for the classifier, including:      
1) Linear kernel
2) RBF kernel
3) Poly kernel (degree = k)      

- Analyze the overall complexity.

- Implement the classifier on several benchmark datasets and analyze the performance compared with Java library.
