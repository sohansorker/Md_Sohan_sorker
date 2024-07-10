# Exercise Badges

![](https://byob.yarr.is/apudasm10/made-template-fau/score_ex1) ![](https://byob.yarr.is/apudasm10/made-template-fau/score_ex2) ![](https://byob.yarr.is/apudasm10/made-template-fau/score_ex3) ![](https://byob.yarr.is/apudasm10/made-template-fau/score_ex4) ![](https://byob.yarr.is/apudasm10/made-template-fau/score_ex5)

# Examining the evolving trends and connection between road accidents and the average temperature in Germany.

The link between environmental conditions and road safety has consistently drawn attention. In this report, I explore how the average temperature in Germany from 2018 to 2020 correlates with the number of accidents on motorways inside and outside built-up areas. Uncovering this relationship can offer crucial information for creating measures to improve road safety and lessen the effects of harsh weather.


## Question

1.The changes of the temparature?
2.How the rate of road accident increasing day by day?
3.Is there any realtion between road accident and the temparature?
## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Federal Statistical Office of Germany

Metadata URL: https://www.destatis.de/

Data URL: https://www-genesis.destatis.de/genesis/online?language=en&sequenz=statistikTabellen&selectionname=46241#abreadcrumb

Data Type: CSV

Description: The road accident data in Germany. This data also shows that the accident in Indoor and outdoor as well.

License Type: OpenData License

### Datasource2: climate_environment/CDC

Metadata URL: https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/

Data URL: https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_01.txt https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_02.txt https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_03.txt https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_04.txt https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_05.txt https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_06.txt https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_07.txt https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_08.txt https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_09.txt https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_10.txt https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_11.txt https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_12.txt

Data Type: txt

License Type: OpenData License

Description: This is monthly average air temparature in Germany. In this dataset it also shows that the temparature in state wise.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Dataset selection
2. Building an Automated Data Pipelines
3. Automated Testing
4. Continuous Integration
5. Feature Engineering and Analysis
6. Reporting on findings
7. Presentation




## Project Work
Your data engineering project will run alongside lectures during the semester. We will ask you to regularly submit project work as milestones so you can reasonably pace your work. All project work submissions **must** be placed in the `project` folder.

### Exporting a Jupyter Notebook
Jupyter Notebooks can be exported using `nbconvert` (`pip install nbconvert`). For example, to export the example notebook to html: `jupyter nbconvert --to html examples/final-report-example.ipynb --embed-images --output final-report.html`


## Exercises
During the semester you will need to complete exercises using [Jayvee](https://github.com/jvalue/jayvee). You **must** place your submission in the `exercises` folder in your repository and name them according to their number from one to five: `exercise<number from 1-5>.jv`.

In regular intervalls, exercises will be given as homework to complete during the semester. Details and deadlines will be discussed in the lecture, also see the [course schedule](https://made.uni1.de/). At the end of the semester, you will therefore have the following files in your repository:

1. `./exercises/exercise1.jv`
2. `./exercises/exercise2.jv`
3. `./exercises/exercise3.jv`
4. `./exercises/exercise4.jv`
5. `./exercises/exercise5.jv`

### Exercise Feedback
We provide automated exercise feedback using a GitHub action (that is defined in `.github/workflows/exercise-feedback.yml`). 

To view your exercise feedback, navigate to Actions -> Exercise Feedback in your repository.

The exercise feedback is executed whenever you make a change in files in the `exercise` folder and push your local changes to the repository on GitHub. To see the feedback, open the latest GitHub Action run, open the `exercise-feedback` job and `Exercise Feedback` step. You should see command line output that contains output like this:

```sh
Found exercises/exercise1.jv, executing model...
Found output file airports.sqlite, grading...
Grading Exercise 1
	Overall points 17 of 17
	---
	By category:
		Shape: 4 of 4
		Types: 13 of 13
```
