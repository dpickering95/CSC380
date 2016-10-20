class Song:
    """ A song in Spot represents the current state of the HMM """

    def __init__(self, features):
        self.features = features

    def getFeature(self, feat):
        return (self.features[feat])

