"""
The question this project poses is, "what if the result of every F1 race was random?"
(i.e., no dominant, top and midfield team(s), all cars/drivers equal)
Obviously this isn't realistic, but that's not the point, which is just to see what
an F1 championship could look like if there was nothing in the way of any driver or
team winning a race and/or championship.

Race/championship-influencing factors that are left out for now: sprint races,
shortened races due to bad weather, DNFs, reserve drivers, etc.
"""

from random import Random
from prettytable import PrettyTable  # conda install -c conda-forge prettytable


class Driver:
    def __init__(self, name: str, racing_number: int, team: str):
        self.name = name
        self.team = team
        self.racing_number = racing_number
        self.championship_points = 0

    def __str__(self):
        return f'Name: {self.name}, Racing Number: {self.racing_number}, Team: {self.team}'


class Roster2023:
    drivers = [
        Driver('Max Verstappen', 1, 'Red Bull'),
        Driver('Sergio Perez', 11, 'Red Bull'),
        Driver('Charles Leclerc', 16, 'Ferrari'),
        Driver('Carlos Sainz', 55, 'Ferrari'),
        Driver('Lewis Hamilton', 44, 'Mercedes'),
        Driver('George Russell', 63, 'Mercedes'),
        Driver('Esteban Ocon', 31, 'Alpine'),
        Driver('Pierre Gasly', 10, 'Alpine'),
        Driver('Lando Norris', 4, 'McLaren'),
        Driver('Oscar Piastri', 81, 'McLaren'),
        Driver('Nico Hulkenberg', 27, 'Haas'),
        Driver('Kevin Magnussen', 20, 'Haas'),
        Driver('Fernando Alonso', 14, 'Aston Martin'),
        Driver('Lance Stroll', 18, 'Aston Martin'),
        Driver('Yuki Tsunoda', 22, 'Alpha Tauri'),
        Driver('Daniel Ricciardo', 3, 'Alpha Tauri'),
        Driver('Valtteri Bottas', 77, 'Alfa Romeo'),
        Driver('Zhou Guanyu', 24, 'Alfa Romeo'),
        Driver('Alex Albon', 23, 'Williams'),
        Driver('Logan Sargeant', 2, 'Williams')
    ]

    def __str__(self):
        return '\n'.join(str(driver) for driver in self.drivers)


class Race:
    # Points awarded for 1st to 10th positions (no points for 11th to 20th)
    points_table = {
        1: 25,
        2: 18,
        3: 15,
        4: 12,
        5: 10,
        6: 8,
        7: 6,
        8: 4,
        9: 2,
        10: 1
    }

    def __init__(self, name: str):
        self.name = name
        self.race_result_title = f'Formula 1 {self.name} Grand Prix - Race Result'
        self.race_result = {}

    def run(self) -> None:
        drivers_temp = Roster2023.drivers  # TODO: this shuffles 2023.drivers, not just temp
        Random().shuffle(drivers_temp)
        # Map positions 1-20 to driver in each of those positions
        self.race_result = dict(zip(range(1, 21), drivers_temp))
        results_table = PrettyTable(['Position', 'Team', 'Driver', 'Points'], 
                                    title=self.race_result_title)
        for pos, driver in self.race_result.items():
            driver_points = self.points_table.get(pos, 0)  # default to 0 if out of the points
            results_table.add_row([pos, driver.team, driver.name, driver_points])
        print(results_table, '\n')


class Season2023:
    def __init__(self):
        self.races = ['Monaco', 'Belgium']

    def run(self) -> None:
        for race_name in self.races:
            race = Race(race_name)
            race.run()


class Team:
    def __init__(self, name: str, drivers: list):
        self.name = name
        self.drivers = drivers
        self.championship_points = 0


def main() -> None:
    Season2023().run()
    # round6 = Race('Monaco')
    # round6.run()

if __name__ == '__main__':
    main()
