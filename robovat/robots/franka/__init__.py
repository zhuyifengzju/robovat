from .franka_panda_sim import FrankaPandaSim

def factory(simulator=None, config=None):
    if simulator is None:
        raise NotImplementedError
    else:
        return FrankaPandaSim(simulator=simulator, config=config)
