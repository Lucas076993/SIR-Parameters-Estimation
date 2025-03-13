# SIR epidemic model parameters estimation

This project was created to try to estimate the parameters of the SIR epidemic model. Actually under work.

## People in this project
Professor: Dr. Marina Ribeiro Barros Dias (Universidade Federal Fluminense - UFF - Brazil)

Student: Lucas da Silva Paiva (Undergraduate Student) (Universidade Federal Fluminense - UFF - Brazil)

## Theory and Fundamentals

The idea behind the techniques applied in this project came from the works of Dr. François G. Schmitt, in his work "An algorithm for the direct estimation of the parameters of the SIR epidemic model from the I(t) dynamics", published in the European Physical Journal Plus. We studied the theory presented in the article, and created a code in Python using Pandas, Scipy and Scikit-learn to estimate the parameters. The main objective of this project is to apply the techniques in data from Brazil.

## Related works and articles
- Dias, M. R. B. and Paiva, L. S., "Estimativa de Parâmetros do Modelo SIR baseada na
dinâmica da população infectada", submitted.

### Patch notes
- 1.0.0: The estimation of the parameters using brazilian data was made. There was some problems with the estimation of french data, mainly because of inconsistencies in the data obtained. For future work, we will try to ajust the data from France to compare to Brazil or obtain new datasets. The code is not so well organized, so we will try to optimize and organize it in future patches.