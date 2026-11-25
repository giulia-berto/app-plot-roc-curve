<h1 align="center">ROC curve (deprecated)</h1>

<p align="center">
  Plot ROC-AUC curve for multi-LAP and multi-NN. Warning: this app can be run ONLY after the app https://doi.org/10.25663/brainlife.app.174. This App was used specifically for a Replicability Study and has been deprecated.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.180"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.180-blue.svg" alt="Run on brainlife.io"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Plot ROC-AUC curve for multi-LAP and multi-NN. Warning: this app can be run ONLY after the app https://doi.org/10.25663/brainlife.app.174. This App was used specifically for a Replicability Study and has been deprecated.**

Deprecated App used for a replicability study. Collects per-subject CSV files with false/true positive rates and AUC for multi-LAP and multi-NN tract segmentation (from brainlife.app.174), interpolates and averages the ROC curves across subjects, and plots the mean ROC-AUC curves for one tract. It only works on the output of that specific App.

| | |
|---|---|
| **Inputs** | `neuro/tractmeasures` |
| **Outputs** | `generic/images` |
| **Container** | `brainlife/dipy:0.16.0` |
| **Resources** | 4 CPUs · 0.17 h walltime |
| **Run it** | [doi.org/10.25663/brainlife.app.180](https://doi.org/10.25663/brainlife.app.180) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `0` | `neuro/tractmeasures` | yes | csv file reporting fdr, tdr and AUC for multi-LAP and multi-NN |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `1` | `generic/images` | PNG plot of the mean ROC curves and AUCs for multi-LAP and multi-NN for the tract. |

<!-- brainlife-app:end -->

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.180](https://doi.org/10.25663/brainlife.app.180), choose `neuro/tractmeasures` from your project and press **Execute**. The results are saved to your project as `generic/images`.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/) (the App runs in `brainlife/dipy:0.16.0`), [`jq`](https://jqlang.github.io/jq/).

1. Clone this repository.
2. Create `config.json` with the paths to your inputs and the parameters:

   ```json
   {
       "measures": "/path/to/0/measures"
   }
   ```

3. Run `./main`.

## Troubleshooting

- **Computation failed.**: No image was produced; check that the inputs are the CSV outputs of brainlife.app.174.

## Citing

If you use this App, please cite it, the software it builds on and brainlife.io:

- ROC curve (deprecated). brainlife.io App. [doi:10.25663/brainlife.app.180](https://doi.org/10.25663/brainlife.app.180)
- Garyfallidis et al. Dipy, a library for the analysis of diffusion MRI data. *Frontiers in Neuroinformatics* 8 (2014). [doi:10.3389/fninf.2014.00008](https://doi.org/10.3389/fninf.2014.00008)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

- Giulia Bertò

## Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io, which runs this App, is publicly funded by Wellcome, the U.S. National Institutes of Health and the U.S. National Science Foundation; acknowledging that support helps keep it running.</sub>
