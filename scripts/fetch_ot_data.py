#!/usr/bin/env python
# scripts/fetch_ot_data.py

from open_targets.adapter.context import AcquisitionContext
from open_targets.definition import (
    node_targets,
    node_diseases,
    node_molecule,
    node_gene_ontology,
    node_mouse_phenotype,
    node_mouse_target,
    edge_target_disease,
    edge_target_go,
)

def main():
    # mirror exactly what open_targets_biocypher_run.py uses:
    node_definitions = [
        node_targets,
        node_diseases,
        node_molecule,
        node_gene_ontology,
        node_mouse_phenotype,
        node_mouse_target,
    ]
    edge_definitions = [
        edge_target_disease,
        edge_target_go,
    ]
    ctx = AcquisitionContext(
        node_definitions=node_definitions,
        edge_definitions=edge_definitions,
        datasets_location="data/ot_files",
    )

    # download each dataset once
    for ds in ctx.datasets:
        print(f"▶ Downloading {ds.id}")
        ctx._acquire_dataset(ds)

    print("✅ All OpenTargets data fetched to data/ot_files/")

if __name__ == "__main__":
    main()
