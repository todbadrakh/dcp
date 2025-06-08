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

### Scaling on 1-16 Ryzen Cores
```! opt freq wb97x-d3 def2-tzvp cpcm(water)```

calculations were scaled from 1-16 Ryzen cores on my home PC to determine the optimal
number of MPI threads. The 16-core calculation used the `--oversubscribe` flag.
Below are timing data in seconds:

| Cores | Total | Startup | SCF | Integrals | SCF_Response | Properties | Gradient | Relax |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1330.390 | 7.037 | 395.357 | 205.315 | 80.578 | 364.523 | 277.551 | 0.028 |
| 2 | 893.907 | 8.350 | 241.852 | 118.206 | 77.460 | 293.731 | 154.279 | 0.029 |
| 4 | 602.663 | 7.938 | 142.488 | 63.524 | 52.047 | 243.069 | 93.544 | 0.053 |
| 8 | 558.574 | 20.068 | 261.110 | 58.512 | 34.472 | 101.446 | 82.934 | 0.033 |

---

### Workflow

1. Optimize geometry of pyridinium.
2. Use the Docker module to generate 10 lowest-energy conformers at the XTB-GFN level.
3. Use `separate-xyz.py` to generate separate xyz files.
4. Use `optimize-conformers.py` to optimize geometries and compute frequencies at the `wB97X-D3/def2-TZVP` level.

---

## Minimum Energy Geometries

**Pyridine(H₂O)** optimized geometries were obtained from the conformer search described above.

*(Insert figure here: e.g., optimized geometries visualization)*

---

## pKa of Pyridinium

The deprotonation Gibbs free energy was computed using the **direct method** [17]:

## References

1. Neese, F. *Software update: The ORCA program system, version 5.0*. **WIRES Comput. Mol. Sci.** 2022, **12**(1), e1606. [https://doi.org/10.1002/wcms.1606](https://doi.org/10.1002/wcms.1606)  
2. Neese, F.; Wennmohs, F.; Hanse, A.; Becker, U. *Efficient, approximate and parallel Hartree-Fock and hybrid DFT calculations. A ‘chain-of-spheres’ algorithm for the Hartree-Fock exchange*. **Chem. Phys.** 2009, **356**(1–3), 98–109. [https://doi.org/10.1016/j.chemphys.2008.10.036](https://doi.org/10.1016/j.chemphys.2008.10.036)  
3. Bykov, D.; Petrekno, T.; Izsak, R.; Kossmann, S.; Becker, U.; Valeev, E.; Neese, F. *Efficient implementation of the analytic second derivatives of Hartree-Fock and hybrid DFT energies: a detailed analysis of different approximations*. **Mol. Phys.** 2015, **113**, 1961–1977. [https://doi.org/10.1080/00268976.2015.1025114](https://doi.org/10.1080/00268976.2015.1025114)  
4. Garcia-Rates, M.; Neese, F. *Efficient implementation of the analytical second derivatives of Hartree-Fock and hybrid DFT energies within the framework of the conductor-like polarizable continuum model*. **J. Comput. Chem.** 2019, **40**, 1816–1828. [https://doi.org/10.1002/jcc.25833](https://doi.org/10.1002/jcc.25833)  
5. Bannwarth, C.; Caldeweyher, E.; Ehlert, S.; Hansen, A.; Pracht, P.; Seibert, J.; Spicher, S.; Grimme, S. *Extended tight-binding quantum chemistry methods*. **WIRES Comput. Mol. Sci.** 2020, **11**(2), e1493. [https://doi.org/10.1002/wcms.1493](https://doi.org/10.1002/wcms.1493)  
6. Garcia-Rates, M.; Neese, F. *Effect of the solute cavity on the solvation energy and its derivatives within the framework of the Gaussian charge scheme*. **J. Comput. Chem.** 2020, **41**, 922–939. [https://doi.org/10.1002/jcc.26139](https://doi.org/10.1002/jcc.26139)  
7. Helmich-Paris, B.; de Souza, B.; Neese, F.; Izsák, R. *An improved chain of spheres for exchange algorithm*. **J. Chem. Phys.** 2021, **155**, 104109. [https://doi.org/10.1063/5.0058766](https://doi.org/10.1063/5.0058766)  
8. Neese, F. *The SHARK integral generation and digestion system*. **J. Comput. Chem.** 2022, 1–16. [https://doi.org/10.1002/jcc.26942](https://doi.org/10.1002/jcc.26942)  
9. Grimme, S.; Antony, J.; Ehrlich, S.; Krieg, H. *A consistent and accurate ab initio parametrization of density functional dispersion correction (DFT-D) for the 94 elements H–Pu*. **J. Chem. Phys.** 2010, **132**, 154104. [https://doi.org/10.1063/1.3382344](https://doi.org/10.1063/1.3382344)  
10. Shami, T. M.; El-Saleh, A. A.; Alswatitti, M.; Al-Tashi, Q.; Summakieh, M. A.; Mirjalili, S. *Particle swarm optimization: A comprehensive survey*. **IEEE Access** 2022, **10**, 10031–10061. [https://doi.org/10.1109/ACCESS.2022.3142859](https://doi.org/10.1109/ACCESS.2022.3142859)  
11. Wang, J. *Predicting pKa values of para-substituted aniline radical cations vs. stable anilinium ions in aqueous media*. **Molecules** 2024, **29**(19), 4522. [https://doi.org/10.3390/molecules29194522](https://doi.org/10.3390/molecules29194522)  
12. Serjeant, E. P. *IUPAC Chemical Data Series: Ionisation Constants of Organic Acids in Aqueous Solution*. Pergamon Press, Oxford, 1979.
