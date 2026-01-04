def calculate_dwb_score(all_scores):
    """
    Implements the Max() logic from the Spectrum-to-Signal paper.
    all_scores: a list of scores [s1, s2, s3... sk] for k attempts.
    """
    # We take the best attempt (Max-K)
    best_attempt = max(all_scores)
    
    # Optional: Penalty if the model is too inconsistent
    # score = best_attempt * (1 - variance(all_scores))
    
    return best_attempt