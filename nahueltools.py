

# Suavizado gaussiano para graficar
def gaussian_smoothing(X, Y, sigma = None, sigma_ratio = 0.1, bins = 100):
    X, Y = np.array(X), np.array(Y)
    X_out = np.linspace(np.min(X), np.max(X), bins)
    sigma = sigma_ratio*(X_out[-1]-X_out[0]) if sigma is None else sigma
    dist_matrix = X_out - X.reshape(-1, 1)
    dist_matrix = np.exp( - dist_matrix**2 / (2*sigma**2))
    Y_smoothed = Y @ dist_matrix / np.sum(dist_matrix, axis=0)
    return X_out, Y_smoothed