import Contact as ct
import Auto as aut

c = ct.Contact('Ailton', '5511952278958')

texto = 'Boa noite {name}, tudo bem?\nSou uma mensagem automatica'
auto = aut.Auto('firefox')

auto.loginWhats()
auto.sendMensage(c, 'none', texto)