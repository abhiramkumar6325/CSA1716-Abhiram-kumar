% Base case: Sum of integers from 1 to 1 is 1.
sum_integers(1, 1).

% Recursive rule: To find the sum of integers from 1 to N,
% we recursively compute the sum of integers from 1 to N-1
% and add N to it.

sum_integers(N, Sum) :-
    N > 1,			 % Ensure N is greater than 1
    Prev is N - 1,               % Compute N-1
    sum_integers(Prev, PrevSum), % Recursively compute sum of integers from 1 to N-1
    Sum is PrevSum + N.          % Calculate sum

% Example query: sum_integers(5, Result).
% This will give Result = 15.
