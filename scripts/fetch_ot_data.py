#!/usr/bin/env python
from open_targets.adapter.context import AcquisitionContext

def main():
    ctx = AcquisitionContext()
    for dataset in ctx.datasets:
        print(f"Downloading {dataset.name}")
        ctx._acquire_dataset(dataset)
    print("✅ Done fetching all OpenTargets files.")

if __name__ == "__main__":
    main()
