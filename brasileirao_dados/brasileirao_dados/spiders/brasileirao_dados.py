# import scrapy
#
#
# class BrasileiraoDadosSpider(scrapy.Spider):
#     name = "brasileirao_dados"
#
#     anos_links = [
#         {"ANO": 2012,
#          "LINK": "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2012"},
#         {"ANO": 2013,
#          "LINK": "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2013"},
#         {"ANO": 2014,
#          "LINK": "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2014"},
#         {"ANO": 2015,
#          "LINK": "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2015"},
#         {"ANO": 2016,
#          "LINK": "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2016"},
#         {"ANO": 2017,
#          "LINK": "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2017"},
#         {"ANO": 2018,
#          "LINK": "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2018"},
#         {"ANO": 2019,
#          "LINK": "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2019"},
#         {"ANO": 2020,
#          "LINK": "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2020"},
#         {"ANO": 2021,
#          "LINK": "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2021"},
#         {"ANO": 2022,
#          "LINK": "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2022"},
#         {"ANO": 2023,
#          "LINK": "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2023"}
#     ]
#
#     def start_requests(self):
#         for item in self.anos_links:
#             yield scrapy.Request(url=item['LINK'], callback=self.parse, meta={'ano': item['ANO']})
#
#     def parse(self, response):
#         ano = response.meta['ano']
#         dados = response.css('.no-underline span::text').getall()
#
#         for i in range(0, len(dados), 3):
#             mandante = dados[i].strip()
#             visitante = dados[i + 1].strip()
#             resultado = dados[i + 2].strip()
#
#             yield {
#                 'ano': ano,
#                 'mandante': mandante,
#                 'visitante': visitante,
#                 'resultado': resultado
#             }

import scrapy


class BrasileiraoDadosSpider(scrapy.Spider):
    name = "brasileirao_dados"

    anos_links = [
        {"ANO": 2012,
         "LINK": "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2012"},
        {"ANO": 2013,
         "LINK": "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2013"},
        {"ANO": 2014,
         "LINK": "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2014"},
        {"ANO": 2015,
         "LINK": "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2015"},
        {"ANO": 2016,
         "LINK": "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2016"},
        {"ANO": 2017,
         "LINK": "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2017"},
        {"ANO": 2018,
         "LINK": "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2018"},
        {"ANO": 2019,
         "LINK": "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2019"},
        {"ANO": 2020,
         "LINK": "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2020"},
        {"ANO": 2021,
         "LINK": "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2021"},
        {"ANO": 2022,
         "LINK": "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2022"},
        {"ANO": 2023,
         "LINK": "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2023"}
    ]

    def start_requests(self):
        for index, item in enumerate(self.anos_links):
            yield scrapy.Request(url=item['LINK'], callback=self.parse, meta={'ano': item['ANO'], 'ano_index': index})

    def parse(self, response):
        ano = response.meta['ano']
        ano_index = response.meta['ano_index']
        dados = response.css('.no-underline span::text').getall()

        for i in range(0, len(dados), 3):
            mandante = dados[i].strip()
            visitante = dados[i + 1].strip()
            resultado = dados[i + 2].strip()
            jogo_index = i // 3  # Índice do jogo dentro do ano

            yield {
                'ano': ano,
                'ano_index': ano_index,
                'jogo_index': jogo_index,
                'mandante': mandante,
                'visitante': visitante,
                'resultado': resultado
            }
