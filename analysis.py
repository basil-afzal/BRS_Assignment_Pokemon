from typing import Any, Optional
import matplotlib.pyplot as plt
import yaml
import requests


class Analysis():

    def __init__(self, analysis_config: str) -> None:
        CONFIG_PATHS = ['configs/system_config.yml', 'configs/user_config.yml']

        # add the analysis config to the list of paths to load
        paths = CONFIG_PATHS + [analysis_config]

        # initialize empty dictionary to hold the configuration
        config = {}

        # load each config file and update the config dictionary
        for path in paths:
            with open(path, 'r') as f:
                this_config = yaml.safe_load(f)
            config.update(this_config)

        self.config = config

        self.pokemon_api_user_config = self.config.get('pokemon_api_user_config', {})
        self.default_pokemon_id = self.pokemon_api_user_config.get('pokemon_id', 25)

        self.pokemon_api_base_url = self.config.get('pokemon_api_base_url')

    def load_data(self) -> None:
        endpoint = f"{self.pokemon_api_base_url}pokemon/{self.default_pokemon_id}/"
        data = requests.get(endpoint).json()
        self.dataset = data

    def compute_analysis(self) -> Any:
        if 'base_experience' in self.dataset:
            mean_base_experience = self.dataset['base_experience'].mean()
            return mean_base_experience
        else:
            raise ValueError("The dataset does not contain the 'base_experience' attribute.")

    def plot_data(self, save_path: Optional[str] = None) -> plt.Figure:
        if 'base_experience' in self.dataset:
            # Create a graph of the base experience values
            plt.hist(self.dataset['base_experience'], bins=20, color='skyblue', edgecolor='black')
            plt.title('Distribution of Base Experience Values')
            plt.xlabel('Base Experience')
            plt.ylabel('Frequency')

            # Save the plot if a save path is provided
            if save_path:
                plt.savefig(save_path)

            # Display the plot
            plt.show()

            # Return the matplotlib Figure
            return plt.gcf()
        else:
            raise ValueError("The dataset does not contain the 'base_experience' attribute.")

    def notify_done(self, message: str) -> None:
        print(f"Notification: {message}")
    