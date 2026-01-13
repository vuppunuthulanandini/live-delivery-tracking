# backend/eta.py
def estimate_eta(lat, lon):
    """
    Dummy ETA function.
    You can later replace this with real distance-based ETA calculation.
    """
    import random
    return random.uniform(2, 15)  # returns ETA between 2 and 15 minutes
