% Check point 3.3
clear all
clc
load data

W_hat = [A; B'] * inv(A) * [A B];

Asi = sqrtm(inv(A));
S = A + Asi * (B*B') * Asi;
[Us, Ls, Ts] = svd(S);
V = [A; B'] * Asi * Us * sqrtm(inv(Ls));
W_hatp = V * Ls * V';

norm(W_hat - W_hatp)
V' * V

