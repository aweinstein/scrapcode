clear all
%close all
clc

%load data
%N = size(pts,1);

%%
dataset = 2;

if dataset == 1,
    N = 150;
    phis = rand(N,1) * 2 * pi;
    R = 1 + 0.1*randn(N,1);
    pts = [R.*cos(phis) R.*sin(phis)];
    rp = randperm(N);
elseif dataset ==2,
    load annulus_clump
    pts = points;
    N = size(pts, 1);
    load i_samples
    rp = i_samples' + 1;
end
    


%% Take random samples
n_samples = 50;

i_a = rp(1:n_samples);
i_b = rp(n_samples+1:end);
pts_a = pts(i_a, :);
pts_b = pts(i_b, :);
A = zeros(n_samples, n_samples);
B = zeros(n_samples, N - n_samples);
sigma = 0.5;
for i = 1:n_samples,
    for j = 1:n_samples,
        if i <= j,
            A(i,j) = exp(-norm(pts_a(i,:) - pts_a(j,:))^2 / (2*sigma^2));
            A(j,i) = A(i,j);
        end
    end
end

for i = 1:n_samples,
    for j = 1: N - n_samples,
        B(i,j) = exp(-norm(pts_a(i,:) - pts_b(j,:))^2 / (2*sigma^2));
    end
end

W = zeros(N, N);
for i = 1:N,
    for j = 1:N,
        if i <= j,
            W(i,j) = exp(-norm(pts(rp(i),:) - pts(rp(j),:))^2 / (2*sigma^2));
            W(j,i) = W(i,j);
        end
    end
end


%%
E = nystrom(A, B);
 
D = diag(sum(W,1));
Dsi = sqrtm(inv(D));
Wn = Dsi * W * Dsi;
[Uw, Sw, Vw] = svd(Wn);
 
if norm(Uw(:,2) - E(:,1)) > norm(Uw(:,2) + E(:,1)),
    E(:,1) = -E(:,1);
end
norm(E(:,1) - Uw(:,2))

figure(1), clf
plot(Uw(:,2))
hold on
plot(E(:,1),'r')