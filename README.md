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

![image](https://github.com/jcmefra/Aguas_Vichy/assets/64992303/36b2c119-a508-41fc-81d7-857a33b5ed95)

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

Forward modeling was employed to establish potential distribution of the resistivity and chargeability anomalies based on the initial hypothesis, subsequently, three Electrical Resistivity Tomography (ERT) transects around the fault map trace were conducted. Two of them were complemented by induced polarization (IP) method.

## Inversion

The inversion process has been done using PyGimli for Schlumberger array and Res2Dinv for mixed (robust) array. PyGimli robust inversion is yet to be available after data conversion. Data analysis has been conducted to identify outliers and remove disperse values.

## Results and Discussion

Two of the ERT transects traverse the fault and revealed resistivity values ranging from near zero to over 1500 ohm.m, with a similar distribution pattern. Low resistivity areas, possibly indicating accumulation of groundwater and geothermal saline fluids, were more pronounced adjacent to the inferred fault trace and at the profile's boundaries. High resistivity anomalies appear at 5 meters depth, defining a possible lower boundary of the quaternary aquifer, and are likely indicative of consolidated or impermeable materials. The third ERT, which was located within the aquifer but doesn’t intersect the fault, showed higher baseline resistivities suggesting a reduced presence of geothermal fluids. IP findings are in alignment with ERT results, where low chargeability suggests the presence of groundwater and geothermal saline fluids.

**NOTE**: The results are not in this repository, they will be published once the citable paper is available.

## Conclusion and Future Work

The inverted sections support the presence of a geothermal system dominated by fluid circulation, which may correlate to faults and fractures ; however, the studied fault trace did not show the expected anomaly for a main geothermal fluid path. We suggest that the following studies improve the geological and structural uncertaintity and contemplate other alternatives such as lateral (advective) fluid flow as the main geothermal water source for the thermal springs. The results obtained reveal a potential energy resource which requires further understanding and encourages continued research into geothermal energy within the Santander department. 

## References

Alfaro Valero, C.M. and Ortiz Martín, I.D. (2010) Inventario nacional de manantiales termales fase 2010, departamento de Boyaca, Santander y Norte de Santander, Servicio Geológico Colombiano. Bogotá, Colombia: Instituto Colombiano de Geología y Minería (INGEOMINAS).

Alfaro, C. M., Rueda Gutiérrez, J. B., Casallas Y. P., Rodríguez G. Z., y Malo J. E. (2020). Estimación Preliminar del Potencial Geotérmico de Colombia. Bogotá: Servicio Geológico Colombiano.

Arnason, K., Karlsdottir, R., Eysteinsson, H., Flóvenz, Ó. G., \& Gudlaugsson, S. T. (2000, May). The resistivity structure of high-temperature geothermal systems in Iceland. In Proceedings of the World Geothermal Congress 2000, Kyushu-Tohoku, Japan (pp. 923-928).

Bona, P., \& Coviello, M. (2016). Valoración y gobernanza de los proyectos geotérmicos en América del Sur: una propuesta metodológica.

Bu, X., Ma, W., \& Li, H. (2012). Geothermal energy production utilizing abandoned oil and gas wells. Renewable energy, 41, 80-85.

Chabaane, A., Redhaounia, B., \& Gabtni, H. (2017). Combined application of vertical electrical sounding and 2D electrical resistivity imaging for geothermal groundwater characterization: Hammam Sayala hot spring case study (NW Tunisia). Journal of African Earth Sciences, 134, 292-298.

Chandrasekharam, D., \& Bundschuh, J. (2008). Low-enthalpy geothermal resources for power generation. CRC press.

Dentith, M., \& Mudge, S. T. (2014). Geophysics for the mineral exploration geoscientist. Cambridge University Press.

Dickson, M. H., \& Fanelli, M. (2013). Geothermal energy: utilization and technology.

González-Idárraga, C. E. (2020). Caracterización resistiva 3D del área geotérmica de Paipa, Colombia. Boletín de Geología, 42(3), 81-97.

Hunt, T. M., Bromley, C. J., Risk, G. F., Sherburn, S., \& Soengkono, S. (2009). Geophysical investigations of the Wairakei Field. Geothermics, 38(1), 85-97.

International Geothermal Association (IGA). (2014). Best Practices Guide for Geothermal Exploration. IGA Service GmbH, Bochum Germany.

Kana, J. D., Djongyang, N., Raïdandi, D., Nouck, P. N., \& Dadjé, A. (2015). A review of geophysical methods for geothermal exploration. Renewable and Sustainable Energy Reviews, 44, 87-95.

Márquez, I. D., Puyo, D. M., Robledo, M. L., \& Valderrama, S. S. (2021). Transición energética: un legado para el presente y el futuro de Colombia. Bogotá DC, Colombia.

Morales, E., Veroslavsky, G., Manganelli, A., Marmisolle, J., Pedro, A., Samaniego, L., Plenc, F., Umpiérrez, R., Ferreiro, M., \& Morales, M. (2021). Potential of geothermal energy in the onshore sedimentary basins of Uruguay. Geothermics, 95, 102165.

Okoroafor, E. R., Smith, C. M., Ochie, K. I., Nwosu, C. J., Gudmundsdottir, H., \& Aljubran, M. J. (2022). Machine learning in subsurface geothermal energy: Two decades in review. Geothermics, 102, 102401.

Ovalle, J. A. (2020). Geotermia en la región central. Convenio Interadministrativo 080 de 2019. Región Administrativa y de Planeación Especial RAP-E - Universidad Distrital Francisco José de Caldas.

Pardo, O. H., \& Eraso, G. C. A. (2011). Caracterización geofísica integrada de las aguas termales de la hostería Balneario El Batán, municipio de Cuitiva, Boyacá, Colombia. Geología Colombiana, 36, 57-72.

Pesce, A., \& Miranda, F. (2003). Catálogo de manifestaciones termales de la República Argentina. Vol. I-II Región Noroeste. SEGEMAR, Buenos Aires, 1666-3462.

Romo-Jones, J. M., Arango-Galván, C., Ruiz-Aguilar, D., Avilés-Esquivel, T., \& Salas-Corrales, J. L. (2021, August). 3D electrical resistivity distribution in Los Humeros and Acoculco geothermal zones, Mexico. In First EAGE Workshop on Geothermal Energy in Latin America (Vol. 2021, No. 1, pp. 1-5). EAGE Publications BV.

Spichak, V., \& Manzella, A. (2009). Electromagnetic sounding of geothermal zones. Journal of Applied Geophysics, 68(4), 459-478.

Tian, B., Lei, X., Jiang, H., Xu, C., \& Song, M. (2022). Multi-Method Geophysical Mapping of a Geothermal Reservoir and Buried Channel in Langfang, Northern Part of China. Journal of Environmental and Engineering Geophysics, 27(1), 1-11.

Zohdy, A. A., Eaton, G. P., \& Mabey, D. R. (1974). Application of surface geophysics to ground-water investigations.
