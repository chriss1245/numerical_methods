from numpy import pi, exp

def fft(signal):
    """
    This function applies the fast fourier transform to a signal
    """
    N = len(signal)
    if N == 1:
        return signal
    else:
        even = fft(signal[::2])
        odd = fft(signal[1::2])
        T = [exp(-2j * pi * k / N) * odd[k] for k in range(N // 2)]
        return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]
        
