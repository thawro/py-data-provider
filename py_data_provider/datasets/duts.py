from py_data_provider.data_providers.duts import DUTSDataProvider
from py_data_provider.datasets.base import BaseSegmentationDataset
from typing import Literal


class DUTSSegmentationDataset(BaseSegmentationDataset):
    def __init__(
        self,
        root: str,
        split: Literal["train", "test"],
        labels_format: Literal["yolo"] = "yolo",
    ):
        data_provider = DUTSDataProvider(root, binarize=True, labels_format=labels_format)
        super().__init__(root, split, data_provider)


if __name__ == "__main__":
    from py_data_provider.utils.config import ROOT

    root = str(ROOT / "data" / "DUTS")
    ds = DUTSSegmentationDataset(root, "train")
    ds = DUTSSegmentationDataset(root, "test")
