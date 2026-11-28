from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    train_file:str 
    test_file:str