clc, clear, close all;

t = 0:0.01:10;          % Time vector
dt = 0.01;              % Time step
fs = 1/dt;              % Sampling frequency

% Time domain signal
Ft = sin(80*t) + sin(100*t);

% Time Domain Plot
figure
plot(t, Ft, 'LineWidth', 1.5)
grid on
title('Time Domain: F(t) = 2 sin(2t)')
xlabel('Time (sec)')
ylabel('F(t) (N)')


% Frequency Domain using FFT
N = length(Ft);             
FFT_vals = fft(Ft);         
FFT_mag = abs(FFT_vals)/N;  

f = (0:N-1)*(fs/N)         % Frequency in Hz
omega = 2*pi*f;             % Convert to rad/sec

% Take only positive frequencies
half = 1:floor(N/2);
omega_half = omega(half);
FFT_half = FFT_mag(half);

figure
stem(omega_half, FFT_half, 'filled')
xlim([0 10])
grid on
title('Frequency Domain')
xlabel('Angular Frequency (rad/sec)')
ylabel('Amplitude')