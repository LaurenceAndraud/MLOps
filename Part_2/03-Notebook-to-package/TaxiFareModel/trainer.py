class Trainer:
    def __init__(self, model, data, **kwargs):
        self.model = model
        self.data = data
        self.kwargs = kwargs
        self.pipeline = None
        
    def set_pipeline(self, pipeline):
        self.pipeline = pipeline
        
    def run(self):
        self.pipeline.fit(self.data["X_train"], self.data["y_train"])
        
    def evaluate(self):
        return self.pipeline.score(self.data["X_test"], self.data["y_test"])