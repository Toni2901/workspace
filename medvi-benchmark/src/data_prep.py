from datasets import load_dataset

def load_medical_dataset():
    """
    Loads the African Medical Records dataset
    and stores it inside the project folder
    """

    dataset = load_dataset(
        "Nigeria-Health-data-OCR-pipeline/African-Medical-Records",
        cache_dir="data/raw"   # saves inside your project
    )

    return dataset


if __name__ == "__main__":
    dataset = load_medical_dataset()

    print(dataset)
    print(dataset['train'][0])