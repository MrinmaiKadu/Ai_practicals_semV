factorial(0, 1).
factorial(N, F) :- N > 0, N1 is N - 1, factorial(N1, F1), F is N * F1.
% To calculate the factorial of 5, in the terminal you can query factorial(5, F).
