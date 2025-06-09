---
title: "Quantum Chemical Characterization of Dicyanopyridine Covalent Organic Frameworks"
author: "Tuguldur T. Odbadrakh and James G. Gaugler"
institute: "National Center for Computational Sciences, Oak Ridge National Laboratory.\nDepartment of Chemistry, University of Tennessee - Knoxville"
layout: default
---

# Theoretical Methods

The pKa of pyridine is calculated at the &omega;B97X-D3/def2-TZVP level of theory
using various levels of explicit solvation. Utility scripts are available at:
[github.com/todbadrakh/orca-tools](https://github.com/todbadrakh/orca-tools)

### Scaling on 1-16 AMD Ryzen Cores
```! opt freq wb97x-d3 def2-tzvp cpcm(water)```

calculations were scaled from 1-16 Ryzen cores on my home PC to determine the optimal
number of MPI threads. The 8- and 16-core calculations used the `--oversubscribe` flag.
Below are timing data in seconds:

| Cores | Total | Startup | SCF | Integrals | SCF_Response | Properties | Gradient | Relax |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1330.390 | 7.037 | 395.357 | 205.315 | 80.578 | 364.523 | 277.551 | 0.028 |
| 2 | 893.907 | 8.350 | 241.852 | 118.206 | 77.460 | 293.731 | 154.279 | 0.029 |
| 4 | 602.663 | 7.938 | 142.488 | 63.524 | 52.047 | 243.069 | 93.544 | 0.053 |
| 8 | 273.224 | 5.678 | 71.567 | 28.211 | 23.406 | 95.248 | 49.097 | 0.016 |
| 16.000 | 314.222 | 12.140 | 90.561 | 33.360 | 36.812 | 86.277 | 55.057 | 0.015 |

### Scaling on 1-128 AMD Epyc Cores

| nproc | Total | Startup | SCF | Integrals | SCF_Response | Properties | Gradient | Relax |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.000 | 39.326 |  |  |  |  |  |  |  |
| 2.000 | 519.989 | 3.297 | 64.776 | 83.844 | 56.143 | 286.403 | 25.520 | 0.006 |
| 4.000 | 267.878 | 2.994 | 34.456 | 42.989 | 30.244 | 143.650 | 13.504 | 0.040 |
| 8.000 | 147.617 | 2.817 | 20.473 | 23.803 | 18.956 | 74.068 | 7.493 | 0.007 |
| 16.000 | 90.550 | 3.383 | 14.550 | 14.644 | 12.945 | 40.362 | 4.660 | 0.006 |
| 32.000 | 64.689 | 3.680 | 11.902 | 10.327 | 11.020 | 24.204 | 3.549 | 0.006 |
| 64.000 | 57.692 | 4.715 | 12.333 | 9.667 | 11.991 | 15.803 | 3.177 | 0.006 |
| 128.000 | 98.103 | 8.270 | 20.010 | 13.730 | 34.766 | 16.577 | 4.745 | 0.006 |

---

### Workflow

1. Optimize geometry of pyridinium.
2. Use the Docker module to generate 10 lowest-energy conformers at the XTB-GFN level.
3. Use `separate-xyz.py` to generate separate xyz files.
4. Use `optimize-conformers.py` to optimize geometries and compute frequencies at the `wB97X-D3/def2-TZVP` level.

---

## Minimum Energy Geometries

### Pyridinium(H<sub>2</sub>O)<sup>+</sup>

![**Figure 1.** Pyridinium(H<sub>2</sub>O)<sup>+</sup> geometries obtained at he wB97X-D3/def2-TZVP level of theory with
CPCM(water) implicit solvation.](images/pyrh-h2o-geometries.png)

**Table 1.** Raw thermodynamic values of minimum energies structures shown in Figure 1 in atomic units. 

| Conformer             | E(electronic)     | ZPE        | Thermal Energy | Entropy Corr | G(final)      |
|-------------------|-------------------|------------|----------------|--------------|---------------|
| a | -325.221695666054 | 0.12703143 | -325.08656022  | -0.04140956  | -325.12702557 |
| b | -325.2145921139   | 0.12640482 | -325.0801985   | -0.04174028  | -325.12099457 |
| c | -325.21303805692  | 0.12625954 | -325.08044245  | -0.03841841  | -325.11791665 |
| d | -325.21365973663  | 0.12695728 | -325.07806879  | -0.04318941  | -325.12031399 |

---

## pKa of Pyridinium

The deprotonation Gibbs free energy was computed using the **direct method** [17]:

## References
[References](./refs.html)
