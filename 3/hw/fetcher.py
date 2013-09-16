#!/usr/bin/python
'''Collection of classes for fetching and processing data
from World Bank databank.

Illustrates object-oriented approach. Looks like over-engineering, but OK
for learning purposes:). Try to add some print statements to follow the call
sequence in class hierarchy.

'''

import json
import urllib2
#Do we need ant additional imports?

class WBDataFetcher(object):
    """Main class to fetch and process data from World Bank.

    """
    _indicators = {
                    'GDP': 'NY.GDP.MKTP.CD',
                    'population': 'SP.POP.TOTL',
                    'urban': 'SP.URB.TOTL',
                }

    def __init__(self, loader, postprocessor):
        '''This class is constructed with pre-created loader and postprocessor.

        '''
        self._loader = loader
        self._postprocessor = postprocessor

    def fetch(self, country, indicator):
        '''Orchestrates loading and postprocessing of data and then
        returns processed data to user.

        Parameters
        ----------
        country : str
            3-letter code of country to fetch data for
        indicator : str
            human readable name of indicator, will be translated to WB notation

        Returns
        -------
        data : 
            Postprocessed data. Actual type is determined by postprocessor used.

        Usage
        -----
        >>> loader = Loader()
        >>> pprocessor = PostProcessor()
        >>> fetcher = WBDataFetcher(loader, pprocessor)
        >>> data = fetcher.fetch('ukr', 'GDP')
        <some data>

        '''
        if indicator not in WBDataFetcher._indicators.keys():
            return None
        raw_data = self._loader.get(country, WBDataFetcher._indicators[indicator])
        self.processed_data = self._postprocessor.process(raw_data)
        return self.processed_data

    def set_indicators(self, indicators):
        '''Allows to change dictionary, which translates human readable
        indicators names to World Bank notation.

        '''
        WBDataFetcher._indicators = indicators

    def get_available_indicators():
        '''Returns readable representation of available indiactors.
        '''
        return '\n'.join(["%s: %s" % pair for pair in WBDataFetcher._indicators.iteritems()])

    get_available_indicators = staticmethod(get_available_indicators)
        
class Loader(object):
    """Loader class which is used by WBDataFetcher to actually
    go to WB databank and fetch JSON data. This class also implements
    rudimentary caching.

    """
    _request_template = "http://api.worldbank.org/countries/{country}/indicators/{indicator}?MRV=10&format=json"

    def __init__(self, *args, **kwargs):
        #Feel free to initialize Loader class if needed
        pass

    def get(self, country, indicator):
        '''Performs actual fetching and translating data
        from JSON to Python dict and returns it.

        Parameters
        ----------
        country : str
            3-letter code of country to fetch data for
        indicator : str
            name of indicator in WB notation

        Returns
        -------
        data : dict
            Dictionary with data in WB format. Check WB docs.

        '''
        #TODO: Your code here
        #Remember to handle empty response from WB databank
        #First, you need to form a request to WB databank
        #URL to request will look like this:
        url = Loader._request_template.format(country=country, indicator=indicator)
        #Second, parse the JSON result
        #Third, extract actual data from it
        return {}

class CachingLoader(Loader):
    """This child of Loader class will cache data and return it if
    the same country and indicator were requested twice in a row.

    """
    def __init__(self, *args, **kwargs):
        super(CachingLoader, self).__init__(args, kwargs)

    def get(self, country, indicator):
        '''Works in the same way as in Loader, except it checks whether
        the same indicator and country were requested in previous request.

        '''
        try:
            if self.country == country and self.indicator == indicator:
                return self.cached_data
            else:
                self._set_cached(country, indicator)
        except AttributeError:
            self._set_cached(country, indicator)
        return self.cached_data
        
    def _set_cached(self, country, indicator):
        self.country = country
        self.indicator = indicator
        self.cached_data = super(CachingLoader, self).get(self.country, self.indicator)        

class PostProcessor(object):
    """Class, which allows WBDataFetcher to postprocess fetched data
    before returning it to user.

    """
    def __init__(self, *args, **kwargs):
        #Again, fell free to do any initialization needed
        pass

    def process(self, data):
        '''Takes Python dictionary with data and process it, of needed.
        Say, you want to save data in local database. Or return construct string
        to insert it in HTML. Or whatever.

        Parameters
        ----------
        data : dict
            Python dict with data in WB format.

        Returns
        -------
        data : 
            Some result. Be creative:) Or leave it empty.

        '''
        #TODO: Your code here
        #Stub code below
        return data