# Aguas de Vichy: ERT Modelling and Inversion

This repository contains code and data for an ERT (Electrical Resistivity Tomography) modelling and inversion project. The goal is to create a subsurface image that shows the aquifer and the hot water infiltration into that aquifer at Aguas de Vichy, a hot spring located in San Andrés, Santander, Colombia.

## Table of Contents

- [Abstract](#abstract)
- [Forward Modelling](#forward-modelling)
- [Data Collection and Processing](#data-collection-and-processing)
- [Inversion](#inversion)
- [Results and Discussion](#results-and-discussion)
- [Conclusion and Future Work](#conclusion-and-future-work)
- [References](#references)

## Abstract

- The Aguas de Vichy thermal spring (SAN-001), located near San Andres, Santander, has geothermal potential with known temperature, stored heat, and geochemistry. The spring's thermal waters are sodium-chloride type with notable salt concentrations. The region has significant faulting and folding trends.

- A fault near the spring site marks the contact between Paleozoic and Cretaceous sedimentary units. The Colombian Geological Survey suggests that the spring's water, salinized and heated by deep infiltration, rises due to temperature differences. Using techniques like ERT and VES, the geothermal fluid's distribution and mechanisms can be studied. 

- These findings will enhance understanding of the geothermal system and encourage geothermal energy exploration in Santander.

## Forward Modelling

The forward modelling process involves simulating electrical resistivity tomography (ERT) data based on the given subsurface geometry and resistivity distribution. This process enables the generation of synthetic data that can be compared with actual measurements.

![image](https://github.com/jcmefra/Aguas_Vichy/assets/64992303/1450be8a-9fb3-4f1c-90d4-6bfde5633dab)

### The key steps in the forward modelling process are as follows:

1. **Geometry Definition:** The subsurface geometry was defined using a combination of layers representing different rock formations, faults, and plume structures. The geometry was constructed to mimic the geological features present near the hot spring location.

2. **Measuring Scheme:** A Schlumberger measuring scheme with 96 electrodes was created along a 700-meter line. Electrode positions were carefully distributed to ensure sufficient mesh refinement and accuracy. The measuring scheme defined how measurements would be taken across the subsurface.

3. **Mesh Generation:** A mesh was generated based on the defined geometry and electrode positions. The mesh quality was controlled to ensure accurate numerical results. Nodes were added to enforce mesh refinement and improve accuracy.

4. **Fluid simulation:**: An inyected diffusive fluid was simulated for the complex model, it has an injection point (fault) and also values of concentration. There are 2 possible behaviors to model the diffusing fluid: Isotropic and anisotropic.

5. **Resistivity Distribution:** Different resistivity values were assigned to various regions within the mesh. These values represented different rock formations and plume structures present in the subsurface. The resistivity values were used to simulate the conductivity variations in the forward modelling process.

6. **Fluid Resistivity Definition:** The fluid resistivity was defined as a linear function of the concentration, see the notebook for more details. 

7. **Simulation:** Using the defined geometry, measuring scheme, and resistivity distribution, synthetic ERT data was generated. The forward simulation process considered factors such as geometric factors and noise levels. The resulting data container contained apparent resistivity values, geometric factors, and estimated data errors.

8. **Data Filtering:** To ensure the quality of the synthetic data, negative data values resulting from noise were removed from the data container. Filtering ensured that only physically meaningful data points were used for further analysis.

The forward modelling process allowed the generation of synthetic ERT data that closely resembled real-world measurements. This synthetic data serves as a foundation for subsequent inversion processes, where the goal is to reconstruct the subsurface resistivity distribution based on the measured data.

**NOTE**: You can find the forward modelling base code in **"Modelling_complex.ipynb"** notebook, we are using **Modelling_scenarios.py** to try different posible geological scenarios and define what acquisition will we do. You can run the script on a PyGimli environment (see https://www.pygimli.org for more information).

## Data Collection and Processing

I will describe how I collected and processed the ERT data. I will mention the equipment, the survey design, the data quality control, and the software tools that I used.

## Inversion

In this section, I will explain how I performed the ERT inversion to reconstruct subsurface properties from the collected data. I will mention the inverse problem, regularization techniques, parameter selection, and optimization methods used in the inversion process.

## Results and Discussion

I will present and discuss the results of my ERT modelling and inversion. I will use figures, tables, and graphs to illustrate my findings. I will also compare my results with previous studies or other methods.

## Conclusion and Future Work

I will summarize my main findings, conclusions, and contributions of the project. I will also suggest some limitations, challenges, and directions for future work.

## References

I will list the references that I cited in my README.md file using any citation style that I prefer.
