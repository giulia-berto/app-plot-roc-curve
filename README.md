[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.180-blue.svg)](https://doi.org/10.25663/brainlife.app.180)

# app-plot-roc-curve
This App plots ROC-AUC curves for multi-LAP and multi-NN to compare the two streamline-based bundle segmentation methods. ROC-AUC analysis is a standard tool for test validation in the field of medical imaging segmentation which plots the sensitivity/specificity curve of the method under evaluation for different cut-off points. In our case, the cut-off points of the ROC curve are represented by the probability of each streamline to belong to the bundle of interest. Performances of multiple methods can be compared through the scalar value represented by the Area Under the Curve (AUC). Higher AUC values mean better segmentation.

### Authors
- Giulia Bertò (giulia.berto.4@gmail.com)

### Funding Acknowledgement
brainlife.io is publicly funded and for the sustainability of the project it is helpful to Acknowledge the use of the platform. We kindly ask that you acknowledge the funding below in your publications and code reusing this code.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)

### Citations
We kindly ask that you cite the following articles when publishing papers and code using this code. 

1. Avesani, P., McPherson, B., Hayashi, S. et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6, 69 (2019). [https://doi.org/10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Running the App 

### On Brainlife.io

You can submit this App online at [https://doi.org/10.25663/bl.app.174](https://doi.org/10.25663/bl.app.174) via the "Execute" tab. WARNING: this app can be run ONLY after the app https://doi.org/10.25663/brainlife.app.174. This App was used specifically for a Reproducibility Study and has been deprecated.

### Running Locally (on your machine)

1. git clone this repo.
2. Inside the cloned directory, create `config.json` with something like the following content with paths to your input files.

```json
{
        "csv": "./output_FiberStats.csv"
}
```

3. Launch the App by executing `main`

```bash
./main
```

### Output
The output file, which is a collection of images, will be generated under the current working directory (pwd). 

### Dependencies
This App only requires [singularity](https://www.sylabs.io/singularity/) to run. 

#### MIT Copyright (c) 2019 Giulia Bertò
