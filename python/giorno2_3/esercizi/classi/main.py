class Country:
    def __init__(self, name):
        self.name = name
        self.regions = []

    def add(self, region):
        if isinstance(region, Region):
            self.regions.append(region)
        else:
            raise TypeError("Puoi aggiungere solo oggetti di tipo Region.")

    @property
    def most_populuous_city(self):
        """Trova la città più popolosa del paese."""
        most_populous = None
        max_population = -1
        for region in self.regions:
            for city in region.cities:
                if city.pop > max_population:
                    most_populous = city
                    max_population = city.pop
        return most_populous

    @property
    def pop(self):
        """The total population of this country"""
        regions_pop = [region.pop for region in self.regions]
        return sum(regions_pop)


class Region:
    def __init__(self, name):
        self.name = name
        self.cities = []  # Lista per memorizzare le città

    def add(self, city):
        if isinstance(city, City):
            self.cities.append(city)
        else:
            raise TypeError("Puoi aggiungere solo oggetti di tipo City.")

    @property
    def pop(self):
        """The total population of this region"""
        cities_pop = [city.pop for city in self.cities]
        return sum(cities_pop)


class City:
    """A city"""
    def __init__(self, name, pop=None):
        self.name = name
        self.pop = pop