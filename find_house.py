from pdb import set_trace
import requests
import zapimoveis_scraper as zap


res = zap.search(localization="sp+sao-paulo+zona-sul+s-judas", acao="venda",
                 tipo="apartamentos", num_pages=5)


max_price = max([float(i.price.replace("R$", "").replace(" ", "").replace(
    "/venda", "").replace(".", "")) for i in res if i.price != "Sob consulta"])

for i in res:
    print(i.price)

set_trace()
