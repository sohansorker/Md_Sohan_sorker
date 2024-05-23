import pandas as pd
from sqlalchemy import create_engine

class Pipeline:
    def __init__(self):
        self.engine = create_engine('sqlite:///data//FinalDB.sqlite')

    def download_temperature_data(self):
        # Define the list of URLs
        url_list = [
            "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_01.txt",
            "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_02.txt",
            "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_03.txt",
            "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_04.txt",
            "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_05.txt",
            "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_06.txt",
            "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_07.txt",
            "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_08.txt",
            "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_09.txt",
            "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_10.txt",
            "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_11.txt",
            "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_12.txt",  
        ]

        # Initialize an empty list to store the DataFrames
        dataframes = []

        # Loop through each URL and read data into a DataFrame
        for url in url_list:
            # Use pd.read_csv to read data from the URL
            df = pd.read_csv(url, sep=';', skiprows=1, skipfooter=0)
            dataframes.append(df)


        # Concatenate the list of DataFrames into a single DataFrame
        complete_df = pd.concat(dataframes, ignore_index=True)

        # Filter the combined DataFrame
        df_filtered = complete_df[(complete_df['Jahr'] >= 2018) & (complete_df['Jahr'] <= 2020)]
        refined_df = df_filtered.sort_values(by=['Jahr', 'Monat'])


        # Store the temperature data in the database
        refined_df.to_sql('AvgTemp', self.engine, if_exists='replace', index=False)

    def collect_additional_data(self):
        # collect additional data from another URL
        url2 = "https://www-genesis.destatis.de/genesisWS/rest/2020/data/tablefile?username=DE9WS28QIO&password=Sohanhasan@123&name=46241-0006&area=all&compress=false&transpose=false&startyear=2018&endyear=2020&language=en"
        data1 = pd.read_csv(url2, sep=';', skiprows=6, skipfooter=3, engine='python')
        df = data1
        df_transposed = df.T

        # Store the additional data in the same database
        df_transposed.to_sql('AccData', self.engine, if_exists='replace', index=False)
        self.engine.dispose()
        

    def run_pipeline(self):
        # Run the entire pipeline
        self.download_temperature_data()
        self.collect_additional_data()

# Create an instance of the Pipeline class
pipeline_instance = Pipeline()

# Run the pipeline
pipeline_instance.run_pipeline()