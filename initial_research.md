# Initial work and code:

- As the first step, we have written a toy logistic regression classifier to have a tiny taste of how does numpy work, gradient descent implemented. Code is in the logistic_regression.py

- For the svm, we will still implement it in Python, mainly because the Numpy package in Python has strong matrix manipulation capacity.    

- We have written starting code to solve the dual optimization problem using QP solver cvxopt, which is a python package for convex optimization problem. We defined three classes, train, test and kernel. Code is in the initial_code.py 

- Next step, we will try to understand how to solve the optimization problem directly, coding stochastic gradient descent on the primal and SMO on the dual prolbem.


# Codes implemented by others:

- Efficient training of Support Vector Machines in Java, use SMO
https://github.com/maling6154/jlibsvm.git

- svm in javascript, use SMO to sovle QP problem
https://github.com/karpathy/svmjs

- svm light, use Stochastic gradient descent on the primal
http://svmlight.joachims.org/



# Papers and Documents

- Pegasos: Primal Estimated sub-GrAdient SOlver for SVM            
This paper is about how to sub-Gradient descent on the primal problem            
http://ttic.uchicago.edu/~shai/papers/ShalevSiSr07.pdf

- Training a Support Vector Machine in the Primal         
This paper introduces an algorithm to solve the primal optimization problem.         

- THE IMPLEMENTATION OF SUPPORT VECTOR MACHINES USING THE SEQUENTIAL MINIMAL OPTIMIZATION ALGORITHM      
This paper talks about SMO algorithm on the dual optimization problem.   

- Fast Training of Support Vector Machines using Sequential Minimal Optimization      
This paper also introduces that how to solve dual using SMO.    

- Training Linear SVMs in Linear Time        
This paper shows a way to do linear SVM in O(sn) time, where n is training examples and
s is the average number of every non-zero features in every training observation.      

- Libsvm-guide: A Practical Guide to Support Vector Classification           
Guide from Libsvm, which is by far the best implementation of svm           
http://www.csie.ntu.edu.tw/~cjlin/papers/guide/guide.pdf

- Libsvm-documents: A Library for Support Vector Machines           
Documents of Libsvm, covers the method which is implemented in Libsvm to solve the dual problem           
http://www.csie.ntu.edu.tw/~cjlin/papers/libsvm.pdf

- NG CS229 lecture notes and notes from other colleges               
This notes gives an overview of svm        

- Time Complexity Analysis of Support Vector Machines (SVM) in LibSVM     
