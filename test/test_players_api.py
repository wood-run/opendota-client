# coding: utf-8

"""
    OpenDota API

    # Introduction The OpenDota API provides Dota 2 related data including advanced match data extracted from match replays.  You can find data that can be used to convert hero and ability IDs and other information provided by the API from the [dotaconstants](https://github.com/odota/dotaconstants) repository.  **Beginning 2018-04-22, the OpenDota API is limited to 50,000 free calls per month and 60 requests/minute** We offer a Premium Tier with unlimited API calls and higher rate limits. Check out the [API page](https://www.opendota.com/api-keys) to learn more.   # noqa: E501

    OpenAPI spec version: 18.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import opendota_client
from opendota_client.api.players_api import PlayersApi  # noqa: E501
from opendota_client.rest import ApiException


class TestPlayersApi(unittest.TestCase):
    """PlayersApi unit test stubs"""

    def setUp(self):
        self.api = opendota_client.api.players_api.PlayersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_players_account_id_counts_get(self):
        """Test case for players_account_id_counts_get

        GET /players/{account_id}/counts  # noqa: E501
        """
        pass

    def test_players_account_id_get(self):
        """Test case for players_account_id_get

        GET /players/{account_id}  # noqa: E501
        """
        pass

    def test_players_account_id_heroes_get(self):
        """Test case for players_account_id_heroes_get

        GET /players/{account_id}/heroes  # noqa: E501
        """
        pass

    def test_players_account_id_histograms_field_get(self):
        """Test case for players_account_id_histograms_field_get

        GET /players/{account_id}/histograms  # noqa: E501
        """
        pass

    def test_players_account_id_matches_get(self):
        """Test case for players_account_id_matches_get

        GET /players/{account_id}/matches  # noqa: E501
        """
        pass

    def test_players_account_id_peers_get(self):
        """Test case for players_account_id_peers_get

        GET /players/{account_id}/peers  # noqa: E501
        """
        pass

    def test_players_account_id_pros_get(self):
        """Test case for players_account_id_pros_get

        GET /players/{account_id}/pros  # noqa: E501
        """
        pass

    def test_players_account_id_rankings_get(self):
        """Test case for players_account_id_rankings_get

        GET /players/{account_id}/rankings  # noqa: E501
        """
        pass

    def test_players_account_id_ratings_get(self):
        """Test case for players_account_id_ratings_get

        GET /players/{account_id}/ratings  # noqa: E501
        """
        pass

    def test_players_account_id_recent_matches_get(self):
        """Test case for players_account_id_recent_matches_get

        GET /players/{account_id}/recentMatches  # noqa: E501
        """
        pass

    def test_players_account_id_refresh_post(self):
        """Test case for players_account_id_refresh_post

        POST /players/{account_id}/refresh  # noqa: E501
        """
        pass

    def test_players_account_id_totals_get(self):
        """Test case for players_account_id_totals_get

        GET /players/{account_id}/totals  # noqa: E501
        """
        pass

    def test_players_account_id_wardmap_get(self):
        """Test case for players_account_id_wardmap_get

        GET /players/{account_id}/wardmap  # noqa: E501
        """
        pass

    def test_players_account_id_wl_get(self):
        """Test case for players_account_id_wl_get

        GET /players/{account_id}/wl  # noqa: E501
        """
        pass

    def test_players_account_id_wordcloud_get(self):
        """Test case for players_account_id_wordcloud_get

        GET /players/{account_id}/wordcloud  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
