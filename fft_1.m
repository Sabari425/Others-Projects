clc, clear, close all;

x = [1 1 1 1 0 0 0 0]
N = 8;
X = fft(x, N)
X_mag = abs(X)
n = 0:N-1; k = 0:N-1;

% (i) Plot k vs |X(k)|
figure
stem(k, X_mag, 'filled')
grid on
title('k vs. |X(k)|')
xlabel('k')
ylabel('|X(k)|')

% (ii) Plot n vs x(n)
figure
stem(n, x, 'filled')
grid on
title('n vs. x(n)')
xlabel('n')
ylabel('x(n)')