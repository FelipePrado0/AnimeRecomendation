import unittest
from unittest.mock import patch
import requests
import sys
import os
from AnimeRecomendation.src.BuscarDescricao import buscar_id_anime_por_descricao

class TestGeminiAPI(unittest.TestCase):

    @patch('requests.get')
    def test_buscar_id_anime_por_descricao(self, mock_get):
        # Mock response data
        mock_response_data = {
            "results": [
                {"id": 12345, "title": "Test Anime"}
            ]
        }
        
        # Configure the mock to return a response with the mock data
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response_data

        # Call the function with a test description
        descricao = "Test description"
        anime_id = buscar_id_anime_por_descricao(descricao)

        # Assert that the function returns the correct anime ID
        self.assertEqual(anime_id, 12345)

    @patch('requests.get')
    def test_buscar_id_anime_por_descricao_no_results(self, mock_get):
        # Mock response data with no results
        mock_response_data = {
            "results": []
        }
        
        # Configure the mock to return a response with the mock data
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response_data

        # Call the function with a test description
        descricao = "Test description"
        anime_id = buscar_id_anime_por_descricao(descricao)

        # Assert that the function returns None when no results are found
        self.assertIsNone(anime_id)

    @patch('requests.get')
    def test_buscar_id_anime_por_descricao_api_error(self, mock_get):
        # Configure the mock to return a response with a 500 status code
        mock_get.return_value.status_code = 500

        # Call the function with a test description
        descricao = "Test description"
        anime_id = buscar_id_anime_por_descricao(descricao)

        # Assert that the function returns None when the API returns an error
        self.assertIsNone(anime_id)

if __name__ == '__main__':
    unittest.main()