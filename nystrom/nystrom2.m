clear all
clc

load data
% What if A = W?
A = W;
B = [];

n = size(A, 1);
m = size(B, 2);

d1 = sum([A;B'], 1);
%d2 = sum(B,1) + sum(B',1) * pinv(A) * B;
d2 = [];
dhat = sqrt(1 ./ [d1 d2])';
A = A .* (dhat(1:n) * dhat(1:n)');
% B = B .* (dhat(1:n) * dhat(n + (1:m))');
Asi = sqrtm(pinv(A));
% Q = A + Asi * (B * B') * Asi;
Q = A;
[U, L, T] = svd(Q);
V = [A; B'] * Asi * U * pinv(sqrt(L));
nvec = 2;
for i = 2:nvec+1,
    E(:,i-1) = V(:,i) ./ V(:,1);
end

Wn = diag(dhat) * W * diag(dhat);
[Uw, Lw, Tw] = svd(Wn);
